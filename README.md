

    curl https://raw.githubusercontent.com/andytwoods/alexaDuploServo/master/servo_server.py servo.py
    sudo pip3 install flask-ask
    sudo pip3 install RPi.GPIO
    sudo pip3 install 'cryptography<2.2'


# alexaDuploServo


edit below file via:

    sudo nano /etc/rc.local

insert below before 'exit 0' <= v important to keep 'exit 0'.

    sudo -E /usr/bin/python3 /home/pi/servo_server.py &
    sudo /home/pi/ngrok http -config=/home/pi/.ngrok2/ngrok.yml -subdomain=robin_rotate 5000 &

    sudo chmod +x /etc/rc.local
