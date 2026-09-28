FastAPI Learning Project

This is a CRUD application I made to learn how backend APIs work. 
I started with everything in one file, then refactored it to a modular folder structure, and now I have integrated a real MySQL database and Dockerized the entire application!

What you need to run this project
You only need Docker and Docker Compose installed on your computer. You don't even need Python installed locally anymore!

How to run the project

Step 1: Start the Docker containers
Make sure you are in the project folder where the docker-compose.yml file is located. Run this command:
docker-compose up -d --build

This will automatically:
1. Download MySQL and start the database server.
2. Build the Python FastAPI image, install all requirements, and start the web server.

Step 2: How to navigate the endpoints and test the project
Once the containers are running, open your web browser.
Go to this address:
http://127.0.0.1:8080/docs

This opens the automatically generated Swagger UI documentation. 
You can test all the CRUD operations directly from this page:
1. Click on POST /students/ to create a new student record (it will be saved to MySQL permanently!).
2. Click on GET /students/ to see all the students.
3. Use PUT to edit a student's info by their ID.
4. Use DELETE to remove a student.

Step 3: Stop the server
To stop the server and the database, run:
docker-compose down
