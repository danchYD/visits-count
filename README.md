# Visits count

[![Status](https://img.shields.io/badge/status-ready-brightgreen)]()
[![Language](https://img.shields.io/badge/language-Python-green)]()

A pet project created while exploring the capabilities of the FastAPI framework. It counts the number of visits to the main page and the number of greetings to different users.

## Contents
- [About project](#about-project)
- [Functionality](#functionality)
- [Technologies](#technologies)
- [Installation](#installation)
- [Project structure](#project-structure)
- [What i learned](#what-i-learned)
- [Contacts](#contacts)

## About project

**Objective:**
- Learning the FastAPI framework

## Functionality
- / - main page, increment counter; showing current count
- /visits - showing current count; with param ?reset=true resets the counter
- /greet/{name} - greeting user by name; showing total greetings for current user

## Technologies

**Stack:**
- **Programming language:** Python 3.14.3
- **Frameworks:** FastAPI
- **Other:** Docker

## Installation

### Prerequisites
- Docker 29.2.0+

### Installation steps
1. **Clone repository:**
```
git clone https://github.com/danchYD/visits-count.git
cd visits-count
```

2. **Docker build:**
```
docker build -t visits-count:latest .
```

3. **Docker container run:**
```
docker run -d -p 8000:8000 visits-count:latest
```

## Project structure

```
visits-count/
├── main.py # Main application
├── .gitignore # Gitignore file
├── Dockerfile # Docker image
├── requirements.txt # Dependencies
└── README.md # Documentation
```

## What i learned

- Creating an application using the FastAPI framework
- Creating a Dockerfile, building an image, running a container
- Writing project documentation for GitHub

## Contacts

**Danila Yakovlev** - dwhytt23@yandex.ru