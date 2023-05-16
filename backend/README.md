
# Install

Install requirements: 

```
python -m pip install -r requirements.txt 
``` 

Copy the config-sample.json file into config.json and fill in the information.

Create the database:

```
python manage.py migrate 
```

Create the admin user: 

```
python manage.py createsuperuser 
``` 
