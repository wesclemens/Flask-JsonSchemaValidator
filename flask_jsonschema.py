"""
 Simple JSON Schema validator for Flask.
"""

import decorators
import jsonschema
import flask

from werkzeug.exceptions import HTTPException


def _json_path_to_string(path):
    formated_path = "(root)"
    for part in path:
        if isinstance(part, int):
            formated_path = "{0}[{1}]".format(formated_path, part)
        else:
            formated_path = "{0}.{1}".format(formated_path, part)
    return formated_path


class validator(decorators.FuncDecorator):
    """
    Simple decorator for validating json request.
    """
    def decorate(self, func, schema, force=False, *dec_a, **dec_kw):
        def decorator(*args, **kwargs):
            if flask.request.mimetype == 'application/json' or force:
                try:
                    jsonschema.validate(
                        flask.request.get_json(force=force),
                        schema,
                        )
                except jsonschema.ValidationError as err:
                    for foo in err.absolute_path:
                        print foo
                    return flask.jsonify(
                        status=400,
                        status_message="Bad Request",
                        error_message=err.message,
                        error_path=_json_path_to_string(err.absolute_path),
                        ), 400
                except HTTPException:
                    return flask.jsonify(
                        status=400,
                        status_message="Bad Request",
                        error_message="Failed to decode request body.",
                        error_path=None,
                        ), 400
            return func(*args, **kwargs)
        return decorator
