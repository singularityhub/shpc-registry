---
layout: container
name:  "quay.io/biocontainers/samrefiner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samrefiner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samrefiner/container.yaml"
updated_at: "2025-12-17 03:39:52.594356"
latest: "1.4.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/samrefiner"
aliases:
 - "SAM_Refiner"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.4--pyhdfd78af_0"
 - "1.4.1--pyhdfd78af_0"
 - "1.4.2--pyhdfd78af_0"
 - "1.4.2.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for samrefiner"
config: {"url": "https://biocontainers.pro/tools/samrefiner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samrefiner", "latest": {"1.4.2.1--pyhdfd78af_0": "sha256:e25a5a664e6f7053fb1d10b2a8f08dddb2eb728aa7535d3b27c1379598eaa256"}, "tags": {"1.4--pyhdfd78af_0": "sha256:85126a1652fc2156b48be7715febef8c88cceb40134c4d03c0ebedc6c29b04f3", "1.4.1--pyhdfd78af_0": "sha256:7a74e7675e95ff5921a5740c18fbdf68fcacdeb76c9784493cec7b44732cf540", "1.4.2--pyhdfd78af_0": "sha256:0f6989edd5866f8e99e37f98ddb7329cd6f16c4b37d453bcbc4c2be37528a458", "1.4.2.1--pyhdfd78af_0": "sha256:e25a5a664e6f7053fb1d10b2a8f08dddb2eb728aa7535d3b27c1379598eaa256"}, "docker": "quay.io/biocontainers/samrefiner", "aliases": {"SAM_Refiner": "/usr/local/bin/SAM_Refiner", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samrefiner.
shpc-registry automated BioContainers addition for samrefiner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samrefiner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samrefiner:1.4.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samrefiner/1.4.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/samrefiner/1.4.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samrefiner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samrefiner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samrefiner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samrefiner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samrefiner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samrefiner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SAM_Refiner

```bash
$ singularity exec <container> /usr/local/bin/SAM_Refiner
$ podman run --it --rm --entrypoint /usr/local/bin/SAM_Refiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAM_Refiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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