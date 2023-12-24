# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# (Update the port as needed, depending on your application)
# EXPOSE 80

# Define environment variable (optional)
# ENV NAME World

# Run app.py when the container launches
CMD ["python", "model.py"]
