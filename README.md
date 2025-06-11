# 💎 Luxury E-Commerce Website — Django

A fully responsive, user-authenticated luxury e-commerce platform built with Django, Bootstrap, and modern frontend design principles. This project features premium product listings, an elegant checkout experience, dynamic cart functionality, invoice generation, and integrated payment simulation.

![Screenshot](screenshots/homepage.png)

---

## ✨ Features

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

> Add your actual screenshots to the `/screenshots` folder.

| Home Page | Product Detail | Checkout |
|-----------|----------------|----------|
| ![](screenshots/homepage.png) | ![](screenshots/product-detail.png) | ![](screenshots/checkout.png) |

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Bootstrap 5, CSS3, JS
- **Database**: django superuser admin
- **PDF Generation**: ReportLab / xhtml2pdf
- **Charts**: Chart.js (for admin dashboard)
- **Auth**: Django built-in auth system

---

## 📦 Project Structure

