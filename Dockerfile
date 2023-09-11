# Download and install base Jupyter image
FROM python:3.11
# FROM jupyter/base-notebook:python-3.10.4

# Copy requirements inot image directory "project"
WORKDIR /home/app
COPY requirements.txt .

# Update pip and install Python package dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# # Execute upon build (for use with docker)
# ENTRYPOINT [ "python3", "frameXtract.py" ]
# CMD [ "python3", "frameXtract.py", "-h" ]