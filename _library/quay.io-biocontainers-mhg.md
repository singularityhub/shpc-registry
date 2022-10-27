---
layout: container
name:  "quay.io/biocontainers/mhg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mhg/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mhg/container.yaml"
updated_at: "2022-10-27 00:47:46.662232"
latest: "1.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mhg"
aliases:
 - "MHG"
 - "MHG-partition"
 - "genome-to-blast-db"
versions:
 - "1.1.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for mhg"
config: {"url": "https://biocontainers.pro/tools/mhg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mhg", "latest": {"1.1.0--hdfd78af_0": "sha256:fb197a0e21bc6ebfb3536f713768a58f2f79c9329c418127b44e5d5403634eb9"}, "tags": {"1.1.0--hdfd78af_0": "sha256:fb197a0e21bc6ebfb3536f713768a58f2f79c9329c418127b44e5d5403634eb9"}, "docker": "quay.io/biocontainers/mhg", "aliases": {"MHG": "/usr/local/bin/MHG", "MHG-partition": "/usr/local/bin/MHG-partition", "genome-to-blast-db": "/usr/local/bin/genome-to-blast-db"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mhg.
shpc-registry automated BioContainers addition for mhg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mhg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mhg:1.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mhg/1.1.0--hdfd78af_0
$ module help quay.io/biocontainers/mhg/1.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mhg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mhg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mhg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mhg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mhg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mhg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MHG

```bash
$ singularity exec <container> /usr/local/bin/MHG
$ podman run --it --rm --entrypoint /usr/local/bin/MHG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MHG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MHG-partition

```bash
$ singularity exec <container> /usr/local/bin/MHG-partition
$ podman run --it --rm --entrypoint /usr/local/bin/MHG-partition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MHG-partition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome-to-blast-db

```bash
$ singularity exec <container> /usr/local/bin/genome-to-blast-db
$ podman run --it --rm --entrypoint /usr/local/bin/genome-to-blast-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome-to-blast-db   -v ${PWD} -w ${PWD} <container> -c " $@"
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