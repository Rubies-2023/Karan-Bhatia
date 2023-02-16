# NodeJS

# Description
This is a Node.js project that implements APIs for user registration and login. The project maintains a list of registered users with their username and password. The registration API performs validation on the username to ensure that it is unique and does not contain special characters or spaces. The API returns an appropriate response on success and sends an appropriate error status and message on failure.

The login API receives the username and password from the user and sends the appropriate login status on success or failure with the proper message. The project stores JSON objects in a file. The project files include index.js, dbconnection.js, routes.js, getUserController.js, loginController.js, registerController.js, and users.json.

# Technologies Used
* Node.js
* MySQL database

# Installation
Clone the repository
Install the required packages using the command npm install
Create a .env file and set the required environment variables
Start the server using the command nodemon index.js

# Usage
1. Clone the project from the Git repository.

2. Install the required dependencies by running npm install.

3. Start the server by running node index.js.

4. You can access the registration API at /register with a POST request, providing the username and password in the request body. The API will validate the username, check if it's unique, and store the user's details in the users.json file. On success, the API will return a status code of 201 and a success message. On failure, it will return an appropriate error status/message.

5. You can access the login API at /login with a POST request, providing the username and password in the request body. The API will check if the user exists in the users.json file and validate the password. On success, the API will return a status code of 200 and a success message. On failure, it will return an appropriate error status/message.

# Endpoints
* `/users` - returns a list of all users
* `/login` - logs a user in and returns an access token
* `/register` - registers a new user and returns a success message

# Configuration
Install Node.js

* Node.js can be downloaded and installed from the official Node.js website: https://nodejs.org/en/

Create a project directory

* Create a project directory with a name of your choice.
* Open a terminal and navigate to the project directory.
*Run the command npm init to create a package.json file.

Install necessary packages

* The project requires express, express-validator, and bcryptjs packages.
* Run the command npm install express express-validator bcryptjs --save to install the packages.

Create required files

* Create the following files in the project directory: index.js, dbconnection.js, routes.js, getUserController.js, loginController.js, registerController.js, and users.json.


# File Structure
* `index.js` - The main entry point of the application
* `dbConnection.js` - Contains the code for establishing a database connection
* `routes.js` - Contains the code for defining the API endpoints
* `controllers/` - Contains the controllers for handling API requests
* `getUserController.js` - Controller for handling requests for getting user data
* `loginController.js` - Controller for handling login requests
* `registerController.js` - Controller for handling registration requests
* `users.json` - The file where user data is stored
