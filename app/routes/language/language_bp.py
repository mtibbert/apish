from flask import Blueprint, Response, make_response
from app.database.models.language import Language

language_bp = Blueprint('language', __name__)


@language_bp.route("/language", methods=["GET"])
def do_get_languages() -> Response:
    """
    Gets all language items.

    :return: Response with a json list of Language items
    """
    languages = Language.query.all()
    res = [language.as_dict() for language in languages]
    return make_response(res, 200)


@language_bp.route("/language/<language_id>", methods=["GET"])
def do_get_language_by_id(language_id: int):
    """
    Gets the language with associated with the language_id

    :param int language_id: Target language_id

    :return: Response with a json Language item if *id* found, otherwise 404 status
    """
    result = Language.query.filter_by(id=language_id).first()
    if result:
        return make_response(result.as_dict(), 200)
    else:
        return make_response({"message": f"Language id '{language_id}' not found"}, 404)
