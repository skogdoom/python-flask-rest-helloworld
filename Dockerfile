FROM python:3
ADD application.py /
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./application.py" ]
EXPOSE 5000/tcp
