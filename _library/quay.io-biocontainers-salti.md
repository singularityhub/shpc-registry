---
layout: container
name:  "quay.io/biocontainers/salti"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/salti/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/salti/container.yaml"
updated_at: "2026-03-28 05:01:06.896892"
latest: "0.7.1--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/salti"
aliases:
 - "salti"
versions:
 - "0.7.1--h4349ce8_0"
description: "singularity registry hpc automated addition for salti"
config: {"url": "https://biocontainers.pro/tools/salti", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for salti", "latest": {"0.7.1--h4349ce8_0": "sha256:5760ea5e582c812e4e3372f103a5a23f527157ae1da9a5b6e07987c140b36fd2"}, "tags": {"0.7.1--h4349ce8_0": "sha256:5760ea5e582c812e4e3372f103a5a23f527157ae1da9a5b6e07987c140b36fd2"}, "docker": "quay.io/biocontainers/salti", "aliases": {"salti": "/usr/local/bin/salti"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/salti.
singularity registry hpc automated addition for salti
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/salti
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/salti:0.7.1--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/salti/0.7.1--h4349ce8_0
$ module help quay.io/biocontainers/salti/0.7.1--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### salti-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### salti-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### salti-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### salti-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### salti-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### salti-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### salti

```bash
$ singularity exec <container> /usr/local/bin/salti
$ podman run --it --rm --entrypoint /usr/local/bin/salti   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/salti   -v ${PWD} -w ${PWD} <container> -c " $@"
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