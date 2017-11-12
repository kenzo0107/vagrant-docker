# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.synced_folder "./docker", "/vagrant", :nfs => true

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", 4096]  # メモリ調整
    vb.customize ["setextradata", :id, "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled", 0] # Vagrant側とホスト(mac, widnwows等)の時刻同期
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    apt-key fingerprint 0EBFCD88
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    apt-get update
    apt-get install -y docker-ce
    groupadd docker
    usermod -aG docker $USER
    curl -L "https://github.com/docker/compose/releases/download/1.12.0/docker-compose-$(uname -s)-$(uname -m)" >  /usr/bin/docker-compose
    chmod +x /usr/bin/docker-compose
  SHELL

  config.vm.network "private_network", ip: "192.168.35.101"
end
