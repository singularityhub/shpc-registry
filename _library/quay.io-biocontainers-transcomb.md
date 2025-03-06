---
layout: container
name:  "quay.io/biocontainers/transcomb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transcomb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transcomb/container.yaml"
updated_at: "2025-03-06 03:31:38.436958"
latest: "1.0--boost1.60_0"
container_url: "https://biocontainers.pro/tools/transcomb"
aliases:
 - "Assemble"
 - "CorrectName"
 - "Pre_Alignment"
 - "TransComb"
 - "bamtools-2.4.0"
 - "bamtools"
 - "easy_install-3.5"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
versions:
 - "1.0--boost1.60_0"
 - "1.0--boost1.61_0"
description: "shpc-registry automated BioContainers addition for transcomb"
config: {"url": "https://biocontainers.pro/tools/transcomb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transcomb", "latest": {"1.0--boost1.60_0": "sha256:c8560ce230f4387c71eb6e18c80788190d9b5986e5608c6df9f374d43983762d"}, "tags": {"1.0--boost1.60_0": "sha256:c8560ce230f4387c71eb6e18c80788190d9b5986e5608c6df9f374d43983762d", "1.0--boost1.61_0": "sha256:991ebb3e93b4c8710dd1d72d115752e59fef83eed39332d41769d653ade230a9"}, "docker": "quay.io/biocontainers/transcomb", "aliases": {"Assemble": "/usr/local/bin/Assemble", "CorrectName": "/usr/local/bin/CorrectName", "Pre_Alignment": "/usr/local/bin/Pre_Alignment", "TransComb": "/usr/local/bin/TransComb", "bamtools-2.4.0": "/usr/local/bin/bamtools-2.4.0", "bamtools": "/usr/local/bin/bamtools", "easy_install-3.5": "/usr/local/bin/easy_install-3.5", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transcomb.
shpc-registry automated BioContainers addition for transcomb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transcomb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transcomb:1.0--boost1.60_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transcomb/1.0--boost1.60_0
$ module help quay.io/biocontainers/transcomb/1.0--boost1.60_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transcomb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transcomb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transcomb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transcomb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transcomb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transcomb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Assemble

```bash
$ singularity exec <container> /usr/local/bin/Assemble
$ podman run --it --rm --entrypoint /usr/local/bin/Assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CorrectName

```bash
$ singularity exec <container> /usr/local/bin/CorrectName
$ podman run --it --rm --entrypoint /usr/local/bin/CorrectName   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CorrectName   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Pre_Alignment

```bash
$ singularity exec <container> /usr/local/bin/Pre_Alignment
$ podman run --it --rm --entrypoint /usr/local/bin/Pre_Alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Pre_Alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TransComb

```bash
$ singularity exec <container> /usr/local/bin/TransComb
$ podman run --it --rm --entrypoint /usr/local/bin/TransComb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TransComb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools-2.4.0

```bash
$ singularity exec <container> /usr/local/bin/bamtools-2.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.5

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m

```bash
$ singularity exec <container> /usr/local/bin/python3.5m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.5m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.5

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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