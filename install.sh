#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-dev python-pip mongodb nginx uwsgi-plugin-python libffi-dev
sudo pip install Flask pymongo uwsgi bcrypt

sudo rm /etc/nginx/sites-enabled/*

# First option was to link from apps-enabled to the /vagrant config files, but later on
# I discovered that doing so it would break nginx and uwsgi since the services are started
# before the /vagrant folder gets mounted, so the servers won't read the config files
cat /vagrant/configs/vagrant_uwsgi.ini | sudo tee /etc/uwsgi/apps-enabled/vagrant_uwsgi.ini
cat /vagrant/configs/nginxConfig | sudo tee /etc/nginx/sites-enabled/queChistoso

#TODO: Decide if continue to setup services this way or modify the upstart jobs to start on vagrant-mount

# Here we add the init declaration so the uwsgi server starts after vagrant folder gets mounted
sudo tee /etc/init/uwsgi.conf <<EOF
description "uWSGI"
start on vagrant-mounted
stop on runlevel [!2345]
expect fork
respawn
respawn limit 10 5

exec uwsgi --master --emperor /etc/uwsgi/apps-enabled/*.ini --die-on-term --uid www-data --gid www-data --logto /var/log/uwsgi/app/vagrant.log
EOF

sudo update-rc.d nginx defaults
sudo update-rc.d uwsgi defaults

sudo service uwsgi restart
sudo service nginx restart

#TODO: Secure mongo installation
#TODO: Secure installation (only login by key)