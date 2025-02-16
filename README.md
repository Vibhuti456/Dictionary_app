
# Dockerized Dictionary Web Application

The Dockerized Dictionary Web Application is a full-stack project that allows users to search for word meanings through a web interface. The application fetches meanings from an external API and stores the search history in an SQLite database. The project is containerized using Docker and Docker Compose, ensuring easy deployment and scalability.

# Tech Stack:
1) Backend: Flask (Python)
2) Frontend: HTML, CSS
3) Database: SQLite
4) Containerization: Dockerfile, Docker Compose
5) API: Dictionary API for fetching word meanings

# Setup Instructions:

#### Clone the repository:

``` bash
git clone git@github.com:Vibhuti456/Dictionary_app.git
cd Dictionary_app
```

#### Build the Docker Image:

``` bash 
docker build -t dictionary-app:latest .
``` 

#### Run the Docker Container:

``` bash 
docker run -d -p 5000:5000 --name dictionary_app dictionary-app:latest 
``` 

#### Build and run the project using Docker Compose:

``` bash 
docker-compose up -d --build
``` 

#### Access the application:
Open a browser and go to https://localhost:5000. 

#### Search for a word:
Enter a word in the input field and get its meaning instantly.

#### Run application through docker compose 
``` bash
docker compose up -d --build
```

#### Database Access:

If your app is running inside a Docker container, follow these steps:

#### Step 1: Open a terminal and list running containers:

``` bash 
docker ps
``` 
#### Step 2: Access the running container (replace dictionary-app with your container name if different):

``` bash 
docker exec -it dictionary_app sh
``` 

#### Step 3: Open the SQLite database:
``` bash 
sqlite3 dictionary.db
``` 

#### Run these SQLite commands:

``` bash
.tables
``` 
(You should see a table named dictionary.)

#### View the structure of the dictionary table:

``` bash 
.schema dictionary
``` 
#### See all stored words and meanings:

``` bash 
SELECT * FROM dictionary;
```

#### Exit the SQLite shell:
``` bash 
exit 
``` 

