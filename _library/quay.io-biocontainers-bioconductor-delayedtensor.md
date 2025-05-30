---
layout: container
name:  "quay.io/biocontainers/bioconductor-delayedtensor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-delayedtensor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-delayedtensor/container.yaml"
updated_at: "2025-05-30 03:18:25.833388"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-delayedtensor"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-delayedtensor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-delayedtensor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-delayedtensor", "latest": {"1.12.0--r44hdfd78af_0": "sha256:f6082aa3016ee27b19bc19f694002f7a95f3011e5aca2f5614ad465406b39455"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:891c8aa10491b6a62051ee9ca8ccb6b2d02752fe455a51fbee987d5f1c95d677", "1.4.0--r42hdfd78af_0": "sha256:d1ad2c2f7049578604b4f4763128146dc38c74d43ba4ec75d4c59b00a42351fe", "1.6.0--r43hdfd78af_0": "sha256:4ca7a338c358cefb4579ece31433fd7a8f94e2955a112ad937c7e7e17351dcc2", "1.8.0--r43hdfd78af_0": "sha256:4708c388a9f4a60743a7cdefde886fa7ac92fc14f37ca30470497718fd43dd28", "1.12.0--r44hdfd78af_0": "sha256:f6082aa3016ee27b19bc19f694002f7a95f3011e5aca2f5614ad465406b39455"}, "docker": "quay.io/biocontainers/bioconductor-delayedtensor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-delayedtensor.
shpc-registry automated BioContainers addition for bioconductor-delayedtensor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedtensor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedtensor:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-delayedtensor/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-delayedtensor/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-delayedtensor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedtensor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedtensor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-delayedtensor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-delayedtensor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-delayedtensor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-delayedtensor

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