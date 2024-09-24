---
layout: container
name:  "quay.io/biocontainers/bioconductor-pepsnmrdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pepsnmrdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pepsnmrdata/container.yaml"
updated_at: "2024-09-24 02:53:59.133234"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pepsnmrdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.15.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pepsnmrdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pepsnmrdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pepsnmrdata", "latest": {"1.20.0--r43hdfd78af_0": "sha256:1006491484c7e80aff1de6f8556609a1f0cdae1664c8beaa6f745c7199746d7d"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:07cd5ff7f9344a5471cc705df967b337b113155959ba2b7aeda7aaa905214e7a", "1.15.0--r42hdfd78af_0": "sha256:6d0a927ab55f43aa212e1265dc3dd0c1e6938cd704cdacb3f3a174fe4b66943c", "1.12.0--r41hdfd78af_1": "sha256:b28572aa82e221c67dd37cda6888a1e31824c0dd661541c99350491503930441", "1.10.0--r41hdfd78af_0": "sha256:7cec63734000421e9a5f3fddbe28485cafb362d7dd099bf393344ff0ea459220", "1.18.0--r43hdfd78af_0": "sha256:5d4fffd19a21c49c85c023f02cdb87cfa75ff4ea6d847e066a823ddea93a3357", "1.20.0--r43hdfd78af_0": "sha256:1006491484c7e80aff1de6f8556609a1f0cdae1664c8beaa6f745c7199746d7d"}, "docker": "quay.io/biocontainers/bioconductor-pepsnmrdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pepsnmrdata.
shpc-registry automated BioContainers addition for bioconductor-pepsnmrdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pepsnmrdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pepsnmrdata:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pepsnmrdata/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pepsnmrdata/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pepsnmrdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepsnmrdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepsnmrdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pepsnmrdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pepsnmrdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pepsnmrdata-inspect-deffile:

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