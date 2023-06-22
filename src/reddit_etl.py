import requests
import pandas as pd
import datetime
import s3fs
import os
import json

dag_path = os.getcwd()
today = datetime.date.today()

def run_extract():

    # Configurações da requisição
    subreddit = 'dataengineering'
    url_template = 'https://www.reddit.com/r/{}/top.json{}'
    params = '?t=day&limit=100'
    headers = { 
        'User-Agent': 'Mozilla/5.0',
    }

    url = url_template.format(subreddit, params)

    # Faz a requisição à API do Reddit
    response = requests.get(url, headers=headers)

    if response.ok:

        posts = response.json()['data']['children']

        with open(f'{dag_path}/top_posts.json', 'w') as file:
            json.dump(posts, file)

    else:
        print(f'Error {response.status_code}')

def run_transform():

    top_posts_list = []

    if not os.path.exists(f'{dag_path}/top_posts.json'):
        raise FileNotFoundError('O arquivo não existe')

    with open(f'{dag_path}/top_posts.json', 'r') as file:
        posts = file.read()

        # Itera sobre os posts e exibe apenas os de formato de texto e cujo link_flair_text é do tipo Career
        for post in posts:
            post_data = post['data']

            # Verifica se o post é do formato de texto e link_flair_text é do tipo Career
            if post_data['is_self'] and post_data['link_flair_text'] == 'Career':
                refined_post = {'author': post_data['author'],
                                'title': post_data['title'],
                                'text': post_data['selftext'],
                                'post_id': post_data['id'],
                                'score': post_data['score'],
                                'date': post_data['created_utc'],
                                'url': 'https://reddit.com' + post_data['permalink']}
                top_posts_list.append(refined_post)

    # Converte a lista obtida para o formato .csv
    os.remove(f'{dag_path}/top_posts.json')
    df = pd.DataFrame(top_posts_list)
    df.to_csv(f'{dag_path}/career_posts.csv')
    
def run_load():

    with open(f'{dag_path}/credentials.txt', 'r') as f:
        credentials = f.read()
        aws_access_key, aws_secret_key = credentials.split(',')

    s3_uri = f's3://reddit_posts/data_engineering/top/{today.year}/{today.month}/{today.day}/career_posts.csv'

    fs = s3fs.S3FileSystem(key=aws_access_key, secret=aws_secret_key)

    with fs.open(s3_uri, 'wb') as s3_file:
        with open(f'{dag_path}/career_posts.csv', 'rb') as local_file:
            s3_file.write(local_file.read())

    os.remove(f'{dag_path}/career_posts.csv')
