# This pupet file manifest and installs flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

notify { 'version of flask':
  require => Package['flask']
}
