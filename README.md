# 📘 **Event Management API System**

## 🧾 Description

This system allows users to register for events, track attendance, and manage both event information and speaker details. It supports CRUD operations and enforces simple validation and relationships between the entities.

---

## 📂 Project Structure

```plaintext
event_management_api/
├── main.py
├── schemas/
│   ├── __init__.py
│   ├── user.py
│   ├── event.py
│   ├── speaker.py
│   ├── registration.py
├── routes/
│   ├── __init__.py
│   ├── user.py
│   ├── event.py
│   ├── speaker.py
│   ├── registration.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   ├── event_service.py
│   ├── speaker_service.py
│   ├── registration_service.py
├── requirements.txt
├── README.md
└── __init__.py

```

⚙️ Project Requirements
Python 3.8+

FastAPI

Uvicorn

Dependencies:

txt
Copy
Edit
fastapi
uvicorn
All dependencies are listed in requirements.txt

## 🚀 Instructions for Running and Testing

1️⃣ Clone the repository

git clone [<github-repo-url>](https://github.com/demiladeore/event-management-api.git)
cd event_management_api

2️⃣ Install dependencies

```py
pip install -r requirements.txt
```

3️⃣ Run the app
bash
Copy
Edit
uvicorn main:app --reload
4️⃣ Access the API
Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc
