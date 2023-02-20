FROM python:3.10-bullseye

WORKDIR /app
ADD ./main.py /
ADD ./requirements.txt /
RUN pip install -r requirements.txt
ENV SERVER_PORT=8088
EXPOSE 8088
CMD [ "python","main.py" ]