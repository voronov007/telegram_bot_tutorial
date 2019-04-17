# Telegram Bot Tutorial
By using this repo I assume that you already created a Telegram Bot using [BotFather](https://telegram.me/botfather).

## Main idea
Create Telegram Bot from scratch. 
* Create project using best practices
* Add basic logic to the bot
* Debug
* Deploy

## Technical info:
* Python (programming language)
* Django (web framework)
* MongoDB (NoSQL database)
* Heroku (hosting server)

## Local Deploy
* Download repo
* Install/set/activate virtual environment
* Install packages (`pip install -r requirements.txt`)
* install and start MongoDB
* Set environment variables: DJANGO_SETTINGS_MODULE (=tb_tutorial.settings.develop), TUTORIAL_BOT_TOKEN
* Run server
* Install and start ngrok (`./ngrok http 8000`)
* Set telegram router to your web server (`https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/`)

## Deploy on Heroku
All necessary files for the deploy are already in the repo.
Login/Register on Heroku. Create an app. Install CLI
* `heroku login`
* `heroku git:remote -a <your app name>`
* Add files to git and commit changes if needed (`git add .`, `git commit -am "some commit message"`)
* `git push heroku master`
* Create a [remote Mongo database](https://mlab.com/). Check db connection string in production settings file and update it if needed
* Set production environment variables: DJANGO_SETTINGS_MODULE (=tb_tutorial.settings.production), 
MONGO_USER, MONGO_PASSWORD, MONGO_HOST, TUTORIAL_BOT_TOKEN
* Set telegram router to your web server (`https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/`)

## Step By Step Tutorial
You may find step by step tutorial for this repo on [medium](https://medium.com/@voronov007/telegram-bot-from-scratch-development-with-python-and-deploying-on-free-of-costs-server-from-2463f2b63d83)
