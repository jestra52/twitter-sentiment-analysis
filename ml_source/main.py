# packages
from flask import Flask, jsonify, make_response, request, redirect
import pickle

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    if request.method == 'GET':
        review = request.args.get('review')
        
        if review:
            tfidf_vectorizer = pickle.load(open('tfidf_model.pkl', 'rb'))
            svm = pickle.load(open('reviews_svm_model.pkl', 'rb'))
            # mnb = pickle.load(open('reviews_mnb_model.pkl', 'rb'))

            review_vector = tfidf_vectorizer.transform([ review ])
            svm_review_result = 'Good movie' if svm.predict(review_vector)[0] == 1 else 'Bad movie'
            # mnb_review_result = 'Good movie' if mnb.predict(review_vector)[0] == 1 else 'Bad movie'

            return make_response(jsonify({
                'sentiment': svm_review_result,
                'review': review,
                'status_code': 200
            }), 200)

        return make_response(jsonify({ 'error':'There was an error!', 'status_code':500 }), 500)

if __name__ == '__main__':
    app.run()
