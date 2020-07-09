FROM python:latest
RUN mkdir /HW-docker
WORKDIR /HW-docker
COPY . .
CMD ["python3", "vm_read.py"]
