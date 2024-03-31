file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  mode    => '0600',
  content => "
    Host your_server_hostname
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
