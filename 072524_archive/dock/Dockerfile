FROM python:3.10.9-buster


# Make a dir for our App
WORKDIR /app

# Install dependacies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copy our source code
COPY /app .

# Run Application
CMD ["python", "main.py"]

