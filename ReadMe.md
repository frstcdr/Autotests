*Use that version only for mac with M1 processor*

## How to use manualy
1. Move locally into the `docker-pytest` folder
2. Run `docker-compose up -d --build`
3. Execute `docker-compose exec pytest bash` to connect to the pytest container
4. Run `pytest tests`
5. If screenshots and report are generated in the local docker-pytest / screenshots / reports folder, you're done!
6. Execute `docker-compose down` when you want to quit

## How to use automaticaly
1. Execute `make run-test` is automaticaly deploying project and run Bash inside the container
2. Run `pytest test` (if you don't need a report.html)
3. Run `py.test --html=reports/demoreport.html` for automatic report generation
4. Run `pytest -s -v -m smoke tests` (if ypu need special tests with marks)
5. Execute `exit` (For exit from container)
6. Execute `make clean-test`
