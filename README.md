> A batteries-included Django starter project.



Almost entirenly taken from https://github.com/wsvincent/djangox/ but with my own touch and twists.

# How to deploy yourself?

For Ubuntu and probably most Linux systems:

1. Make a user called noteglow0
2. rsync to remote $HOME/noteglow0/app
3. add a .env.json file with your specs
4. install using pip install -r requirements.txt
5. run ./bin/start
6. Make a HTTP Reverse engine to point to $HOME/noteglow0/data/gunicorn.sock
7. Enjoy life



```
# .env.json file example
{
  "ENV": 0,
  "PROJECT": "noteglow0",
  "DATA_DIR": "/home/noteglow0/data",
  "WEB_URL": "https://noteglow.com",
  "API_URL": "https://noteglow.com",
  "ADMIN_PATH": "admin",
  "SECRET_KEY": "YOUR_SUPER_SECRET_KEY_HERE",
  "DEBUG": false 
}
```



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
