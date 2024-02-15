---
layout: container
name:  "quay.io/biocontainers/bioconductor-erma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-erma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-erma/container.yaml"
updated_at: "2024-02-15 03:22:44.223048"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-erma"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-erma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-erma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-erma", "latest": {"1.18.0--r43hdfd78af_0": "sha256:d38591bafa81c1d6d7c305ee17a83b04ba241c324f52c5a21b08b74bb8fbdac3"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:4d6b1d1b47feecb063df3f2ff8ee0fbca8eb879904d79bf3bef12b7653e18dc7", "1.10.0--r41hdfd78af_0": "sha256:8744d5f2145f02ed8df0502072cb70ec288ee1348416d10e635ec46654fb38a2", "1.14.0--r42hdfd78af_0": "sha256:5b47248c9d2ab58471fd6608920c11576ccaf135f5c43ad665979100ee51b99f", "1.16.0--r43hdfd78af_0": "sha256:11922be55dddea7b5104265f4a1607b646945ec56378ceb32df5bb1a5232659b", "1.18.0--r43hdfd78af_0": "sha256:d38591bafa81c1d6d7c305ee17a83b04ba241c324f52c5a21b08b74bb8fbdac3"}, "docker": "quay.io/biocontainers/bioconductor-erma", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-erma.
shpc-registry automated BioContainers addition for bioconductor-erma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-erma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-erma:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-erma/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-erma/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-erma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-erma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-erma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-erma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-erma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-erma-inspect-deffile:

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