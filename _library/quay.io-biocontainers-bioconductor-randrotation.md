---
layout: container
name:  "quay.io/biocontainers/bioconductor-randrotation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-randrotation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-randrotation/container.yaml"
updated_at: "2025-01-24 03:21:39.514257"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-randrotation"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-randrotation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-randrotation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-randrotation", "latest": {"1.18.0--r44hdfd78af_0": "sha256:0413a31ecbe456d831b4f8c32437c8160d05b7622a56213da2cfce48bcda2604"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:786dab0b38caa583502e90dddd40c06191d971ed7d232bbac4ce9754284b4776", "1.10.0--r42hdfd78af_0": "sha256:ce3380d85fd5fdbf236181e60ad80a869a073cac6a115e340c7d4dfd9495324e", "1.12.0--r43hdfd78af_0": "sha256:ab5e4cc3cf304309032b2e3d9af612baedc1ec383c25fec3d9c6d9c87b2428cc", "1.14.0--r43hdfd78af_0": "sha256:519f2c058ba9f6289e6a106d10e12bf3feaed02e77ae33142b05354d8aaa311f", "1.18.0--r44hdfd78af_0": "sha256:0413a31ecbe456d831b4f8c32437c8160d05b7622a56213da2cfce48bcda2604"}, "docker": "quay.io/biocontainers/bioconductor-randrotation"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-randrotation.
shpc-registry automated BioContainers addition for bioconductor-randrotation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-randrotation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-randrotation:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-randrotation/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-randrotation/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-randrotation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-randrotation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-randrotation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-randrotation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-randrotation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-randrotation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-randrotation

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