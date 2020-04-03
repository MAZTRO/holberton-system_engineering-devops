# Script to install a gem with Puppet
# Instal HAproxy and an initial config

exec { 'HTTP Config':
  provider => shell,
  command  => 'apt-get update && sudo apt-get install nginx -y && echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html && sed -i "18 a \ \n\t rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default && sed -i "/http {/a \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
}
