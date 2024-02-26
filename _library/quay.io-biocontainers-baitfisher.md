---
layout: container
name:  "quay.io/biocontainers/baitfisher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/baitfisher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/baitfisher/container.yaml"
updated_at: "2024-02-26 02:53:09.031713"
latest: "1.0--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/baitfisher"
aliases:
 - "BaitFilter"
 - "BaitFisher"
versions:
 - "1.0--h9f5acd7_4"
 - "1.0--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for baitfisher"
config: {"url": "https://biocontainers.pro/tools/baitfisher", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for baitfisher", "latest": {"1.0--h4ac6f70_6": "sha256:d5c18f6017fb11ac9ae3e2fb1f8b5514df23e063407506699ebad3ac9eb29720"}, "tags": {"1.0--h9f5acd7_4": "sha256:2df41913a7c8553153e0343bc96f32a5bf47ee90215c5275fb82d4d57a1be6e2", "1.0--h4ac6f70_6": "sha256:d5c18f6017fb11ac9ae3e2fb1f8b5514df23e063407506699ebad3ac9eb29720"}, "docker": "quay.io/biocontainers/baitfisher", "aliases": {"BaitFilter": "/usr/local/bin/BaitFilter", "BaitFisher": "/usr/local/bin/BaitFisher"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/baitfisher.
shpc-registry automated BioContainers addition for baitfisher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/baitfisher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/baitfisher:1.0--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/baitfisher/1.0--h4ac6f70_6
$ module help quay.io/biocontainers/baitfisher/1.0--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### baitfisher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### baitfisher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### baitfisher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### baitfisher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### baitfisher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### baitfisher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BaitFilter

```bash
$ singularity exec <container> /usr/local/bin/BaitFilter
$ podman run --it --rm --entrypoint /usr/local/bin/BaitFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BaitFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BaitFisher

```bash
$ singularity exec <container> /usr/local/bin/BaitFisher
$ podman run --it --rm --entrypoint /usr/local/bin/BaitFisher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BaitFisher   -v ${PWD} -w ${PWD} <container> -c " $@"
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