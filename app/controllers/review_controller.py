from flask import Blueprint, jsonify, request
from models.review import Review
from services.review import ReviewService

review_controller = Blueprint('review', __name__)

@review_controller.route('/create', methods=['POST'])
def create_review():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Введите текст для анализа!"}), 400

    sentiment = ReviewService.analyze_text(data['text'])
    created_review = Review.create_review(data['text'], sentiment)
    return jsonify(created_review), 201


@review_controller.route('/get', methods=['GET'])
def get_reviews():
    sentiment_filter = request.args.get('sentiment')
    reviews = Review.get_reviews(sentiment=sentiment_filter)
    return jsonify(reviews)