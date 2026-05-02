
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/processed/processed_credit_data.csv")

rfm = df[[
    'months_on_book',
    'total_trans_ct',
    'total_trans_amt'
]].copy()

rfm.columns = ['recency', 'frequency', 'monetary']

scaler = StandardScaler()
scaled = scaler.fit_transform(rfm)

kmeans = KMeans(n_clusters=3, random_state=42)
rfm['segment'] = kmeans.fit_predict(scaled)

segment_map = {
    0: 'High Engagement',
    1: 'Medium Engagement',
    2: 'Low Engagement'
}

rfm['segment_name'] = rfm['segment'].map(segment_map)

rfm.to_csv("data/processed/customer_segments.csv", index=False)

print(rfm['segment_name'].value_counts())
print("Customer segmentation completed.")
