# Increase Open Files Limit
exec { 'Hard nofile':
  command  => 'sudo sed -i \'s/holberton hard nofile 5/holberton hard nofile 65536/g\' /etc/security/limits.conf',
  provider => 'shell',
}
exec { 'Soft nofile':
  command  => 'sudo sed -i \'s/holberton soft nofile 4/holberton soft nofile 65536/g\' /etc/security/limits.conf',
  provider => 'shell',
}
