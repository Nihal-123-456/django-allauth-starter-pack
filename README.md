# Django Project Setup Guide

This guide will help you set up and run the project locally.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <your-repository-folder>
````

---

### 2. Install Dependencies

Make sure you have Python and pip installed, then run:

```bash
pip install -r requirements.txt
```

---

### 3. Create a `.env` File

Inside the project root, create a `.env` file and add the following environment variables:

```env
SECRET_KEY=your-django-secret-key
DATABASE_URL=your-database-url
CONN_MAX_AGE=maximum lifetime of your database connection at the end of a request
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
CLOUDINARY_CLOUDNAME=your-cloud-name
CLOUDINARY_API_KEY=your-cloudinary-api-key
CLOUDINARY_API_SECRET=your-cloudinary-api-secret
DEBUG=True
```

---

### 4. Configure Secrets and Services

* Generate a new **Django secret key** for your django project and add it to your `.env` file:

  ```bash
  cd src && py generate_secret_key.py
  ```
* Add the **database connection string** (e.g., from [Neon Postgres](https://neon.tech/)).
* Configure your **email credentials** for sending emails.
* Configure your **Cloudinary credentials** for storing media files.

---

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

---

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

* After creating a superuser, log in to Django admin and add your **social application credentials**.
* This project has **Google** configured. You can add others (e.g., LinkedIn) by following the [Django Allauth documentation](https://django-allauth.readthedocs.io/).

---

### 7. Configure Sites and Social Applications

* In Django admin, create a **Site** entry (e.g., `example.com` or `localhost:8000`).
* Add it to your **Social Application**.
* Set the correct `SITE_ID` in your `settings.py`.

---

## ✅ Run the Server

Once everything is configured, start the development server:

```bash
python manage.py runserver
```

Your project should now be running at [http://localhost:8000](http://localhost:8000) 🎉

---

## 📖 Notes

* You can extend social login by adding more providers through Django Allauth.
* Make sure your `.env` file is **never committed** to Git. Add it to `.gitignore`.


