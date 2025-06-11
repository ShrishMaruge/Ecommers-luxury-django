# 💎 Luxury E-Commerce Website — Django

A fully responsive, user-authenticated luxury e-commerce platform built with Django, Bootstrap, and modern frontend design principles. This project features premium product listings, an elegant checkout experience, dynamic cart functionality, invoice generation, and integrated payment simulation.

![homepage](https://github.com/user-attachments/assets/083478a4-82d9-4411-afd9-de1ddb40e18a)


---


### 🛍️ Shopping
- Product listing with search & category filters
- Product detail pages with rich UX
- Wishlist, cart, and browsing history

### 💼 Checkout
- Multi-step checkout flow (Cart → Shipping → Payment → Review)
- Elegant tabbed UI with animated progress bar
- Simulated payment options: Credit/Debit, UPI (PhonePe), COD

### 🧾 Invoicing
- Downloadable invoice PDF with order & payment details

### 👤 User Profiles
- Order history, recent cart items, saved addresses
- Profile picture upload, loyalty points, smart recommendations
- Download past orders as CSV

### 🔐 Authentication
- Login / Signup with sessions
- Restriction: Only logged-in users can "Add to Cart" or "Buy Now"

---

## 🖼️ Screenshots

>  actual screenshots.

| Home Page | Product Detail | Checkout |
|-----------|----------------|----------|
| ![homepage](https://github.com/user-attachments/assets/083478a4-82d9-4411-afd9-de1ddb40e18a) | ![Screenshot 2025-06-11 201126](https://github.com/user-attachments/assets/e0c04a06-3a2c-4ba9-bceb-64539bf85f0b) |![Screenshot 2025-06-11 200804](https://github.com/user-attachments/assets/3c2c1609-f373-4d43-95b8-0abfab51bc7f) |

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Bootstrap 5, CSS3, JS
- **Database**: django superuser admin
- **PDF Generation**: ReportLab / xhtml2pdf
- **Charts**: Chart.js (for admin dashboard)
- **Auth**: Django built-in auth system

---

## 🔐 Admin Access

For demonstration/testing purposes, admin access can be provided on request.

- **Username**: [Available upon request]
- **Password**: [Available upon request]

📩 DM [@ShrishMaruge](https://github.com/ShrishMaruge) for credentials or email me.
<a href="mailto:shrishmaruge@gmail.com">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" width="28" style="vertical-align: middle; margin-right: 6px;" />
  shrishmaruge@gmail.com
</a>
Email : shrish.maruge99@gmail.com

## Setup

```bash
env\Scripts\activate
cd Ecommers
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

##Run

python manage.py runserver

 


