---
layout: container
name:  "quay.io/biocontainers/bioconductor-rsubread"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rsubread/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rsubread/container.yaml"
updated_at: "2025-11-25 04:05:16.576097"
latest: "2.16.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rsubread"

versions:
 - "2.8.2--r41hc0cfd56_0"
 - "2.12.0--r42hc0cfd56_0"
 - "2.12.0--r42ha9d7317_1"
 - "2.14.2--r43ha9d7317_0"
 - "2.16.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rsubread"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rsubread", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rsubread", "latest": {"2.16.0--r43ha9d7317_0": "sha256:39f4d78a0e2abc33b468c3ec4bb08e07c13e8a71e2120aa3b4d1aa3ecb6ca2b5"}, "tags": {"2.8.2--r41hc0cfd56_0": "sha256:a95e788d3ec62d2450e50584d5bc785edfd3593d116ef70bd2996e04195de6a2", "2.12.0--r42hc0cfd56_0": "sha256:fe2aa17bb1b8fe926ff6019bd7df3274ae5e1db73e21f5cd3150eb71e1c6073b", "2.12.0--r42ha9d7317_1": "sha256:9bb3342815d2d9220169c47a35fd77cd919a33dbddcc472c8833d235c348ec56", "2.14.2--r43ha9d7317_0": "sha256:29c9ca926c86658800a4da8ad3413c218ea43dc75193c2e76cc5e61cd60e580a", "2.16.0--r43ha9d7317_0": "sha256:39f4d78a0e2abc33b468c3ec4bb08e07c13e8a71e2120aa3b4d1aa3ecb6ca2b5"}, "docker": "quay.io/biocontainers/bioconductor-rsubread"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rsubread.
shpc-registry automated BioContainers addition for bioconductor-rsubread
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rsubread
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rsubread:2.16.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rsubread/2.16.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-rsubread/2.16.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rsubread-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsubread-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsubread-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rsubread-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rsubread-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rsubread-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rsubread

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