Testing multiple Flask version on Travis-CI
===========================================

:public: True
:tags: ["flask", "extension", "testing", "travis-ci"]
:summary: "As a Flask extension developer you want normaly to test your extension agains a list of Flask versions."

As a `Flask`_ extension developer you want normaly to test your extension agains a list of Flask versions. On `Travis-CI`_ it's very simple and upsetting powerful.

The following ``.travis.yml`` file shows you how I test my Flask extensions.

.. sourcecode:: yaml

    language: python
    python:
      - "2.5"
      - "2.6"
      - "2.7"
    env:
      - FLASK=dev
      - FLASK=0.9
      - FLASK=0.8
      - FLASK=0.7
      - FLASK=0.6
      - FLASK=0.5
    install:
      - pip install flask==$FLASK --use-mirrors
      - pip install -e . --use-mirrors
    script:
      - python setup.py test

The trick is to define the Flask versions as ``env`` variables and install the Flask package befor the other packages and take the specify version from the ``env`` variable.

.. _Flask: http://flask.pocoo.org/
.. _Travis-Ci: http://travis-ci.org/