# configure my 2 webservers using puppet to return their webserver
# install nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom Nginx configuration file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    # Add custom HTTP header
    add_header X-Served-By $hostname;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
",
  require => Package['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
