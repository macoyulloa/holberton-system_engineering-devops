# Install nginx and set custom header response http
exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}
->package { 'nginx':
  ensure  => 'present',
}
->file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
->service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
->exec { 'initialize server':
  command => '/usr/sbin/service nginx restart',
}
