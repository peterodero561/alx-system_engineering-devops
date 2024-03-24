# This manifest kilss a process called killmenow

exec {
  command     => 'pkill killmenow',
  refreshonly => true,
}
