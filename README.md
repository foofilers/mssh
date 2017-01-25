# mssh
Ssh connection manager

[![Build Status](https://travis-ci.org/foofilers/mssh.svg?branch=master)](https://travis-ci.org/foofilers/mssh)

# INSTALLATION

```
$> pip3 install --upgrade mssh
$> sudo mssh --setup
$> mssh --edit
```

# USAGE

```
usage: mssh [-h] [--setup] [--edit] [env] [product] [server] [user] ...

Ssh Manager

positional arguments:
  env         Environment
  product     Product name
  server      Server name or alias
  user        User
  command     Command

optional arguments:
  -h, --help  show this help message and exit
  --setup     Setup auto completions
  --edit      Edit configuration

```

# EXAMPLE
## CONFIGURATION
Path : $HOME/.config/mssh/config.yml
```
servers:
  server1: &server1
    host: server1.example.com
    users:
      - user1
      - user2
environments:
  dev:
    software1:
      servers:
        aliasSrv1:
          <<: *server1
          users:
            - user3
          commands:
            test: 'ls -l /tmp'
```

## SSH CONNECTION
```
$> mssh dev software1 aliasSrv1 user3
```

## SSH REMOTE COMMAND with ALIAS
```
$> mssh dev software1 aliasSrv1 user3 test
```
## SSH REMOTE COMMAND 
```
$> mssh dev software1 aliasSrv1 user3 tail -f /var/log/syslog
```

