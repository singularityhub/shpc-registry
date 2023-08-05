---
layout: container
name:  "quay.io/biocontainers/oases"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oases/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oases/container.yaml"
updated_at: "2023-08-05 02:47:09.694764"
latest: "0.2.09--h470a237_1"
container_url: "https://biocontainers.pro/tools/oases"
aliases:
 - "oases"
 - "oases_pipeline.py"
 - "velvetg"
 - "velveth"
versions:
 - "0.2.09--h470a237_1"
description: "shpc-registry automated BioContainers addition for oases"
config: {"url": "https://biocontainers.pro/tools/oases", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for oases", "latest": {"0.2.09--h470a237_1": "sha256:e8317fa87375bb07cca81447fc9160322e1f3b14f9aef5511500e60cdf009af2"}, "tags": {"0.2.09--h470a237_1": "sha256:e8317fa87375bb07cca81447fc9160322e1f3b14f9aef5511500e60cdf009af2"}, "docker": "quay.io/biocontainers/oases", "aliases": {"oases": "/usr/local/bin/oases", "oases_pipeline.py": "/usr/local/bin/oases_pipeline.py", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oases.
shpc-registry automated BioContainers addition for oases
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oases
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oases:0.2.09--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oases/0.2.09--h470a237_1
$ module help quay.io/biocontainers/oases/0.2.09--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oases-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oases-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oases-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oases-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oases-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oases-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### oases

```bash
$ singularity exec <container> /usr/local/bin/oases
$ podman run --it --rm --entrypoint /usr/local/bin/oases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oases_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/oases_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/oases_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oases_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
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