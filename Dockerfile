FROM python:3.13
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash", "-c", "./init.sh && python -m app"]
