---
layout: container
name:  "quay.io/biocontainers/bioconductor-ctrap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ctrap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ctrap/container.yaml"
updated_at: "2024-02-09 03:33:14.271126"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ctrap"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ctrap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ctrap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ctrap", "latest": {"1.20.0--r43hdfd78af_0": "sha256:e8d68366a232e3f198e99538371943db3d510c97b0773370824aa1619cc7343b"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:4caaf1bc57b6f492dbf92bbd654d6d0723ace99116c1d72090ddb432f6b0102b", "1.16.0--r42hdfd78af_0": "sha256:157cc91f356c64bd75d94ada2b468c084c714ff7a56936e0b51e41110629d3d5", "1.12.0--r41hdfd78af_0": "sha256:d4a74d6059e03e71b1fc2a82c0e8530b390e297d23dfd1ece029ea78979431a8", "1.10.0--r41hdfd78af_0": "sha256:278e68d4f41d8e45d3a301086c150cd8188d3c31521ce0b3ade82bbe4b09219c", "1.18.0--r43hdfd78af_0": "sha256:291f4820ef73318a0d4b28252c7ec41031c717a97b8121fcd9efced52c4fbd41", "1.20.0--r43hdfd78af_0": "sha256:e8d68366a232e3f198e99538371943db3d510c97b0773370824aa1619cc7343b"}, "docker": "quay.io/biocontainers/bioconductor-ctrap", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ctrap.
shpc-registry automated BioContainers addition for bioconductor-ctrap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ctrap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ctrap:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ctrap/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ctrap/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ctrap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctrap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctrap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ctrap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ctrap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ctrap-inspect-deffile:

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