## ny-times-articles
The NY Times Most Popular Articles API

## Build and Run Locally
Make sure you have Python 3.10 [installed locally](https://docs.python-guide.org/starting/installation/). 

> If you are using heroku you may follow the steps below:

```sh
heroku config:set API_KEY={Put the api key from heroku}
heroku config:set filename_ref={Put the html template file name}
heroku config:set filename={Put the rendered html file name}

```

```sh
$ git clone https://github.com/herochua617/ny-times-articles.git
$ cd ny-times-articles

$ pip install -r requirements.txt

$ heroku local web -f Procfile.windows
```
For more information, you may refer to https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524

> If you do not have heroku then you may follow the steps below:

1. Create an .env file with the variables below:

``` sh

API_KEY={Put the api key from heroku}
filename_ref={Put the html template file name}
filename={Put the rendered html file name}

```

2. Run the command below in git bash
```sh
$ git clone https://github.com/herochua617/ny-times-articles.git
$ cd ny-times-articles

$ pip install -r requirements.txt

```

3. Put the .env in the same directory as main.py


4. Run the command below in git bash

``` sh

$ python main.py

```

Your app should now be running on http://localhost:5000/

heroku URL: https://ny-times-article-app.herokuapp.com/

