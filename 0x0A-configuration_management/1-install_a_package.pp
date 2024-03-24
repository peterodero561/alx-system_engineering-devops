# This pupet file manifest and installs flask

package { 'install_flask_2.1.0':
  command   => 'pip3 install flask=2.1.0',
  path    => '/usr/bin',
  unless  => 'pip3 show flask | grep -q "Version: 2.1.0"',
}
