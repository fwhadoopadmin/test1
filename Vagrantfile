# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  servers=[
    {
      :hostname => "server1",
      :box => "centos/7",
      :ip => "10.0.2.16",
      :ssh_port => "2200"
      #:box.vbguest.installer_options = { allow_kernel_upgrade: true }
    },
    {
      :hostname => "server2",
      :box => "centos/7",
      :ip => "10.0.2.17",
      :ssh_port => "2200"
    },
    {
      :hostname => "server3",
      :box => "centos/7",
      :ip => "10.0.2.18",
      :ssh_port => "2200"
   }
  ]

  #define the loop 
  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
            node.vm.box = machine[:box]
            node.vm.hostname  = machine[:hostname]
            node.vm.network :private_network, ip: machine[:ip]
            node.vm.network "forwarded_port", guest: 22, host: machine[:ssh_port], id: "ssh" 
            #node.vm.synced_folder "vagworkstation\\data", "/home/vagrant/data"
            #node.vm.provision "file", source: "vagworkstation\\data\\copiedfile.txt", destination: "/home/vagrant/data/copiedfile.txt"
            node.vm.box_version = "1809.01"
            node.vbguest.auto_update = false


            node.vm.provider :virtualbox do |vb|
              vb.customize ["modifyvm", :id, "--memory", 1024]
              vb.customize ["modifyvm", :id, "--cpus", 2]
            end
    end 
  end
end 
