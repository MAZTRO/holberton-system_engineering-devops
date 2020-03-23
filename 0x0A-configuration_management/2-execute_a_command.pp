# Script to kill a specific process
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}
