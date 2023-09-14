---
layout: container
name:  "quay.io/biocontainers/rnacode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnacode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnacode/container.yaml"
updated_at: "2023-09-14 03:19:23.388848"
latest: "0.3--hec16e2b_3"
container_url: "https://biocontainers.pro/tools/rnacode"
aliases:
 - "RNAcode"
versions:
 - "0.3--hec16e2b_3"
description: "shpc-registry automated BioContainers addition for rnacode"
config: {"url": "https://biocontainers.pro/tools/rnacode", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnacode", "latest": {"0.3--hec16e2b_3": "sha256:b73fc2d9fb7f96fbba1cfd39a849b304628c245d562dd6a5e4c8bd1b708c2fc8"}, "tags": {"0.3--hec16e2b_3": "sha256:b73fc2d9fb7f96fbba1cfd39a849b304628c245d562dd6a5e4c8bd1b708c2fc8"}, "docker": "quay.io/biocontainers/rnacode", "aliases": {"RNAcode": "/usr/local/bin/RNAcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnacode.
shpc-registry automated BioContainers addition for rnacode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnacode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnacode:0.3--hec16e2b_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnacode/0.3--hec16e2b_3
$ module help quay.io/biocontainers/rnacode/0.3--hec16e2b_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnacode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnacode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnacode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnacode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnacode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnacode-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAcode

```bash
$ singularity exec <container> /usr/local/bin/RNAcode
$ podman run --it --rm --entrypoint /usr/local/bin/RNAcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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