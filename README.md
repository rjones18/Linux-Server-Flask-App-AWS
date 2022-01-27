# Linux-Server-Flask-App-AWS
In this mini project I deployed a basic flask application on a Linux server. The Linux server is being ran on a AWS EC2 Instance and is using NGINX as the webserver.

In this mini project I deployed a basic python flask application on a Linux server. The Linux server is on a EC2 Instance in AWS and is running [NGINX](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/) to forward the request from the public IP address of the server to the local webserver. Gunicorn is also used to run our flask application.

Link to the App: http://flask2.reggiestestdomain.com (VM Currently turned off)

## Application Breakdown

The construction of the application broken down into the architecture below:

![awsflask](https://github.com/rjones18/Images/blob/main/AWSFlaskAPP2.drawio.png)

### Front-End

- HTML
- CSS


### Back-End 

- [Python](https://www.python.org/) 
- [Flask (Python Framework)](https://flask.palletsprojects.com/en/1.1.x/)

### Web Server/HTTP Server

- [Nginx](https://www.nginx.com/)
- [Gunicorn](https://gunicorn.org/)

### Deployment Platform

- Linux Server hosted in AWS

### DNS

- [Route 53](https://aws.amazon.com/route53/)
