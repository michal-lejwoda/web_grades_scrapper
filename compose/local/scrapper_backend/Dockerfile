FROM python:3.10.12-bullseye
LABEL authors="michal"
WORKDIR /usr/src/app

#COPY requirements.txt ./
COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./compose/local/scrapper_backend/start_scrapper_backend /start_scrapper_backend

RUN sed -i 's/\r$//g' /start_scrapper_backend
RUN chmod +x /start_scrapper_backend


#RUN sed -i 's/\r$//g' /start_scrapper_frontend
#RUN chmod +x /start_scrapper_frontend
#CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]