-- Handle null values
UPDATE recallsraw
SET impacted_product = 'None given'
WHERE impacted_product IS NULL;

-- Make impacted products table and insert
-- impacted products id into recallsraw
ALTER TABLE recallsraw
ADD COLUMN impacted_product_id INT;

DROP TABLE IF EXISTS impacted_products;
CREATE TABLE impacted_products (impacted_product_id SERIAL, impacted_product VARCHAR, PRIMARY KEY(impacted_product_id));
SELECT DISTINCT impacted_product FROM recallsraw;
INSERT INTO impacted_products (impacted_product) SELECT DISTINCT impacted_product FROM recallsraw;


UPDATE recallsraw
SET impacted_product_id = (SELECT impacted_products.impacted_product_id FROM impacted_products WHERE impacted_products.impacted_product = recallsraw.impacted_product);


-- Make title table, insesrt title id to recallsraw
ALTER TABLE recallsraw 
ADD COLUMN recall_title_id INT;

DROP TABLE IF EXISTS recall_titles;
CREATE TABLE recall_titles (recall_title_id SERIAL, recall_title VARCHAR, PRIMARY KEY (recall_title_id));
SELECT DISTINCT recall_title FROM recallsraw;
INSERT INTO recall_titles (recall_title) SELECT DISTINCT recall_title FROM recallsraw;

UPDATE recallsraw
SET recall_title_id = (SELECT recall_titles.recall_title_id FROM recall_titles WHERE recall_titles.recall_title = recallsraw.recall_title);

-- Create reasons table and insert reason id into recallsraw
ALTER TABLE recallsraw
ADD COLUMN reason_id VARCHAR;

DROP TABLE IF EXISTS reasons;
CREATE TABLE reasons (reason_id SERIAL, reason VARCHAR, PRIMARY KEY (reason_id));
SELECT DISTINCT reason FROM recallsraw;
INSERT INTO reasons (reason) SELECT DISTINCT reason FROM recallsraw;

UPDATE recallsraw
SET reason_id = (SELECT reasons.reason_id FROM reasons WHERE recallsraw.reason = reasons.reason);

SELECT * FROM recallsraw