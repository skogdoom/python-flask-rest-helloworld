FROM python:3
ADD application.py /
RUN pip install Flask
CMD [ "python", "./application.py" ]
EXPOSE 5000/tcp
