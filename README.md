# 🚀 FastAPI CRUD App (In-Memory Storage)

A simple FastAPI project for beginners to understand CRUD operations using temporary in-memory storage (Python list).

---

## 📌 Features

* Create User
* Get All Users
* Get Single User by ID
* Update User
* Delete User
* No database required (uses Python list)

---

## 🛠️ Tech Stack

* Python 3.x
* FastAPI
* Uvicorn

---

## 📁 Project Structure

```
project/
│── main.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-crud.git
cd fastapi-crud
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` not present:

```bash
pip install fastapi uvicorn
```

---

### 4. Run the Server

```bash
uvicorn main:app --reload
```

Server will start at:
👉 http://127.0.0.1:8000

---

## 📖 API Documentation

FastAPI provides built-in docs:

* Swagger UI:
  👉 http://127.0.0.1:8000/docs

* ReDoc:
  👉 http://127.0.0.1:8000/redoc

---

## 📬 API Endpoints

### ➕ Create User

**POST** `/todo`

```json
{
  "id": 1,
  "name": "Pankaj",
  "city": "Noida",
  "age": 25
}
```

---

### 📄 Get All Users

**GET** `/todo`

---

### 🔍 Get User by ID

**GET** `/todo/{id}`

Example:

```
/todo/1
```

---

### ✏️ Update User

**PUT** `/todo/{id}`

```json
{
  "id": 1,
  "name": "Updated Name",
  "city": "Delhi",
  "age": 26
}
```

---

### ❌ Delete User

**DELETE** `/todo/{id}`

---

## ⚠️ Important Notes

* Data is stored in memory (list), so it will reset when server restarts
* Not suitable for production
* Good for learning and testing

---

## 📦 requirements.txt

```
fastapi
uvicorn
```

---

## 🙌 Future Improvements

* Add MongoDB / Database
* Add Authentication (JWT)
* Connect with React Frontend
* Deploy on cloud (Render / AWS / Vercel)

---

## 👨‍💻 Author

Pankaj Ranjan Sinha

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
