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
