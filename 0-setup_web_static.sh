#!/usr/bin/env bash
# sets up servers for deplyoment
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Bonaparte UTERAMAHORO
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo echo '
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/Forecast;
	location /hbnb_static {
		alias /data/web_static/current/;

}
        index index.html index.htm 404.html index.nginx-debian.html;
        server_name _;
        add_header X-Served-By $HOSTNAME;
        error_page 404 /5-design_a_beautiful_404_page.html;
}

' > /etc/nginx/sites-enabled/default

sudo service nginx restart
