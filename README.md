# library_django

1. clone the repository
2. enter library_django directory and run "python -m venv venv"
4. enter /library directory
3. run python -m pip install -r requirements.txt
5. run python manage.py migrate
6. run python manage.py createsuperuser (Credentials are needed for swagger authentication)
7. create .env file in library_django directory and add SECRET_KEY='<any key here>' inside
7. run python manage.py runserver

Swagger UI is available at http://localhost:8000/docs
Admin Panel is available at http://localhost:8000/admin

<!-- IMPORTANT NOTE! -->
To add or remove a book from borrowed books use this request body template:
{
    "book_id":""
}
