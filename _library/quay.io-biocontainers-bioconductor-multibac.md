---
layout: container
name:  "quay.io/biocontainers/bioconductor-multibac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multibac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multibac/container.yaml"
updated_at: "2025-11-08 03:37:21.175120"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multibac"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multibac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multibac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multibac", "latest": {"1.16.0--r44hdfd78af_0": "sha256:16672c58a59a791164d20ec6f343708647e17691371f9611e731dcd2e8ef14e4"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:dc8ba6e2e63482463e6d811838f64da78f7784a74cd2a56be9e2af0c73a1d6ab", "1.8.0--r42hdfd78af_0": "sha256:5238b488a65cb31a201797c171e3f2b2860c087797fff13a917de4b8b31d51fa", "1.10.0--r43hdfd78af_0": "sha256:c3e6bea1a05292a9676e7716761a79daebf15a54b62aefd814c33f5db7238d45", "1.12.0--r43hdfd78af_0": "sha256:b39a4c8dd4da22679b888562afff58a0a9e8a086c34f78a68858de2a3f42beea", "1.16.0--r44hdfd78af_0": "sha256:16672c58a59a791164d20ec6f343708647e17691371f9611e731dcd2e8ef14e4"}, "docker": "quay.io/biocontainers/bioconductor-multibac"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multibac.
shpc-registry automated BioContainers addition for bioconductor-multibac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multibac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multibac:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multibac/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multibac/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multibac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multibac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multibac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multibac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multibac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multibac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-multibac

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