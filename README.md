> A batteries-included Django starter project.



Almost entirenly taken from https://github.com/wsvincent/djangox/ but with my own touch and twists.



# How it works

```
python -m venv venv # make environment (once)
. venv/bin/activate # Activate environment. Everytime you start a new console
pip install -r requirements.txt # Install dependencies. Everytime dependencies (requirements.txt)
./manage.py runserver
./manage.py createsuperuser
./manage.py makemigrations # make migrations out of your models file. Only needed to run when the models change.
./manage.py migrate # migrate changes. Everytime new migration files.
```
