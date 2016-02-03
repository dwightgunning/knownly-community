import os
import datetime
import logging

ORDER = 999
GALLERY_PATH = 'gallery/'
GALLERY_SITES = []

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

    global GALLERY_SITES

    # Build all the gallery sites
    for page in site.pages():
        if page.path.startswith(GALLERY_PATH):
            # Skip the index and non html gallery sites
            if page.path == '%sindex.html' % GALLERY_PATH \
                    or page.path.endswith('example/index.html') \
                    or not page.path.endswith('index.html'):
                continue

            gallery_site_id =  os.path.dirname(page.path).lstrip(GALLERY_PATH)

            # Find a specific defined variable in the page context,
            # and throw a warning if we're missing it.
            
            def find(name):
                pageContext = page.context()
                if not name in pageContext:
                    logging.info("Missing info '%s' for gallery site %s" % (name, page.path))
                    return ''
                return pageContext.get(name, '')

            # Build a context for each gallery site
            
            gallery_site_context = {}
            gallery_site_context['page'] = page
            gallery_site_context['title'] = find('title')
            gallery_site_context['headline'] = find('headline')
            gallery_site_context['author'] = find('author')
            gallery_site_context['date'] = find('date')
            gallery_site_context['img_src'] = find('img_src')
            gallery_site_context['img_attr'] = find('img_attr')

            gallery_site_context['body'] = getNode(get_template(page.path), page.context(), name="body")

            # Parse the date into a date object
            try:
                gallery_site_context['date'] = datetime.datetime.strptime(gallery_site_context['date'], '%d-%m-%Y')
            except Exception, e:
                logging.warning("Date format not correct for page %s, should be dd-mm-yy\n%s" % (page.path, e))
                continue

            GALLERY_SITES.append(gallery_site_context)

    # Sort the gallery sites by date
    GALLERY_SITES = sorted(GALLERY_SITES, key=lambda x: x['date'])
    GALLERY_SITES.reverse()

    indexes = xrange(0, len(GALLERY_SITES))

    for i in indexes:
        if i+1 in indexes: GALLERY_SITES[i]['prevgallerysite'] = GALLERY_SITES[i+1]
        if i-1 in indexes: GALLERY_SITES[i]['nextgallerysite'] = GALLERY_SITES[i-1]


def preBuildPage(site, page, context, data):
    """
    Add the list of gallery sites to every page context so we can
    access them from wherever on the site.
    """
    context['gallery_sites'] = GALLERY_SITES

    for gallery_site in GALLERY_SITES:
        if gallery_site['page'].final_url == page.final_url:
            context.update(gallery_site)

    return context, data
