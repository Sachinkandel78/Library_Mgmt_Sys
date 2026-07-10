# Library Management System

A Django-based web application for managing library books and authors, including borrowing and returning functionality.

## Features

- Add, view, edit, and delete Authors
- Add, view, edit, and delete Books
- Each Book is linked to an Author
- Search books by title or author name
- Borrow and Return functionality that updates copy availability in real time
- Availability status (Available / Not Available) shown automatically based on copies available
- Django Admin panel for quick data management
- Responsive UI styled with Bootstrap

## Requirements

- Python 3.10+
- pip

## Setup Instructions

1. Clone or download this repository, then navigate into the project folder: cd Library_Mgmt_sys
2. Create and activate a virtual environment:
   -> python -m venv .venv
   -> venv\Scripts\activate      # Windows
   -> source .venv/bin/activate   # Mac/Linux
3. Install dependencies:pip install -r requirements.txt
4. Apply database migrations: python manage.py migrate  (makemigrations chai models.py ma kam garesi garni)
5. (Optional) Create an admin account to access the Django admin panel: python manage.py createsuperuser 
6. Run the development server: python manage.py runserver
7. Open your browser and visit: http://127.0.0.1:8000/

## Project Structure
Library_Mgmt_sys/
├── library/                   # Main app (models, views, admin, urls)
├── Library_Mgmt_System/        # Project settings
├── templates/                  # HTML templates
├── Screenshots/                # App screenshots for README
├── requirements.txt
└── manage.py

## Models

**Author**
- name, bio, date_of_birth

**Book**
- title, author (linked to Author), isbn, published_date, copies_total, copies_available
- 'is_available' is automatically calculated based on whether copies_available > 0

## Bonus Features
Searching Books:
On the book list page, use the search bar to find books by title or author name. The search is case-insensitive and matches partial text



## Screenshots

Screenshots/                # App screenshots
   ├── Author_Detail.png
   ├── Author_edit.png
   ├── Author_list.png
   ├── Book_add.png
   ├── Book_detail.png
   ├── Book_list.png
   ├── Delete_Author.png
   └── Home_Page.png
