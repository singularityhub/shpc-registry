---
layout: container
name:  "quay.io/biocontainers/bioconductor-synmut"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-synmut/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-synmut/container.yaml"
updated_at: "2024-05-20 03:08:50.791993"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-synmut"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-synmut"
config: {"url": "https://biocontainers.pro/tools/bioconductor-synmut", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-synmut", "latest": {"1.18.0--r43hdfd78af_0": "sha256:a1db92d09f6be635152c372ff7a45a2cbba656d29b6eee57a19741090de82af6"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:379d55f88d0f53925b07ccfc075ef03fd3b3c03ead317e576db61f313c97756c", "1.14.0--r42hdfd78af_0": "sha256:6aef673ae541b62c3108e258eb0049efd23d444a07efa64f82f2910cd28e0a9d", "1.10.0--r41hdfd78af_0": "sha256:7a6f63fc0ec1835aa29d57c116616997bbaab9dc544604ac52f551501abc273c", "1.16.0--r43hdfd78af_0": "sha256:f5f20dfe27031a8884a916288373abf4acbc054280fef815549eecc0e6a5fa6e", "1.18.0--r43hdfd78af_0": "sha256:a1db92d09f6be635152c372ff7a45a2cbba656d29b6eee57a19741090de82af6"}, "docker": "quay.io/biocontainers/bioconductor-synmut", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-synmut.
shpc-registry automated BioContainers addition for bioconductor-synmut
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-synmut
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-synmut:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-synmut/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-synmut/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-synmut-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synmut-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synmut-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-synmut-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-synmut-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-synmut-inspect-deffile:

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