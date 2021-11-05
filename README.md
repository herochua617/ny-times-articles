## ny-times-articles
The NY Times Most Popular Articles API

## Build and Run Locally
Make sure you have Python 3.10 [installed locally](https://docs.python-guide.org/starting/installation/). 

If you are using heroku you may follow the steps below:

```sh
$ git clone https://github.com/herochua617/ny-times-articles.git
$ cd ny-times-articles

$ pip install -r requirements.txt

$ heroku local web -f Procfile.windows
```
If you do not have heroku then you may follow the steps below:

```sh
$ git clone https://github.com/herochua617/ny-times-articles.git
$ cd ny-times-articles

$ pip install -r requirements.txt

$ python main.py
```

Your app should now be running on http://localhost:5010/



