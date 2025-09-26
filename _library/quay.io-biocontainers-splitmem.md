---
layout: container
name:  "quay.io/biocontainers/splitmem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/splitmem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/splitmem/container.yaml"
updated_at: "2025-09-26 03:48:51.499581"
latest: "1.0--h9948957_7"
container_url: "https://biocontainers.pro/tools/splitmem"
aliases:
 - "splitMEM"
versions:
 - "1.0--h9f5acd7_4"
 - "1.0--h4ac6f70_6"
 - "1.0--h9948957_7"
description: "shpc-registry automated BioContainers addition for splitmem"
config: {"url": "https://biocontainers.pro/tools/splitmem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for splitmem", "latest": {"1.0--h9948957_7": "sha256:4e609e4b0c5b99d36c21e701a6fae8e4d50ab64bda3ddd2057932315862f01a9"}, "tags": {"1.0--h9f5acd7_4": "sha256:f157295b5dda2e29a559fe549ae5b0e9feae9dc47ee0510db1f978683c337493", "1.0--h4ac6f70_6": "sha256:031a2fe0c1058f71e882236294b8f077185f37dd6fbaed48b448c799ad355c19", "1.0--h9948957_7": "sha256:4e609e4b0c5b99d36c21e701a6fae8e4d50ab64bda3ddd2057932315862f01a9"}, "docker": "quay.io/biocontainers/splitmem", "aliases": {"splitMEM": "/usr/local/bin/splitMEM"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/splitmem.
shpc-registry automated BioContainers addition for splitmem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/splitmem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/splitmem:1.0--h9948957_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/splitmem/1.0--h9948957_7
$ module help quay.io/biocontainers/splitmem/1.0--h9948957_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### splitmem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### splitmem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### splitmem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### splitmem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### splitmem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### splitmem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### splitMEM

```bash
$ singularity exec <container> /usr/local/bin/splitMEM
$ podman run --it --rm --entrypoint /usr/local/bin/splitMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
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