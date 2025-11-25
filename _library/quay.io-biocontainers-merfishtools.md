---
layout: container
name:  "quay.io/biocontainers/merfishtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/merfishtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/merfishtools/container.yaml"
updated_at: "2025-11-25 04:04:34.427980"
latest: "1.5.0--py312h9d36253_3"
container_url: "https://biocontainers.pro/tools/merfishtools"
aliases:
 - "merfishtools"
 - "conv-template"
 - "from-template"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
 - "python3.5-config"
 - "python3.5m"
 - "python3.5m-config"
 - "pyvenv-3.5"
versions:
 - "1.5.0--py35h549429d_0"
 - "1.5.0--py36h549429d_0"
 - "1.5.0--py312hb511c5e_2"
 - "1.5.0--py312h9d36253_3"
description: "shpc-registry automated BioContainers addition for merfishtools"
config: {"url": "https://biocontainers.pro/tools/merfishtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for merfishtools", "latest": {"1.5.0--py312h9d36253_3": "sha256:58c420479e1b45fd53cb838227abb39a3d094ea4fb39bf72d2f2a3640daec5f1"}, "tags": {"1.5.0--py35h549429d_0": "sha256:7c2a5e6f50526fe7fbba6fd74cf6afca6c60626c8e841b9e028a42739de8a54f", "1.5.0--py36h549429d_0": "sha256:dd3e8d8cf86a19f2a9a0cd86127e0165ae48c9dabd59cd413727d558c1c1b6b6", "1.5.0--py312hb511c5e_2": "sha256:f3c33582db8494719b41afb0a3befdbfa6aec6fd99e68ba83ffbbebe55c3136d", "1.5.0--py312h9d36253_3": "sha256:58c420479e1b45fd53cb838227abb39a3d094ea4fb39bf72d2f2a3640daec5f1"}, "docker": "quay.io/biocontainers/merfishtools", "aliases": {"merfishtools": "/usr/local/bin/merfishtools", "conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5", "python3.5-config": "/usr/local/bin/python3.5-config", "python3.5m": "/usr/local/bin/python3.5m", "python3.5m-config": "/usr/local/bin/python3.5m-config", "pyvenv-3.5": "/usr/local/bin/pyvenv-3.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/merfishtools.
shpc-registry automated BioContainers addition for merfishtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/merfishtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/merfishtools:1.5.0--py312h9d36253_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/merfishtools/1.5.0--py312h9d36253_3
$ module help quay.io/biocontainers/merfishtools/1.5.0--py312h9d36253_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### merfishtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### merfishtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### merfishtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### merfishtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### merfishtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### merfishtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### merfishtools

```bash
$ singularity exec <container> /usr/local/bin/merfishtools
$ podman run --it --rm --entrypoint /usr/local/bin/merfishtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merfishtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
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