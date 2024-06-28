# Configure both web servers to return their hostname
# This manifest ensures packages are updated, Nginx is installed, and a custom configuration is applied.

# Update package lists
exec { 'update_packages':
  command => '/usr/bin/apt update',
  path    => '/usr/bin',
}

# Ensure Nginx is installed
package { 'nginx':
  ensure  => 'present',
  require => Exec['update_packages'],
}

# Define custom header configuration
file { '/etc/nginx/conf.d/custom_http_response_header.conf':
  ensure  => 'file',
  content => template('nginx/custom_http_response_header.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and restarted to apply changes
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/conf.d/custom_http_response_header.conf'],
}

# Template for custom Nginx configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/custom_http_response_header.conf.erb':
  ensure  => 'file',
  content => @("END"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name peterdev.tech;

    location / {
        add_header X-Served-By <%= @::hostname %>;
    }
}
| END
  require => Package['nginx'],
}
