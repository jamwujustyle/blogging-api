from api import get_articles
from db import get_connection, release_connection
import logging



table_name = 'articles'

def destructure_article(article): 
    name = article.get('source', {}).get('name', 'no name available')
    author = article.get('author', 'no author available')
    title = article.get('title', 'no titlte available')
    description = article.get('description', 'no description available')
    content = article.get('content', 'no content available')
    published_at = article.get('publishedAt', 'no publishedAt available')
    return (name, author, title, description, content, published_at)


def batch_insert_articles(articles_batch): 
    query = """
        INSERT INTO articles (uuid, name, author, title, description, content, published_at)
        VALUES (gen_random_uuid(), %s, %s, %s, %s, %s, %s)
        ON CONFLICT (uuid) DO NOTHING
            """ 
    conn = None
    try:
      conn = get_connection()
      cursor = conn.cursor()
      cursor.executemany(query, articles_batch)
      conn.commit()
      logging.info(f'inserted batch of {len(articles_batch)} into table {table_name}')
      cursor.close()
    except Exception as ex:
        logging.error(f'error in batch insert: {ex}')
    finally:
        if conn:
            release_connection(conn)

def iterate_over_articles(batch_size=10):
    articles_batch = []
    articles = get_articles()
    logging.info(f"Retrieved {len(articles)} articles")

    for article in articles:
        articles_batch.append(destructure_article(article))
        if(len(articles_batch) == batch_size):
            batch_insert_articles(articles_batch)
            articles_batch = []

    if articles_batch:
        batch_insert_articles(articles_batch)