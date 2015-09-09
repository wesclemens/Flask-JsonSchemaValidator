"""
    Simple JSON Schema validator for Flask.

    :copyright: (c) 2015 by William Clemens.
    :license: MIT, see LICENSE for more details.
"""
import flask
import functools
import jsonschema

from werkzeug.exceptions import BadRequest


def _json_path_to_string(path):
    formated_path = "(root)"
    for part in path:
        if isinstance(part, int):
            formated_path = "{0}[{1}]".format(formated_path, part)
        else:
            formated_path = "{0}.{1}".format(formated_path, part)
    return formated_path


def validate(schema, force=False, json_cache=True):
    """Simple decorator for validating JSON request.

    :param schema: python object conforming to JSON schema.
    :param force: forces validation if mimetype is not
                  'application/json'.
    :param json_cache: caches parsed JSON object.  This is recommend as
                       if the request body is going to be used in the
                       request.
    """
    def decorator(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            if flask.request.mimetype == 'application/json' or force:
                try:
                    jsonschema.validate(
                            flask.request.get_json(force=force, cache=json_cache),
                            schema,
                            )
                except jsonschema.ValidationError as err:
                    return flask.jsonify(
                            status=400,
                            status_message="Bad Request",
                            error_message=err.message,
                            error_path=_json_path_to_string(err.absolute_path),
                            ), 400
                except BadRequest as err:
                    return flask.jsonify(
                            status=err.code,
                            status_message=err.name,
                            error_message="Failed to decode request body.",
                            error_path=None,
                            ), err.code

            return func(*args, **kwargs)
        return func_wrapper
    return decorator
