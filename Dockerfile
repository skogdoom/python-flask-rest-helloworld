FROM python:3
ADD /src/application.py /
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./application.py" ]
EXPOSE 5000/tcp
