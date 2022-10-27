---
layout: container
name:  "quay.io/biocontainers/cblaster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cblaster/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cblaster/container.yaml"
updated_at: "2022-10-27 01:07:24.801563"
latest: "1.3.9--pyhb7b1952_0"
container_url: "https://biocontainers.pro/tools/cblaster"
aliases:
 - "cblaster"
 - "clinker"
versions:
 - "1.3.9--pyhb7b1952_0"
description: "shpc-registry automated BioContainers addition for cblaster"
config: {"url": "https://biocontainers.pro/tools/cblaster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cblaster", "latest": {"1.3.9--pyhb7b1952_0": "sha256:3b41c02e0ae141309bda49bfc64ceecf5737118436dafbce5c5695e33fec776b"}, "tags": {"1.3.9--pyhb7b1952_0": "sha256:3b41c02e0ae141309bda49bfc64ceecf5737118436dafbce5c5695e33fec776b"}, "docker": "quay.io/biocontainers/cblaster", "aliases": {"cblaster": "/usr/local/bin/cblaster", "clinker": "/usr/local/bin/clinker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cblaster.
shpc-registry automated BioContainers addition for cblaster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cblaster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cblaster:1.3.9--pyhb7b1952_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cblaster/1.3.9--pyhb7b1952_0
$ module help quay.io/biocontainers/cblaster/1.3.9--pyhb7b1952_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cblaster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cblaster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cblaster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cblaster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cblaster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cblaster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cblaster

```bash
$ singularity exec <container> /usr/local/bin/cblaster
$ podman run --it --rm --entrypoint /usr/local/bin/cblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clinker

```bash
$ singularity exec <container> /usr/local/bin/clinker
$ podman run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
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