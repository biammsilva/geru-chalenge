FROM python:3
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop
RUN pip3 install -e .
EXPOSE 8080
ENTRYPOINT ["pserve", "--reload", "development.ini"]
