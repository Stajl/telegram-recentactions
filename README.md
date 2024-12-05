# telegram-recentactions
load and save to file recent actions log from telegram group

pip freeze > requirements.txt
use credentials from .env

API_ID=XXXXXXXXX
API_HASH=YYYYYYYYYYYYYYYYYYYYYYYY
GROUP_CHAT_ID=-100ZZZZZZZZZZ

Obtaining api_id : https://core.telegram.org/api/obtaining_api_id
In order to obtain an API id and develop your own application using the Telegram API you need to do the following:

    Sign up for Telegram using an official application.
    Log in to your Telegram core: https://my.telegram.org.
    Go to "API development tools" and fill out the form.
    You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.
    For the moment each number can only have one api_id connected to it.

We will be sending important developer notifications to the phone number that you use in this process, so please use an up-to-date number connected to your active Telegram account.

GROUP_CHAT_ID: Go to https://web.telegram.org
Look at the URL and find the part that looks like c12112121212_17878787878787878
Remove the underscore and after c12112121212
Remove the prefixed letter 12112121212
Prefix with a -100 so -10012112121212
