FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD /src/*.py /
CMD [ "python", "./application.py" ]
EXPOSE 5000/tcp
