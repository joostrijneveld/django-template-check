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


def _template_names(proj_only=False):
    for engine in settings.TEMPLATES:
        if (engine['BACKEND']
                == 'django.template.backends.django.DjangoTemplates'):
            for template_dir in chain(engine['DIRS'],
                                      get_app_template_dirs('templates')):
                if not proj_only or template_dir.startswith(settings.BASE_DIR):
                    for dirpath, dirnames, filenames in os.walk(template_dir):
                        for template_name in filenames:
                            yield os.path.join(dirpath[len(template_dir)+1:],
                                               template_name)
        else:
            raise NotImplementedError(
                "Currently only supports default DjangoTemplates backend."
            )


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
                logging.exception('{}: {}'.format(t_name, e))
                return_code = 1
        sys.exit(return_code)
