FROM python:3.9
WIRKDRI /app
COPY . /app/
RUN pip3 install -U -r requirements.txt
CMD ["python3", "fsubbot.py"]
