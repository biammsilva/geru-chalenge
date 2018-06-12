FROM python:3
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python3", "app.py" ]
