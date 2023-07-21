---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcyjs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcyjs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcyjs/container.yaml"
updated_at: "2023-07-21 03:26:12.524570"
latest: "2.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcyjs"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_0"
 - "2.20.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.12.0--r40hdfd78af_1"
 - "2.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcyjs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcyjs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcyjs", "latest": {"2.20.0--r42hdfd78af_0": "sha256:e91b654f29030b3402b7d481c7361368cb68a8a24eca6f4d6b75224f6dd314ab"}, "tags": {"2.8.0--r36_0": "sha256:737601347e76a7caa627d26f01ef38c4fcb983d8d1336968550b377fb87821f6", "2.20.0--r42hdfd78af_0": "sha256:e91b654f29030b3402b7d481c7361368cb68a8a24eca6f4d6b75224f6dd314ab", "2.16.0--r41hdfd78af_0": "sha256:1888f3684a818e4515282fb29494e842062727d75376c8b8534c3bb916298b29", "2.12.0--r40hdfd78af_1": "sha256:5784f8b3efabd10e286fbbc131cde3941614cdb495a008fc019904d5969bd87e", "2.10.0--r40_0": "sha256:6f891413baa3ff4514b432db31d9cd8b49c0f3ddfff3a8c6bcf35822282cf310"}, "docker": "quay.io/biocontainers/bioconductor-rcyjs", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcyjs.
shpc-registry automated BioContainers addition for bioconductor-rcyjs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcyjs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcyjs:2.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcyjs/2.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcyjs/2.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcyjs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcyjs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcyjs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcyjs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcyjs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcyjs-inspect-deffile:

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