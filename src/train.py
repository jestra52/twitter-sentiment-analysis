# packages
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
import pickle
import re
import sys
# Local packages
from format_dataset import FormatDataset

DATASET_DIR = sys.argv[1]
N_GRAM = 2

format_ds = FormatDataset()
train_tweets, test_tweets = format_ds.load_train_test_imdb_data(DATASET_DIR)

print('TRAIN REVIEW TWEETS:\n', train_tweets.head(10), '\n')
print('TEST REVIEW TWEETS:\n', test_tweets.head(10), '\n')

# Transform each review into TF-IDF vector
print('Cleaning and vectorizing reviews with n_gram size=%s...' % N_GRAM, '\n')

tfidf_vectorizer = TfidfVectorizer(
    ngram_range=(1, N_GRAM),
    preprocessor=format_ds.clear_text,
    stop_words='english')

training_features = tfidf_vectorizer.fit_transform(train_tweets['text'])

pickle.dump(tfidf_vectorizer.vocabulary_, open('reviews_tfidf_features.pkl', 'wb'))
# test_features = vectorizer.transform(test_tweets['text'])

# # Training with SVM
# print('Training with SVM...\n')
# svm = LinearSVC()
# svm.fit(training_features, train_tweets['sentiment'])

# # Testing with SVM
# print('Testing with SVM...')
# y_pred_svm = svm.predict(test_features)
# acc_svm = accuracy_score(test_tweets['sentiment'], y_pred_svm)
# print('SCORE: %s' % (acc_svm * 100))
# print('CONFUSION MATRIX: \n', confusion_matrix(test_tweets['sentiment'], y_pred_svm), '\n')

# # Training with MNB
# print('Training with Multinomial Naive-Bayes...\n')
# mnb = MultinomialNB()
# mnb.fit(training_features, train_tweets['sentiment'])

# # Testing with MNB
# print('Testing with Multinomial Naive-Bayes...')
# y_pred_mnb = mnb.predict(test_features)
# acc_mnb = accuracy_score(test_tweets['sentiment'], y_pred_mnb)
# print('SCORE: %s' % (acc_mnb * 100))
# print('CONFUSION MATRIX: \n', confusion_matrix(test_tweets['sentiment'], y_pred_mnb), '\n')
