
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score
from xgboost import XGBClassifier

df = pd.read_csv("data/processed/processed_credit_data.csv")

features = [
    'customer_age',
    'months_on_book',
    'credit_limit',
    'total_trans_amt',
    'total_trans_ct',
    'spend_velocity',
    'engagement_score',
    'category_mix'
]

X = df[features]
y = df['cross_sell_target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

lr = LogisticRegression()
lr.fit(X_train, y_train)

lr_preds = lr.predict(X_test)

print("\nLogistic Regression Results")
print("Accuracy:", round(accuracy_score(y_test, lr_preds), 3))
print("Precision:", round(precision_score(y_test, lr_preds), 3))
print("Recall:", round(recall_score(y_test, lr_preds), 3))
print("ROC-AUC:", round(roc_auc_score(y_test, lr_preds), 3))

xgb = XGBClassifier(
    eval_metric='logloss',
    random_state=42
)

xgb.fit(X_train, y_train)

xgb_preds = xgb.predict(X_test)

print("\nXGBoost Results")
print("Accuracy:", round(accuracy_score(y_test, xgb_preds), 3))
print("Precision:", round(precision_score(y_test, xgb_preds), 3))
print("Recall:", round(recall_score(y_test, xgb_preds), 3))
print("ROC-AUC:", round(roc_auc_score(y_test, xgb_preds), 3))

print("\nCross-sell propensity modeling completed.")
