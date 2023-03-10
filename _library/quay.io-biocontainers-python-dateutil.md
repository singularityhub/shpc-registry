---
layout: container
name:  "quay.io/biocontainers/python-dateutil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/python-dateutil/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/python-dateutil/container.yaml"
updated_at: "2023-03-10 03:18:31.733695"
latest: "2.6.0--py34_0"
container_url: "https://biocontainers.pro/tools/python-dateutil"
aliases:
 - "2to3-3.4"
 - "easy_install-3.4"
 - "idle3.4"
 - "pydoc3.4"
 - "python3.4"
 - "python3.4-config"
 - "python3.4m"
 - "python3.4m-config"
 - "pyvenv-3.4"
 - "tclsh8.5"
 - "wish8.5"
 - "pyvenv"
versions:
 - "2.6.0--py34_0"
description: "shpc-registry automated BioContainers addition for python-dateutil"
config: {"url": "https://biocontainers.pro/tools/python-dateutil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for python-dateutil", "latest": {"2.6.0--py34_0": "sha256:405fbdf4d1624658cdb24203b4f1051e7e0271b939fb9873d389733018c74a30"}, "tags": {"2.6.0--py34_0": "sha256:405fbdf4d1624658cdb24203b4f1051e7e0271b939fb9873d389733018c74a30"}, "docker": "quay.io/biocontainers/python-dateutil", "aliases": {"2to3-3.4": "/usr/local/bin/2to3-3.4", "easy_install-3.4": "/usr/local/bin/easy_install-3.4", "idle3.4": "/usr/local/bin/idle3.4", "pydoc3.4": "/usr/local/bin/pydoc3.4", "python3.4": "/usr/local/bin/python3.4", "python3.4-config": "/usr/local/bin/python3.4-config", "python3.4m": "/usr/local/bin/python3.4m", "python3.4m-config": "/usr/local/bin/python3.4m-config", "pyvenv-3.4": "/usr/local/bin/pyvenv-3.4", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/python-dateutil.
shpc-registry automated BioContainers addition for python-dateutil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/python-dateutil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/python-dateutil:2.6.0--py34_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/python-dateutil/2.6.0--py34_0
$ module help quay.io/biocontainers/python-dateutil/2.6.0--py34_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-dateutil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-dateutil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-dateutil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-dateutil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-dateutil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-dateutil-inspect-deffile:

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


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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