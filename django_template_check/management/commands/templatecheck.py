import django
from django.conf import settings
from django.template.loaders.app_directories import get_app_template_dirs
from django.core.management.base import BaseCommand
from django import template

import os
import sys
import logging
from itertools import chain


logger = logging.getLogger(__name__)

#: Supported Django backend
DJANGO_BACKEND = 'django.template.backends.django.DjangoTemplates'


def _template_names(proj_only=False):
    for engine in settings.TEMPLATES:
        if engine['BACKEND'] != DJANGO_BACKEND:
            raise NotImplementedError(
                "Currently only supports default DjangoTemplates backend."
            )

        for template_dir in chain(
                engine['DIRS'], get_app_template_dirs('templates')):
            template_dir = str(template_dir)  # coerce pathlike
            if not proj_only or (template_dir.startswith(
                    str(settings.BASE_DIR))):
                for dirpath, _dirnames, filenames in os.walk(template_dir):
                    for template_name in filenames:
                        yield os.path.join(
                            dirpath[len(template_dir)+1:], template_name)


class Command(BaseCommand):
    help = "Perform (minimal) syntax checks for Django templates."

    def add_arguments(self, parser):
        parser.add_argument(
            '--project-only',
            action='store_true',
            help='Only check templates that live in the project directory.',
        )

    def handle(self, *args, **options):
        return_code = 0
        for t_name in _template_names(options['project_only']):
            try:
                if django.VERSION < (2,):
                    # Prior to 2.0, we need to pass the template to
                    # template.Template()
                    tpl = template.loader.get_template(t_name)
                else:
                    # post 2.0, template.Template() expects the template
                    # location
                    tpl = t_name
                t = template.Template(tpl)
                t.render(template.Context())
            except Exception as e:
                logging.exception('%s: %s', t_name, e)
                return_code = 1
        sys.exit(return_code)
