from flask import Flask, request
from flask_restful import Resource, Api
from flask import json, Response

from libvoikko import Voikko

app = Flask(__name__)
api = Api(app)

v = Voikko('fi')

class Finnish_text_analysis(Resource):
    def get(self):
        word = request.args.get('word')
        res = self.process(word)
        json_string = json.dumps(res, ensure_ascii=False)
        response = Response(json_string, content_type="application/json; charset=utf-8")
        return response

class Analyze(Finnish_text_analysis):
    def process(self, word):
        return v.analyze(word)

class Spell(Finnish_text_analysis):
    def process(self, word):
        return { "spelling" : v.spell(word) }

class Suggest(Finnish_text_analysis):
    def process(self, word):
        return v.suggest(word)

class Hyphenate(Finnish_text_analysis):
    def process(self, word):
        return { "hyphenated" : v.hyphenate(word), "pattern": v.getHyphenationPattern(word)}

api.add_resource(Analyze, '/analyze')
api.add_resource(Spell, '/spell')
api.add_resource(Suggest, '/suggest')
api.add_resource(Hyphenate, '/hyphenate')

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port='8899')
