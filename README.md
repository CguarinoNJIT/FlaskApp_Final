# Project Description
TODO

# Run from Command Line Interface
This project requires [Docker](https://www.docker.com/) as a dependency. This application uses docker compose to launch a container running a flask application that uses a uses a MySQL database running in a separate container. This application also (eventually) uses a Redis database running in a docker container to store user session data.

To run this project navigate to the project home directory and run all of the commands below in order.

1) This command will build all docker containers in the `docker-compose.yaml` file.
    ```bash
    docker-compose build
    ```

2) This command will run all built docker containers.
   ```bash
   docker-compose up
   ```

3) At this point navaigate to `localhost:5000` in your browser and interact with the Flask web application.

4) Use this command to confirm that docker container are running as expected.
    ```bash
    docker ps
    ```

5) This command will stop all running docker containers.
    ```bash
    docker-compose down
    ```

# Breakdown
## Final Project
Flask Tutorial - https://hackersandslackers.com/your-first-flask-application
### To Run - 
# 1. Creating Your First Flask Application
![Screen Shot 2021-08-03 at 12 34 05 PM](https://user-images.githubusercontent.com/85355712/128052790-6415998e-d341-4d14-bdb8-e96278b2934c.png)
![Screen Shot 2021-08-03 at 12 22 22 PM](https://user-images.githubusercontent.com/85355712/128052878-a302fcdc-eacf-4bfb-9701-7fbd560b250c.png)
# 2. Rendering Pages in Flask Using Jinja
![Screen Shot 2021-08-03 at 12 37 09 PM](https://user-images.githubusercontent.com/85355712/128053343-1521e261-f831-4384-9ca4-537375d4948e.png)
# 3. Handling Forms in Flask with Flask-WTF
![Screen Shot 2021-08-03 at 12 25 58 PM](https://user-images.githubusercontent.com/85355712/128051685-e83c058f-40db-48ac-a9c2-c223df5ad949.png)
![Screen Shot 2021-08-03 at 12 22 53 PM](https://user-images.githubusercontent.com/85355712/128051441-b2efe6af-1f29-418d-9d5f-7f048e381a02.png)
![Screen Shot 2021-08-03 at 12 23 27 PM](https://user-images.githubusercontent.com/85355712/128051470-467c3f1f-26a5-41a8-b1ce-c0cb755801d4.png)
![Screen Shot 2021-08-03 at 12 42 51 PM](https://user-images.githubusercontent.com/85355712/128053938-4a0d62b5-d9c9-48a8-a542-820a18e06fe7.png)
# 4. The Art of Routing in Flask
> Complete. All routing in separate routing file.
# 5. Configuring Your Flask App 
![Screen Shot 2021-08-03 at 12 28 14 PM](https://user-images.githubusercontent.com/85355712/128052006-ae2c193d-967c-4004-86d2-8dccd9774c45.png)
# 6. Demystifying Flask’s Application Factory 
> Completed
