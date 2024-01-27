# Web grades scrapper - Simple app which get data from pages like Opencritic, Metacritic, Imdb and display them in simple form. 


## Technology stack

### DevOps
- Nginx
- Docker
### Backend 
- Fast api
### Frontend:
- React

## Application technology description

To create this app i used Fast api as backend and react as frontend. For backend side of application i created tests of every single request to make sure that eveything works fine. Application utilizes Docker containers for seamless deployment and execution. 
Just like my other apps This application is hosted on my vps server too and with each approved PR app is built and reloaded automatically thanks to github actions.

## Application allows to:

- Display games data from Metacritic
- Display games data from Opencritic
- Display film data from Imdb

## Problems
- During the writing of the application I encountered several problems, for example, 
2 months after writing the application metacritic refreshed the layout of their site so I had to write the script again, and from time to time they add changes so it happens that not everything downloads correctly
- An api is required to display the list from opencritic, which doesn't have as many queries as I would like it to have

## PS
Originally the application was a bot for discord but I decided it would be good to have a site that displays this data in one place
