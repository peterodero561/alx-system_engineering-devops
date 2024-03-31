# This manifest kilss a process called killmenow

exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  path        => '/usr/bin',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
