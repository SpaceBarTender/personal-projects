ALTER TABLE recalls1nf
DROP CONSTRAINT recalls1nf_pkey;

ALTER TABLE recalls1nf
ADD PRIMARY KEY (title, impacted_products, location); -- Official First Normal Form

ALTER TABLE recalls1nf -- Begin setting to Second Normal Form
DROP COLUMN id;