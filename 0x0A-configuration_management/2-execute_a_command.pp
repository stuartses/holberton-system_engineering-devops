# Kill process named killmenow
exec { 'kill killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}