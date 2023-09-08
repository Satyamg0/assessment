# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the local requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container at /app
COPY . /app

# Define environment variable
ENV NAME CurrencyConverter

# Expose the port your application will run on
EXPOSE 7850

# Run app.py when the container launches
CMD ["python", "app.py"]
