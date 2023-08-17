# %%
import pandas as pd
import boto3
import os

from io import BytesIO
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer

# %%

# Load the environment file with credentials
dotenv_path = os.path.join(os.path.abspath(''), 'aws-credentials.env')
load_dotenv(dotenv_path)

BUCKET_NAME = "nlp-topic-modeling-project" # S3 bucket name
KEY = 'insurance_journal_articles.parquet'

session = boto3.Session(
        aws_access_key_id=os.environ['aws_access_key_id'],
        aws_secret_access_key=os.environ['aws_secret_access_key']
    )

# Creating S3 resource from Session
s3 = session.resource('s3')

# Create a buffer, which stores the data in memory
buffer = BytesIO()

# Download file from S3
s3.Object(BUCKET_NAME, KEY).download_fileobj(buffer)

# Read the buffer
df = pd.read_parquet(buffer)

# %%
cv = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
