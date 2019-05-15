from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import nltk
import re

# nltk.download('popular') # execute this only once

SPECIAL_CHARS_NO_SPACE = re.compile(r"[.;:!\'?,\"()\[\]]")
SPECIAL_CHARS_WITH_SPACE = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)")

train_tweets = open('../movie_data/full_train.txt', 'r')
test_tweets = open('../movie_data/full_test.txt', 'r')

def preprocess_reviews(reviews):
    reviews = [SPECIAL_CHARS_NO_SPACE.sub('', line.lower()) for line in reviews]
    reviews = [SPECIAL_CHARS_WITH_SPACE.sub(' ', line) for line in reviews]
    return reviews

def clear_reviews(train, test):
    train_reviews = []
    test_reviews = []

    for tweet in train:
        train_reviews.append(tweet.strip())

    for tweet in test:
        test_reviews.append(tweet.strip())

    return {
        'clean_train_reviews': preprocess_reviews(train_reviews),
        'clean_test_reviews': preprocess_reviews(test_reviews),
    }

def remove_stopwords(corpus):
    eng_stopwords = stopwords.words('english')
    removed_stopwords = []

    for review in corpus:
        removed_stopwords.append(' '.join([
            word for word in review.split() if word not in eng_stopwords
        ]))

    return removed_stopwords

clean_reviews = clear_reviews(train_tweets, test_tweets)
clean_train_reviews = clean_reviews['clean_train_reviews']
clean_test_reviews = clean_reviews['clean_test_reviews']
train_reviews_with_no_sw = remove_stopwords(clean_train_reviews)

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(train_reviews_with_no_sw)
X = tfidf_vectorizer.transform(train_reviews_with_no_sw)
# X_test = tfidf_vectorizer.transform(clean_test_reviews)

# X_train, X_val, y_train, y_val = train_test_split(
#     X, X_test, train_size = 0.75
# )

print(tfidf_vectorizer.get_feature_names())
print(X.shape)
