# fixing the error
exec {'number of sessions hard':
    path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
    command => "sed -i 's/nofile 5/nofile 100/g' /etc/security/limits.conf",
}
-> exec {'number of sessions soft':
    path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
    command => "sed -i 's/nofile 4/nofile 100/g' /etc/security/limits.conf",
}