---
layout: container
name:  "quay.io/biocontainers/bioconductor-multiassayexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multiassayexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multiassayexperiment/container.yaml"
updated_at: "2025-04-14 03:29:54.292703"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multiassayexperiment"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multiassayexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multiassayexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multiassayexperiment", "latest": {"1.32.0--r44hdfd78af_0": "sha256:9fdb60120bbbeb7160ca735af82ce68ec4b3eb56554f99780947981da57da201"}, "tags": {"1.8.1--r351_0": "sha256:e2253b83a7ae27f5c5b6639352eed27d2bc3002c2072c3ad727ff226675f189b", "1.24.0--r42hdfd78af_0": "sha256:bae54a9065ae6c8940f36859ee88eb952f258efa52e5c5897b5dba10d09a6930", "1.20.0--r41hdfd78af_0": "sha256:dea7a5e10ebb3d3ac78ab12d254dfc4fef711634229a0c53798a2f190dfad804", "1.18.0--r41hdfd78af_0": "sha256:60346afe982a51dc5a8e3000b30b32d1b6ee4495f049c3b69daca709a30be112", "1.16.0--r40hdfd78af_1": "sha256:bc95f014e0ffc1fad31ab1a484ed30edc7953d17e10c8dfbfc2acfced3fff3a7", "1.14.0--r40_0": "sha256:0b4625feab8dba5586b07735ef343cbc5d25a822ba5b7576f43b75d530f41e33", "1.26.0--r43hdfd78af_0": "sha256:3d0825880121cc7ac7d60479f11dbc71557403081071ef8595966b3a4133d43a", "1.28.0--r43hdfd78af_0": "sha256:ec19b8f2b6c44e5d38c91a9b992900c2f7fd215c56f587e8b3c299e9a9025fb7", "1.32.0--r44hdfd78af_0": "sha256:9fdb60120bbbeb7160ca735af82ce68ec4b3eb56554f99780947981da57da201"}, "docker": "quay.io/biocontainers/bioconductor-multiassayexperiment", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multiassayexperiment.
shpc-registry automated BioContainers addition for bioconductor-multiassayexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multiassayexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multiassayexperiment:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multiassayexperiment/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multiassayexperiment/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multiassayexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiassayexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiassayexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multiassayexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multiassayexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multiassayexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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