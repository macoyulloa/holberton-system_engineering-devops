# install nginx
exec { '/usr/bin/env apt-get update': }
exec { '/usr/bin/env apt-get -y install nginx': }
exec { '/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html': }
exec { '/usr/bin/env sed -i "42i\ location /redirect_me { return 301 https://www.google.com; }" /etc/nginx/sites-available/default': }
exec { '/usr/bin/env sed -i "46i\ error_page 404 /custom_404.html;\nlocation = /custom_404.html {\nroot /var/www/html;\ninternal; }':}
exec { '/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html': }
exec { '/usr/bin/env service nginx restart': }
