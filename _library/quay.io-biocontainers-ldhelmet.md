---
layout: container
name:  "quay.io/biocontainers/ldhelmet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ldhelmet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ldhelmet/container.yaml"
updated_at: "2024-10-31 03:13:24.680291"
latest: "1.10--heacdb12_7"
container_url: "https://biocontainers.pro/tools/ldhelmet"
aliases:
 - "ldhelmet"
versions:
 - "1.10--h057f3fe_4"
 - "1.10--heb38167_6"
 - "1.10--heacdb12_7"
description: "shpc-registry automated BioContainers addition for ldhelmet"
config: {"url": "https://biocontainers.pro/tools/ldhelmet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ldhelmet", "latest": {"1.10--heacdb12_7": "sha256:858b3063e8373293be271049cb43661618e0b289b9afd8f39e5a3de487196c99"}, "tags": {"1.10--h057f3fe_4": "sha256:8f72a7b2974aa2501d080b49c523ccde29785004a24d60566f96654255c853f7", "1.10--heb38167_6": "sha256:4d61e2c6d1d2debf5daf3f2e19c9885d517681acc7a6771564a9def21d610633", "1.10--heacdb12_7": "sha256:858b3063e8373293be271049cb43661618e0b289b9afd8f39e5a3de487196c99"}, "docker": "quay.io/biocontainers/ldhelmet", "aliases": {"ldhelmet": "/usr/local/bin/ldhelmet"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ldhelmet.
shpc-registry automated BioContainers addition for ldhelmet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ldhelmet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ldhelmet:1.10--heacdb12_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ldhelmet/1.10--heacdb12_7
$ module help quay.io/biocontainers/ldhelmet/1.10--heacdb12_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ldhelmet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ldhelmet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ldhelmet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ldhelmet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ldhelmet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ldhelmet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ldhelmet

```bash
$ singularity exec <container> /usr/local/bin/ldhelmet
$ podman run --it --rm --entrypoint /usr/local/bin/ldhelmet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldhelmet   -v ${PWD} -w ${PWD} <container> -c " $@"
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