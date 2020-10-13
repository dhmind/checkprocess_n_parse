FROM python:3.7

COPY ./requirements.txt /requirements.txt
COPY ./parse.py /parse.py

RUN pip install -r /requirements.txt

ENTRYPOINT [ "/usr/bin/python"]
CMD [ "/parse.py" ]
