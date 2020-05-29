# Change Nginc ULLIMIT
exec { 'ullimit':
  command  => 'sudo sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/g\' /etc/default/nginx',
  provider => 'shell',
}

exec { 'restar nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}