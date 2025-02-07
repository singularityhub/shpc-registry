---
layout: container
name:  "quay.io/biocontainers/bioconductor-h5vcdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-h5vcdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-h5vcdata/container.yaml"
updated_at: "2025-02-07 03:18:56.696527"
latest: "2.26.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-h5vcdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.9.0--r40_0"
 - "2.18.0--r42hdfd78af_0"
 - "2.17.0--r42hdfd78af_0"
 - "2.14.0--r41hdfd78af_1"
 - "2.12.0--r41hdfd78af_0"
 - "2.10.0--r40hdfd78af_1"
 - "2.20.0--r43hdfd78af_0"
 - "2.22.0--r43hdfd78af_0"
 - "2.26.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-h5vcdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-h5vcdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-h5vcdata", "latest": {"2.26.0--r44hdfd78af_0": "sha256:2ac39e17e5e4afcd27ad7368b8b59143499c153876121adc56bdd1ba22e2482c"}, "tags": {"2.9.0--r40_0": "sha256:3491c0f8728c3afa2c1f309c1659397097d987e7d3831b93b958ec2b6eeab8c9", "2.18.0--r42hdfd78af_0": "sha256:8305e68b25558f63b6ffc15fd11bbeca0405440e618e8b35c01028c3ec7a32d6", "2.17.0--r42hdfd78af_0": "sha256:483a2dd4974a7cfa3b9cd11921d56a00fb8934df231739b6c1b83556c1883ae2", "2.14.0--r41hdfd78af_1": "sha256:aafc081e8cabb512dea4ebfd3722744547a06064c7f3555563593b7322370ec8", "2.12.0--r41hdfd78af_0": "sha256:c39215130ec727dc4c4062418657dfdf4917340c689bed07dea3d1c04f023060", "2.10.0--r40hdfd78af_1": "sha256:5b66d834739d4e8f868fa580152055aaddff32fcfe3d914002f96d349566c890", "2.20.0--r43hdfd78af_0": "sha256:22a9822bd7ebd7722ade6406cf24b0fccbe1e3cd3a7e0d73c59d3ce7feaae271", "2.22.0--r43hdfd78af_0": "sha256:d6c4afc8c7a967506325c731292614d31566970f8ef600b7be08690601409e9c", "2.26.0--r44hdfd78af_0": "sha256:2ac39e17e5e4afcd27ad7368b8b59143499c153876121adc56bdd1ba22e2482c"}, "docker": "quay.io/biocontainers/bioconductor-h5vcdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-h5vcdata.
shpc-registry automated BioContainers addition for bioconductor-h5vcdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-h5vcdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-h5vcdata:2.26.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-h5vcdata/2.26.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-h5vcdata/2.26.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-h5vcdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h5vcdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h5vcdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-h5vcdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-h5vcdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-h5vcdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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