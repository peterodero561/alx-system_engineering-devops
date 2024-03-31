# puppet to set up my ssh to connect to my server without a password
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
    Host your_server_hostname
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
