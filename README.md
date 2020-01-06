# alexaDuploServo


edit below file via:

    sudo nano /etc/rc.local

insert below before 'exit 0' <= v important to keep 'exit 0'.

    sudo -E /usr/bin/python3 /home/pi/servo_server.py &
    sudo /home/pi/ngrok http -config=/home/pi/.ngrok2/ngrok.yml -subdomain=robin_rotate 5000 &

    sudo chmod +x /etc/rc.local
