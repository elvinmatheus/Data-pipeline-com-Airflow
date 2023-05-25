import requests
import pandas as pd
import datetime
import s3fs

def run_reddit_etl():
    today = datetime.date.today()

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

    top_posts_list = []

    # Verifica se a requisição foi bem-sucedida
    if response.ok:
        
        # Obtém os posts retornados
        posts = response.json()['data']['children']

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

    else:
        print(f'Error {response.status_code}')

    # Converte a lista obtida para o formato .csv
    df = pd.DataFrame(top_posts_list)
    df.to_csv(f's3://reddit-etl-project/{today.year}/{today.month}/{today.day}/top_{subreddit}_{today.year}-{today.month}-{today.day}_career_posts.csv')