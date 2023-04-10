---
layout: container
name:  "quay.io/biocontainers/mysqlclient"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mysqlclient/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mysqlclient/container.yaml"
updated_at: "2023-04-10 02:41:25.743461"
latest: "1.3.10--py36_0"
container_url: "https://biocontainers.pro/tools/mysqlclient"
aliases:
 - "easy_install-2.7"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "tclsh8.5"
versions:
 - "1.3.9--py27_0"
 - "1.3.10--py36_0"
description: "shpc-registry automated BioContainers addition for mysqlclient"
config: {"url": "https://biocontainers.pro/tools/mysqlclient", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mysqlclient", "latest": {"1.3.10--py36_0": "sha256:c491371db47b1eb925db64f01d57abdcafe45d7213e23e6e300afe2133a8eaed"}, "tags": {"1.3.9--py27_0": "sha256:02245055f0576434dc080344832bdda981b4fbc4db4c67f9c61e65a963015dd9", "1.3.10--py36_0": "sha256:c491371db47b1eb925db64f01d57abdcafe45d7213e23e6e300afe2133a8eaed"}, "docker": "quay.io/biocontainers/mysqlclient", "aliases": {"easy_install-2.7": "/usr/local/bin/easy_install-2.7", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "tclsh8.5": "/usr/local/bin/tclsh8.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mysqlclient.
shpc-registry automated BioContainers addition for mysqlclient
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mysqlclient
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mysqlclient:1.3.10--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mysqlclient/1.3.10--py36_0
$ module help quay.io/biocontainers/mysqlclient/1.3.10--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mysqlclient-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mysqlclient-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mysqlclient-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mysqlclient-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mysqlclient-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mysqlclient-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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