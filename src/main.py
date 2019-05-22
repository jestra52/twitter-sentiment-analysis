# packages
import pickle

review = 'Wow. #AvengersEndgame is staggering. It’s surprising in ways I never saw coming and satisfying in ways I didn’t realize I needed. It’s kind of the ultimate gift to fans of the MCU. It’s very long and has a few hiccups, but is everything you’re hoping for and more.'

tfidf_vectorizer = pickle.load(open('tfidf_model.pkl', 'rb'))
svm = pickle.load(open('reviews_svm_model.pkl', 'rb'))
mnb = pickle.load(open('reviews_mnb_model.pkl', 'rb'))

review_vector = tfidf_vectorizer.transform([ review ])
svm_review_result = 'Good movie' if svm.predict(review_vector)[0] == 1 else 'Bad movie'
mnb_review_result = 'Good movie' if mnb.predict(review_vector)[0] == 1 else 'Bad movie'

print('REVIEW:\n', review)
print('Result with SVM:', svm_review_result)
print('Result with Multinomial Naive-Bayes:', mnb_review_result)
