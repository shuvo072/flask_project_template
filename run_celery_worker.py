import subprocess

def run_worker():
    subprocess.call(
        ["celery","-A","manage:celery","worker","--loglevel=info","--beat", "--loglevel=info"]
    )

run_worker()