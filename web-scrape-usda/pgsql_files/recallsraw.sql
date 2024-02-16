UPDATE recallsraw
SET impacted_product = 'None given'
WHERE impacted_product IS NULL;

ALTER TABLE recallsraw
ADD COLUMN location_id INT;

SELECT * FROM recallsraw;


DROP TABLE IF EXISTS locations;
CREATE TABLE locations (location_id SERIAL, location VARCHAR, PRIMARY KEY(location));
SELECT DISTINCT location FROM recallsraw;
INSERT INTO locations (location) SELECT DISTINCT location from recallsraw;

UPDATE recallsraw
SET location_id = (SELECT locations.location_id FROM locations WHERE locations.location = recallsraw.location);

DROP TABLE IF EXISTS impacted_products;
CREATE TABLE impacted_products (impacted_product_id SERIAL, impacted_product VARCHAR, PRIMARY KEY(impacted_product_id));
SELECT DISTINCT impacted_product FROM recallsraw;
INSERT INTO impacted_products (impacted_product) SELECT DISTINCT impacted_product FROM recallsraw;

-- ALTER TABLE recalls1nf
-- ADD PRIMARY KEY (recall_id, impacted_products, location); -- Officially set to First Normal Form