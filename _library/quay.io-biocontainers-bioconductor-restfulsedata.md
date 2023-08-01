---
layout: container
name:  "quay.io/biocontainers/bioconductor-restfulsedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-restfulsedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-restfulsedata/container.yaml"
updated_at: "2023-08-01 03:33:00.638484"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-restfulsedata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_1"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-restfulsedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-restfulsedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-restfulsedata", "latest": {"1.20.0--r42hdfd78af_0": "sha256:c5c2af004089f82b7812400a38f1f73ce72ac9f7a8843b83e60f19802c3b1766"}, "tags": {"1.8.0--r36_0": "sha256:e550024320b43792b27cb2c4096d5d2b8d3f07202cb9c499b35091239934f09e", "1.16.0--r41hdfd78af_1": "sha256:30145d46542439afda78fa66d3a7111baf8f03f330818525c5c945d6784cba14", "1.14.0--r41hdfd78af_0": "sha256:2fac5163e72eebd0101c50c806f6816c54d32785b81f659ef6d54f252fcbeaf5", "1.12.0--r40hdfd78af_1": "sha256:9dde939121fd0f8377aaf73ac26bbc23ee80160dc6bfd91d41bc5b325f207919", "1.10.0--r40_0": "sha256:a015804680950b30ec4be1a920cc9bd05148dc5fe13f0a50b07c0d8729804c4f", "1.20.0--r42hdfd78af_0": "sha256:c5c2af004089f82b7812400a38f1f73ce72ac9f7a8843b83e60f19802c3b1766"}, "docker": "quay.io/biocontainers/bioconductor-restfulsedata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-restfulsedata.
shpc-registry automated BioContainers addition for bioconductor-restfulsedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-restfulsedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-restfulsedata:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-restfulsedata/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-restfulsedata/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-restfulsedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-restfulsedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-restfulsedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-restfulsedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-restfulsedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-restfulsedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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