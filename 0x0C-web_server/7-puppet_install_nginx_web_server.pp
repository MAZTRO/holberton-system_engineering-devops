#!/usr/bin/env bash
# Using PUPPET to install Nginx in a Server

exec { 'nginx':
  provider => shell,
  command  => 'sudo apt update && sudo apt install nginx -y'
  command  => "sed -i '18 a \ \n\t rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default"
  command  => 'echo "Holberton School for the win!" | sudo tee /var/www/html/index.html'
  command  => 'sudo service nginx restart'
}
