ALTER TABLE recalls1nf
DROP CONSTRAINT recalls1nf_pkey;

ALTER TABLE recalls1nf
ADD PRIMARY KEY (title, impacted_products, location);

ALTER TABLE recalls1nf
DROP COLUMN id;