Dash.app - Documentation Browser for Mac
========================================

:public: True
:tags: ["mac", "dash", "docs", "flask"]
:summary: "A programmer needs documentation."

Documentation. Every programmer needs documentation about a framework or the standard library of a programming language. If you using Mac OS than you should take a look on `Dash`_. It's a great application to browse in documentation or manage snippets. I'm not the guy with millions snippets so I am not qualified to rate the snippet part of Dash but the documentation browsing part is amazing.

.. image:: /static/img/2012-07-30-dash/search_datetime.png
    :target: /static/img/2012-07-30-dash/search_datetime.png
    :alt: Search datetime in Dash

This is the normal browser and search window of Dash. The search is faster than I can typing. Dash deliver by default some nice docsets. This is my current collection of docsets.

.. image:: /static/img/2012-07-30-dash/docsets.png
    :target: /static/img/2012-07-30-dash/docsets.png
    :alt: Docsets in Dash

Without the Flask docset there all default docsets provided by Dash. You are able to generate own docsets from existing `Sphinx`_ documentations like Flask or other Python projects. Sadly not direct in Dash but with a small python tool called `doc2dash`_.

.. github-repo:: hynek/doc2dash

Generate docsets from Sphinx docs
*********************************

To generate a docset from a existing sphinx doc is very simple. In this small how to I will generate a docset for `Flask`_.

To beginning we need the code and documentation base of Flask. The best way is to clone it from `GitHub <https://github.com/mitsuhiko/flask>`_.::

    $ git clone https://github.com/mitsuhiko/flask.git

If you are using virtualenvwrapper than you can use the ``mktmpenv`` command which create a virtualenv which will destroyed by ``deactivate``. But every normal virtualenv or also the global environment should working.::

    $ mktmpenv
    New python executable in f006786c-91a8-4d44-aa73-752c2121a51a/bin/python
    Installing distribute done.
    Installing pip done.
    
Now we need to install flask and some other packages.::
  
    $ cd flask/
    $ python setup.py install
    $ pip install sphinx doc2dash

But there is something missing. Flask uses his own sphinx theme which is included over git submodule so we must fetch it first with. Other python docs use default themes which are already installed over the ``sphinx`` package.::

    $ git submodule update --init
    
After this big installation party we go into the ``docs/`` folder and generate the html version of the documentation.::

    $ cd docs/
    $ make html
    sphinx-build -b html -d _build/doctrees   . _build/html
    Running Sphinx v1.1.3
    loading pickled environment... not yet created
    loading intersphinx inventory from http://docs.python.org/dev/objects.inv...
    loading intersphinx inventory from http://werkzeug.pocoo.org/docs/objects.inv...
    loading intersphinx inventory from http://wtforms.simplecodes.com/docs/0.5/objects.inv...
    loading intersphinx inventory from http://www.sqlalchemy.org/docs/objects.inv...
    loading intersphinx inventory from http://discorporate.us/projects/Blinker/docs/1.1/objects.inv...
    building [html]: targets for 67 source files that are out of date
    updating environment: 67 added, 0 changed, 0 removed
    reading sources... [100%] views                                                                                                                                      
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [100%] views                                                                                                                                       
    writing additional files... genindex search
    copying images... [100%] _static/yes.png                                                                                                                             
    copying static files... done
    dumping search index... done
    dumping object inventory... done
    build succeeded, 2 warnings.
    
    Build finished. The HTML pages are in _build/html.

But we want a docset not a html version? Yes you are right but we use doc2dash which want a html version of the sphinx documentation. So lets great the right docset.::

    $ doc2dash -n Flask -i _static/flask.png -a -d ~/Library/Application\ Support/Dash/DocSets/Flask _build/html/
    Converting sphinx docs from "_build/html/" to "/Users/Christoph/Library/Application Support/Dash/DocSets/Flask/Flask.docset".
    Parsing HTML...
    Creating database...
    Added 245 index entries.
    Adding table of contents meta data...

Done! We generated the ``Flask.docset`` and placed it into the Application Support folder of Dash over the ``-d`` flag. With the ``-n`` flag we set the Name of the docset and with ``-i`` we used the Flask logo as icon for the docset but a icon is not necessary to generate a docset. The ``-a`` flag add the generated docset to your list of docsets in Dash.

Now we can browse with dash inside of the flask documentation and use the search. Also you have a offline version of the documentation with the benefits and disadvantages like you must update the docsets by hand.

.. image:: /static/img/2012-07-30-dash/flask.png
    :target: /static/img/2012-07-30-dash/flask.png
    :alt: Flask docs in Dash

.. _Dash: http://itunes.apple.com/us/app/dash/id458034879?ls=1&mt=12
.. _Sphinx: http://sphinx.pocoo.org
.. _Flask: http://flask.pocoo.org
.. _doc2dash: http://pypi.python.org/pypi/doc2dash/