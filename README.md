# ✅ TodoManager

A simple and efficient web-based to-do list manager built with **Django** and **PostgreSQL**.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Live Demo](#-live-demo)
- [Getting Started](#-getting-started)

---

## 📖 Overview
**TodoManager** is a task management web application that allows users to organize their daily activities. Users can register, log in, create tasks, mark them as complete or pending, update them, and delete them as needed. It’s a simple solution designed for anyone looking to track their tasks with a clean and responsive UI.

---

## ✨ Features
✅ User Authentication (Signup / Login / Logout)  
✅ Create, Edit, and Delete Tasks  
✅ Mark Tasks as Completed or Pending  
✅ Responsive UI with Bootstrap  
✅ Django Class-Based Views and Forms  

---

## 🛠 Tech Stack
| Layer        | Technology  |
|-------------|-------------|
| Backend     | Django      |
| Database    | PostgreSQL  |
| Frontend    | HTML, CSS   |
| UI Framework| Bootstrap   |

---

## 🌐 Live Demo
🚀 You can access the deployed version here:  
**http://3.111.130.128:8002/**


---

## ⚙ Getting Started

### ✅ Prerequisites
Ensure you have the following installed:
- Python 3.x
- PostgreSQL
- pip
- virtualenv (recommended)

---

### 📥 1. Clone the Repository
```bash
git clone https://github.com/uditnarayan-dev/TodoManager.git

cd TodoManager
virtualenv todo_env
source todo_env/bin/activate   # On Linux/Mac
todo_env\Scripts\activate      # On Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Open your browser and visit: http://127.0.0.1:8000/

---

