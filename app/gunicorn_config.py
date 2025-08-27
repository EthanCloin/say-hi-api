import os


workers = int(os.environ.get("GUNICORN_PROCESSES", "2"))
threads = int(os.environ.get("GUNICORN_THREADS", "4"))
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "30"))

bind = os.environ.get("GUNICORN_BIND", "unix:/run/api.say-hi/gunicorn.sock")
umask = 0o007  # ensures socket is rw for user+group, no world access

forwarded_allow_ips = "*"
secure_scheme_headers = {"X-Forwarded-Proto": "https"}
