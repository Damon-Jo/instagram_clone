# django_zero_to_instagram


This is Instagram clone cording using Django

---

## How to run

After installing Python 3.7 or a higher version,

```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source ./venv/Scripts/activate

# Install the required packages
pip install -r requirements.txt

# Create the database using migrate command
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver

# Access the application in your browser
http://127.0.0.1:8000/main/
```
