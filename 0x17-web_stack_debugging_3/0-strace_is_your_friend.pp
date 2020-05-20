# Fix a PHP file of a WordPress webpage

exec { 'Fix php file':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
