# 🎮 Media Review Aggregator Website  

## 📖 Overview  

Originally developed as a **Discord bot**, this project evolved into a **standalone web platform** that aggregates review data from sources such as **OpenCritic**, **Metacritic**, and **IMDb**.  
- The application **scrapes relevant information** and presents key ratings and summaries in a user-friendly format.  
- It provides a **quick and reliable reference** for evaluating games, movies, and TV shows without browsing multiple websites.  
- Built with **FastAPI** and **React + TypeScript**, the platform is **Dockerized** for easy deployment and automatically updated via **GitHub Actions**.  

---

## 🚀 Features  

- 🎮 **Games Data Aggregation** - display ratings from **Metacritic** and **OpenCritic**  
- 🎬 **Movie & TV Show Data** - display IMDb ratings and summaries  
- 🖥️ **Web Interface** - clean, responsive design built with **React + Tailwind**  
- ⚙️ **Automated Deployment** - Docker + GitHub Actions  
- ✅ **Backend Tests** - requests and endpoints tested using **pytest**  

---

## 🛠️ Technology Stack  

### 🔙 Backend
- **FastAPI** - API framework  
- **BeautifulSoup** - web scraping of review data  
- **Pytest** - backend testing  
- **Docker** - containerized deployment  

### 🎨 Frontend
- **React + TypeScript** - interactive UI  
- **TailwindCSS** - styling  

### ⚙️ DevOps
- **Docker** - containerized deployment  
- **Nginx** - serving static files & reverse proxy  
- **GitHub Actions** - CI/CD automation  

---

## ⚠️ Known Issues / Challenges

- Metacritic occasionally **updates its site layout**, requiring adjustments in scraping scripts.  
- OpenCritic API **has limited queries**, which may restrict the amount of data fetched.  
- Scraping relies on external site structures, so occasional **data inconsistencies** may occur.  

---

## 🏗️ Architecture  

🔹 **Frontend (React + TypeScript)** - UI and display of aggregated reviews  
🔹 **Backend (FastAPI + BeautifulSoup)** - scraping, aggregation, and API endpoints  
🔹 **Nginx** - static file serving and reverse proxy  
🔹 **Docker + GitHub Actions** - containerized deployment and CI/CD  

---
