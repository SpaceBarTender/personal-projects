-- Handle null values
UPDATE recallsraw
SET impacted_product = 'None given'
WHERE impacted_product IS NULL;


ALTER TABLE recallsraw
ADD COLUMN impacted_product_id INT;

DROP TABLE IF EXISTS impacted_products;
CREATE TABLE impacted_products (impacted_product_id SERIAL, impacted_product VARCHAR, PRIMARY KEY(impacted_product_id));
SELECT DISTINCT impacted_product FROM recallsraw;
INSERT INTO impacted_products (impacted_product) SELECT DISTINCT impacted_product FROM recallsraw;


UPDATE recallsraw
SET impacted_product_id = (SELECT impacted_products.impacted_product_id FROM impacted_products WHERE impacted_products.impacted_product = recallsraw.impacted_product);


SELECT * FROM recallsraw