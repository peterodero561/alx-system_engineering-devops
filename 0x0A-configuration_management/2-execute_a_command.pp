# This manifest kilss a process called killmenow

exec {
  command => 'pkill killmenow',
  path  => '/usr/bin',
  onlyif  => 'pgrep killmenow',
}
