from flask import Blueprint, Response, make_response

home_bp = Blueprint('root', __name__)


@home_bp.route("/", methods=["GET"])
@home_bp.route("/home", methods=["GET"])
def do_get_home() -> Response:
    """
    Gets home page.
    """
    return make_response("<p>Apish home</p>", 200)
