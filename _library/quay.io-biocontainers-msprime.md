---
layout: container
name:  "quay.io/biocontainers/msprime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msprime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msprime/container.yaml"
updated_at: "2024-02-05 03:12:30.695522"
latest: "0.4.0--py34_gsl1.16_2"
container_url: "https://biocontainers.pro/tools/msprime"
aliases:
 - "2to3-3.4"
 - "easy_install-3.4"
 - "idle3.4"
 - "msp"
 - "mspms"
 - "pydoc3.4"
 - "python3.4"
 - "python3.4-config"
 - "python3.4m"
 - "python3.4m-config"
 - "pyvenv-3.4"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5import"
 - "h5jam"
 - "h5ls"
 - "h5mkgrp"
versions:
 - "0.4.0--py34_gsl1.16_2"
description: "shpc-registry automated BioContainers addition for msprime"
config: {"url": "https://biocontainers.pro/tools/msprime", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msprime", "latest": {"0.4.0--py34_gsl1.16_2": "sha256:12b8da552f7dcb575c5855738a4b0029eacf78efa47f6ec60f00c133f6c1d8f6"}, "tags": {"0.4.0--py34_gsl1.16_2": "sha256:12b8da552f7dcb575c5855738a4b0029eacf78efa47f6ec60f00c133f6c1d8f6"}, "docker": "quay.io/biocontainers/msprime", "aliases": {"2to3-3.4": "/usr/local/bin/2to3-3.4", "easy_install-3.4": "/usr/local/bin/easy_install-3.4", "idle3.4": "/usr/local/bin/idle3.4", "msp": "/usr/local/bin/msp", "mspms": "/usr/local/bin/mspms", "pydoc3.4": "/usr/local/bin/pydoc3.4", "python3.4": "/usr/local/bin/python3.4", "python3.4-config": "/usr/local/bin/python3.4-config", "python3.4m": "/usr/local/bin/python3.4m", "python3.4m-config": "/usr/local/bin/python3.4m-config", "pyvenv-3.4": "/usr/local/bin/pyvenv-3.4", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug", "h5diff": "/usr/local/bin/h5diff", "h5import": "/usr/local/bin/h5import", "h5jam": "/usr/local/bin/h5jam", "h5ls": "/usr/local/bin/h5ls", "h5mkgrp": "/usr/local/bin/h5mkgrp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/msprime.
shpc-registry automated BioContainers addition for msprime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msprime
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msprime:0.4.0--py34_gsl1.16_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msprime/0.4.0--py34_gsl1.16_2
$ module help quay.io/biocontainers/msprime/0.4.0--py34_gsl1.16_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msprime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msprime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msprime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msprime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msprime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msprime-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.4

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.4

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.4

```bash
$ singularity exec <container> /usr/local/bin/idle3.4
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msp

```bash
$ singularity exec <container> /usr/local/bin/msp
$ podman run --it --rm --entrypoint /usr/local/bin/msp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mspms

```bash
$ singularity exec <container> /usr/local/bin/mspms
$ podman run --it --rm --entrypoint /usr/local/bin/mspms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mspms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.4

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.4
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4

```bash
$ singularity exec <container> /usr/local/bin/python3.4
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4-config

```bash
$ singularity exec <container> /usr/local/bin/python3.4-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4m

```bash
$ singularity exec <container> /usr/local/bin/python3.4m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.4m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.4

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5diff

```bash
$ singularity exec <container> /usr/local/bin/h5diff
$ podman run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5import

```bash
$ singularity exec <container> /usr/local/bin/h5import
$ podman run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5jam

```bash
$ singularity exec <container> /usr/local/bin/h5jam
$ podman run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5ls

```bash
$ singularity exec <container> /usr/local/bin/h5ls
$ podman run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5mkgrp

```bash
$ singularity exec <container> /usr/local/bin/h5mkgrp
$ podman run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
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