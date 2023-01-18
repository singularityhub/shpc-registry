---
layout: container
name:  "quay.io/biocontainers/mysql-connector-c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mysql-connector-c/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mysql-connector-c/container.yaml"
updated_at: "2023-01-18 03:25:44.470277"
latest: "6.1.6--2"
container_url: "https://biocontainers.pro/tools/mysql-connector-c"
aliases:
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
versions:
 - "6.1.6--2"
description: "shpc-registry automated BioContainers addition for mysql-connector-c"
config: {"url": "https://biocontainers.pro/tools/mysql-connector-c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mysql-connector-c", "latest": {"6.1.6--2": "sha256:48c7eef63472057baccd8d6f0ae72733d171adc14df5c835244f7cca36b8d5e1"}, "tags": {"6.1.6--2": "sha256:48c7eef63472057baccd8d6f0ae72733d171adc14df5c835244f7cca36b8d5e1"}, "docker": "quay.io/biocontainers/mysql-connector-c", "aliases": {"my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mysql-connector-c.
shpc-registry automated BioContainers addition for mysql-connector-c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mysql-connector-c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mysql-connector-c:6.1.6--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mysql-connector-c/6.1.6--2
$ module help quay.io/biocontainers/mysql-connector-c/6.1.6--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mysql-connector-c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mysql-connector-c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mysql-connector-c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mysql-connector-c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mysql-connector-c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mysql-connector-c-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
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