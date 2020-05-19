#!/usr/bin/env bash
# Fix a PHP file of a WordPress webpage

/* exec { 'Install stdlib':
  provider => shell,
  command  => '/usr/bin/puppet module install puppetlabs-stdlib',
}

include stdlib

file_line { 'Fix a line to /var/www/html/wp-settings.php':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match  => 'phpp',
  require => Exec['Install stdlib']
} */

exec { 'Fix php file':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
