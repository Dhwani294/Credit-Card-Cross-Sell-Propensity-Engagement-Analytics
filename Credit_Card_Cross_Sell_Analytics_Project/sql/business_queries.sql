
-- 1. Month-over-Month Spend Trends
SELECT
    months_on_book,
    SUM(total_trans_amt) AS total_spend
FROM credit_customers
GROUP BY months_on_book
ORDER BY months_on_book;

-- 2. Top Spend Categories Proxy
SELECT
    card_category,
    AVG(total_trans_amt) AS avg_spend
FROM credit_customers
GROUP BY card_category
ORDER BY avg_spend DESC;

-- 3. Engagement Scoring
SELECT
    clientnum,
    engagement_score
FROM credit_customers
ORDER BY engagement_score DESC
LIMIT 20;

-- 4. Cohort Analysis
SELECT
    months_on_book,
    COUNT(*) AS customers
FROM credit_customers
GROUP BY months_on_book;

-- 5. Dormant vs Active Customers
SELECT
    CASE
        WHEN total_trans_ct < 40 THEN 'Dormant'
        ELSE 'Active'
    END AS customer_status,
    COUNT(*) AS total_customers
FROM credit_customers
GROUP BY customer_status;

-- 6. Cross-Sell Opportunity Sizing
SELECT
    COUNT(*) AS high_propensity_customers
FROM credit_customers
WHERE cross_sell_target = 1;
