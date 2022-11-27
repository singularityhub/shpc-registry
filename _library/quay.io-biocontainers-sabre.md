---
layout: container
name:  "quay.io/biocontainers/sabre"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sabre/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sabre/container.yaml"
updated_at: "2022-11-27 00:41:30.065330"
latest: "1.000--h7132678_3"
container_url: "https://biocontainers.pro/tools/sabre"
aliases:
 - "sabre"
versions:
 - "1.000--h7132678_3"
description: "shpc-registry automated BioContainers addition for sabre"
config: {"url": "https://biocontainers.pro/tools/sabre", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sabre", "latest": {"1.000--h7132678_3": "sha256:2ad6f6e463453b4e5471dcb0ff45c082dc4a4aca22b620b6bfde0cd1aa900af7"}, "tags": {"1.000--h7132678_3": "sha256:2ad6f6e463453b4e5471dcb0ff45c082dc4a4aca22b620b6bfde0cd1aa900af7"}, "docker": "quay.io/biocontainers/sabre", "aliases": {"sabre": "/usr/local/bin/sabre"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sabre.
shpc-registry automated BioContainers addition for sabre
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sabre
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sabre:1.000--h7132678_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sabre/1.000--h7132678_3
$ module help quay.io/biocontainers/sabre/1.000--h7132678_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sabre-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sabre-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sabre-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sabre-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sabre-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sabre-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sabre

```bash
$ singularity exec <container> /usr/local/bin/sabre
$ podman run --it --rm --entrypoint /usr/local/bin/sabre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sabre   -v ${PWD} -w ${PWD} <container> -c " $@"
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