# BeaconNotifier-Discord
This is to notify you via Discord whenever there is a new beacon.

Make sure you have python3 installed

Steps:

1) Create a Discord Server and get a Webhook URL (Server settings > Integration > Webhooks > Create/New_Webhooks > Copy Webhook URL)
2) Paste the URL in request.py
3) Edit the path of request.py in notify.cna
4) Edit the message as you want (Optional)
5) Run the cna as following:

./agscript [C2 IP] [C2 Port] [user name] [C2 password] [path to cna]
