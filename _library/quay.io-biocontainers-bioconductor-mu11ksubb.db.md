---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu11ksubb.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu11ksubb.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu11ksubb.db/container.yaml"
updated_at: "2026-01-01 07:52:16.191545"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mu11ksubb.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mu11ksubb.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu11ksubb.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu11ksubb.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:f8d4247285a16cc6ecc0f6e9309880055d4c1117387c9e81e57a9093e36f3b6f"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:f9baa109ee4cc23fe5a21a1ba62db95ece9b0ca5ede1e62bb2d5f8fb4eeeb924", "3.13.0--r42hdfd78af_2": "sha256:263705653178ac2484aa95a64056d3867e830be633a94d2be701701c4bf67265", "3.13.0--r43hdfd78af_3": "sha256:f481393fbbbd9fa1a2cca23ba9854afc91293f48061c4e45e645558fe120c3e6", "3.13.0--r43hdfd78af_4": "sha256:45f9d4ecc913c388bb89d7b41937ffeda9afde57587cc0d2bb33166f19fdfef2", "3.13.0--r44hdfd78af_5": "sha256:f8d4247285a16cc6ecc0f6e9309880055d4c1117387c9e81e57a9093e36f3b6f"}, "docker": "quay.io/biocontainers/bioconductor-mu11ksubb.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu11ksubb.db.
shpc-registry automated BioContainers addition for bioconductor-mu11ksubb.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubb.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubb.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu11ksubb.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mu11ksubb.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu11ksubb.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubb.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubb.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu11ksubb.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu11ksubb.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu11ksubb.db-inspect-deffile:

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