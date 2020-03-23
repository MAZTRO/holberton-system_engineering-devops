# Script to install a gem with Puppet
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
