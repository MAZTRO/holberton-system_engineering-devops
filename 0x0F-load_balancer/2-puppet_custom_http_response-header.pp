# Script to install a gem with Puppet
# Instal HAproxy and an initial config

exec { 'HTTP Config':
  provider => shell,
  command  => "apt-get update && apt-get install haproxy -y && echo 'Holberton School' | sudo tee /var/www/html/index.html && sed -i '18 a \ \n\t rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default && sed -i '/http {/a \ \tadd_header X-Served-By $HOSTNAME;' /etc/nginx/nginx.conf && service nginx restart",
}
