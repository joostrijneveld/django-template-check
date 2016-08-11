from django.conf import settings
from django.template.loaders.app_directories import get_app_template_dirs
from django.core.management.base import BaseCommand
from django import template

import os
import sys
from itertools import chain


def _template_names():
    for engine in settings.TEMPLATES:
        if (engine['BACKEND']
                == 'django.template.backends.django.DjangoTemplates'):
            for template_dir in chain(engine['DIRS'],
                                      get_app_template_dirs('templates')):
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

    def handle(self, *args, **options):
        return_code = 0
        for t_name in _template_names():
            try:
                t = template.Template(template.loader.get_template(t_name))
                t.render(template.Context())
            except Exception as e:
                print('{}: {}'.format(t_name, e))
                return_code = 1
        sys.exit(return_code)
