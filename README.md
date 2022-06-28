## Weather advice product app

A product recommendation system application builds using Python, JWT Token,
Django, Django rest framework, and drf_spectacular package for API docs. Where customers 
will be able to see product recommendations depending on the current
weather condition grabbed from the free weather API. For example, 
If the temperature is in the normal range, the user will be 
recommended the normal weather clothes.


## Installation
```
Python version 3.10.4
git clone https://github.com/shoumitro-cse/weather_advice_product_app.git
cd weather_advice_product_app
cp env.example .env
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
rm -rf static
mv staticfiles static
python manage.py runserver
```

## API docs

```
Here, has been used a drf_spectacular package for API docs, I think that it will be 
very helpful for frontend developers. If you would like to see special instructions 
for each api, please keep your eye on each API doc.
protocol = http, https
domain = localhost or others
port = 80, 8000 etc
{protocol}://{domain}:{port}/api/docs/ (for API HTTP methods and descriptions)
{protocol}://{domain}:{port}/api/redocs/
{protocol}://{domain}:{port}/api/schema/ (for download API ymal file)
```
![](https://github.com/shoumitro-cse/weather_advice_product_app/blob/main/docs/api_doc_image.png?raw=true)

## Testing
```
Here, A total of 31 (Thirty one)  unit test has been added. also, you can run it separately. 
Each testing class doc provides instructions on how to run it
To run all test cases:
python manage.py test tests
```

![](https://github.com/shoumitro-cse/weather_advice_product_app/blob/main/docs/test_image.png?raw=true)


