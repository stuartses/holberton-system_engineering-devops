# Kill process named killmenow
exec { 'kill killmenow':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => shell
}