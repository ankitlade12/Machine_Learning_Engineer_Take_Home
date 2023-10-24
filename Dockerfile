# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose a port for the Streamlit app
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "app.py"]