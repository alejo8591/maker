# encoding: utf-8
# Copyright 2013 maker
# License


from django.core.management.base import BaseCommand, CommandError
from maker.core.conf import settings
import simplejson as json
import subprocess
from os import path
import sys

PROJECT_ROOT = getattr(settings, 'PROJECT_ROOT')
MAKER_DB_SETTINGS_FILE = path.join(PROJECT_ROOT, 'core/db/dbsettings.json')

class Command(BaseCommand):
    args = ''
    help = 'Installs the database prompting the user for all details'

    def handle(self, *args, **options):

        initial_db = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': './initial.db',
            'HOST': '',
            'USER': '',
            'PASSWORD': ''
        }

        db = {}
        db['ENGINE'] = raw_input('Enter database engine <mysql,postgresql,oracle,sqlite3> (defaults to sqlite3): ')
        if not db['ENGINE']:
            db['ENGINE'] = 'sqlite3'

        if db['ENGINE'] in ('mysql', 'postgresql', 'oracle', 'sqlite3'):
            db['ENGINE'] = 'django.db.backends.' + db['ENGINE']
        else:
            raise CommandError('Unkown database engine: %s' % db['ENGINE'])

        db['NAME'] = raw_input('Enter database name (defaults to maker.db): ')

        if not db['NAME']:
            db['NAME'] = 'maker.db'

        if not db['ENGINE'].endswith('sqlite3'):
            db['USER'] = raw_input('Database user (defaults to maker): ')
            if not db['USER']:
                db['USER'] = 'maker'

            db['PASSWORD'] = raw_input('Database password: ')

            db['HOST'] = raw_input('Hostname (empty for default): ')
            db['PORT'] = raw_input('Port (empty for default): ')

        self.stdout.write('\n-- Installing database...\n')
        self.stdout.flush()

        f = open(MAKER_DB_SETTINGS_FILE, 'w')
        json.dump({'default': db}, f)
        f.close()

        exit_code = subprocess.call([sys.executable, 'manage.py', 'syncdb', '--all', '--noinput'])
        if not exit_code == 0:
            self.stdout.flush()
            f = open(MAKER_DB_SETTINGS_FILE, 'w')
            json.dump({'default': initial_db}, f)
            f.close()
            raise CommandError('Failed to install database.')

        exit_code = subprocess.call([sys.executable, 'manage.py', 'migrate', '--all', '--fake', '--noinput', '--no-initial-data'])

        self.stdout.write('\n-- Successfully installed database. \n-- You\'re ready to go!\n\n')

