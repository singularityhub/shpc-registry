---
layout: container
name:  "quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db/container.yaml"
updated_at: "2025-09-06 03:19:45.845938"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-raex10sttranscriptcluster.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-raex10sttranscriptcluster.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-raex10sttranscriptcluster.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-raex10sttranscriptcluster.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:5c13961a3961b5b4367e208357606ac68c7c21c415d6b715f6ec13b07d3472c4"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:58a7efdd0233247b1f52f5caea33b4d8b1a0f35382f12057fa75f55d44ec2a07", "8.8.0--r42hdfd78af_2": "sha256:cd7902669692ccb57c9e154c1f2a39bc3bc8f7a0b2d27f2d29ce7471936ea5c9", "8.8.0--r43hdfd78af_3": "sha256:b2ab6a382f1e0cfb7ac401a288a741d35ea027597cd8d29f628344fd03430deb", "8.8.0--r43hdfd78af_4": "sha256:ed6b9eb1ba670b43c4b0faa24f69f38502e6661a9e41104907cd29ea9afd1a15", "8.8.0--r44hdfd78af_5": "sha256:5c13961a3961b5b4367e208357606ac68c7c21c415d6b715f6ec13b07d3472c4"}, "docker": "quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db.
shpc-registry automated BioContainers addition for bioconductor-raex10sttranscriptcluster.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-raex10sttranscriptcluster.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-raex10sttranscriptcluster.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-raex10sttranscriptcluster.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-raex10sttranscriptcluster.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-raex10sttranscriptcluster.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-raex10sttranscriptcluster.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-raex10sttranscriptcluster.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-raex10sttranscriptcluster.db

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