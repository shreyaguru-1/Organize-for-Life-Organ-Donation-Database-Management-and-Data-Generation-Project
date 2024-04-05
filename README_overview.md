# Organize-for-Life-Organ-Donation-Database-Management-and-Data-Generation-Project


## Introduction
Organize For Life is a project aimed at addressing the challenges of organ availability and donor awareness in the field of organ transplantation. The project proposes the development of a comprehensive PostgreSQL database to efficiently match donors with recipients based on various parameters. This README file provides an overview of the project structure, database details, SQL queries, normalization process, indexing, and contributions.

## Project Structure
The project consists of the following components:
1. **Database Creation**: Utilizing PostgreSQL to create a database using organ donation dataset files in CSV format.
2. **Database Tables**: Creation of multiple tables including `user_info`, `donor`, `recipient`, `organ`, and `health_history` to store relevant information.
3. **SQL Queries**: Execution of various SQL queries for data retrieval, manipulation, and maintenance.
4. **Normalization**: Ensuring the database tables satisfy Boyce-Codd Normal Form (BCNF).
5. **Indexing**: Implementing secondary indexing to optimize query performance.
6. **Website**: Designing a website using Streamlit to visualize database queries and results.

## Database Details
The database comprises five tables:
- `user_info`
- `donor`
- `recipient`
- `organ`
- `health_history`

Each table contains specific attributes to store user information, donor details, recipient details, organ information, and health history the below shows the relationship between them.
![ER_Diagram](https://github.com/shreyaguru-1/Organize-for-Life-Organ-Donation-Database-Management-and-Data-Generation-Project/assets/166087435/d9965de2-0db6-4013-bb76-b9fbe22388d3)


## SQL Queries
A variety of SQL queries are executed to demonstrate different functionalities of the database, including SELECT, WHERE, GROUP BY, AVERAGE, JOIN, SUBQUERY, UPDATE, DELETE, and INSERT.

## Normalization
The database tables are normalized to ensure they adhere to Boyce-Codd Normal Form (BCNF). Functional dependencies for each relation are identified and verified.

## Indexing
Secondary indexing is implemented to enhance query performance. Relevant columns are indexed to optimize query execution time.

## Website
A website is developed using Streamlit to interact with the database, visualize queries, and display query results.


## References
- Online Data Generator: [https://www.onlinedatagenerator.com/](https://www.onlinedatagenerator.com/)
- Streamlit: [https://streamlit.io/](https://streamlit.io/)
- Database Systems: The Complete Book by Garcia-Molina, H., Ullman, J. D., & Widom, J. (2nd ed.)
- Microsoft SQL Server Documentation on Indexes: [https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver15](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver15)
- Essential SQL: Database Normalization: [https://www.essentialsql.com/database-normalization/](https://www.essentialsql.com/database-normalization/)
