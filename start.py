import subprocess

subprocess.run(['flask', 'db', 'init'])
subprocess.run(['flask', 'db', 'migrate', '-m', 'moving files'])
subprocess.run(['flask', 'db', 'upgrade'])