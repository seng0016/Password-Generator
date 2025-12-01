FROM python:3.11
COPY passwordgenerator.py .
CMD ["python", "passwordgenerator.py"]
