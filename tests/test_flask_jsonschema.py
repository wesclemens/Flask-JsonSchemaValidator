import flask
import os
import tempfile
import unittest
import json

from flask.ext.jsonschema import validate

class JsonSchema(unittest.TestCase):
    def setUp(self):
        test_app = flask.Flask("test_app")

        @test_app.route('/',methods=['POST'])
        @validate({
                    'type': 'object',
                    'properties': {
                        'string': {'type': 'string'},
                    },
                    'required': ['string',],
                })
        def index():
            return flask.jsonify(status="Success")

        @test_app.route('/force',methods=['POST'])
        @validate({
                    'type': 'object',
                    'properties': {
                        'string': {'type': 'string'},
                    },
                    'required': ['string',],
                }, force=True)
        def force():
            return flask.jsonify(status="Success")

        self.client = test_app.test_client()
        self.app = test_app

    def tearDown(self):
        pass

    def test_valid_request(self):
        rv = self.client.post(
                path='/',
                data='{"string": "True"}',
                content_type='application/json')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(json.loads(rv.data)['status'], 'Success')

    def test_invalid_request(self):
        rv = self.client.post('/',
                data='{"string": 123}',
                content_type='application/json')
        self.assertEqual(rv.status_code, 400)
        self.assertNotEqual(json.loads(rv.data)['status'], 'Success')

    def test_force_options(self):
        rv = self.client.post('/force',
                data='{"string": 123}')
        self.assertEqual(rv.status_code, 400)
        self.assertNotEqual(json.loads(rv.data)['status'], 'Success')

if __name__ == '__main__':
    unittest.main()
