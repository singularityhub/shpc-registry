---
layout: container
name:  "quay.io/biocontainers/menetools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/menetools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/menetools/container.yaml"
updated_at: "2022-11-04 00:01:52.316950"
latest: "2.0.6--py_0"
container_url: "https://biocontainers.pro/tools/menetools"
aliases:
 - "menecheck"
 - "menecof"
 - "menepath"
 - "menescope"
 - "xslt-config"
 - "xsltproc"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
versions:
 - "2.0.6--py_0"
description: "shpc-registry automated BioContainers addition for menetools"
config: {"url": "https://biocontainers.pro/tools/menetools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for menetools", "latest": {"2.0.6--py_0": "sha256:1ae447a78343b646e4301da62214a5425dd0986bd7af4795b5d6742357e5d0e2"}, "tags": {"2.0.6--py_0": "sha256:1ae447a78343b646e4301da62214a5425dd0986bd7af4795b5d6742357e5d0e2"}, "docker": "quay.io/biocontainers/menetools", "aliases": {"menecheck": "/usr/local/bin/menecheck", "menecof": "/usr/local/bin/menecof", "menepath": "/usr/local/bin/menepath", "menescope": "/usr/local/bin/menescope", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/menetools.
shpc-registry automated BioContainers addition for menetools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/menetools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/menetools:2.0.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/menetools/2.0.6--py_0
$ module help quay.io/biocontainers/menetools/2.0.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### menetools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### menetools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### menetools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### menetools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### menetools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### menetools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### menecheck

```bash
$ singularity exec <container> /usr/local/bin/menecheck
$ podman run --it --rm --entrypoint /usr/local/bin/menecheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/menecheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### menecof

```bash
$ singularity exec <container> /usr/local/bin/menecof
$ podman run --it --rm --entrypoint /usr/local/bin/menecof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/menecof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### menepath

```bash
$ singularity exec <container> /usr/local/bin/menepath
$ podman run --it --rm --entrypoint /usr/local/bin/menepath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/menepath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### menescope

```bash
$ singularity exec <container> /usr/local/bin/menescope
$ podman run --it --rm --entrypoint /usr/local/bin/menescope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/menescope   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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