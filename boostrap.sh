#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-dev python-pip mongodb nginx uwsgi-plugin-python
sudo pip install Flask pymongo uwsgi

sudo rm /etc/nginx/sites-enabled/*

# First option was to link from apps-enabled to the /vagrant config files, but later on
# I discovered that doing so it would break nginx and uwsgi since the services are started
# before the /vagrant folder gets mounted, so the servers never can read the config files
cat /vagrant/vagrant_uwsgi.ini | sudo tee /etc/uwsgi/apps-enabled/vagrant_uwsgi.ini
cat /vagrant/nginxConfig | sudo tee /etc/nginx/sites-enabled/queChistoso

# Here we add the init declaration so the uwsgi server starts at startup
sudo tee /etc/init/uwsgi.conf <<EOF
description "uWSGI"
start on runlevel [2345]
stop on runlevel [06]
respawn

exec uwsgi --master --emperor /etc/uwsgi/apps-enabled/*.ini --die-on-term --uid www-data --gid www-data 
EOF

sudo update-rc.d nginx enable
sudo update-rc.d uwsgi enable

sudo service uwsgi restart
sudo service nginx restart