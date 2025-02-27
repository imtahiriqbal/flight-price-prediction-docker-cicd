# Deploy Flight Price Prediction (Flask App) using:
- ### Docker
- ### Heroku
- ### Github Actions (CI/CD)

## Docker Setup
### Create a ```Dockerfile```
```
FROM python:3.10.12
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=2 --max-requests=1000 --max-requests-jitter=50 --bind 0.0.0.0:$PORT app:app
```
- Pull python version 3.10 from docker hub
- Copy current directory files into image ```/app``` path
- Set ```/app``` path as working directory
- Install dependencies
- Expose port to serve
- To run app

## Heroku Setup
- Create a new Heroku app
- Using app name as ```HEROKU_APP_NAME``` in documentation
- (Optional) Set heroku app stack as container using Heroku CLI
    - ```heroku stack:set container --app HEROKU_APP_NAME```
    

## Github Actions Setup
- Go to repository:
    - ```Settings -> Secrets and Variables -> Actions```
- Add new repository secret
    - ```HEROKU_APP_NAME```
    - ```HEROKU_API_KEY```
    - ```HEROKU_EMAIL```

- Create new workflow file under ```.github/workflows``` directory
    - Name the workflow file as ```main.yml``` (which contains all deployment process)
    - Refer this file for more details [main.yml](https://github.com/imtahiriqbal/flight-price-prediction-docker-cicd/.github/workflows/main.yml)


## Run app through Github Actions (CI/CD) using Docker on Heroku
- Push code to repository
- Wait for Github Actions to run the workflow
- Check the status of the workflow in the repository
- Once the workflow is successful, check the Heroku app for the deployed application
- Check the logs for any errors or issues ```heroku logs --tail```

## Halt or stop app:
- Turn off Dyno from Heroku Web UI<br>
<b>OR</b>
- ```heroku ps:scale web=0 --app HEROKU_APP_NAME``` (from CLI)
