django-template-check
=====================

This package makes it possible to easily check for basic syntax errors in all loaded Django templates. This can be useful as part of a continuous integration step in a build process, so as not to discover these problems at runtime.

Currently, checking is very minimal, simply relying on the exceptions raised by Django's compile and render template pipeline. Furthermore, only the default Django template backend is tested and supported.

Requirements
------------

This package requires Django version 1.8 or greater, and has been tested with 1.10.

Installation
------------

Simply get the package from ``pip``:

::

    pip install django-embed-template

Then make sure to add ``django_embed_template`` to your ``INSTALLED_APPS`` in your ``settings.py``.

Usage
-----

After installing this package, simply use it by calling the management command:

::

    python manage.py templatecheck


License
-------

All included code is available under the CC0 1.0 Universal Public Domain Dedication.
