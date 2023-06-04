---
layout: container
name:  "quay.io/biocontainers/genmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genmap/container.yaml"
updated_at: "2023-06-04 03:29:00.934845"
latest: "1.3.0--h87f3376_2"
container_url: "https://biocontainers.pro/tools/genmap"
aliases:
 - "genmap"
versions:
 - "1.3.0--h87f3376_2"
description: "shpc-registry automated BioContainers addition for genmap"
config: {"url": "https://biocontainers.pro/tools/genmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genmap", "latest": {"1.3.0--h87f3376_2": "sha256:33fac3318194845d21605cc9df342aeda22d3823f35b351a7d63880da1301c30"}, "tags": {"1.3.0--h87f3376_2": "sha256:33fac3318194845d21605cc9df342aeda22d3823f35b351a7d63880da1301c30"}, "docker": "quay.io/biocontainers/genmap", "aliases": {"genmap": "/usr/local/bin/genmap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genmap.
shpc-registry automated BioContainers addition for genmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genmap:1.3.0--h87f3376_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genmap/1.3.0--h87f3376_2
$ module help quay.io/biocontainers/genmap/1.3.0--h87f3376_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genmap

```bash
$ singularity exec <container> /usr/local/bin/genmap
$ podman run --it --rm --entrypoint /usr/local/bin/genmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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