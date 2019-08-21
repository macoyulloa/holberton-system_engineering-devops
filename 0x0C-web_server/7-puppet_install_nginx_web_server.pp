# install nginx
exec { '/usr/bin/env apt-get update': }
exec { '/usr/bin/env apt-get -y install nginx': }
exec { '/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html': }
