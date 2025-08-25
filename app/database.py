from flask import current_app, g
import sqlite3
import click


def init_app(app):
    """allows db to be initialized by the flask cli"""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def get_db():
    """access the database connection at runtime"""

    def dict_factory(cursor, row):
        """https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory"""
        fields = [x[0] for x in cursor.description]
        return {k: v for k, v in zip(fields, row)}

    # 'g' is a flask object generated on each unique request.
    # if a single request hits the db multiple times, it would reuse the
    # db reference already present in 'g'

    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = dict_factory

    return g.db


def init_db():
    """run the initialize sql script"""
    db = get_db()
    create_schema_sql = """
create table if not exists Hellos (
    HelloID integer primary key,
    CreatedDate datetime default current_timestamp
);"""
    db.executescript(create_schema_sql)


def close_db(e=None):
    """teardown connection"""
    db = g.pop("db", None)

    if db is not None:
        db.close()


if __name__ == "__main__":
    pass
