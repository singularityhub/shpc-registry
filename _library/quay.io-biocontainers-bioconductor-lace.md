---
layout: container
name:  "quay.io/biocontainers/bioconductor-lace"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lace/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lace/container.yaml"
updated_at: "2025-03-19 03:43:19.660814"
latest: "2.10.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lace"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "2.2.0--r42hdfd78af_0"
 - "2.4.0--r43hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
 - "2.10.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lace"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lace", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lace", "latest": {"2.10.0--r44hdfd78af_0": "sha256:15dc3d039968271b8202c2b079eb3b8dfb008fb6dd60283e2b9bb80fdb34b428"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:8ae85d97e6b6c2582a75c811bedb146c1108b3edeaa46a63be73b3d25a1cbf5d", "2.2.0--r42hdfd78af_0": "sha256:b2dacc60fe0f9274b0b56c28cbcb49a546e76a3912bdb5056c37752e43331c85", "2.4.0--r43hdfd78af_0": "sha256:f8c2278b898ac6f18315cca5b8fa555d0463210bbcf871f76a8267c7fa71eb29", "2.6.0--r43hdfd78af_0": "sha256:a5e0e2baf4d41fe8cabd1c91b0be2991e295cd0220f6d04a5015f5b27bd7ef68", "2.10.0--r44hdfd78af_0": "sha256:15dc3d039968271b8202c2b079eb3b8dfb008fb6dd60283e2b9bb80fdb34b428"}, "docker": "quay.io/biocontainers/bioconductor-lace"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lace.
shpc-registry automated BioContainers addition for bioconductor-lace
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lace
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lace:2.10.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lace/2.10.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lace/2.10.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lace-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lace-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lace-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lace-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lace-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lace-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lace

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