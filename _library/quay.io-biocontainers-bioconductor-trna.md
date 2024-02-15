---
layout: container
name:  "quay.io/biocontainers/bioconductor-trna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trna/container.yaml"
updated_at: "2024-02-15 03:33:12.215995"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trna"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trna", "latest": {"1.20.0--r43hdfd78af_0": "sha256:7c20dce8c4bcac45a3d9d12fc7c1fba86df76e2975aa94573d6b49ea9820aad5"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:26e16a7d74888fc0036e7bc22560d1c5e752b5335b55c4a04364d2c5ba02e9c8", "1.16.0--r42hdfd78af_0": "sha256:535e629ebaf54598ef9dd86cfbd8249d0c606c7c58e5494ffde7b1c8e72e62d8", "1.12.0--r41hdfd78af_0": "sha256:9e58abf2f25a875c1220616c317191801a450aa6ba5d865aeef32e27a98b9857", "1.10.0--r41hdfd78af_0": "sha256:2b39b6895dd5c7ee40d6e6b34842840b0cdfa7aff2f5d27bc840b3b861ffd292", "1.18.0--r43hdfd78af_0": "sha256:9dbef919143faf972b28f66a2d4193a005843702839a26e202400e7cbf35172b", "1.20.0--r43hdfd78af_0": "sha256:7c20dce8c4bcac45a3d9d12fc7c1fba86df76e2975aa94573d6b49ea9820aad5"}, "docker": "quay.io/biocontainers/bioconductor-trna", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trna.
shpc-registry automated BioContainers addition for bioconductor-trna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trna:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trna/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trna/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trna-inspect-deffile:

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