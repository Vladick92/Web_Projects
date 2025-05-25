These apps are for park. 
    Types of users:
    1) Owner - can give tasks to rangers, to do some stuff with plant. Also can add to task message about details of task
    2) Ranger - can complete tasks from owners and can send some details about completed tasks

Entities in db:
    1) Owner
    2) Ranger
    3) Plant
    4) Task

    park_api: just API
    park_microservices: have same entities as API, but i turned it to microservices

Built with: FastAPI, sqlalchemy, postgresql, pydantic, Docker
