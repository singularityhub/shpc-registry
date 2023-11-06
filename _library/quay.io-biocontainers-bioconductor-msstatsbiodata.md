---
layout: container
name:  "quay.io/biocontainers/bioconductor-msstatsbiodata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msstatsbiodata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msstatsbiodata/container.yaml"
updated_at: "2023-11-06 03:08:41.796890"
latest: "1.13.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msstatsbiodata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.13.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.11.0--r40_0"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msstatsbiodata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msstatsbiodata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msstatsbiodata", "latest": {"1.13.0--r41hdfd78af_0": "sha256:d39b3260194a1bbc9d20730c34f225945902d702ce58716c46217547a62cfdaf"}, "tags": {"1.8.0--r36_0": "sha256:cd419f0c3f77e0d0706939168363d697cc8c4f9f646bc25964d05ecded57eb65", "1.13.0--r41hdfd78af_0": "sha256:d39b3260194a1bbc9d20730c34f225945902d702ce58716c46217547a62cfdaf", "1.12.0--r40hdfd78af_1": "sha256:d389137c17aa20ac0d3878cc2842050074f1711002a50ad4fc9c8f382de05139", "1.11.0--r40_0": "sha256:022aa5f1df6531dd9c421764e937f1a7d56c2657fa8e71fdd2cd6f98b420c702", "1.10.0--r40_0": "sha256:ce707a598f74c44a8d3f0b0e3c40dcfdcb82b27433b7efe2c972c9f447838834"}, "docker": "quay.io/biocontainers/bioconductor-msstatsbiodata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msstatsbiodata.
shpc-registry automated BioContainers addition for bioconductor-msstatsbiodata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatsbiodata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msstatsbiodata:1.13.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msstatsbiodata/1.13.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msstatsbiodata/1.13.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msstatsbiodata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatsbiodata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msstatsbiodata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msstatsbiodata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msstatsbiodata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msstatsbiodata-inspect-deffile:

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