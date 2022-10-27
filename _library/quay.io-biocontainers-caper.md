---
layout: container
name:  "quay.io/biocontainers/caper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/caper/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/caper/container.yaml"
updated_at: "2022-10-27 00:29:35.713439"
latest: "1.1.0--py_0"
container_url: "https://biocontainers.pro/tools/caper"
aliases:
 - "autouri"
 - "aws"
 - "aws.cmd"
 - "aws_bash_completer"
 - "aws_completer"
 - "aws_zsh_completer.sh"
 - "caper"
 - "create_instance.sh"
 - "miniwdl"
 - "pygtail"
 - "pyhocon"
 - "run_mysql_server_docker.sh"
 - "run_mysql_server_singularity.sh"
versions:
 - "1.1.0--py_0"
description: "shpc-registry automated BioContainers addition for caper"
config: {"url": "https://biocontainers.pro/tools/caper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for caper", "latest": {"1.1.0--py_0": "sha256:92f482ea771f9a097030d21dea4ed9720400cea5b4d56b5d0c37e23477e55a67"}, "tags": {"1.1.0--py_0": "sha256:92f482ea771f9a097030d21dea4ed9720400cea5b4d56b5d0c37e23477e55a67"}, "docker": "quay.io/biocontainers/caper", "aliases": {"autouri": "/usr/local/bin/autouri", "aws": "/usr/local/bin/aws", "aws.cmd": "/usr/local/bin/aws.cmd", "aws_bash_completer": "/usr/local/bin/aws_bash_completer", "aws_completer": "/usr/local/bin/aws_completer", "aws_zsh_completer.sh": "/usr/local/bin/aws_zsh_completer.sh", "caper": "/usr/local/bin/caper", "create_instance.sh": "/usr/local/bin/create_instance.sh", "miniwdl": "/usr/local/bin/miniwdl", "pygtail": "/usr/local/bin/pygtail", "pyhocon": "/usr/local/bin/pyhocon", "run_mysql_server_docker.sh": "/usr/local/bin/run_mysql_server_docker.sh", "run_mysql_server_singularity.sh": "/usr/local/bin/run_mysql_server_singularity.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/caper.
shpc-registry automated BioContainers addition for caper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/caper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/caper:1.1.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/caper/1.1.0--py_0
$ module help quay.io/biocontainers/caper/1.1.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### caper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### caper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### caper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### caper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### caper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### caper-inspect-deffile:

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