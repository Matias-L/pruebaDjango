# Pull base image
FROM python:3

# Set environment varibles
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir code code/projecto code/aplicaciones
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/