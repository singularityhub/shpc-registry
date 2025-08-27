---
layout: container
name:  "quay.io/biocontainers/bioconductor-cohcapanno"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cohcapanno/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cohcapanno/container.yaml"
updated_at: "2025-08-27 03:47:51.601817"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cohcapanno"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cohcapanno"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cohcapanno", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cohcapanno", "latest": {"1.42.0--r44hdfd78af_0": "sha256:12071763c055354ae863ae553920816ca8753f594cff228c100bd1b667dcec8b"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:5485c1cfebbde03e7437ed27b0af364e8fb363a0a739c2af2fb9f42e692a8a44", "1.34.0--r42hdfd78af_0": "sha256:5eaa684117f39eefe05b9efbfbaae91102f042edcf7b48ca476d317bdd98d1ce", "1.33.0--r42hdfd78af_0": "sha256:e4f444a517fb0a02e0816d04b9a5fea40e519e74f684960328b3fbba1272d127", "1.36.0--r43hdfd78af_0": "sha256:3ce92fdb631c0e99ce9bd4f1c3af19750b7260be5e7805ba641a28506292758c", "1.38.0--r43hdfd78af_0": "sha256:8655aec1b5bfc10ffbe96e5e09d99f46c205a0f9d0b352cb743c63771fd59bd2", "1.42.0--r44hdfd78af_0": "sha256:12071763c055354ae863ae553920816ca8753f594cff228c100bd1b667dcec8b"}, "docker": "quay.io/biocontainers/bioconductor-cohcapanno"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cohcapanno.
shpc-registry automated BioContainers addition for bioconductor-cohcapanno
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cohcapanno
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cohcapanno:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cohcapanno/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cohcapanno/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cohcapanno-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cohcapanno-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cohcapanno-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cohcapanno-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cohcapanno-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cohcapanno-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cohcapanno

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