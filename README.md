
# Credit Card Cross-Sell Propensity & Engagement Analytics

## Overview
This project simulates a real-world fintech analytics workflow inspired by commercial card and customer engagement analytics teams.


The project focuses on:
- Customer engagement analytics
- Credit card spend behavior analysis
- Cross-sell propensity modeling
- Customer segmentation
- ETL pipeline automation
- SQL business intelligence analytics
- Dashboard reporting

## Business Objective
Identify high-value customers most likely to adopt a second financial product using transaction behavior, engagement metrics, and customer segmentation.
---

## Dataset Recommendation

### Dataset
Credit Card Customers Dataset (Kaggle)

### Link
https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

### Suggested File
BankChurners.csv

---

## Project Architecture

```

data/
├── raw/
├── processed/

src/
├── etl_pipeline.py
├── segmentation.py
├── propensity_model.py
├── dashboard.py

sql/
├── business_queries.sql

reports/
├── executive_summary.md

dashboard/
├── dashboard_guide.md

requirements.txt
README.md

```

---

## Key Features

### ETL Pipeline
- Missing value handling
- Outlier detection
- Feature engineering
- Spend velocity calculation
- Engagement score generation
- Category mix analysis

### Customer Segmentation
- RFM Analysis
- KMeans clustering
- Engagement tier classification

### Cross-Sell Propensity Modeling
Models:
- Logistic Regression
- XGBoost

Evaluation Metrics:
- Accuracy
- Precision
- Recall
- ROC-AUC

### SQL Analytics Layer
Includes:
- MoM spend trends
- Top spend categories
- Cohort analysis
- Engagement scoring
- Dormant vs active users
- Cross-sell opportunity sizing

### Dashboard
Visualizations:
- Segment distribution
- Propensity score distribution
- Spend trend over time
- Category spend breakdown
- Engagement funnel

---

## Suggested Resume Bullet

Built an end-to-end fintech analytics platform for credit card engagement and cross-sell propensity modeling using Python, SQL, Machine Learning, and Power BI-style analytics. Analyzed customer behavior, segmented users using RFM + KMeans clustering, and identified high-value cross-sell opportunities using Logistic Regression and XGBoost models.

---

## How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Place Dataset
Download the Kaggle dataset and place:
`BankChurners.csv`
inside:
`data/raw/`

### 3. Run ETL
```bash
python src/etl_pipeline.py
```

### 4. Run Segmentation
```bash
python src/segmentation.py
```

### 5. Run Propensity Modeling
```bash
python src/propensity_model.py
```

### 6. Run Dashboard
```bash
python src/dashboard.py
```

---

## Expected Outputs
- Customers analyzed: ~10,000+
- Segments identified: 3–5
- Cross-sell opportunities identified
- Engagement score distribution
- Model performance metrics
- SQL business insights
- Visual analytics dashboard

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SQLite
- Matplotlib
- Seaborn
- SQL
