UPDATE recallsraw
SET impacted_product = 'None given'
WHERE impacted_product IS NULL;

SELECT * FROM recallsraw;

SELECT * FROM recallsraw;

DROP TABLE IF EXISTS locations;
CREATE TABLE locations (location_id SERIAL, location VARCHAR, PRIMARY KEY(location));
SELECT DISTINCT location FROM recallsraw;
INSERT INTO locations (location) SELECT DISTINCT location from recallsraw;


-- ALTER TABLE recalls1nf
-- ADD PRIMARY KEY (recall_id, impacted_products, location); -- Officially set to First Normal Form