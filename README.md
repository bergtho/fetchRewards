# fetchRewards
This is the repository holding the code for my Fetch Rewards coding assessment.

# Running the code

  - First, make sure you have docker installed by following the steps corresponding to your operating system.
    - Windows: https://docs.docker.com/desktop/windows/install/
    - Mac: https://docs.docker.com/desktop/mac/install/
    - Ubuntu: https://docs.docker.com/engine/install/ubuntu/
  - Here are some helpful links
    - docker dashboard: https://docs.docker.com/desktop/dashboard/
    - getting started (The youtube video seems like a good overview of what a container is) https://docs.docker.com/get-started/
    - intro article that I followed to get started: https://docker-curriculum.com/
      - Note: there's an example of sending a curl request to a container after "Now, lets try to see if can send a request to the Elasticsearch container. We use the 9200 port to send a cURL request to the container."
      - Note: can create other types of networks in docker and can read about them in the official docs. Is there a test one??
        - Ans: use docker compose
    - Overview of compose: https://docs.docker.com/compose


# Checklist (for my reference)
  - Get the docker container working with a basic flask app
  - Get dummy testing working
  - write some initial tests
    - need to find a good example workflow letting you test docker compose
    - just use dummy data for the tests
  - write the app stuff
