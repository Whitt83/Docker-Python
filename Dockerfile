FROM python:3
ADD requirements.txt ./tmp/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r ./tmp/requirements.txt
WORKDIR /code
