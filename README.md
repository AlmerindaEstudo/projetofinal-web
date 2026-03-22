


1   git clone -b principal --single-branch https://github.com/AlmerindaEstudo/projetofinal-web.git

2   cd projetofinal-web


3 python -m venv venv


4 venv\Scripts\Activate


5 pip install -r requirements.txt

6 cd backend

7 python manage.py makemigrations


8  python manage.py migrate


9 python manage.py runserver

