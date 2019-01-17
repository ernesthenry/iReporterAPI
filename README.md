[![Build Status](https://travis-ci.com/ernesthenry/iReporterAPI.svg?branch=ft-user)](https://travis-ci.com/ernesthenry/iReporterAPI)
[![Coverage Status](https://coveralls.io/repos/github/ernesthenry/iReporterAPI/badge.svg?branch=develop)](https://coveralls.io/github/ernesthenry/iReporterAPI?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/f4fed7a1485aff2d4a2b/maintainability)](https://codeclimate.com/github/ernesthenry/iReporterAPI/maintainability)
# iReporterAPI
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention. iReporter is an App that is aimed at solving this.


This repository contains my code for the Andela iReporter Challenge 2.

## Languages and Tools Used

* [Python 3.5](https://www.python.org)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://www.heroku.com/)
* [Travis C!](https://travis-ci.org/)
* [Coveralls](https://coveralls.io/)
* [Code Climate](https://codeclimate.com/)
* [Data structures in Python](https://docs.python.org/3/tutorial/datastructures.html)



### Getting Started

## Clone the project

```
git clone https://github.com/ernesthenry/iReporterAPI.git
```

## Installation


### create a virtual environment:

```
virtualenv venv
```

### Activate the virtual environment:

```
 source venv\bin\activate
```

### Install requirements from the requirements.txt file:

```
pip install -r requirements.txt
```

### Run the Application:

```
python app.py 
```

### Run Tests

```
pytest
```


## API Endpoints

|REQUEST TYPE| URL | DESCRIPTION |
|------------|-----|-------------|
|POST| /api/v1/red-flags/create |Create a red flag record|
|GET| /api/v1/red-flags |Get all red flag records |
|GET| /api/v1/red-flags/<int:flag_id> |Get specific red flag record|
|DELETE| /api/v1/red-flags/<int:flag_id>|Delete a specific red flag record|
|PATCH| /api/v1/red-flags/<int:flag_id>/comment |Update comment of a specific red flag record|
|PATCH| /api/v1/red-flags/<int:flag_id>/location |Update location of a specific red flag record|


### Author of the codebase

# Kato Ernest Henry 


## Deployment

Application is deployed using Heroku.

checkout it on [HEROKU](https://ireporter-api-ernest.herokuapp.com/)