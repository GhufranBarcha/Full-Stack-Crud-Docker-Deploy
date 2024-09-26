# Full Stack CRUD Application

Render link: [https://full-stack-crud-application-se3r.onrender.com/](https://full-stack-crud-application-se3r.onrender.com/)

Vercel Link: [https://full-stack-crud-application-git-main-ghufranbarchas-projects.vercel.app/](https://full-stack-crud-application-git-main-ghufranbarchas-projects.vercel.app/)

## Login Details
If you have trouble logging into the app, use the below details:
- Email: @gmail.com
- Password: ...

## Overview

This is a full-stack CRUD application built using Flask as the backend framework and React as the frontend framework. The application allows users to browse products, add them to the cart, and checkout.

## Technologies Used

* **Backend**: Flask, SQLAlchemy
* **Frontend**: React, React Router, Bootstrap
* **Database**: SQLite
* **Login Authentication**: Firebase

## Setup Instructions

### Backend and Frontend

1. Clone the repository: `git clone GhufranBarcha/Full-stack-Crud-Application`
2. Install the required packages: `pip install -r requirements.txt` in the Backend folder.
3. Run `npm install` and `npm run build` in the Frontend folder, then go to the Backend folder and run `flask run`.
4. Start the backend and frontend server: `python app.py` in the backend and `npm run dev` in the frontend folder.

## API Documentation

### API Endpoints

#### Products

* `GET /products`: Get all products
* `GET /products/:id`: Get a product by ID
* `POST /products`: Create a new product
* `PUT /products/:id`: Update a product
* `DELETE /products/:id`: Delete a product

## Troubleshooting

If you encounter any issues while setting up or running the application, please check the following:

* Make sure you have the required packages installed.
* Check the database connection settings.
* Verify that the backend and frontend servers are running correctly.

## Docker Deployment Instructions

To deploy the application using Docker, you will need Docker installed on your machine. Follow the steps below:

### 1. Build and Run Docker Containers

- Ensure you are in the root directory of the project where the `docker-compose.yml` file is located.
- Run the following command to build and start the containers:
  ```bash
  docker-compose up --build
