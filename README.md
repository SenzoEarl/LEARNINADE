# Learninade
An online education system

### Live: [Learninade on Vercel](https://learninade.vercel.app)
___

#### Demo: [Learninade on Railway](https://blognificent.up.railway.app/)

___

### Database: 
![DB](/media/db-main.png)
___
### Local Server 
1. Clone the repository [here](gh repo clone SenzoEarl/LEARNINADE-docker)
2. run `pip install -r requirements.txt` to install all packages
3. In the project directory, run `py manage.py runserver 8000 --settings=LEARNIFY.settings.local` 
4. Open [http://localhost/](http://localhost/) in your web browser
5. run `py manage.py createsuperuser` and create new user admin

### Production Server 
1. Requires docker
2. Clone the repository [here](gh repo clone SenzoEarl/LEARNINADE-docker)
2. run `docker compose up` to install all packages
4. Open [http://localhost/](http://localhost/) in your web browser
5. run `docker compose exec web python /code/manage.py makemigrations`
6. run `docker compose exec web python /code/manage.py migrate`
7. run `docker compose exec web python /code/manage.py createsuperuser` and create user

___

### Links: 
1.  [Django](https://www.djangoproject.com/)
2. [Bootstrap](https://getbootstrap.com/)
3. [Railway](https://railway.app/)
4. [Vercel](https://vercel.com/)
5. [Font Awesome](https://fontawesome.com/)