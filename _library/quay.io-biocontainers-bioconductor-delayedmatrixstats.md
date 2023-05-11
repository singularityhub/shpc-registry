---
layout: container
name:  "quay.io/biocontainers/bioconductor-delayedmatrixstats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-delayedmatrixstats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-delayedmatrixstats/container.yaml"
updated_at: "2023-05-11 02:38:27.117622"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-delayedmatrixstats"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.3--r40hdfd78af_0"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-delayedmatrixstats"
config: {"url": "https://biocontainers.pro/tools/bioconductor-delayedmatrixstats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-delayedmatrixstats", "latest": {"1.20.0--r42hdfd78af_0": "sha256:b2e019d410f698f3e2ca92603434212d8d19e861bbd182227714f12cb6285605"}, "tags": {"1.8.0--r36_0": "sha256:ff42ee2c7667ca75e6214dd6215fff5f0e8649bc929b4ca5eb689f4639f47e3c", "1.20.0--r42hdfd78af_0": "sha256:b2e019d410f698f3e2ca92603434212d8d19e861bbd182227714f12cb6285605", "1.16.0--r41hdfd78af_0": "sha256:a9d7586fa7a2783a713dce7361110f6f45be5575154faafebd51dafa5172fb25", "1.14.0--r41hdfd78af_0": "sha256:a7423fef38b1304c7a1dc37c22f08bb8720b2a9ba8183072004d7dcd5b417edc", "1.12.3--r40hdfd78af_0": "sha256:2f5b044acb6ad1eef17525c6587e3fe86d30016f9ff362bc5d66c9bdd8994f89", "1.10.0--r40_0": "sha256:c98b6c6bb8b73e7f86152d6e6509cf54a63e32c59cb132cd7e9f98624b90e0b4"}, "docker": "quay.io/biocontainers/bioconductor-delayedmatrixstats", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-delayedmatrixstats.
shpc-registry automated BioContainers addition for bioconductor-delayedmatrixstats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedmatrixstats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedmatrixstats:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-delayedmatrixstats/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-delayedmatrixstats/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-delayedmatrixstats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedmatrixstats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedmatrixstats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-delayedmatrixstats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-delayedmatrixstats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-delayedmatrixstats-inspect-deffile:

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