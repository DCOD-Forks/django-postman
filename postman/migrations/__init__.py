# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured


# Ensure the user is not using Django 1.6 or below with South
try:
    from django.db import migrations
except ImportError:

    SOUTH_ERROR_MESSAGE = """\n
    For South support, customize the "SOUTH_MIGRATION_MODULES" setting like so:

        SOUTH_MIGRATION_MODULES = {
            "postman": "postman.south_migrations",
        }
    """

    raise ImproperlyConfigured(SOUTH_ERROR_MESSAGE)
