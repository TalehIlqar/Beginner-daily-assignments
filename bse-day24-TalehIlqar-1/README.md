# Flask :crystal_ball:

We require you to solve the following tasks. Remember to read the requirements first.

#### Topics you need to know and use to solve tasks

* Flask Models
* Flask Object-relational mapping
* Flask SQLAlchemy
* Flask Model fields
* Flask Model relations
* Flask Insert, Select, Delete, Querying

# Assignments' list 

## Assignment 1   :star:  :star:  :star:  :star:

### Description

![image](https://i.ibb.co/7W716nR/screenshot-docs-google-com-2020-09-04-14-50-28.png)

Prepare a table that contains **Products** using model and model fields. Let the products have the following attributes:

* id (number type)
* name (character type) - can have a maximum of 40 characters. The name must be unique.
* description (text type)  - Can’t be null
* category_id (number type) Can’t be null and must be foreign key relation with categories.id field.
* amount (number type) equal to 0 by default.
* price (decimal digits type) The price is 0.00 per default. 
* production date (date and time type)
* is new (binary type) set to false by default.
* rating (decimal digits type) - 0.0 by default. The number can be 1 before the comma and 1
after the comma. Not required to be added. It cannot be less than 0 and greater than 5. Write a validator to check these conditions.
* created_at  - Should be equal to the default creation date.
* updated_at  - Should be equal to the default updated date.


Prepare a table that contains **Categories** using model and model fields. Let the products have the following attributes:

* id (number type)
* name (character type) - can have a maximum of 30 characters. The name must be unique.
* created_at  - Should be equal to the default creation date.
* updated_at  - Should be equal to the default updated date.

## Assignment 2  :star:  :star:  :star:  :star:

### Description

* Add Shopping Goods, Specialty Goods categories to **Categories** Model
* Add some under data to **Products** Models:
   - Name: Computer,  description: “Some Text” category_id: 2, amount: 10, price: 1000, production date: 2020, is_new: true,rating: 3.5
   - Name: Mobile phone,  description: “Some Text” category_id: 2, amount: 30, price: 500, production date: 2020, is_new: true,rating: 4.1
   - Name: Clothing,  description: “Some Text” category_id: 1, amount: 30, price: 20, production date: 2020, is_new: true,rating: 3.2
   - Name: Sports equipment,  description: “Some Text” category_id: 1, amount: 30, price: 500, production date: 2018, is_new: false,rating: 2.6

## Assignment 3  :star:  :star:  :star:  :star:

### Description

* Read products which category is Shopping Goods.
* Retrieve all products objects which price less than 100
* Retrieve all categories objects which title contains “a” character
* Update product name to  “clothes”  object which primary key equal to 3
* Retrieve all new products and order by the rating




**Powered by [TechAcademy](https://www.tech.edu.az/)**

