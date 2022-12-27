FROM python:3.9-slim

WORKDIR /fastapi
COPY requirements.txt ./
RUN pip install -r requirements.txt
# COPY main.py ./
# ADD sql sql
# ADD alembic alembic
# COPY main.py ./
# ENV PYTHONPATH "${PYTHONPATH}:/fastapi"
# CMD python fastapi/main.py
CMD tail -f /dev/null