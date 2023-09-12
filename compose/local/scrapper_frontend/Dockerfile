FROM node:18.16-bullseye AS development
LABEL authors="michal"
#ENV NODE_ENV development
# Add a work directory
WORKDIR /usr/src/frontend
# Cache and Install dependencies

COPY web_grades_scrapper .

COPY ./compose/local/scrapper_frontend/start_scrapper_frontend ./start_scrapper_frontend


RUN sed -i 's/\r$//g' ./start_scrapper_frontend
RUN chmod +x ./start_scrapper_frontend

RUN npm install

CMD ["npm", "run", "dev"]

#COPY package.json .
#COPY yarn.lock .
#RUN yarn install
## Copy app files
#COPY . .
## Expose port
#EXPOSE 3000
## Start the app
#CMD [ "yarn", "start" ]
