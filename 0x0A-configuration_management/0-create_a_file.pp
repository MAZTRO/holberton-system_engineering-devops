# Script to create a file in a specific path
file { '/tmp/holberton':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
