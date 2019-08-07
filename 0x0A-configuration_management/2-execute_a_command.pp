# kills process named killemenow
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin/',
}
