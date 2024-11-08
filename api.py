import requests

api_key = "ca23ea4f74a443f3b8895e4b267784a0"
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

headers = {
    "Accept": "application/json"
}
def get_articles():
    try:
        print('reached checkpoint 1 ')
        response = requests.get(url, headers=headers)
        print('reached checkpoint 2 ')
        
        if response.status_code == 200:
            print('retrieved successfully')
            data = response.json().get('articles', [])
            print(data)
            return data
        else:
            print(f'error retrieving data: {response.status_code}, message: {response.text}')
    except Exception as ex:
        print(f'an error occured: {ex}')

articles = get_articles()
if articles: 
    print('reached checkpoint 3')
else: 
    print('error invoking func')