---
layout: container
name:  "quay.io/biocontainers/bioconductor-exomecopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-exomecopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-exomecopy/container.yaml"
updated_at: "2025-11-06 03:51:10.920332"
latest: "1.48.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-exomecopy"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
 - "1.44.0--r42ha9d7317_1"
 - "1.46.0--r43ha9d7317_0"
 - "1.48.0--r43ha9d7317_0"
 - "1.48.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-exomecopy"
config: {"url": "https://biocontainers.pro/tools/bioconductor-exomecopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-exomecopy", "latest": {"1.48.0--r43ha9d7317_1": "sha256:9c33058d6f94ef07ffa9f08c701cbb3df1af938831a893387c58613e5abeb63e"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:1ee29299606ec531c3cb60ac5e6fb99a81c003e81e514b6fd0a831587e45227d", "1.44.0--r42hc0cfd56_0": "sha256:17ec3e23146669e7bb29c338cf1c8817f0aadeb4e6ece9c1a74357a829402f21", "1.44.0--r42ha9d7317_1": "sha256:d3f256ab3c0ffbf7aa180fb9d532701169a53d1d3653b2e149a91246886d2301", "1.46.0--r43ha9d7317_0": "sha256:014309d32d8ad4027416f50e9d2d7d63ca783b8e67899c0eaaf298bef89a4084", "1.48.0--r43ha9d7317_0": "sha256:c2a10ba7f6a363756c4c942db528e1f40a5b4641e0b233170418f00c7afed352", "1.48.0--r43ha9d7317_1": "sha256:9c33058d6f94ef07ffa9f08c701cbb3df1af938831a893387c58613e5abeb63e"}, "docker": "quay.io/biocontainers/bioconductor-exomecopy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-exomecopy.
shpc-registry automated BioContainers addition for bioconductor-exomecopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-exomecopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-exomecopy:1.48.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-exomecopy/1.48.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-exomecopy/1.48.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-exomecopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-exomecopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-exomecopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-exomecopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-exomecopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-exomecopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-exomecopy

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