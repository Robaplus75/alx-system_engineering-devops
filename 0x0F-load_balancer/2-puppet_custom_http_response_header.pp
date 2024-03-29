# Puppet manifest to setup up an ubuntu server
# With nginx, custom http headers

exec { 'update system':
        command => '/usr/bin/apt-get update',
        provider => 'shell'
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

# file

file {'/var/www/html/index.html':
	content => 'Hello World!',
  owner => 'ubuntu', 
  group => 'ubuntu', 
  mode => '7624'
}

# exec function

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'Custom HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# service here

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
