FROM ubuntu:16.04
MAINTAINER goldragoon paganinist@gmail.com

# Make sure that OS is latest state
RUN apt-get update
RUN apt-get upgrade

# Install Preliminaries
RUN apt-get install -y python-pip python-dev python2.7-dev build-essential python-mysqldb
RUN apt-get install -y wget git 

# Install Front End Frameworks
RUN apt-get install -y ruby-full
RUN gem install sass

# Fetching Project 
RUN git clone https://github.com/UtopiaSoftware/PatientManagementSystem.git

# Install Back End Frameworks
RUN pip install -r PatientManagementSystem/requirements.txt

EXPOSE 80
EXPOSE 443
EXPOSE 8080

CMD ["python", "/PatientManagementSystem/PMS-server/run.py", "-p 8080"]
