# Flask-JsonSchemaValidator

Basic JSON Schema Validator for the [Flask](http://flask.pocoo.org/) web framework.

## Usage

Basic usage is to apply the `@validate` decorator to a route. If request validates the route will be called as normal. If the request doesn't validate an error message will be genrated and a `400 BAD REQUEST` will be returned with the error message in the body.

```
validate(schema, force=False, json_cache=True)
```
schema: [jsonschema](http://json-schema.org/) to validate against

force: try to validate request if `Content-Type` is not `applciation/json` 

json_cache: cache json with `flask.request.get_json` 


### Example

```python
from flask_jsonschema import validate

@app.route("/", methods=['POST'])
@validate({
	        'type': 'object',
	        'properties': {
	            'foo': {'type': 'string'},
	            'bar': {'type': 'number'},
	        },
	        'required': ['bar', 'foo'],
	    })
def index_post():
    return flask.jsonify(
            time=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            )
```

#### Valid Request

Request:

```http
POST / HTTP/1.1
Content-Type: application/json
Host: localhost:5000
Content-Length: 26

{"foo":"String","bar":123}
```

Response:

```http
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 35
Server: Werkzeug/0.10.4 Python/3.4.3
Date: Thu, 27 Aug 2015 04:05:24 GMT

{
  "time": "2015-08-27 04:05:24"
}
```
#### Invalid Request

Request:

```http
POST / HTTP/1.1
Content-Type: application/json
Host: localhost:5000
Content-Length: 37

{"foo":"String","bar":"Not a number"}
```

Response:

```http
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 145
Server: Werkzeug/0.10.4 Python/3.4.3
Date: Thu, 27 Aug 2015 03:53:39 GMT

{
  "error_message": "'Not a number' is not of type 'number'",
  "error_path": "(root).bar",
  "status": 400,
  "status_message": "Bad Request"
}
```
