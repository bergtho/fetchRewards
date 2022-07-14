import pytest, json, sys, os
#myPath = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, myPath + '/../')
from app import app # the flask instance

class TestFlask:
    def test_index_route(self):
        resp = app.test_client().get('/')
        
        assert resp.status_code == 200
        assert resp.data.decode('utf-8') == '<h1>Hello, World</h1>'

    def test_capitalize(self):
        word = 'bird'
        resp = app.test_client().get('/capitalize/' + word)
        
        assert resp.data.decode('utf-8') == 'The word is: ' + word


