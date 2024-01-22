---
layout: container
name:  "quay.io/biocontainers/croo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/croo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/croo/container.yaml"
updated_at: "2024-01-22 03:31:18.724569"
latest: "0.6.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/croo"
aliases:
 - "autouri"
 - "aws"
 - "aws.cmd"
 - "aws_bash_completer"
 - "aws_completer"
 - "aws_zsh_completer.sh"
 - "caper"
 - "create_instance.sh"
 - "croo"
 - "miniwdl"
 - "pygtail"
 - "pyhocon"
 - "run_mysql_server_docker.sh"
 - "run_mysql_server_singularity.sh"
 - "wsdump.py"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "coloredlogs"
 - "humanfriendly"
 - "xkbcli"
 - "jp.py"
 - "py.test"
 - "pytest"
versions:
 - "0.6.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for croo"
config: {"url": "https://biocontainers.pro/tools/croo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for croo", "latest": {"0.6.0--pyhdfd78af_0": "sha256:9113ed9172e6644ab28850dd9c5f9f1ee149514e12e5147607fac8fad5a621ee"}, "tags": {"0.6.0--pyhdfd78af_0": "sha256:9113ed9172e6644ab28850dd9c5f9f1ee149514e12e5147607fac8fad5a621ee"}, "docker": "quay.io/biocontainers/croo", "aliases": {"autouri": "/usr/local/bin/autouri", "aws": "/usr/local/bin/aws", "aws.cmd": "/usr/local/bin/aws.cmd", "aws_bash_completer": "/usr/local/bin/aws_bash_completer", "aws_completer": "/usr/local/bin/aws_completer", "aws_zsh_completer.sh": "/usr/local/bin/aws_zsh_completer.sh", "caper": "/usr/local/bin/caper", "create_instance.sh": "/usr/local/bin/create_instance.sh", "croo": "/usr/local/bin/croo", "miniwdl": "/usr/local/bin/miniwdl", "pygtail": "/usr/local/bin/pygtail", "pyhocon": "/usr/local/bin/pyhocon", "run_mysql_server_docker.sh": "/usr/local/bin/run_mysql_server_docker.sh", "run_mysql_server_singularity.sh": "/usr/local/bin/run_mysql_server_singularity.sh", "wsdump.py": "/usr/local/bin/wsdump.py", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "xkbcli": "/usr/local/bin/xkbcli", "jp.py": "/usr/local/bin/jp.py", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/croo.
shpc-registry automated BioContainers addition for croo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/croo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/croo:0.6.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/croo/0.6.0--pyhdfd78af_0
$ module help quay.io/biocontainers/croo/0.6.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### croo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### croo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### croo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### croo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### croo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### croo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autouri

```bash
$ singularity exec <container> /usr/local/bin/autouri
$ podman run --it --rm --entrypoint /usr/local/bin/autouri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autouri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws

```bash
$ singularity exec <container> /usr/local/bin/aws
$ podman run --it --rm --entrypoint /usr/local/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws.cmd

```bash
$ singularity exec <container> /usr/local/bin/aws.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/aws.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_bash_completer

```bash
$ singularity exec <container> /usr/local/bin/aws_bash_completer
$ podman run --it --rm --entrypoint /usr/local/bin/aws_bash_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_bash_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_completer

```bash
$ singularity exec <container> /usr/local/bin/aws_completer
$ podman run --it --rm --entrypoint /usr/local/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_zsh_completer.sh

```bash
$ singularity exec <container> /usr/local/bin/aws_zsh_completer.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws_zsh_completer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_zsh_completer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### caper

```bash
$ singularity exec <container> /usr/local/bin/caper
$ podman run --it --rm --entrypoint /usr/local/bin/caper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/caper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_instance.sh

```bash
$ singularity exec <container> /usr/local/bin/create_instance.sh
$ podman run --it --rm --entrypoint /usr/local/bin/create_instance.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_instance.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### croo

```bash
$ singularity exec <container> /usr/local/bin/croo
$ podman run --it --rm --entrypoint /usr/local/bin/croo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/croo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniwdl

```bash
$ singularity exec <container> /usr/local/bin/miniwdl
$ podman run --it --rm --entrypoint /usr/local/bin/miniwdl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniwdl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygtail

```bash
$ singularity exec <container> /usr/local/bin/pygtail
$ podman run --it --rm --entrypoint /usr/local/bin/pygtail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygtail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyhocon

```bash
$ singularity exec <container> /usr/local/bin/pyhocon
$ podman run --it --rm --entrypoint /usr/local/bin/pyhocon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyhocon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_mysql_server_docker.sh

```bash
$ singularity exec <container> /usr/local/bin/run_mysql_server_docker.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_mysql_server_docker.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_mysql_server_docker.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_mysql_server_singularity.sh

```bash
$ singularity exec <container> /usr/local/bin/run_mysql_server_singularity.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_mysql_server_singularity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_mysql_server_singularity.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump.py

```bash
$ singularity exec <container> /usr/local/bin/wsdump.py
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)