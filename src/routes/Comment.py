from flask import Blueprint, jsonify, request

#Entities
from models.entities.comentario import Comment

#Models
from models.CommentModels import CommentModels

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route("/add/<id>", methods= ['POST'])
def add_comment(id):
    try:
        comment = request.json['Comentario']
    
        affected_rows = CommentModels.add_comment(id,comment)

        if affected_rows == 1:
            return jsonify({'Message':"Comment added to news"})
        else:
            return jsonify({'Message': 'News not foudn '}), 404
    except Exception as e:
        return jsonify({'Message': str(e)}),500
    
@comment_bp.route('/all_full_notice')
def get_fullnotice():
    try:
        fullnotices = CommentModels.get_fullnews()
        return jsonify(fullnotices)
    except Exception as e: 
        return jsonify({'Message': str(e)})