FROM python:3.9-slim

RUN pip install flask

RUN pip install flask-cors

# Install checkdmarc
RUN pip install checkdmarc

# Copy the app code
COPY app.py /app.py

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
