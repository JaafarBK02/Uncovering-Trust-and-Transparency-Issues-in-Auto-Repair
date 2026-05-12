# Uncovering Trust and Transparency Issues in Auto Repair

## Overview
This project analyzes customer reviews from Bay Area auto repair shops to identify recurring patterns of distrust, overcharging, and poor communication. 
Using NLP and machine learning, we validated that the frustration drivers feel at auto repair shops is not isolated, it is a systemic, measurable, and predictable problem.

This research was conducted as part of CS163 at San Jose State University and 
serves as the data foundation for Whipify, a transparency tool for auto repair 
that was selected as a finalist in the Silicon Valley Innovation Challenge.

## Research Questions & Hypotheses
1. Pricing transparency is a primary driver of negative sentiment
2. Communication quality strongly influences customer satisfaction
3. A small number of complaint categories dominate negative feedback

## Dataset
Source: Yelp reviews collected via Zembra API
Size: 11,022 reviews from 32 Bay Area auto repair shops
Cities: San Francisco, Oakland, San Jose, Berkeley, Fremont, Hayward, Santa Clara, Sunnyvale, Daly City
Negative reviews (1-2 stars): 656 (6%)
Features: star rating, review text, review length, VADER sentiment score

## Key Findings
Pricing & Labor is the #1 complaint category (189 reviews, sentiment: -0.242)
Communication Issues is the 2nd largest category (166 reviews, sentiment: -0.206)
Brake & Repair Quality accounts for 164 reviews (sentiment: -0.214)
Oil Change Problems accounts for 137 reviews (sentiment: -0.215)
VADER sentiment correlates strongly with star ratings (r = 0.57)
Lower rated reviews are longer (r = -0.22), confirming dissatisfied customers write more detailed complaints

## Methods
| Method | Purpose |
|--------|---------|
| VADER Sentiment Analysis | Score each review from -1 to +1 |
| Pearson Correlation | Measure relationships between numeric features |
| LDA Topic Modeling | Identify recurring complaint categories |
| Keyword Frequency Analysis | Validate LDA topics with raw word counts |

## Project Structure

```
1_data_collection.ipynb       Zembra API pipeline to collect Yelp reviews
2_eda.ipynb                   Data loading, cleaning, feature engineering, EDA
3_nlp_analysis.ipynb          VADER, LDA topic modeling, keyword analysis
app.py                        ML inference service
main.py                       Main application entry point
app.yaml                      Deployment configuration
Dockerfile                    Container setup
requirements.txt              Python dependencies
index.html                    Project website
reviews_clean.csv             Cleaned reviews dataset
negative_reviews_with_topics.csv    Negative reviews with LDA topic labels
Final Proposal.pdf            Original project proposal
Preliminary Results.pdf       Preliminary results report
```



## Pipeline

**Pipeline 1 — Data Collection** (1_data_collection.ipynb)
Connects to the Zembra API, searches for auto repair shops across 9 Bay Area cities, creates review scraping jobs, and saves shop and job metadata to Drive.

**Pipeline 2 — EDA** (2_eda.ipynb)
Loads JSON review files from Google Drive, cleans business names, engineers review_length and sentiment_score features, and produces all EDA visualizations.

**Pipeline 3 — NLP Analysis** (3_nlp_analysis.ipynb)
Runs keyword frequency analysis and LDA topic modeling on 656 negative reviews, produces topic distribution and sentiment visualizations.

## How to Run
1. Open each notebook in Google Colab
2. Mount your Google Drive
3. Add your Zembra API key in Pipeline 1
4. Run cells in order

## Tech Stack
Python, Pandas, Matplotlib, Seaborn
VADER (vaderSentiment)
Gensim (LDA)
Zembra API
Google Colab and Google Drive



## Links

Project Website: https://auto-repair-cs163.wl.r.appspot.com/

ML Inference API: https://auto-repair-inference-590605587424.us-west2.run.app/

Whipify: https://whipify.it.com


## Contributors
[Jaafar Ben Khaled](https://github.com/JaafarBK02)
[fnuhasham](https://github.com/fnuhasham)

## Related
[Whipify](https://whipify.it.com) — The transparency tool built on these insights




