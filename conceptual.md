### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
	+ PostgreSQL is an open source object-relational database system

- What is the difference between SQL and PostgreSQL?
	+ `SQL` is a structured query language used to communicate with a database.  PostgreSQL uses `SQL` in the management of a database system.

- In `psql`, how do you connect to a database?
	+ psql -d [dbname [username]]

- What is the difference between `HAVING` and `WHERE`?
	+ `WHERE` clause is used to filter the records from the table or used while joining more than one table.  Only those records that satisfy the condition of the  `WHERE` clause will be extracted from the table.  It can be used with `SELECT`, `UPDATE`, `DELETE` statements.  `HAVING` clause is used to filter the records form the groups based on the given condition in the `HAVING` clause.  It can only be used with `SELECT` statement. 

- What is the difference between an `INNER` and `OUTER` join?
	+ The major difference between inner and outer joins is that inner joins result in the intersection of two tables, whereas outer joins result in the union of two tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
	+ Left and right outer joins are useful if you want to get all the values from one table but only the rows that match that table from the other table.  So in a left outer join, all rows from the left table will be returned plus the rows that the right table had in common. In contrast, for a right outer join, all rows from the right table will be returned plus the rows that the left table had in common.

- What is an ORM? What do they do?
	+ Object-relational-mapping is the idea of being able to write queries like the one above, as well as much more complicated ones, using the object-oriented paradigm of your preferred programming language.  In essence, it is a way to interact with a database using a language such as Python instead of `SQL`.  Most people refer to a library that uses abstraction to interact with a database as the Object-relational-mapper.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?
	+ HTTP requests using AJAX is done through the browser via JavaScript. It may actually be faster as it doesn't need flask. Info is then stored in JavaScript. On the other hand, using a server side library like `requests` makes it easier to store data in a database on your computer. It also adds security to your program by giving you an API key and secret (like a username and password).

- What is CSRF? What is the purpose of the CSRF token?
	+ A CSRF Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. The tokens are generated and submitted by the server-side application in a subsequent HTTP request made by the client.  After the request is made, the server side application compares the two tokens found in the user session and in the request. If the token is missing or does not match the value within the user session, the request is rejected, the user session terminated and the event logged as a potential CSRF attack.

- What is the purpose of `form.hidden_tag()`?
	+ The `form.hidden_tag()` template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected is include this hidden field and have the `SECRET_KEY` variable defined in the Flask configuration.
