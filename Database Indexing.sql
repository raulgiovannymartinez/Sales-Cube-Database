-- Create indices for Sales Cube to deliver top performance on queries

-- sales table
CREATE INDEX sales_customerid_idx 
ON sales(customer_id)
;

CREATE INDEX sales_productid_idx 
ON sales(product_id)
;



-- products table 
CREATE INDEX products_name_idx 
ON products(name)
;



-- customers table
CREATE INDEX customers_stateid_idx 
ON customers(state_id)
;