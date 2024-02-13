---
layout: container
name:  "quay.io/biocontainers/pbcoretools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbcoretools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbcoretools/container.yaml"
updated_at: "2024-02-13 02:28:40.941367"
latest: "0.8.1--py_1"
container_url: "https://biocontainers.pro/tools/pbcoretools"
aliases:
 - "bamsieve"
 - "dataset"
 - "pbtools-gather"
 - "pbvalidate"
 - "avro"
 - "f2py3.7"
 - "chardetect"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
versions:
 - "0.8.1--py_1"
description: "shpc-registry automated BioContainers addition for pbcoretools"
config: {"url": "https://biocontainers.pro/tools/pbcoretools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbcoretools", "latest": {"0.8.1--py_1": "sha256:f7e6370222d5f5035ee2f32dd75d5c8b50d3d6106d18b7d6bf45fbfbb2e6dd15"}, "tags": {"0.8.1--py_1": "sha256:f7e6370222d5f5035ee2f32dd75d5c8b50d3d6106d18b7d6bf45fbfbb2e6dd15"}, "docker": "quay.io/biocontainers/pbcoretools", "aliases": {"bamsieve": "/usr/local/bin/bamsieve", "dataset": "/usr/local/bin/dataset", "pbtools-gather": "/usr/local/bin/pbtools-gather", "pbvalidate": "/usr/local/bin/pbvalidate", "avro": "/usr/local/bin/avro", "f2py3.7": "/usr/local/bin/f2py3.7", "chardetect": "/usr/local/bin/chardetect", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbcoretools.
shpc-registry automated BioContainers addition for pbcoretools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbcoretools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbcoretools:0.8.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbcoretools/0.8.1--py_1
$ module help quay.io/biocontainers/pbcoretools/0.8.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbcoretools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbcoretools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbcoretools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbcoretools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbcoretools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbcoretools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamsieve

```bash
$ singularity exec <container> /usr/local/bin/bamsieve
$ podman run --it --rm --entrypoint /usr/local/bin/bamsieve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamsieve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataset

```bash
$ singularity exec <container> /usr/local/bin/dataset
$ podman run --it --rm --entrypoint /usr/local/bin/dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbtools-gather

```bash
$ singularity exec <container> /usr/local/bin/pbtools-gather
$ podman run --it --rm --entrypoint /usr/local/bin/pbtools-gather   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbtools-gather   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbvalidate

```bash
$ singularity exec <container> /usr/local/bin/pbvalidate
$ podman run --it --rm --entrypoint /usr/local/bin/pbvalidate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbvalidate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### avro

```bash
$ singularity exec <container> /usr/local/bin/avro
$ podman run --it --rm --entrypoint /usr/local/bin/avro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/avro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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