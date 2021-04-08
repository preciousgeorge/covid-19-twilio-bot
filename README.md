# TWILIO COVID-19 UPDATE BOT

## DEPLOY
This instruction is strictly for how to deploy to `google cloud platform`.
Login to your `google cloud platform` and once on the dashboard, click on the sidebar menu and click on `cloud functions` and set your function name to whatever you prefer. Also check `Allow unauthenticated invocations` to make the webhook publicly available. Click on `Save`.

Click `next`, and you should see a page to put the code on `main.py`. Set the `Runtime` to `Python 3.9` and the `Entry point` to `whatsapp_webhook`. Replace the contents of the *main.py* file on the left with those from this main.py  Do the same for the `requirements.txt` file so as to have those functionalities available to the script. After all that, click `deploy`


