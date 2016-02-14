def preBuildPage(page, context, data):
    """
    Updates the context of the page to include: the page itself
    as {{ CURRENT_PAGE }}
    """

    # This will run for each page that Cactus renders.
    # Any changes you make to context will be passed to the template
    # renderer for this page.

    extra = {
        "CURRENT_PAGE": page,
        "MIXPANEL_TOKEN": page.site.config.get('mixpanel-token', ''),
        "GA_TRACKING_ID": page.site.config.get('ga-tracking-id', ''),
        "DISQUS_SHORTNAME": page.site.config.get('disqus-shortname', '')
    }

    context.update(extra)
    return context, data
