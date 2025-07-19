# 🛒 E-commerce Backend API (FastAPI + MongoDB)

A simple asynchronous backend built with **FastAPI** and **MongoDB** using the **Motor** driver. Supports product listings and order management with pagination and filtering.

---

## 🚀 Features

- Create, list, and filter products
- Place and retrieve customer orders
- Pagination and search support
- MongoDB Atlas or local DB support
- Asynchronous and scalable design using FastAPI + Motor

---

## 🧱 Tech Stack

- **Backend:** FastAPI
- **Database:** MongoDB (Atlas or local)
- **ODM/Driver:** Motor (async MongoDB driver)
- **Validation:** Pydantic
- **Testing:** Postman / Swagger UI

---

## 📦 Installation

```bash
git clone https://github.com/dev-arhaan/fastapi_ecommerce.git
cd fastapi_ecommerce
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````


---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

* Visit the docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📬 API Endpoints

### 📦 Products

* `POST /products/` — Create a product
* `GET /products/` — List products (supports `?search`, `?skip`, `?limit`)

### 📑 Orders

* `POST /orders/` — Place an order
* `GET /orders/` — List all orders

---

## 🧪 Testing

Use your favorite tool:

* [Postman](https://www.postman.com/) — import requests from Swagger UI
* Swagger UI at [localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠 TODO

* [ ] Add product categories
* [ ] Add user authentication
* [ ] Order status tracking
* [ ] Admin dashboard

---

## 📝 License

MIT License

---

## 📫 Contact

Built with ❤️ by [Arhaan](https://github.com/dev-arhaan)
