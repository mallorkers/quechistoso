# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.network "forwarded_port", host: 5000, guest: 5000
  config.vm.network "forwarded_port", host: 8080, guest: 80
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "shell", path: "install.sh"
end
