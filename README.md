# ForkTheRepo

## Table of Contents

* [Purpose](#purpose)
* [Process](#process)
* [Running Locally](#running-locally)
* [Running Tests](#running-tests)

## Purpose

ForkTheRepo fork's it's own Github repo into a user's Github account.

## Process

The application uses Flask (fronted by gunicorn) to serve the simple UI to the user.


Once clicked the "ForkTheRepo" button redirects the user to Github's OAuth flow. If the user
accepts then the application will have the necessary permissions to fork "ForkTheRepo"'s
repository to the user's Github account.

A new html page is served to the browser on successful authorization informing that the fork was
successfully requested.

## Running the application locally

1. Populate the `.env` file in the project's root with values for the 

```shell
# .env

GITHUB_CLIENT_ID=<your-github-applications-client-id>
GITHUB_CLIENT_SECRET=<your-github-applications-client-secret>
```

2. Build and run the image

```shell
# build the image
docker build -t forktherepo .

# run the image using the .env variables and exposing port 8080
docker run --env-file .env -p 8080:8080 forktherepo
```

3. Navigate to the 

## Running tests

```shell
# run the tests by over-riding the container entrypoint
docker run -it --env-file .env --entrypoint "pytest" forktherepo
```

# Future Enhancements

* more tests
* separate tests and test dependencies from same docker image as prd
* use flask application factory pattern
* redirect to user's github account
