# Uncovering Trust and Transparency Issues in Auto Repair

## What is this repo?
This project uses NLP and machine learning to analyze 11,022 Yelp reviews from 
32 Bay Area auto repair shops. The goal is to identify recurring patterns of 
overcharging, poor communication, and dishonest repairs, and validate that these 
frustrations are not isolated experiences but a systemic, measurable industry problem.

This research was conducted as part of CS163 at San Jose State University and serves 
as the data foundation for our personal project called Whipify, a transparency tool for auto repair selected as 
a finalist in the Silicon Valley Innovation Challenge.

Project Website: https://auto-repair-cs163.wl.r.appspot.com/
ML Inference API: https://auto-repair-inference-590605587424.us-west2.run.app/
additional link for curious people: Whipify: https://whipify.it.com

## Research Questions & Hypotheses
1. Pricing transparency is a primary driver of negative sentiment
2. Communication quality strongly influences customer satisfaction
3. A small number of complaint categories dominate negative feedback

## Key Findings
Pricing & Labor is the #1 complaint category
- 189 reviews | Sentiment: -0.242
Communication Issues is the 2nd largest category
- 166 reviews | Sentiment: -0.206
Brake & Repair Quality
- 164 reviews | Sentiment: -0.214
Oil Change Problems
- 137 reviews | Sentiment: -0.215
VADER sentiment strongly correlates with star ratings
- r = 0.57
Lower-rated reviews are longer
- r = -0.22
- Dissatisfied customers tend to leave more detailed feedback

## Dataset
Source: Yelp reviews collected via Zembra API
Size: 11,022 reviews from 32 Bay Area auto repair shops
Cities: San Francisco, Oakland, San Jose, Berkeley, Fremont, Hayward, 
Santa Clara, Sunnyvale, Daly City
Negative reviews (1-2 stars): 656 (6%)
Features: star rating, review text, review length, VADER sentiment score
Cloud Storage: dataset is stored in Google Cloud Storage and consumed by the 
inference service and website at runtime

## Project Structure

1_data_collection.ipynb          Zembra API pipeline to collect Yelp reviews
2_eda.ipynb                      Data loading, cleaning, feature engineering, EDA
3_nlp_analysis.ipynb             VADER, LDA topic modeling, keyword analysis
app.py                           ML inference service (Flask API, input/output below)
main.py                          Main application entry point
app.yaml                         Google AppEngine deployment configuration
Dockerfile                       Container setup for Cloud Run inference service
requirements.txt                 Python dependencies
index.html                       Project website (hosted on AppEngine)
reviews_clean.csv                Cleaned reviews dataset (11,022 reviews)
negative_reviews_with_topics.csv Negative reviews with LDA topic labels
Final Proposal.pdf               Original project proposal
Preliminary Results.pdf          Preliminary results report


## Pipeline

**Pipeline 1 — Data Collection** (1_data_collection.ipynb)
Connects to the Zembra API, searches for auto repair shops across 9 Bay Area 
cities, creates Yelp review scraping jobs, and saves shop and job metadata to 
Google Drive as CSV files.

**Pipeline 2 — EDA** (2_eda.ipynb)
Loads JSON review files from Google Drive, cleans business names, engineers 
review_length and sentiment_score features via VADER, and produces all EDA 
visualizations including rating distribution, box plots, scatter plot, and 
correlation heatmap.

**Pipeline 3 — NLP Analysis** (3_nlp_analysis.ipynb)
Runs keyword frequency analysis and LDA topic modeling on 656 negative reviews, 
assigns dominant topics to each review, and produces topic distribution and 
sentiment per topic visualizations. Saves final labeled dataset to Drive.

## System Design

The system has 3 connected components:

**Website** hosted on Google AppEngine
Reads dataset from Google Cloud Storage at page load to render 
analysis results and visualizations.

**Google Cloud Storage**
Stores reviews_clean.csv (11,022 reviews) and 
negative_reviews_with_topics.csv (656 labeled reviews).
Both files are consumed by the website and inference service at runtime.

**ML Inference Service** hosted on Google Cloud Run (Dockerized Flask API)
Loads LDA model and VADER at startup.
Input: POST /predict with raw review text
Output: predicted complaint topic + VADER sentiment score
GET /health for health checks
Scales automatically with traffic.

## Inference Service
Location: app.py + Dockerfile
The inference service is a Flask API deployed on Google Cloud Run.

Input: POST request with raw review text
Output: predicted complaint topic (Pricing & Labor, Communication Issues, 
Brake & Repair Quality, or Oil Change Problems) + VADER sentiment score

Endpoints:
POST /predict — takes review text, returns topic and sentiment
GET /health — health check endpoint

The Docker container loads the trained LDA model and VADER sentiment analyzer 
at startup. The website calls this service to classify new reviews in real time.

## Data Stored in the Cloud
Storage: Google Cloud Storage bucket — auto-repair-dataset-cs163

Files stored:
reviews_clean.csv — 11,022 cleaned Yelp reviews
https://storage.googleapis.com/auto-repair-dataset-cs163/reviews_clean.csv

negative_reviews_with_topics.csv — 656 negative reviews with LDA topic labels
https://storage.googleapis.com/auto-repair-dataset-cs163/negative_reviews_with_topics.csv

How it is consumed: the project website reads these files from GCS at page load 
to render the analysis results and visualizations. The inference service also 
reads the data at startup to initialize the model.

## How to Run
1. Open each notebook in Google Colab
2. Mount your Google Drive
3. Add your Zembra API key in Pipeline 1
4. Run cells in order: 1_data_collection > 2_eda > 3_nlp_analysis

## Methods
| Method | Purpose |
|--------|---------|
| VADER Sentiment Analysis | Score each review from -1 to +1 |
| Pearson Correlation | Measure relationships between numeric features |
| LDA Topic Modeling | Identify recurring complaint categories |
| Keyword Frequency Analysis | Validate LDA topics with raw word counts |

## Tech Stack
Python, Pandas, Matplotlib, Seaborn
VADER (vaderSentiment)
Gensim (LDA)
Flask (inference API)
Docker (containerization)
Google AppEngine (website hosting)
Google Cloud Run (inference service)
Google Cloud Storage (dataset storage)
Zembra API (data collection)

## Contributors
[Jaafar Ben Khaled](https://github.com/JaafarBK02)
[fnuhasham](https://github.com/fnuhasham)





































