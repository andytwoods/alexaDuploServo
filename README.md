# alexaDuploServo


edit below file via:

    sudo nano /etc/rc.local

insert below before 'exit 0' <= v important to keep 'exit 0'.

    python3 /home/pi/servo_server.py &
    sudo /home/pi/ngrok http -subdomain=robin_rotate 5000 &

    sudo chmod +x /etc/rc.local
