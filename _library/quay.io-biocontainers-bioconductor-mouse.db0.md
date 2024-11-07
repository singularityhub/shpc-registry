---
layout: container
name:  "quay.io/biocontainers/bioconductor-mouse.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mouse.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mouse.db0/container.yaml"
updated_at: "2024-11-07 03:05:49.394453"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mouse.db0"
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
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mouse.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mouse.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mouse.db0", "latest": {"3.18.0--r43hdfd78af_0": "sha256:d97fd94ab8469d53fa1f0322938ac5694be8d5e9c716ad2ee15b0d1605ead830"}, "tags": {"3.8.2--r36_1": "sha256:8c3d9e41f00972fbe445475500de6ed9df55f3ea7535d6a28312cfab37bc4c42", "3.16.0--r42hdfd78af_0": "sha256:08184ca7fd2d20a75b6995176840b892ec40a3e945ee3d7547e32bad52116bab", "3.14.0--r41hdfd78af_1": "sha256:3dadc0c8a61f82477e62ef020998b0e2a3785f446698810ca596333755c4e41c", "3.13.0--r41hdfd78af_0": "sha256:0063772069f0fa9e6c78650d310498b8d8e174618a88d0c9579721d9a08982bb", "3.12.0--r40hdfd78af_1": "sha256:9c0c4013bb723404202dffeeb21b28304d92c8d82e5e29220e9915598f003e34", "3.11.2--r40_0": "sha256:09ec348f2149c434d5e7a37b60ccaa2100fd7ed518b56b0292cec3cce4cc32c4", "3.17.0--r43hdfd78af_0": "sha256:9c9d4b87c608afe6edcce2a84f55ceaf817007265ece4960ae0acff42d057ccc", "3.18.0--r43hdfd78af_0": "sha256:d97fd94ab8469d53fa1f0322938ac5694be8d5e9c716ad2ee15b0d1605ead830"}, "docker": "quay.io/biocontainers/bioconductor-mouse.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mouse.db0.
shpc-registry automated BioContainers addition for bioconductor-mouse.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse.db0:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mouse.db0/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mouse.db0/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mouse.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mouse.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mouse.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mouse.db0-inspect-deffile:

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