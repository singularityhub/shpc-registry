---
layout: container
name:  "quay.io/biocontainers/bioconductor-omicspcadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omicspcadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omicspcadata/container.yaml"
updated_at: "2024-07-05 02:42:52.496154"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-omicspcadata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-omicspcadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omicspcadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-omicspcadata", "latest": {"1.20.0--r43hdfd78af_0": "sha256:4d663a469fb04b84b9e5f0abc1e7692ceafa5723be91982c9ea89bdff60c35a7"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:6fbd4674fde033f244d586630f4cde857aef8d58c01db5bd2057601487ecde56", "1.16.0--r42hdfd78af_0": "sha256:4bed0b2f55b0ee40b81c0acd697edd64dc6415664d0e0dabbfe7e78de89a1f37", "1.12.0--r41hdfd78af_1": "sha256:173045b04c8e965e971df392261fb66d3b745383b9449b3c300aa6a06862b7f3", "1.10.0--r41hdfd78af_0": "sha256:002907838ea860ce5df3c0aab02518e24c6b5de4c91ef1cce4130df19629c047", "1.18.0--r43hdfd78af_0": "sha256:1ed87a6d7775ce426c1e9504f077c9c8e7b938b00a5ed2386b4822220fcc1af4", "1.20.0--r43hdfd78af_0": "sha256:4d663a469fb04b84b9e5f0abc1e7692ceafa5723be91982c9ea89bdff60c35a7"}, "docker": "quay.io/biocontainers/bioconductor-omicspcadata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omicspcadata.
shpc-registry automated BioContainers addition for bioconductor-omicspcadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omicspcadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omicspcadata:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omicspcadata/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-omicspcadata/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omicspcadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omicspcadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omicspcadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omicspcadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omicspcadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omicspcadata-inspect-deffile:

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