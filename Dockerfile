# Operating system
FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Run as non-root user
RUN adduser -D myuser
USER myuser

# Run gunicorn
CMD gunicorn boatrent.wsgi:application --bind 0.0.0.0:$PORT