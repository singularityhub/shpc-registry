---
layout: container
name:  "quay.io/biocontainers/bioconductor-adductdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adductdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adductdata/container.yaml"
updated_at: "2024-08-22 20:11:49.458032"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-adductdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-adductdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adductdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-adductdata", "latest": {"1.18.0--r43hdfd78af_0": "sha256:36cca7c2238682f715e24157360fef15eff4807ed38f7ce7a11aea35ed9a032a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:0d2cae4c422e50a69db28d99bda2edf5ae9b112cc6260500c70d83361b770a60", "1.14.0--r42hdfd78af_0": "sha256:0e0a0de22cd4d56ef44ddbbf05a6b9567fd8ab41884c89f1223a3832fc44ba64", "1.10.0--r41hdfd78af_1": "sha256:d86fde138d2fdb6b5e793d8324897a962ba80cc6938f5aa90a8ea17f13722db2", "1.16.0--r43hdfd78af_0": "sha256:5d315016886e0544864434cd47252661dc029bc8a3e1fe69246c4d0747d793a5", "1.18.0--r43hdfd78af_0": "sha256:36cca7c2238682f715e24157360fef15eff4807ed38f7ce7a11aea35ed9a032a"}, "docker": "quay.io/biocontainers/bioconductor-adductdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adductdata.
shpc-registry automated BioContainers addition for bioconductor-adductdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adductdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adductdata:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adductdata/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-adductdata/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adductdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adductdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adductdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adductdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adductdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adductdata-inspect-deffile:

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