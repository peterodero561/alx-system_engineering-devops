# configure my 2 webservers using puppet to return their webserver
# install nginx package
class { 'nginx':
  ensure => installed,
}

# define custom HTTP configuration
nginx::resource::server { 'my_server':
  listen_options => 'default_server',
  server_name    => 'localhost',
  location       => '/my_location',
  add_header     => {
    'X-Served-By' => $::hostname,
  },
}
