FROM python:3.11

RUN python -m pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8050
CMD ["python", "main.py"]

# ENTRYPOINT [ "uvicorn" ]
# CMD [ "--host", "0.0.0.0", "main:app" ]