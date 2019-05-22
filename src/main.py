# packages
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
import numpy as np
import pickle
# Local packages
from format_dataset import FormatDataset

format_ds = FormatDataset()
loaded_vec = TfidfVectorizer(
    vocabulary=pickle.load(open('reviews_tfidf_features.pkl', 'rb')))

print(loaded_vec)

# svm = LinearSVC()
# svm.fit(loaded_vec.get_feature_names(), loaded_vec.vocabulary)

# # Testing with SVM
# print('Testing with SVM...')
# y_pred_svm = svm.predict(docs_vec)
# acc_svm = accuracy_score(test_tweets['sentiment'], y_pred_svm)
# print('SCORE: %s' % (acc_svm * 100))
# print('CONFUSION MATRIX: \n', confusion_matrix(test_tweets['sentiment'], y_pred_svm), '\n')