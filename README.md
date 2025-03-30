# BSAD_384_EcommerceClothingRetailerSystem

This project is an emulation of the creation of a proposed solution to the information management needs 
of a online clothing retailer - particularly as it relates to the customer facing side - sales, reviews, 
and order fufillment; how they would manage data, what data is important, as well as a peak at what metrics 
they might consider important.

Information management of this nature is crucial to organizations and stakeholders; information helps 
us to understand the company, be it for the purpose of strategic decision making, investing, or deliberation between
projects - relevant, quality information, is nessesairy. 

Data for this project was created at random. See the 'pre-prossesing' directory. Note that this data is not 
representative of any real entity and created purely to populate this database.


Project Progression Through Milestones:

[Term project - Milestone 1.pdf](https://github.com/user-attachments/files/19449956/BSAD.384.Term.Assignment.-.Milestone.1.pdf)

[Term project - Milestone 2.pdf](https://github.com/user-attachments/files/19449922/Term.project.-.Milestone.2.pdf)

[Term project - Milestone 3.pdf](https://github.com/user-attachments/files/19450006/_Term.project.-.Milestone.3.pdf)


Modeling Schemas:

**Entity Relation Diagram**

![image](https://github.com/user-attachments/assets/bf6def4d-fcda-407d-9c38-2c3c3aff94ac)


**Relational Schema**

![image](https://github.com/user-attachments/assets/e88c5185-1084-4796-953b-647e4beef47c)


**Resoure Locations: **

Data preprocessing scripts can be found in /pre-processing

Table delete & create statments can be found in /table_creation

[drop script](https://github.com/DylanFClark/BSAD_384_EcommerceClothingRetailerSystem/blob/main/table_creation/drop_script.sql)
[create script](https://github.com/DylanFClark/BSAD_384_EcommerceClothingRetailerSystem/blob/main/table_creation/create_table_script.sql)

Data can be found in /data

Data population script can be found in '/data insertion & test queries'

[populate.sql](https://github.com/DylanFClark/BSAD_384_EcommerceClothingRetailerSystem/blob/main/data%20insertion%20%26%20test%20queries/populate.sql)

Sample sql queries can be found in /test_queries

1) Retrieve the total of every cart, with more expensive carts first. 
   
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

2) 


