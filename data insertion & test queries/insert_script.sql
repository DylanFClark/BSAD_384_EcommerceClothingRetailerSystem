
-- Please see insert script w/ data in data insertion & test queries/query.txt --

INSERT INTO supplier(id, company, acct_created)
VALUES 

INSERT INTO supplier_rep(id, fname, lname, start_date, phone, email, supplier_id) 
VALUES

INSERT INTO product(id, name, list_data, description, rep_id)
VALUES

INSERT INTO item(id, size, color, price, product_id)
VALUES

INSERT INTO customer(id, fname, lname, DOB, phone, email, address, province, creation_date)
VALUES

INSERT INTO review(id, rating, comment, when_reviewed, product_id, customer_id)
VALUES

INSERT INTO cart(id, when_ordered, departure_datetime, arrival_datetime, customer_id)
VALUES

INSERT INTO cart_item(cart_item_id, cart_id, item_id, quantity)
VALUES

