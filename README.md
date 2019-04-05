Redis powered flask upload counter, based on the example at https://docs.docker.com/compose/gettingstarted/

This one has a button and implements AJAX to do the server call.

# Usage

Clone repo:

    git clone https://github.com/vulcan25/flask_incr_counter

Change to directory and build:

    cd flask_incr_counter
    docker-compose build

Launch:

    docker-compose up

Connect to `http://localhost:5000` and start clicking the button:

![screencap][https://i.imgur.com/Nmm1GGS.png]

