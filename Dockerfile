FROM python:3

RUN pip install --no-cache-dir -r ./requirements.txt
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["/bin/sh", "-c", "while :; do sleep 10; done"]