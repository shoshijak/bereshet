"""
Defines entry-point of Bereshet application.

What this means is ...
"""

from bereshet import create_reshet, db, cli
from bereshet.elements import Makor, Mechaber, Sefer

reshet = create_reshet()
cli.register(reshet)


@reshet.shell_context_processor
def make_shell_context():
    """
    Define something.

    when using flask shell, the command pre-imports the application instance. The nice
    thing about flask shell is not that it pre-imports app, but that you can configure a
    "shell context", which is a list of other symbols to pre-import.

    The following function in microblog.py creates a shell context that adds the
    database instance and models to the shell session

    After you add the shell context processor function you can work with database
    entities without having to import them
    """
    return {"db": db, "Makor": Makor, "Mechaber": Mechaber, "Sefer": Sefer}
