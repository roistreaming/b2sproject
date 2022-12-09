# Assume a linux kernel
FROM python:3.10-bullseye
COPY requirements.txt /app/requirements.txt
WORKDIR /app
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python3", "mysql_wrapper.py"]