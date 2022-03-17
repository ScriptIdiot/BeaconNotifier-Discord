# BeaconNotifier-Discord
Cobalt strike CNA script to notify you via Discord whenever there is a new beacon.

Make sure you have python3 installed

Steps:

1) Create a Discord Server and get a Webhook URL (Server settings > Integration > Webhooks > Create/New_Webhooks > Copy Webhook URL)
2) Paste the URL in request.py
3) Edit the path of request.py in notify.cna
4) Edit the message as you want (Optional)
5) Run the cna as following:

./agscript [C2 IP] [C2 Port] [username] [C2 password] [path to cna]


![image](https://user-images.githubusercontent.com/21979646/151166400-26fbd802-e8fa-4a72-afb6-b334fb935c83.png)




Reference:

https://download.cobaltstrike.com/aggressor-script/functions.html
https://stackoverflow.com/questions/62731561/discord-send-message-only-from-python-app-to-discord-channel-one-way-communic
