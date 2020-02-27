import json
import pandas as pd

def load_news_dataset(datafile):
    data = []
    with open(datafile) as f:
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

def load_cybertroll_dataset(datafile):
    data = []
    with open(datafile) as f:
        content = f.readlines()
        for i in range(len(content)):
            txt = content[i]
            data_dict = json.loads(txt)
            headline = data_dict['content']
            category = 'USER' if int(data_dict['annotation']['label'][0]) == 0 else 'CYBERTROLL'
            data.append({'id': i, 'category': category, 'headline': headline})

    return pd.DataFrame(data)
