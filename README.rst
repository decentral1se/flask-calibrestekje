.. _header:

*******************
flask-calibrestekje
*******************

.. image:: https://img.shields.io/badge/license-GPL-brightgreen.svg
   :target: LICENSE
   :alt: Repository license

.. image:: https://badge.fury.io/py/flask-calibrestekje.svg
   :target: https://badge.fury.io/py/flask-calibrestekje
   :alt: PyPI package

.. image:: https://travis-ci.com/decentral1se/flask-calibrestekje.svg?branch=master
   :target: https://travis-ci.com/decentral1se/flask-calibrestekje
   :alt: Travis CI result

.. image:: https://readthedocs.org/projects/calibrestekje/badge/?version=latest
   :target: https://calibrestekje.readthedocs.io/en/latest/
   :alt: Documentation status

.. image:: http://img.shields.io/liberapay/patrons/decentral1se.svg?logo=liberapay
   :target: https://liberapay.com/decentral1se
   :alt: Support badge

.. _introduction:

Library prototyping based on Calibre with Flask
-----------------------------------------------

.. _example:

Example
*******

.. code-block:: python

    from calibrestekje import Book
    from flask import Flask, jsonify

    from flask_calibrestekje import CalibreStekje

    app = Flask(__name__)
    app.config.from_pyfile("config.cfg")
    db = CalibreStekje(app)

    @app.route("/")
    def home():
        return jsonify({"book-count": db.session.query(Book).count()})

.. _documentation:

Documentation
*************

* https://calibrestekje.readthedocs.io/
