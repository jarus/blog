import os

from fabric.api import task, env, run, cd

from fabric_gunicorn import reload

env.hosts = ["thelabmill.de"]
env.user = "christoph-blog"

def in_lwd(path):
    """Complete relative path to full path on local system"""
    return os.path.join(env.local_workdir, path)

def in_rwd(path):
    """Complete relative path to full path on remote system"""
    return os.path.join(env.remote_workdir, path)

env.remote_workdir = '/home/%s/' % env.user
env.virtualenv_dir = env.remote_workdir

env.requirements_file = in_rwd('src/requirements.txt')
env.source_dir = in_rwd('src/')
env.gunicorn_pidpath = in_rwd('var/run/gunicorn.pid')

@task
def git_pull():
    with cd(env.source_dir):
        run('git reset --hard HEAD')
        run('git pull')

@task
def update_virtualenv():
    with cd(env.source_dir):
        run('pip install -r %s' % env.requirements_file)

@task
def deploy():
    git_pull()
    update_virtualenv()
    reload()