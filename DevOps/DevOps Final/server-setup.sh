#!/usr/bin/env bash

# Set parameters
environment=$1
ip1=$2
ip2=$3
password=$4

# Assume root so you can edit the config and hosts files
sudo su

# Install Ansible and Nano
sudo yum install ansible
sudo yum install nano

# Set up ansible.cfg
echo "host_key_checking = False" >> /etc/ansible/ansible.cfg

# Set up hosts file
echo "  #Grouped $environment" >> /etc/ansible/hosts
echo "  [$environment]" >> /etc/ansible/hosts
echo "  $ip1" >> /etc/ansible/hosts
echo "  $ip2" >> /etc/ansible/hosts

echo "  [$environment:vars]" >> /etc/ansible/hosts
echo "  ansible_user=root" >> /etc/ansible/hosts
echo "  ansible_password=$4" >> /etc/ansible/hosts

#run ansible scripts
mkdir ansible-playbooks
cd ansible-playbooks

cat > server-setup.yml << 'endmsg'
---
  - name: Install Apache and NodeJS
    hosts: $environment
    tasks:
      - name: Install Apache
        yum:
          name: apache2
          state: present
      - name: Install NodeJS
        yum:
          name: nodejs
          state: present
endmsg

cat > mariadb-install.yml << 'endmsg'
---
  - name: Install MariaDB
    hosts: $ip2
    tasks:
      - name: Install MariaDB
        yum:
          name: mariadb-server
          state: present
endmsg
cat > github-clone.yml << 'endmsg'
---
  - name: Clone repo
    hosts: $environment
    tasks:
      - name: delete path
        file:
          state: absent
          path: /var/www/html
      - name: Clone Git Repository
        git:
          repo: https://github.com/ttu-bburchfield/swollenhippofinal.git
          dest: "/var/www/html"
          version: "test"
endmsg
