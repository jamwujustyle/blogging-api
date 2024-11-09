import requests
import logging
api_key = "ca23ea4f74a443f3b8895e4b267784a0"
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

headers = {
    "Accept": "application/json"
}
def get_articles():
    try:
        logging.info('starting request for articles')
        response = requests.get(url, headers=headers)
        logging.info('API request completed')        
        if response.status_code == 200:
            data = response.json().get('articles', [])
            logging.info(f'retrieved {len(data)} articles successfully')
            return data
        else:
            logging.error(f'error retrieving data: {response.status_code}, message: {response.text}')
            return []
    except Exception as ex:
        logging.error('exception occured during api request {ex}')
        return []