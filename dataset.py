import json
import pandas as pd

DATA_DIR = './data/'
DATA_FILE = DATA_DIR + 'news_train.data'

def load_news_dataset():
    data = []
    with open(DATA_FILE) as f:
        content = f.readlines()
        for i in range(len(content)):
            txt = content[i]
            data_dict = json.loads(txt)

            category = data_dict['category']
            headline = data_dict['headline']
            authors = data_dict['authors']
            link = data_dict['link']
            short_description = data_dict['short_description']
            date = data_dict['date']

            data.append({'id': i, 'category': category, 'headline': headline, 'authors': authors, 'link': link,
                         'short_description': short_description, 'date': date})

    return pd.DataFrame(data)

