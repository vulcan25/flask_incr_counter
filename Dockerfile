# Slight play on the official example.  Putting the COPY line early means it doesn't re-run pip every time the code changes.
FROM python:alpine
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
ADD ./src /code
WORKDIR /code
CMD ["python", "app.py"]
