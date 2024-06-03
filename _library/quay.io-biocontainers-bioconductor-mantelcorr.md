---
layout: container
name:  "quay.io/biocontainers/bioconductor-mantelcorr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mantelcorr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mantelcorr/container.yaml"
updated_at: "2024-06-03 02:48:02.710313"
latest: "1.72.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mantelcorr"

versions:
 - "1.64.0--r41hdfd78af_0"
 - "1.68.0--r42hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mantelcorr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mantelcorr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mantelcorr", "latest": {"1.72.0--r43hdfd78af_0": "sha256:3b5acfd965bda08b82395e8dd535beb374604f915d523d75d4a06138af571bb0"}, "tags": {"1.64.0--r41hdfd78af_0": "sha256:2f3aa333cf02c6c13f3f0fe2c7dfe25e7fbcf1a4dde4e254e8833e6ffc3fbd06", "1.68.0--r42hdfd78af_0": "sha256:513c387d02929505ea70a0a34338a54122cc279a93cbb8dcd72d9f711f218423", "1.70.0--r43hdfd78af_0": "sha256:fe1f99c65fb6feb1e71896362336d105a18e72c490a4b61cc3631dff891911ea", "1.72.0--r43hdfd78af_0": "sha256:3b5acfd965bda08b82395e8dd535beb374604f915d523d75d4a06138af571bb0"}, "docker": "quay.io/biocontainers/bioconductor-mantelcorr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mantelcorr.
shpc-registry automated BioContainers addition for bioconductor-mantelcorr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mantelcorr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mantelcorr:1.72.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mantelcorr/1.72.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mantelcorr/1.72.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mantelcorr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mantelcorr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mantelcorr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mantelcorr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mantelcorr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mantelcorr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mantelcorr

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