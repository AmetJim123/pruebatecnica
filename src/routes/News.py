
from flask import Blueprint, jsonify, request
import uuid
from decouple import config
import traceback

#Entities
from models.entities.noticia import Noticia

#Models
from models.NewsModels import NewsModels

news_bp = Blueprint('news_bp', __name__)
health_bp = Blueprint('health_bp', __name__)

@health_bp.route('/', methods=['GET'])
def health():
    return jsonify({"status": "ok",
                    "message": "News service is running",
                    'environment': config('ENVIRONMENT')})

@news_bp.route("/add", methods=['POST'])
def add_user():
    try:
        id = uuid.uuid4()
        title = request.json['Título']
        description = request.json['Descripción']

        new=Noticia(str(id),title,description)
        affected_rows = NewsModels.add_news(new)

        if affected_rows ==1:
            return jsonify({'Message': 'News created susccessfuly'})
        else:
            return jsonify({'Message': 'Error during creation '}), 500
    except Exception as e:
        return jsonify({'Message': str(e)}), 500

@news_bp.route("/<id>")
def get_new(id):
    try:
        news = NewsModels.get_new(id)
        if news != None:
            return jsonify(news)
        else:
            return jsonify({'Message': 'News not found'}), 404
    except Exception as e:
        print(traceback.print_exc())
        return jsonify({'Message': str(e)},500)

@news_bp.route("/all_news")
def get_news():
    try:
        news = NewsModels.get_news()
        return jsonify(news)
    except Exception as e:
        return jsonify({'Message': str(e)},500)


@news_bp.route("/update/<id>", methods = ['PUT'])
def update_new(id):
    try:
        title = request.json['Título']
        description = request.json['Descripción']
        news = Noticia(id, title, description)
        affected_rows = NewsModels.update_news(news)
        
        if affected_rows == 1:
            return jsonify({'Message': 'News updated susccessfuly',
                            'News': news.to_json()})
        else:
            return jsonify({'Message': 'News not found'}), 404
    except Exception as e:
        return jsonify({'Message': str(e)},500)

@news_bp.route("/delete/<id>", methods = ['DELETE'])
def delete_news(id):
    try:
        affected_rows = NewsModels.delete_news(id)
        
        if affected_rows == 1:
            return jsonify({"Message": "News has been delete"})
        else:
            return jsonify({'Message': 'News not found'}), 404
    except Exception as e:
        return jsonify({'Message': str(e)},500)