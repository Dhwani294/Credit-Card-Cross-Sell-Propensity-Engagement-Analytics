
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/processed_credit_data.csv")
segments = pd.read_csv("data/processed/customer_segments.csv")

plt.figure(figsize=(8,5))
segments['segment_name'].value_counts().plot(kind='bar')
plt.title("Customer Segment Distribution")
plt.xlabel("Segment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("dashboard/segment_distribution.png")

plt.figure(figsize=(8,5))
df['engagement_score'].hist(bins=30)
plt.title("Engagement Score Distribution")
plt.tight_layout()
plt.savefig("dashboard/engagement_distribution.png")

plt.figure(figsize=(8,5))
df['total_trans_amt'].hist(bins=30)
plt.title("Spend Distribution")
plt.tight_layout()
plt.savefig("dashboard/spend_distribution.png")

print("Dashboard visualizations generated.")
