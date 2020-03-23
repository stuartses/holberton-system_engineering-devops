# Creates a file in /tmp/holberton path
file { 'Holberton':
  path    =>'/tmp/holberton',
  mode    =>'0744',
  content =>'I love Puppet',
  group   =>'www-data',
  owner   =>'www-data',
}