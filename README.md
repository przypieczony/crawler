# crawler dev crew 

Way of Working (WoW):

- All documentation, docstrings, comments, code will be written English.
- Do not commit directly to master. Pull requests with at least one reviewer 
  must be approved before it comes to master branch.
- Keep code clean, provide docstrings and follow these rules: 
  https://www.python.org/dev/peps/pep-0008/
- Eat, sleep, code, repeat ;)

Prerequisits:
- `docker` on host machine

Instructions:
- Crawler is containerized so in order to launch it you have to build docker image and run it as container. Execute `docker-compose up` (or `docker-compose up --build` to rebuild docker image, necessary to apply changes in code) inside crawler directory in order to launch application. After that, visit `localhost:8000` and check whether application is working.

