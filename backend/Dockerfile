# use official python slim 3.9 as base image.
FROM python:3.9-slim

# update system packages and install dependencies.
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# set working directory inside container.
WORKDIR /todo-app/backend

# install project dependencies.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy application code into container.
COPY . .

# expose the application port.
EXPOSE 5000

# specify the commands to run the application.
CMD ["python","server.py"]