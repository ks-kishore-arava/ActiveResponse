#!/bin/bash

# Start the Uvicorn server
exec uvicorn application.main:app --host 0.0.0.0 --port 8000 --workers 4

exec `tail -f /dev/null`