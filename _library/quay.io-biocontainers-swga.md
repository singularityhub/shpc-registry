---
layout: container
name:  "quay.io/biocontainers/swga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/swga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/swga/container.yaml"
updated_at: "2024-08-08 03:19:43.128678"
latest: "0.4.4--py27heb12742_2"
container_url: "https://biocontainers.pro/tools/swga"
aliases:
 - "Tm"
 - "dsk"
 - "pskel"
 - "pwiz.py"
 - "set_finder"
 - "swga"
 - "ws"
 - "py.test"
 - "pytest"
 - "faidx"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.4.4--py27heb12742_2"
description: "shpc-registry automated BioContainers addition for swga"
config: {"url": "https://biocontainers.pro/tools/swga", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for swga", "latest": {"0.4.4--py27heb12742_2": "sha256:13a1c4e5d8855f93b4c0b2d5626ed32a9cb9c8d63884af1ef3da33e27795cb5e"}, "tags": {"0.4.4--py27heb12742_2": "sha256:13a1c4e5d8855f93b4c0b2d5626ed32a9cb9c8d63884af1ef3da33e27795cb5e"}, "docker": "quay.io/biocontainers/swga", "aliases": {"Tm": "/usr/local/bin/Tm", "dsk": "/usr/local/bin/dsk", "pskel": "/usr/local/bin/pskel", "pwiz.py": "/usr/local/bin/pwiz.py", "set_finder": "/usr/local/bin/set_finder", "swga": "/usr/local/bin/swga", "ws": "/usr/local/bin/ws", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "faidx": "/usr/local/bin/faidx", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/swga.
shpc-registry automated BioContainers addition for swga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/swga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/swga:0.4.4--py27heb12742_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/swga/0.4.4--py27heb12742_2
$ module help quay.io/biocontainers/swga/0.4.4--py27heb12742_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### swga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### swga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### swga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### swga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### swga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### swga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Tm

```bash
$ singularity exec <container> /usr/local/bin/Tm
$ podman run --it --rm --entrypoint /usr/local/bin/Tm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Tm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsk

```bash
$ singularity exec <container> /usr/local/bin/dsk
$ podman run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pskel

```bash
$ singularity exec <container> /usr/local/bin/pskel
$ podman run --it --rm --entrypoint /usr/local/bin/pskel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pskel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pwiz.py

```bash
$ singularity exec <container> /usr/local/bin/pwiz.py
$ podman run --it --rm --entrypoint /usr/local/bin/pwiz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pwiz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### set_finder

```bash
$ singularity exec <container> /usr/local/bin/set_finder
$ podman run --it --rm --entrypoint /usr/local/bin/set_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/set_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swga

```bash
$ singularity exec <container> /usr/local/bin/swga
$ podman run --it --rm --entrypoint /usr/local/bin/swga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ws

```bash
$ singularity exec <container> /usr/local/bin/ws
$ podman run --it --rm --entrypoint /usr/local/bin/ws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ws   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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