
# young-aspirant-developer-contest
Repository for the Young Aspirant Developer Contest
----------------------------------------------------------------------

! Features implemented for Phase 2 of development are outlined in phase2.txt !

A Django web application used to host an online programming contest for aspiring programmers in high school.
The project will be used as an outreach tool to engage and inspire young people to start pursuing computer science early.

Compatible Platforms:
    1. Linux (Only tested on Ubuntu 16.04 & 18.04)

Notes:
    Because the web application relies on a Django framework, dependencies need to be installed first.
    The dependency installer, install-dependencies.sh, will automate the installs, or manually install:
        virtualenv
        pip
        django

How to run:
    1. Install dependencies: ./install-dependencies.sh
    2. Run the web application: ./run.sh
    run.sh will automate some of the complexities of starting the server.
    After executing run.sh on a terminal, the application will be running on 127.0.0.1:8000 or localhost:8000
    The application can then be reached on a web browser at that address. 
    If the shell script fails, the application can be started manually with these steps:
        1. Activate virtual environment (in yadc/): source .venv/bin/activate
        2. Run the python manager (in yadc/): python serverapp/manage.py runserver
>>>>>>> be88eb75850d02ca1c0d8df7f334efed3f94c361
