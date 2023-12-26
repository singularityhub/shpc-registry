---
layout: container
name:  "quay.io/biocontainers/reago"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reago/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reago/container.yaml"
updated_at: "2023-12-26 02:51:14.967522"
latest: "1.1--py34_0"
container_url: "https://biocontainers.pro/tools/reago"
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
 - "reago.py"
 - "tclsh8.5"
 - "wish8.5"
 - "pyvenv"
versions:
 - "1.1--py34_0"
description: "shpc-registry automated BioContainers addition for reago"
config: {"url": "https://biocontainers.pro/tools/reago", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for reago", "latest": {"1.1--py34_0": "sha256:6e1d0e05a5bd28e2eb859c5e808f7bee6d9c844778f60da6b76ff16bc1a5e55a"}, "tags": {"1.1--py34_0": "sha256:6e1d0e05a5bd28e2eb859c5e808f7bee6d9c844778f60da6b76ff16bc1a5e55a"}, "docker": "quay.io/biocontainers/reago", "aliases": {"2to3-3.4": "/usr/local/bin/2to3-3.4", "easy_install-3.4": "/usr/local/bin/easy_install-3.4", "idle3.4": "/usr/local/bin/idle3.4", "pydoc3.4": "/usr/local/bin/pydoc3.4", "python3.4": "/usr/local/bin/python3.4", "python3.4-config": "/usr/local/bin/python3.4-config", "python3.4m": "/usr/local/bin/python3.4m", "python3.4m-config": "/usr/local/bin/python3.4m-config", "pyvenv-3.4": "/usr/local/bin/pyvenv-3.4", "reago.py": "/usr/local/bin/reago.py", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reago.
shpc-registry automated BioContainers addition for reago
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reago
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reago:1.1--py34_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reago/1.1--py34_0
$ module help quay.io/biocontainers/reago/1.1--py34_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reago-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reago-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reago-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reago-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reago-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reago-inspect-deffile:

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


#### reago.py

```bash
$ singularity exec <container> /usr/local/bin/reago.py
$ podman run --it --rm --entrypoint /usr/local/bin/reago.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reago.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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