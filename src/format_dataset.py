import numpy as np
import os
import pandas as pd
import re

HTML_TAGS = re.compile(r'<.*?>')
SPECIAL_CHARS_NO_SPACE = re.compile(r'[.;:!\'?,\"()\[\]]')
SPECIAL_CHARS_WITH_SPACE = re.compile(r'(<br\s*/><br\s*/>)|(\-)|(\/)')

class FormatDataset:
    def load_train_test_imdb_data(self, data_dir):
        data = {}

        for split in ['train', 'test']:
            data[split] = []

            for sentiment in ['neg', 'pos']:
                score = 1 if sentiment == 'pos' else 0
                path = os.path.join(data_dir, split, sentiment)
                file_names = os.listdir(path)

                for f_name in file_names:
                    with open(os.path.join(path, f_name), 'r') as f:
                        review = f.read()
                        data[split].append([review, score])

        np.random.shuffle(data['train'])        
        data['train'] = pd.DataFrame(data['train'], columns=['text', 'sentiment'])

        np.random.shuffle(data["test"])
        data['test'] = pd.DataFrame(data['test'], columns=['text', 'sentiment'])

        return data['train'], data['test']

    def clear_text(self, text):
        text = HTML_TAGS.sub('', text.lower())
        text = SPECIAL_CHARS_NO_SPACE.sub('', text)
        text = SPECIAL_CHARS_WITH_SPACE.sub('', text)
        return text

