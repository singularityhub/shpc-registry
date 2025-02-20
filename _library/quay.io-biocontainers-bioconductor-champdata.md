---
layout: container
name:  "quay.io/biocontainers/bioconductor-champdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-champdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-champdata/container.yaml"
updated_at: "2025-02-20 02:56:51.936682"
latest: "2.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-champdata"

versions:
 - "2.26.0--r41hdfd78af_1"
 - "2.30.0--r42hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
 - "2.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-champdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-champdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-champdata", "latest": {"2.38.0--r44hdfd78af_0": "sha256:ee7aae5bc71e820f58c0c3fae31b2000163fe51339d5492a8b5db638fb4d689f"}, "tags": {"2.26.0--r41hdfd78af_1": "sha256:47517caecacd1453fb2e1861df56d87c803cf66cc1b6c2e27a542d636798d4d5", "2.30.0--r42hdfd78af_0": "sha256:e83632a053a49d4cc55d21bf4801e5fac5213e3b2ed51038b89bc547b3b5f874", "2.32.0--r43hdfd78af_0": "sha256:9c329bbe7a8faacc9e9796b6d777b42ddf0634b0b9d7728c09be78b1e8546af9", "2.34.0--r43hdfd78af_0": "sha256:e93522579481778c71762f5f53d79b88119e9f8ca59862074bcd7c87fe2c776e", "2.38.0--r44hdfd78af_0": "sha256:ee7aae5bc71e820f58c0c3fae31b2000163fe51339d5492a8b5db638fb4d689f"}, "docker": "quay.io/biocontainers/bioconductor-champdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-champdata.
shpc-registry automated BioContainers addition for bioconductor-champdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-champdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-champdata:2.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-champdata/2.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-champdata/2.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-champdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-champdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-champdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-champdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-champdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-champdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-champdata

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