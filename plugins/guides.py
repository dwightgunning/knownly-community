import os
import datetime
import logging

ORDER = 999
GUIDES_PATH = 'guides/'
GUIDES = []

from django.template import Context
from django.template.loader import get_template
from django.template.loader_tags import BlockNode, ExtendsNode

def getNode(template, context=Context(), name='subject'):
    """
    Get django block contents from a template.
    http://stackoverflow.com/questions/2687173/
    django-how-can-i-get-a-block-from-a-template
    """
    for node in template:
        if isinstance(node, BlockNode) and node.name == name:
            return node.render(context)
        elif isinstance(node, ExtendsNode):
            return getNode(node.nodelist, context, name)
    raise Exception("Node '%s' could not be found in template." % name)


def preBuild(site):

    global GUIDES

    # Build all the guides
    for page in site.pages():
        if page.path.startswith(GUIDES_PATH):
            # Skip the index and non html guides
            if page.path == '%sindex.html' % GUIDES_PATH \
                    or page.path.endswith('example/index.html') \
                    or not page.path.endswith('index.html'):
                continue

            guide_id =  os.path.dirname(page.path).lstrip(GUIDES_PATH)

            # Find a specific defined variable in the page context,
            # and throw a warning if we're missing it.
            
            def find(name):
                pageContext = page.context()
                if not name in pageContext:
                    logging.info("Missing info '%s' for guide %s" % (name, page.path))
                    return ''
                return pageContext.get(name, '')

            # Build a context for each guide
            
            guideContext = {}
            guideContext['title'] = find('title')
            guideContext['headline'] = find('headline')
            guideContext['author'] = find('author')
            guideContext['date'] = find('date')
            guideContext['img_src'] = find('img_src')
            guideContext['img_attr'] = find('img_attr')
            guideContext['path'] = '%s/%s' % (page.site.url or '', page.path)

            guideContext['body'] = getNode(get_template(page.path), page.context(), name="body")

            # Parse the date into a date object
            try:
                guideContext['date'] = datetime.datetime.strptime(guideContext['date'], '%d-%m-%Y')
            except Exception, e:
                logging.warning("Date format not correct for page %s, should be dd-mm-yy\n%s" % (page.path, e))
                continue

            GUIDES.append(guideContext)

    # Sort the guides by date
    GUIDES = sorted(GUIDES, key=lambda x: x['date'])
    GUIDES.reverse()

    indexes = xrange(0, len(GUIDES))

    for i in indexes:
        if i+1 in indexes: GUIDES[i]['prevGuide'] = GUIDES[i+1]
        if i-1 in indexes: GUIDES[i]['nextGuide'] = GUIDES[i-1]


def preBuildPage(site, page, context, data):
    """
    Add the list of guides to every page context so we can
    access them from wherever on the site.
    """
    context['guides'] = GUIDES

    for guide in GUIDES:
        if guide['path'] == page.path:
            context.update(guide)

    return context, data
