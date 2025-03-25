
CREATE DATABASE IF NOT EXISTS clothing_ecommerce_retailer;

USE clothing_ecommerce_retailer;

CREATE TABLE supplier(
	id INT NOT NULL,
	company VARCHAR(255) UNIQUE NOT NULL,
	acct_created DATETIME  NOT NULL,

	PRIMARY KEY (id)
);

CREATE TABLE supplier_rep(
	id INT NOT NULL,
	fname VARCHAR(255) NOT NULL,
	lname VARCHAR(255) NOT NULL,
	start_date DATETIME NOT NULL,
	phone VARCHAR(255) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	supplier_id INT NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

CREATE TABLE product (
	id INT NOT NULL,
	name VARCHAR(255) UNIQUE,
	list_date DATETIME,
	description VARCHAR(255),
	rep_id INT NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY (rep_id) REFERENCES supplier_rep(id)
);

CREATE TABLE customer(
	id INT NOT NULL,
	fname VARCHAR(255) NOT NULL,
	lname VARCHAR(255) NOT NULL,
	DOB DATETIME NOT NULL,
	phone VARCHAR(255) UNIQUE NOT NULL,
	email VARCHAR(255) NOT NULL,
	address VARCHAR(255) NOT NULL,
	province VARCHAR(255) NOT NULL,
	creation_date DATETIME NOT NULL,
	PRIMARY KEY (id)
);



CREATE TABLE review(
	id INT NOT NULL,
	rating INT NOT NULL
		CHECK ( rating BETWEEN 1 AND 5 ),
	comment VARCHAR(255),
	when_reviewed DATETIME NOT NULL,
	product_id INT NOT NULL,
	customer_id INT NOT NULL,
	
	PRIMARY KEY (id),
	FOREIGN KEY ( customer_id ) REFERENCES customer(id),
	FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE item(
	id INT NOT NULL,
	size VARCHAR(255) NOT NULL,
	color VARCHAR(255) NOT NULL, 
	price DECIMAL(10, 2) NOT NULL,
	product_id INT NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE cart(
	id INT NOT NULL,
	when_ordered DATETIME NOT NULL,
	departure_datetime DATETIME,
	arrival_datetime DATETIME,
	customer_id INT NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE cart_item(
	cart_item_id INT NOT NULL,
	cart_id INT NOT NULL,
	item_id INT NOT NULL,
	quantity INT NOT NULL
	CHECK ( quantity > 0 ),

	PRIMARY KEY (cart_item_id),
	FOREIGN KEY (cart_id) REFERENCES cart(id),
	FOREIGN KEY (item_id) REFERENCES item(id)
);
