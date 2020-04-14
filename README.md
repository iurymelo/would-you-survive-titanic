# Would you Survive Titanic?
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Version: Python](https://img.shields.io/badge/Python-3.7.6-blue)](https://www.python.org/downloads/)  [![Version: scikit](https://img.shields.io/badge/scikit-0.22.2-blue)](https://scikit-learn.org/stable/) [![Version: Flask](https://img.shields.io/badge/Flask-1.1.X-blue)](https://flask.palletsprojects.com/en/1.1.x/) [![Version: ReactJS](https://img.shields.io/badge/ReactJS-16.13.1-blue)](https://reactjs.org/)

Webapp to predict if you would survive the Titanic sink using machine learning. Machine learning algorithm made in Python, back end in Flask, and front end in ReactJs.
This project uses Dask to parallelize data loading. It is just for demo purposes, though. You can use regular pandas.
This project is also ready to run on containers. To preview, just click in: [Visit the WebApp!](https://wys-titanic.web.app/)

## Technologies :rocket: :

  * [Python](https://reactjs.org/)
  * [scikit](https://scikit-learn.org/stable/)
  * [Dask](https://dask.org/)
  * [Docker](https://www.docker.com/)
  * [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  * [ReactJS](https://pt-br.reactjs.org/)
 

## Setup
Just clone the repo:
```sh
git clone https://github.com/iurymelo/would-you-survive-titanic 
cd would-you-survive-titanic
```

# With Docker
You need to instal [Docker Community and Docker Compose](https://www.docker.com/get-started) for your machine. After installing just follow the steps below.
## Training the network
Run: 
```sh
cd machine-learning
sudo docker-compose build
sudo docker-compose up
cd ..
```

## Using the Web App
Just run
```sh
sudo docker-compose build
sudo docker-compose up
```
The development server will be listening in:
http://127.0.0.1:3000 
for the react app, and
http://127.0.0.1:9000 
for the api.

# Without Docker
## Train the network
Go to the path:
```sh
cd machine-learning
```
Run:
```sh
python3 training/train.py
```

## Starting API and React
First, start Flask. In the path
back-end/flask
run:
```sh
python3 run.py
```
The service will be listening in
http://127.0.0.1:5000

Navigate back and edit the file
front-end/axios.js
to use the new IP.
Change the line 
```js
baseURL: '0.0.0.0:9000'
```
to 
```js
baseURL: '127.0.0.1:5000'
```
Run npm install
```sh
npm install
```
Run npm start
```sh
npm start
```
### Footnotes
This project is not configured for production.

**Made by Iury Melo**
