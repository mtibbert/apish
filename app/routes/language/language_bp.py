from flask import Blueprint, Response, make_response, request
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.database.models.language import Language
import json

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


@language_bp.route("/language", methods=["POST"])
def do_post() -> Response:
    """
    Create new Language item.

    :return: Response with a json list of Language items
    """
    if request.method == 'POST':
        _res: Response
        item = Language(language=request.json["language"],
                        description=request.json["description"])
        try:
            db.session.add(item)
            db.session.commit()
            _res = make_response()
            _res.status_code = 201
            _res.headers["location"] = item.id.__str__()
        except SQLAlchemyError:
            _res = make_response({
                "message": f'Unable to create using ' +
                           f'{json.dumps(request.json)}'},
                400)
        return _res


@language_bp.route("/language/<language_id>", methods=["PUT"])
def do_put(language_id: str) -> Response:
    """

    Update Language item.

    :param language_id:
    :return: Language object, as JSON, with status code 200 if successful
    """
    idx = int(language_id.__str__())
    response = make_response({
        "message": f'Unprocessable Content: ' +
                   f'Invalid Language id ({language_id}).'},
        422)
    if idx > 0:
        item = Language.query.filter_by(id=idx).first()
        if item:
            if request.json["language"]:
                item.language = request.json["language"]
            if request.json["description"]:
                item.description = request.json["description"]
            db.session.commit()
            response = make_response(item.as_dict(), 200)
        else:
            response = make_response({
                "message": f'Not Found: {language_id}'},
                404)

    return response


@language_bp.route("/language/<language_id>", methods=["DELETE"])
def do_delete(language_id: str) -> Response:
    """

    Delete Language item.

    :param language_id:
    :return: Language object, as JSON, with status code 200 if successful
    """
    idx = int(language_id.__str__())
    response = make_response({
        "message": f'Unprocessable Content: ' +
                   f'Invalid Language id ({language_id}).'},
        422)
    if idx > 0:
        item: Language = Language.query.filter_by(id=idx).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            response = make_response(item.as_dict(), 200)
        else:
            response = make_response({
                "message": f'Not Found: {language_id}'},
                404)

    return response
