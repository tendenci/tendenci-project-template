#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    os.environ.setdefault('TENDENCI_PROJECT_ROOT', PROJECT_ROOT)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
