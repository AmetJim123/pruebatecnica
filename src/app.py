from flask import Flask
from config import config
from routes import User, News, Comment
app = Flask(__name__)


def page_not_found(error):
    return "<h1>Page Not Found</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprint
    app.register_blueprint(User.users_bp, url_prefix="/api/users")
    app.register_blueprint(News.news_bp, url_prefix ="/api/news")
    app.register_blueprint(Comment.comment_bp, url_prefix = "/api/comments")
    # ErrorHandler
    app.register_error_handler(404, page_not_found)

    app.run()
