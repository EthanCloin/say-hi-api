from flask import Blueprint, render_template
from .database import get_db


bp = Blueprint("main", __name__, url_prefix=None)


@bp.get("/")
def index():
    return "Hello from Main"


@bp.post("/hi")
def say_hi():
    cxn = get_db()
    insert_query = "insert into Hellos default values;"
    count_query = "select count(*) as hello_count from Hellos;"

    cxn.execute(insert_query)
    count = cxn.execute(count_query).fetchone()["hello_count"]
    cxn.commit()

    return render_template("fading-thanks.html", hello_count=count)


@bp.get("/hi")
def get_hi_btn():
    return render_template("say-hi-button.html")
