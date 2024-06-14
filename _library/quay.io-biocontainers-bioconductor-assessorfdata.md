---
layout: container
name:  "quay.io/biocontainers/bioconductor-assessorfdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-assessorfdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-assessorfdata/container.yaml"
updated_at: "2024-06-14 02:57:18.292308"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-assessorfdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-assessorfdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-assessorfdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-assessorfdata", "latest": {"1.20.0--r43hdfd78af_0": "sha256:31161e8fce3060ba830225af83bf49b2fc59e447dc070a4bf0b5b33134947f01"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:7b375210fa91081638cb05e654a39bd1070fe450f8d2c1c35abad6be1159f38d", "1.16.0--r42hdfd78af_0": "sha256:7e5d3c79dfb02d1f01ddd2efe4978ce3e0177fdd6c5e0efddf8799a2f196090a", "1.12.0--r41hdfd78af_1": "sha256:bb2957a01ae86c808d78368f7f6d5dd819273a64689c4923c6ee1d86400f2b9c", "1.10.0--r41hdfd78af_0": "sha256:d40f011b27b242aa448a01adc96584ae0c4a9ffec44757520c745147b7c0c54d", "1.18.0--r43hdfd78af_0": "sha256:c316c275f9417dfa6f3ea66797e4f56fc187082a65599ae1eec2f209e139c5e4", "1.20.0--r43hdfd78af_0": "sha256:31161e8fce3060ba830225af83bf49b2fc59e447dc070a4bf0b5b33134947f01"}, "docker": "quay.io/biocontainers/bioconductor-assessorfdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-assessorfdata.
shpc-registry automated BioContainers addition for bioconductor-assessorfdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-assessorfdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-assessorfdata:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-assessorfdata/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-assessorfdata/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-assessorfdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-assessorfdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-assessorfdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-assessorfdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-assessorfdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-assessorfdata-inspect-deffile:

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