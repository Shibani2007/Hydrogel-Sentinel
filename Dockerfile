FROM python:3.10-slim
WORKDIR /app
COPY src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
CMD ["python","src/app.py","--input","data/sample_input.csv","--output","data/sample_output.csv"]
