FROM python:3.10.12
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE $PORT
# CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
# Above written takes more memory on heroku, using this instead
CMD gunicorn --workers=2 --max-requests=1000 --max-requests-jitter=50 --bind 0.0.0.0:$PORT app:app
