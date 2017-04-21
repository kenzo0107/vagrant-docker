# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "kenzo0107/ubuntu14.04.5LTS-docker-dockercompose"
  config.vm.box_url = "https://atlas.hashicorp.com/kenzo0107/boxes/ubuntu14.04.5LTS-docker-dockercompose"
  config.vm.synced_folder "./docker", "/vagrant", :nfs => true

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", 4096]  # メモリ調整
    vb.customize ["setextradata", :id, "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled", 0] # Vagrant側とホスト(mac, widnwows等)の時刻同期
  end

  config.vm.network "private_network", ip: "192.168.35.101"
end
