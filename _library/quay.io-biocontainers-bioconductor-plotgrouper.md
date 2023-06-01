---
layout: container
name:  "quay.io/biocontainers/bioconductor-plotgrouper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plotgrouper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plotgrouper/container.yaml"
updated_at: "2023-06-01 03:25:45.635802"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-plotgrouper"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-plotgrouper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plotgrouper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plotgrouper", "latest": {"1.16.0--r42hdfd78af_0": "sha256:bbfdc7efcae99fa5714e642609f0318e65e82c74d5fccff5fd5023b7531ac2e4"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:8deff548cec9b68298a6fe70b72c8d69dad2b6c7491daf6204c023eb1709617c", "1.16.0--r42hdfd78af_0": "sha256:bbfdc7efcae99fa5714e642609f0318e65e82c74d5fccff5fd5023b7531ac2e4", "1.12.0--r41hdfd78af_0": "sha256:40eb0062260258d628b637cdf0f862a349c377a3543286d74d5e399cc73bab52", "1.10.0--r41hdfd78af_0": "sha256:1cad300d61fb636cad129a1d49dae4b4c2266eb60c5bd2d864a569ed2f693d5c"}, "docker": "quay.io/biocontainers/bioconductor-plotgrouper", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plotgrouper.
shpc-registry automated BioContainers addition for bioconductor-plotgrouper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plotgrouper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plotgrouper:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plotgrouper/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-plotgrouper/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plotgrouper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plotgrouper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plotgrouper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plotgrouper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plotgrouper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plotgrouper-inspect-deffile:

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