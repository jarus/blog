# -*- coding: utf-8 -*-
SITE_NAME = "Christoph Heer"
AUTHOR_NAME = "Christoph Heer"
AUTHOR_EMAIL = "christoph.heer@googlemail.com"

MODULES = {
    'flaskrst.modules.page': {},
    'flaskrst.modules.blog': {
        'body_as_summary_fallback': True
    },
    'flaskrst.modules.archive': {},
    'flaskrst.modules.tags': {},
    'flaskrst.modules.atom': {},
    'flaskrst.modules.pygments': {
        'css_file_route': '/pygments.css'
    },
    'flaskrst.modules.github': {},
    'flaskrst.modules.disqus': {
        'shortname': 'christophheer'
    }
}

NAVIGATION = [
    {
        'label': 'Christoph Heer',
        'route': 'page.show',
        'file_path': 'about',
    },
    {
        'label': 'Projects',
        'route': 'page.show',
        'file_path': 'projects',
    },
    {
        'label': 'Blog',
        'route': 'blog.index'
    },
    {
        'label': 'Archive', 
        'route': 'archive.index'
    },
    {
        'label': 'Tags', 
        'route': 'tags.cloud'
    },
]

STYLESHEETS = [
    '/static/css/bootstrap.min.css',
    '/static/css/bootstrap-responsive.min.css',
    '/static/css/font-awesome.css',
    '/static/css/costum.css',
]
