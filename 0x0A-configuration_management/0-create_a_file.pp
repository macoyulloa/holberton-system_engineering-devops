#Create file in /tmp path
file { '/tmp/holberton':
    mode    =>  '0744',
    owner   =>  'www-data',
    group   =>  'www-data',
    content =>  'I love Puppet',
}
