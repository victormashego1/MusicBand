#Dockerfile

FROM python:3.11-alpine
# create directory
WORKDIR /mysite

# copying all the files
COPY mysite .

# Downloading the needed dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Setting up the DB
RUN python manage.py makemigrations
RUN python manage.py migrate

# Opening port 8000 in container
EXPOSE 8000/tcp

# command to be executed when container is running
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]