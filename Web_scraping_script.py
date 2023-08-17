# %% 
from bs4 import BeautifulSoup
import requests
import pandas as pd
import boto3
import os
from io import BytesIO
from dotenv import load_dotenv

# %% 
# # Step 1: URL Collection
base_url = "https://www.insurancejournal.com/news/national/"
landing_page = base_url

max_pages = 100
pages_scraped = 0

articles = []
urls = []

while landing_page and pages_scraped < max_pages:
    
    response = requests.get(landing_page)
    doc1 = BeautifulSoup(response.content, 'html.parser')

    # Assuming articles are linked with <a> tags within a specific class, like 'article-link' (this is just an example)
    article_links_full = doc1.select('main.main div.entry a')
    article_links = [link['href'] for link in article_links_full]

    # Step 2: Article Collection
    for url in article_links:

        # Get the HTML content
        page = requests.get(url)
        doc2 = BeautifulSoup(page.content, 'html.parser')
        
        urls.append(url)

        try:
            # Get the title of the article
            title = doc2.find('div', id='article-header').find('h1').get_text()

            # Find the article text, get the paragraphs, and join them together
            article = doc2.find('div', class_='article-content clearfix')
            paragraphs = article.find_all('p')
            content = "\n".join([para.text for para in paragraphs])
            content_title = "\n".join([title, content])

            articles.append(content_title)
            print('Successfully scraped an article...')

        except Exception as e:
            print("Error with article: ", url)
            print("Exception:", e)

    # Step 3: Pagination
    try:
        # Find the next page button
        next_page = doc1.find('div', class_='nav-next').find('a')['href']
        landing_page = next_page
        pages_scraped += 1

        print('\nGoing to the next page...\n')
    
    except:
        print("Next page not found")
        landing_page = None

print('Scraping complete!')

# Step 4: Save to parquet
file_name = 'insurance_journal_articles.parquet'
articles_df = pd.DataFrame(articles, columns=['article'])
articles_df.to_parquet(file_name)

# Step 5: Load to S3
# Load the environment file with credentials
dotenv_path = os.path.join(os.path.dirname(__file__), 'aws-credentials.env')
load_dotenv(dotenv_path)

BUCKET_NAME = "nlp-topic-modeling-project" # S3 bucket name
KEY = file_name # Name of file object

session = boto3.Session(
        aws_access_key_id=os.environ['aws_access_key_id'],
        aws_secret_access_key=os.environ['aws_secret_access_key']
    )

# Creating S3 resource from Session
s3 = session.resource('s3')
s3.create_bucket(Bucket=BUCKET_NAME)

# Create a buffer, which stores the data in memory
buffer = BytesIO()

# Save the dataframe into parquet and save in the buffer
articles_df.to_parquet(buffer)

# Store the file into S3
s3.Object(BUCKET_NAME, KEY).put(Body=buffer.getvalue())