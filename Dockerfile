FROM python:3.7.5-slim

WORKDIR /usr/src/app

RUN python -m pip install \
         requests bs4 tabulate \
         numpy matplotlib

COPY covid19.py .

CMD ["python", "covid19.py"] 
