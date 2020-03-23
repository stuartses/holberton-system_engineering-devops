# Install Puppet Lint Style checker
package { 'Install puppet-lint':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem'
}