# Use a base Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY frontend/requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY frontend/ui.py ./

# Expose the Gradio port
EXPOSE 7861

# Run the Gradio application
CMD ["python", "ui.py"]
