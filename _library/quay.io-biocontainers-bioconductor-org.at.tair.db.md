---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.at.tair.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.at.tair.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.at.tair.db/container.yaml"
updated_at: "2024-09-06 03:10:07.727504"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.at.tair.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.at.tair.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.at.tair.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.at.tair.db", "latest": {"3.18.0--r43hdfd78af_0": "sha256:f90b38ce840ae7ca8fcb33a9273095483c37ff111a9a0d7f9d1ff28889ffba3a"}, "tags": {"3.8.2--r36_1": "sha256:d7b41e0e606717ea85b984e80343fb93c00f6013cd249465b1d7eb6c88b06326", "3.16.0--r42hdfd78af_0": "sha256:64e8faae5b0a0b419647f2357d429fef7d28efb14a6492240a413a16ec93894e", "3.14.0--r41hdfd78af_1": "sha256:caa9ab19702e0074f6b698f198fd6a48b95cd223ab3bceb1823320345d39fbee", "3.13.0--r41hdfd78af_0": "sha256:887551dc17e96c603e80cc42fcc39d59956bb1d085aab5179024a01d0243ea74", "3.12.0--r40hdfd78af_1": "sha256:d6629388f5a26753e38af421d07ab050aa1ca41d4b7d6681eab074c57f83c3c1", "3.11.1--r40_0": "sha256:5788c89a7a2af6ad5ee687b1bebd3e52ea437f2d72bc22e3f132163d83933bc3", "3.17.0--r43hdfd78af_0": "sha256:3f87aa6b0eb4fb9ee57d4c414c709dfbf3d8cf17c0099381c74045ac8571fa23", "3.18.0--r43hdfd78af_0": "sha256:f90b38ce840ae7ca8fcb33a9273095483c37ff111a9a0d7f9d1ff28889ffba3a"}, "docker": "quay.io/biocontainers/bioconductor-org.at.tair.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.at.tair.db.
shpc-registry automated BioContainers addition for bioconductor-org.at.tair.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.at.tair.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.at.tair.db:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.at.tair.db/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.at.tair.db/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.at.tair.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.at.tair.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.at.tair.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.at.tair.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.at.tair.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.at.tair.db-inspect-deffile:

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