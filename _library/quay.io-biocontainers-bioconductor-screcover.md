---
layout: container
name:  "quay.io/biocontainers/bioconductor-screcover"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-screcover/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-screcover/container.yaml"
updated_at: "2023-09-04 04:10:19.505609"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-screcover"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.13.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-screcover"
config: {"url": "https://biocontainers.pro/tools/bioconductor-screcover", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-screcover", "latest": {"1.16.0--r43hdfd78af_0": "sha256:c22fcab57ffa50a86688f51d812c1ca1743800af1501ebbe75c9418d78321912"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a9c4cbbb53c78b7bbfc8f06f0aeb9de38091e2ea814242b9b7566e55bed507c4", "1.13.0--r42hdfd78af_0": "sha256:8d2ba1f67f8479da01a0640812b7327fcbbec5ab96b2d00f9fcc422f474ddb92", "1.10.0--r41hdfd78af_0": "sha256:a17a99c8dfce4c3167606bd0234d332748a3fcc5c54353f805c8e5ab682cd828", "1.16.0--r43hdfd78af_0": "sha256:c22fcab57ffa50a86688f51d812c1ca1743800af1501ebbe75c9418d78321912"}, "docker": "quay.io/biocontainers/bioconductor-screcover", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-screcover.
shpc-registry automated BioContainers addition for bioconductor-screcover
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-screcover
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-screcover:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-screcover/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-screcover/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-screcover-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screcover-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screcover-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-screcover-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-screcover-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-screcover-inspect-deffile:

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