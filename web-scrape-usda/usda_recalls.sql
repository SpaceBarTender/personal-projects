SELECT (CASE WHEN impacted_products IS NULL THEN
	   'None given'
	   ELSE
	   impacted_products
	   END) FROM recalls1nf;