---
layout: container
name:  "quay.io/biocontainers/bioconductor-breakpointr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-breakpointr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-breakpointr/container.yaml"
updated_at: "2024-07-30 02:44:32.912758"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-breakpointr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-breakpointr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-breakpointr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-breakpointr", "latest": {"1.20.0--r43hdfd78af_0": "sha256:215ebe8d1104f244cd7d3393f69cd8e685b9ac57a38d302b047a1a11dcf05d46"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:50dcd0f9f3e2b19ba7db3c28190b443828878e2ecfc191767d4a5a67dc16d296", "1.16.0--r42hdfd78af_0": "sha256:738662e2583c4cb7a6ce903a0c94adc3f88d29637b3878c696d10d6871402fcb", "1.12.0--r41hdfd78af_0": "sha256:6cc6ff514c6e8894e04528eaebc51cececfc010f53c1d22a106084996bc503de", "1.10.0--r41hdfd78af_0": "sha256:e7ca174c28515c8ecbb20a984a84008bbd8de3ccdf4be358b956b70a794b947a", "1.20.0--r43hdfd78af_0": "sha256:215ebe8d1104f244cd7d3393f69cd8e685b9ac57a38d302b047a1a11dcf05d46"}, "docker": "quay.io/biocontainers/bioconductor-breakpointr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-breakpointr.
shpc-registry automated BioContainers addition for bioconductor-breakpointr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-breakpointr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-breakpointr:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-breakpointr/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-breakpointr/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-breakpointr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breakpointr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breakpointr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-breakpointr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-breakpointr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-breakpointr-inspect-deffile:

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