# Insurance News Topic Modeling and Clustering

Click [HERE](https://github.com/choijin/NLP_Topic_Modeling) to see the full and detailed script

## Table of Contents

1. [Project Overview](#project-overview)
2. [Objectives](#objectives)
3. [Data Preparation](#data-preparation)
4. [Topic Modeling](#topic-modeling)
5. [Advanced Modeling Techniques](#advanced-modeling-techniques)
6. [Evaluation Metrics](#evaluation-metrics)
7. [Results](#results)
8. [Applications in the Insurance Industry](#applications-in-the-insurance-industry)

## Project Overview

This project aims to use NLP to categorize and understand insurance news articles scraped from a news website. The goal is to use NLP to derive actionable insights and trends from these articles that could inform business decisions. LDA, which stands for Latent Dirichlet Allocation, helps in capturing underlying themes in the data which might not be immediately apparent. These themes can be crucial in understanding behavior or trends that are predictive of certain outcomes. Advanced analysis was conducted to improve upon the baseline LDA model, by adding a K-means cluster and later a BERT model.

![](/images/project_pipeline.png) 

## Objectives

1. Webscrape and collect news articles and store in S3.
2. Perform topic modeling using LDA model and improve upon baseline using K-means Clustering and BERT.
3. Evaluate its performance using various metrics such as topic coherence and silhouette score.
4. Visualize the word importance per topic and summarize each articles using BART.

## Data Preparation

### Data and Web Scraping

* The data was collected from `https://www.insurancejournal.com/news/national/`, an insurance journal news website. 
* Utilized BeautifulSoup to scrape news articles.
* Converted articles scraped into parquet format.

### Data Storage

* Used boto3 API to save scraped data into S3 buckets.
* Credentials were securely managed using `.env` files. This allows users to retrieve credentials without hard-coding them.
* To enure the code runs, you must have a `.env` file in the same directory as other files, and that you provide your AWS access key and secret key.

### Data Cleaning and Vectorization

* Used `Spacy` to lemmatize and keep only alphanumeric words, filtering out unnecessary characters and words.
* Applied `Count Vectorizer` to convert articles into numerical vectors.

## Topic Modeling

### LDA (Latent Dirichlet Allocation)

* Applied `LDA` to create a topic distribution matrix and identified the most probable topic for each document. Classified text documents into multiple topics.
* Generated `word plots` to understand the relevance and importance of each word to its topic.

### Evaluation Metrics

* `Silhouette Score`: Measures the similarity of each sample in one cluster to the samples in the neighboring clusters.
* `Topic Coherence`: Measures the semantic similarity between high-scoring words within a topic.
* `Topic Diversity`: Measures how distinct each topic is compared to the others, aiming for more diverse topics.

## Advanced Modeling Techniques

`K-means Clustering`: Used K-means clustering on the document-topic matrix to further segment articles. K-means clustering was used to refine the LDA topics and find nuanced groupings.

`BERT (Bidirectional Encoder Representations from Transformers)`: Applied BERT and combined its embeddings with LDA topics and K-means clusters to create more contextual embeddings.

`UMAP (Uniform Manifold Approximation and Projection)`: Used UMAP to reduce the feature space of BERT embeddings for easier computation and analysis. Hyper-parameter tuned the components to find the most useful components for clustering.

`BART (Bidirectional and Auto-Regressive Transformers)`: Used BART to generate summaries of each article to summarize the articles for easier understanding and verification.

## Applications

The topics generated from this project can be invaluable for business strategy in the insurance sector. Understanding what themes and issues are prevalent in insurance news can guide companies in their marketing strategies, product development, and customer engagement efforts. Furthermore, the advanced NLP techniques used here are skills that are highly valued in data-driven industries like insurance for deriving actionable insights from large volumes of data.

* Behavioral Differences: Once these clusters are identified, the researchers can further study if there are differences in customer behavior across these clusters. For example, the "fire related claims" cluster might have a higher loss ratio compared to the "storm related claims" cluster.

* Tailored Marketing: Companies can use this information for targeted marketing. If a user falls into the "fire related claims" cluster, they might receive more focused ratings that deals with fire claims.

# End
