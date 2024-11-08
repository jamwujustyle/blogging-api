from api import get_articles
from db import get_connection 

articles = get_articles()
table_name = 'articles'

def desctructure_article(article): 
    print('reached checkpoint 4 ')
    name = article.get('source', {}).get('name', 'no name available')
    author = article.get('author', 'no author available')
    title = article.get('title', 'no titlte available')
    description = article.get('description', 'no description available')
    content = article.get('content', 'no content available')
    published_at = article.get('publishedAt', 'no publishedAt available')
    return name, author, title, description, content, published_at


def insert_into_table(name, author, title, description, content, published_at, table_name): 
    query = """
        INSERT INTO articles (uuid, name, author, title, description, content, published_at)
        VALUES (gen_random_uuid(), %s, %s, %s, %s, %s, %s)
            """ 
    try:
      print('reached checkpoint 5')
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute(query, (name, author, title, description, content, published_at))
      conn.commit()
      print(f"inserted into table {table_name}")
      cursor.close()
      conn.close()
    except Exception as ex:
        print(f"error inserting into table {table_name}: {ex}")

def iterate_over_articles():
    print('reached checkpoint 6')
    for article in articles:
        name, author, title, description, content, published_at = desctructure_article(article)
        insert_into_table(name, author, title, description, content, published_at, table_name)

