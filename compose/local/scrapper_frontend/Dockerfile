FROM node:18.16-alpine AS development
LABEL authors="michal"
ENV NODE_ENV development
# Add a work directory
WORKDIR /usr/src/app
# Cache and Install dependencies

COPY . .

COPY ./compose/local/scrapper_frontend/start_scrapper_frontend /start_scrapper_frontend

RUN sed -i 's/\r$//g' /start_scrapper_frontend
RUN chmod +x /start_scrapper_frontend


#COPY package.json .
#COPY yarn.lock .
#RUN yarn install
## Copy app files
#COPY . .
## Expose port
#EXPOSE 3000
## Start the app
#CMD [ "yarn", "start" ]
