# gunicorn config for ch8 project
wsgi_app = 'mysite.wsgi'
# bind = '0:8081'
bind = 'unix:/tmp/gunicorn.sock'
chdir = '/home/shkim/pyBook/ch8'
pythonpath = '/home/shkim/pyBook/ch8/venv/lib/python3.10/site-packages'
# user = 'shkim'
# group = 'shkim'
user = 'nginx'
group = 'nginx'
workers = 3
daemon = True
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
