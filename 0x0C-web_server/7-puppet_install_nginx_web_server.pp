# install Nginx package
package { 'nginx':
  ensure => installed,
}

# configure Nginx
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => present,
  content => "
    server {
      listen 80;
      server_name peterdev.tech;

      location /redirect_me {
        return 301 https://google.com;
      }
      location / {
        return 404;
      }
    }
  ",
  notify  => Service['nginx']
}

# create symbolic link to enable the redirection configuration
file { '/etc/nginx/sites-enabled/redirect_me:'
  ensure => 'link',
  target => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
}
# ensure nginx is running
service {'nginx'
  ensure => 'running'
  enable => true,
}
