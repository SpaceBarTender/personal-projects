UPDATE recallsraw
SET impacted_product = 'None given'
WHERE impacted_product IS NULL;

SELECT * FROM recallsraw;

-- ALTER TABLE recalls1nf
-- ADD PRIMARY KEY (recall_id, impacted_products, location); -- Officially set to First Normal Form