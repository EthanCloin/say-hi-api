from flask import Blueprint
from .database import get_db


bp = Blueprint("bookings", __name__, url_prefix=None)


@bp.get("/")
def index():
    return "Hello from Main"


# TODO: build a GET endpoint which provides the HTML content that allows users to hit the /hi endpoint.
# will be interesting to figure out how to style and size the content
@bp.post("/hi")
def say_hi():
    cxn = get_db()
    insert_query = "insert into Hellos default values;"
    count_query = "select count(*) as hello_count from Hellos;"

    cxn.execute(insert_query)
    count = cxn.execute(count_query).fetchone()["hello_count"]
    cxn.commit()

    return f"Thanks for giving us Hello #{count}"
