import re

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

clean_reviews = clear_reviews(train_tweets, test_tweets)
clean_train_reviews = clean_reviews['clean_train_reviews']
clean_test_reviews = clean_reviews['clean_test_reviews']

print('First clean train review:\n', clean_train_reviews[0], '\n')
print('First clean test review:\n', clean_test_reviews[0], '\n')
