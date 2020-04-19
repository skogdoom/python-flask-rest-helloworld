FROM python:3
ADD application.py /
CMD [ "python", "./application.py" ]
