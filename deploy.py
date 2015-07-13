import subprocess

subprocess.check_call(['python', 'manage.py',  'migrate', '--noinput'])
subprocess.check_call(['python', 'manage.py',  'collectstatic', '--noinput'])
subprocess.check_call(['python', 'manage.py',  'update_settings'])
subprocess.check_call(['python', 'manage.py',  'clear_theme_cache'])
subprocess.check_call(['python', 'manage.py',  'populate_default_entity'])
subprocess.check_call(['python', 'manage.py',  'populate_entity_and_auth_group_columns'])
