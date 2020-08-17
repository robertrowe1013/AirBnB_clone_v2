#!/usr/bin/env bash
# Prep web servers
sudo apt-get update -y
sudo apt-get install -y nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "Test Script" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '37a location /hbnb_static {\nalias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
