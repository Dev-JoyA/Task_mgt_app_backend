# Task Management Dashboard Backend

## Objective

A backend for a task management dashboard application using Django and Python 3.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This project serves as the backend for a task management dashboard application. It provides a RESTful API for managing tasks and users, built using Django.

## Features

- Set up a Django project for the task management application.
- Create models for Task and User with necessary fields.
- Implement CRUD operations for tasks through API endpoints.
- Fetch tasks based on their status (In Progress, Completed, Overdue).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a working computer with an internet connection.
- You have installed [Python 3](https://www.python.org/downloads/).
- You have installed [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager).
- You have installed [Virtual Environment](https://docs.python.org/3/library/venv.html) (recommended).
- You have installed [Visual Studio Code](https://code.visualstudio.com/).

## Installation

Follow these steps to set up the project locally.

### 1. Clone the repository

Open your terminal and run the following commands:

### 2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3. Install the required packages using pip:
pip install -r requirements.txt

### 4. Run the following commands to apply the database migrations:
python3 manage.py makemigrations
python3 manage.py migrate


### 5. To start the Django development server, use:
python3 manage.py runserver

### 5. Usage
You can now test on postman , or start the frontend project 
