
# Extraa
Prototype add-on advice tool created for Holiday Extras' challenge as part of Canterbury Christ Church Hackabury 2025, developed initially over 24 hours using Django and Tailwind CSS. Find out more about Hackabury 2025 [here](https://benjaminalbert387.github.io/hackabury/).

## Team Members
This prototype was submitted under team Temporary Fix. The team was made up of the following members:
| Team member      | Email Address          |
|------------------|------------------------|
| Jessica Excell   | je398@canterbury.ac.uk |
| Alireza Khandan  | ak718@canterbury.ac.uk |
| George Graham    | gg287@canterbury.ac.uk |
| Alex Ward        | aw949@canterbury.ac.uk |
| Ethan McGuinness | em814@canterbury.ac.uk |

## Getting Started
### Prerequisites
Before setting up the project, please ensure the following are installed:
- Python 3 - Install from https://www.python.org/downloads/
- Pip (if this isn't installed with Python 3) - Install from https://pip.pypa.io/en/stable/installation/ 

### Configuring the Project
First, clone the project:
```
https://github.com/jess-excell/hackabury-submission
```
Then install the necessary requirements (Django) using pip. **It is recommended that you do so inside a virtual environment.**
```
pip install -r requirements.txt
```
Next, set up the database.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Finally, populate the database.
```
python manage.py populate
```
You can also add a superuser at this stage if you wish to use the Admin interface. Documentation explaining how to create a superuser is available here: https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user

### Running the Project
To run the project, start the development server:
```
python manage.py runserver
```
You should be able to then access the server at `localhost:8000`.

## External Documentation
- Django docs: https://docs.djangoproject.com/en/5.2/
- Tailwind CSS docs: https://tailwindcss.com/