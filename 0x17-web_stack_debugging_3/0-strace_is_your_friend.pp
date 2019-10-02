# fixing the error
file { '/var/www/html/wp-settings.php':
    ensure => present,
} ->
file_line { 'replace':
    path  => '/var/www/html/wp-settings.php',
    line  => "require_once( ABSPATH . WPINC . '/class-wp-locale.php');",
    match =>  '^*phpp.*$',
}
