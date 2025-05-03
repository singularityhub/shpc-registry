---
layout: container
name:  "quay.io/biocontainers/skesa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/skesa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/skesa/container.yaml"
updated_at: "2025-05-03 03:40:55.357570"
latest: "2.5.1--h077b44d_2"
container_url: "https://biocontainers.pro/tools/skesa"
aliases:
 - "skesa"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "2.4.0--he1c1bb9_0"
 - "2.5.1--hdcf5f25_0"
 - "2.5.1--hdcf5f25_1"
 - "2.5.1--h077b44d_2"
description: "shpc-registry automated BioContainers addition for skesa"
config: {"url": "https://biocontainers.pro/tools/skesa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for skesa", "latest": {"2.5.1--h077b44d_2": "sha256:a90d146ba0eb514588fa337306c9e504e04dde23f4a8bf89cd888bf0a926a38e"}, "tags": {"2.4.0--he1c1bb9_0": "sha256:f52ffc73ff62fdbf0ee176d020117cc6d077aaf7efc38dd1c3fc66bffc01773c", "2.5.1--hdcf5f25_0": "sha256:9af5d78d5eee2beb65c5270524861997e36de933a74db3ebcc3565cade190510", "2.5.1--hdcf5f25_1": "sha256:b75026331e1658aeff8884c215478c4f9997859359457cfb99e2ad423ea5f030", "2.5.1--h077b44d_2": "sha256:a90d146ba0eb514588fa337306c9e504e04dde23f4a8bf89cd888bf0a926a38e"}, "docker": "quay.io/biocontainers/skesa", "aliases": {"skesa": "/usr/local/bin/skesa", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/skesa.
shpc-registry automated BioContainers addition for skesa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/skesa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/skesa:2.5.1--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/skesa/2.5.1--h077b44d_2
$ module help quay.io/biocontainers/skesa/2.5.1--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### skesa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### skesa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### skesa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### skesa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### skesa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### skesa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### skesa

```bash
$ singularity exec <container> /usr/local/bin/skesa
$ podman run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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