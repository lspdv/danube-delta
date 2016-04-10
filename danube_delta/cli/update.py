
from . import blog
from .helpers import run


@blog.command()
def update():
    """Gets other people's changes from GitHub"""

    run('git pull origin master')
    run('pip install -r requirements.txt --upgrade')
