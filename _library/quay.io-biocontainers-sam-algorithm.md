---
layout: container
name:  "quay.io/biocontainers/sam-algorithm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sam-algorithm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sam-algorithm/container.yaml"
updated_at: "2023-10-11 02:48:13.845863"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sam-algorithm"
aliases:
 - "get_objgraph"
 - "undill"
 - "numba"
 - "pycc"
 - "natsort"
 - "tqdm"
 - "f2py3.8"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
versions:
 - "0.9.0--pyhdfd78af_0"
 - "1.0.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for sam-algorithm"
config: {"url": "https://biocontainers.pro/tools/sam-algorithm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sam-algorithm", "latest": {"1.0.2--pyhdfd78af_0": "sha256:6cfb040e3b8980debab5c448aacb2cc29f209ba212017879e3b9381d6d4d4753"}, "tags": {"0.9.0--pyhdfd78af_0": "sha256:436babf48dcba4a5441c305b34db06c58b879a0442ca26be28e1450e738f394e", "1.0.2--pyhdfd78af_0": "sha256:6cfb040e3b8980debab5c448aacb2cc29f209ba212017879e3b9381d6d4d4753"}, "docker": "quay.io/biocontainers/sam-algorithm", "aliases": {"get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "natsort": "/usr/local/bin/natsort", "tqdm": "/usr/local/bin/tqdm", "f2py3.8": "/usr/local/bin/f2py3.8", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sam-algorithm.
shpc-registry automated BioContainers addition for sam-algorithm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sam-algorithm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sam-algorithm:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sam-algorithm/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/sam-algorithm/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sam-algorithm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sam-algorithm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sam-algorithm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sam-algorithm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sam-algorithm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sam-algorithm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
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