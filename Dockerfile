# start with a lightweight Python image
# the below command gives you a small image with Python installed, but without unnecessary packages
FROM python:3.14-slim
# set the working directory in the container
WORKDIR /app
# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
# the --no-cache-dir option prevents pip from caching the packages, which reduces the size of the image
RUN pip install --no-cache-dir -r requirements.txt
# COPY the rest of the application code and saved models to the working directory
COPY . .
# Document the port the app runs on
EXPOSE 8000

# command to run the application
# start the api server when the container starts
# 0000 allows the server to be accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]