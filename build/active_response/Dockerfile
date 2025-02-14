FROM python:3.11-alpine

# Install necessary packages including tzdata
RUN apk add --update runit libpq libffi-dev postgresql-client tzdata

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements file
COPY ../../active_response/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN apk add --no-cache postgresql-libs && \
    apk add --update build-base bash git linux-headers python3-dev py-psutil && \
    rm -rf /var/cache/apk/* && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r /tmp/requirements.txt && \
    apk --purge del .build-deps

# Set timezone (example: UTC)
RUN cp /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" > /etc/timezone

# Copy application code
COPY ../../active_response/ /src/active_response/

# Make entrypoint script executable
RUN chmod a+x /src/active_response/entrypoint.sh

# Set working directory
WORKDIR /src/active_response/

# Set entrypoint
ENTRYPOINT ["sh", "/src/active_response/entrypoint.sh"]