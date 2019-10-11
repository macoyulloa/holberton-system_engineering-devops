# fixing the error
exec {'number files':
    path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
    command => "sed -i 's/15/1024/g' /etc/default/nginx",
}
-> exec  { 'restart':
    command => 'sudo service nginx restart',
    path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
}
