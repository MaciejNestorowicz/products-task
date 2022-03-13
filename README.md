# products-task
Solution to Python Flask task

-DESCRIPTION-
There are three endpoints:

GET /products - list all products. Expected status code 200 on success.

POST /products - will create prdouct or increment amount if product exists.
- example of expected body as json:
{
    "name": "orange",
    "amount": 2
}
*workflow
- if product with given name does not exist it will be added to db with given amount. Expected status code 201.
- if product with given name does exist it's amount will be incremented by the amount given in request body. Expected status code 200.
*constarints:
- currently amount has to be larger than 0 and not bigger than 10. This configuration can be easily changed in source code

PUT /products - will order named product in effect amount of this product will be decreased in db
- example of expected body as json:
{
    "name": "orange",
    "amount": 2
}
*workflow
- if product with given name does not exist it will display a message that product was not found. Expected status code 400.
- if product with given name does exist it's amount will be decreased by amount given in request body. Expected status code 200.
*constarints:
- currently amount has to be larger than 0 and not bigger than 10. This configuration can be easily changed in source code
- if the amount provided in request body will be larger than the amount in stock there will be a message displayed that there are not enough items in stock. Expected status code 400.

-RUN APP-
*Locally
- To run the application use command 'python ./app.py' or 'flask run' from products_manager directory. Running this application locally expects that you have MySQL database prepared with needed tables.

*Docker
- You can build docker image from Dockerfile that is present in products_manager directory. This approach also expects that you have MySQL database prepared
with needed tables.

*Docker-compose
- You can create image for Python/Flask project and MySQL databes with docker-compose. To run it use 'docker-compose up' command from products-task directory.

!warning - be aware that ports 5000 and 3306 must be free for docker images to start.

-TEST-
Best way to test application is to use tool like Postman to sen request to described enpoints with given bodies shown as examples.