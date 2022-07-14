# fetchRewards
This is the repository holding the code for my Fetch Rewards coding assessment.

# Running the code

  - First, make sure you have docker installed by following the steps corresponding to your operating system.
    - Windows: https://docs.docker.com/desktop/windows/install/
    - Mac: https://docs.docker.com/desktop/mac/install/
    - Ubuntu: https://docs.docker.com/engine/install/ubuntu/
  - Clone this repository and navigate into the project's base directory
  - Run "bash run.sh"
    - This will check that no containers with the same name exist, and then create the docker image, and then run the docker container.
  - Once the container is running
    - Do a post with the inputs via TODO (localhost:5000 or 0.0.0.0:5000)
      - curl -X POST -H "Content-type: text/plain" -d "(10,12),[(1.5,1.5),(4.0,1.5),(1.5,8.0),(4.0,8.0)]" "0.0.0.0:5000/pix-cords"
    - Run the tests via TODO - change python, app.run to pytest

# Notes on my project
TODO

# Ways to improve the code / project
TODO
