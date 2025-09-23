---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95av2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95av2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95av2.db/container.yaml"
updated_at: "2025-09-23 04:50:57.524861"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95av2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r40hdfd78af_9"
 - "3.13.0--r42hdfd78af_2"
 - "3.2.3--r41hdfd78af_10"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95av2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95av2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95av2.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:76a55f95cade5293afd25aa83019d540badf079737288699bbad1c13097ab754"}, "tags": {"3.2.3--r40hdfd78af_9": "sha256:ec64af06a04e1093f22fa464c9c77e69b023ecd0cdf0c54a90682bb35076f2fc", "3.13.0--r42hdfd78af_2": "sha256:88ed92b7492444a5831807d523fc0adb759f29ee209f6bd8e58e74b987ad26ef", "3.2.3--r41hdfd78af_10": "sha256:ab0a4fe74f0f047c8c9c18ad8bd92dc5dce8e5005524fc462a6de7e4189f8658", "3.13.0--r43hdfd78af_3": "sha256:d847a91bf4cdd10d676e72173764de09af6539a977ca7e31d7788545d9e97fd9", "3.13.0--r43hdfd78af_4": "sha256:3fe4909b7cbd33a9a96dd70886567cf9f00ba740b01c8c16a2a31f73bb9c650a", "3.13.0--r44hdfd78af_5": "sha256:76a55f95cade5293afd25aa83019d540badf079737288699bbad1c13097ab754"}, "docker": "quay.io/biocontainers/bioconductor-hgu95av2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95av2.db.
shpc-registry automated BioContainers addition for bioconductor-hgu95av2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95av2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95av2.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95av2.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-hgu95av2.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95av2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95av2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95av2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95av2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95av2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95av2.db-inspect-deffile:

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