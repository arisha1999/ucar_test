from flask import Flask
from controllers.review_controller import review_controller
from models.review import Review

app = Flask(__name__)
app.register_blueprint(review_controller, url_prefix='/api/reviews')
Review.init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0')