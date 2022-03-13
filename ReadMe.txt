How to use manualy
Move locally into the docker-pytest folder
Run docker-compose up -d --build
Execute docker-compose exec pytest bash to connect to the pytest container
Run pytest tests
If screenshots are generated in the local docker-pytest / screenshots folder, you're done!
Execute docker-compose down when you want to quit

How to use automaticaly
1  Execute make run-tests is automaticaly deploying project and run  Bash inside the container
2  Run pytest tests
3  Execute exit (For exit from container)
4  Execute make tests-cleanup