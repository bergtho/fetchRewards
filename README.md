# fetchRewards
This is the repository holding the code for my Fetch Rewards coding assessment.

# Running the code
  1. Clone the repository
  2. From within the repository, execute "bash run.sh"  
    - This will check that no containers with the same name exist, then create the docker image and run the docker container. 
    - The container is run in detached mode, so you can execute the curls from within the same terminal.
  3. Once the container is running, do a post from your terminal or postman on http://0.0.0.0:5000/pix-coords
      - The content type should be plain text and that the body of the payload should be a string holding a tuple of the image dimensions followed by a comma and the list of two-element tuples defining corner points.
      - example: curl -X POST -H "Content-type: text/plain" -d "(10,12),[(1.5,1.5),(4.0,1.5),(1.5,8.0),(4.0,8.0)]" 0.0.0.0:5000/pix-cords

# Tests
  - To run the tests, just run "pytest"
  - The tests are in test_flask.py if you want to see them

# Notes on my project
  - The code is definitely not production ready. In particular, I use 'eval' to load the corner points and image dimensions without doing any checks on the data string. 
  - Unless there's a pre-built script to run tests with json as the content type, I thought that using plain text would be the easiest content type for the code to be tested with.
