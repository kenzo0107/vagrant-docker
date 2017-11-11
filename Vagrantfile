# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.synced_folder "./docker", "/vagrant", :nfs => true

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", 4096]  # メモリ調整
    vb.customize ["setextradata", :id, "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled", 0] # Vagrant側とホスト(mac, widnwows等)の時刻同期
  end

  config.vm.network "private_network", ip: "192.168.35.101"
end
