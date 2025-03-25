SELECT 
	c.id as cart_id,
	sum(i.price * ci.quantity) as total
FROM 
	cart_item ci
JOIN 
	cart c 
	ON c.id = ci.cart_id
JOIN item i
	ON i.id = ci.item_id
GROUP BY
	c.id
ORDER BY
	total desc;

select * from supplier;

SELECT 
	p.id as product_id,
	p.name as product,
	avg(r.rating * 1.0) as average,
	count(r.id) as num_reviews
FROM
	review r
JOIN 
	product p 
	ON p.id = r.product_id
GROUP BY 
	p.id,
	p.name
ORDER BY 
	average DESC;

SELECT 
	p.id as product_id, 
	p.name as product, 
	sum(ci.quantity) as total_sold
FROM 
	product p
JOIN
	item i
	ON i.product_id = p.id
JOIN	
	cart_item ci
	ON ci.item_id = i.id
GROUP BY
	p.id, p.name
ORDER BY
	sum(ci.quantity) DESC;

SELECT 
	SUM(i.price * ci.quantity) / COUNT(DISTINCT c.id) AS AOV
FROM 
	cart c
join 
	cart_item ci
	ON ci.cart_id = c.id
join 
	item i 
	ON i.id = ci.item_id;
