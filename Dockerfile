FROM ubuntu:16.04
MAINTAINER goldragoon paganinist@gmail.com

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y python-pip python-dev python2.7-dev build-essential
RUN apt-get install -y wget git ruby-full

RUN git clone https://github.com/UtopiaSoftware/PatientManagementSystem.git

RUN pip install -r PatientManagementSystem/requirements.txt

EXPOSE 80
EXPOSE 443
EXPOSE 8080

CMD ["python", "/PatientManagementSystem/run.py", "-p 8080"]
