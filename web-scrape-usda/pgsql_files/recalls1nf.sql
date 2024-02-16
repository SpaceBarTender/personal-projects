DROP TABLE IF EXISTS recalls1nf;

CREATE TABLE recalls1nf (
			sur_key SERIAL,
            recall_id INT,
            recall_status VARCHAR,
            title VARCHAR,
            reason VARCHAR,
            summary VARCHAR,
            link VARCHAR,
            start_date DATE,
            date_status VARCHAR,
			impacted_product_id INT,
            impacted_product VARCHAR DEFAULT 'No value',
			location_id INT,
            location VARCHAR,
			UNIQUE (recall_id)
);

