# Deployment Notes

Build Docker image:
docker build -t cossen-pipeline .

Run container (mount data to persist output):
docker run --rm -v "$(pwd)/data:/app/data" cossen-pipeline
