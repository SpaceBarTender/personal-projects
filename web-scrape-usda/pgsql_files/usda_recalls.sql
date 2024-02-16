UPDATE recalls1nf
SET impacted_products = 'None given'
WHERE impacted_products IS NULL;

ALTER TABLE recalls1nf
ADD PRIMARY KEY (recall_id, impacted_products, location); -- Officially set to First Normal Form