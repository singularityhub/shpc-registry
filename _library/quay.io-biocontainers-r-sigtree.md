---
layout: container
name:  "quay.io/biocontainers/r-sigtree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-sigtree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-sigtree/container.yaml"
updated_at: "2025-02-15 02:56:43.264446"
latest: "1.10.6--r43h56115f1_12"
container_url: "https://biocontainers.pro/tools/r-sigtree"

versions:
 - "1.10.6--r41h73dbb54_9"
 - "1.10.6--r42h73dbb54_10"
 - "1.10.6--r42h56115f1_11"
 - "1.10.6--r43h56115f1_12"
description: "shpc-registry automated BioContainers addition for r-sigtree"
config: {"url": "https://biocontainers.pro/tools/r-sigtree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-sigtree", "latest": {"1.10.6--r43h56115f1_12": "sha256:b6be1217b139b32baf636900b4f46c158f47d279554a28e980ad90d535d48410"}, "tags": {"1.10.6--r41h73dbb54_9": "sha256:15cba20b52d3e01055b8be8ea06509ba7b3313c0570fe365c0fc6c7ae93cc236", "1.10.6--r42h73dbb54_10": "sha256:70fe1f758c62b58035f8cf62fe4a83b8aae521b303f62a432ca54653862f19de", "1.10.6--r42h56115f1_11": "sha256:f0ff82a6d49500a8643366e2c9dd822f2be273d9d5bdf728c61c77924adb9b7a", "1.10.6--r43h56115f1_12": "sha256:b6be1217b139b32baf636900b4f46c158f47d279554a28e980ad90d535d48410"}, "docker": "quay.io/biocontainers/r-sigtree"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-sigtree.
shpc-registry automated BioContainers addition for r-sigtree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-sigtree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-sigtree:1.10.6--r43h56115f1_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-sigtree/1.10.6--r43h56115f1_12
$ module help quay.io/biocontainers/r-sigtree/1.10.6--r43h56115f1_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-sigtree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-sigtree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-sigtree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-sigtree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-sigtree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-sigtree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-sigtree

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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