from bereshet import create_reshet, db, cli
from bereshet.models import Makor, Mechaber, Sefer

reshet = create_reshet()
cli.register(reshet)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Makor": Makor, "Mechaber": Mechaber, "Sefer": Sefer}
