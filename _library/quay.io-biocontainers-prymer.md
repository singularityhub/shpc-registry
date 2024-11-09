---
layout: container
name:  "quay.io/biocontainers/prymer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prymer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prymer/container.yaml"
updated_at: "2024-11-09 02:56:28.390122"
latest: "2.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/prymer"
aliases:
 - "amplicon3_core"
 - "long_seq_tm_test"
 - "ntdpal"
 - "ntthal"
 - "oligotm"
 - "primer3_core"
 - "primer3_masker"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "2.0.0--pyhdfd78af_0"
 - "2.1.1--pyhdfd78af_0"
 - "2.0.0--pyhdfd78af_1"
 - "2.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for prymer"
config: {"url": "https://biocontainers.pro/tools/prymer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for prymer", "latest": {"2.2.0--pyhdfd78af_0": "sha256:30c714816e69a501fb2d0c6d672ffe8e53316e638f7f8ffc45090e9c7f4b3357"}, "tags": {"2.0.0--pyhdfd78af_0": "sha256:4f7d639e0369dea186635d4d4307f2fe9a87c2a02dab0787ff2ef120adedccd5", "2.1.1--pyhdfd78af_0": "sha256:b31ea29d6f193625b4772d7935c36cee2ddf411f9e763c583267327d204962df", "2.0.0--pyhdfd78af_1": "sha256:5004212429af75148a5360d65a89f5090604a543868e7bf20cdf9e34e57c2eea", "2.2.0--pyhdfd78af_0": "sha256:30c714816e69a501fb2d0c6d672ffe8e53316e638f7f8ffc45090e9c7f4b3357"}, "docker": "quay.io/biocontainers/prymer", "aliases": {"amplicon3_core": "/usr/local/bin/amplicon3_core", "long_seq_tm_test": "/usr/local/bin/long_seq_tm_test", "ntdpal": "/usr/local/bin/ntdpal", "ntthal": "/usr/local/bin/ntthal", "oligotm": "/usr/local/bin/oligotm", "primer3_core": "/usr/local/bin/primer3_core", "primer3_masker": "/usr/local/bin/primer3_masker", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prymer.
singularity registry hpc automated addition for prymer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prymer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prymer:2.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prymer/2.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/prymer/2.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prymer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prymer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prymer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prymer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prymer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prymer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amplicon3_core

```bash
$ singularity exec <container> /usr/local/bin/amplicon3_core
$ podman run --it --rm --entrypoint /usr/local/bin/amplicon3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicon3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### long_seq_tm_test

```bash
$ singularity exec <container> /usr/local/bin/long_seq_tm_test
$ podman run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntdpal

```bash
$ singularity exec <container> /usr/local/bin/ntdpal
$ podman run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntthal

```bash
$ singularity exec <container> /usr/local/bin/ntthal
$ podman run --it --rm --entrypoint /usr/local/bin/ntthal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntthal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oligotm

```bash
$ singularity exec <container> /usr/local/bin/oligotm
$ podman run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primer3_core

```bash
$ singularity exec <container> /usr/local/bin/primer3_core
$ podman run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primer3_masker

```bash
$ singularity exec <container> /usr/local/bin/primer3_masker
$ podman run --it --rm --entrypoint /usr/local/bin/primer3_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primer3_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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