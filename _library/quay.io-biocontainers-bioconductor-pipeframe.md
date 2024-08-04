---
layout: container
name:  "quay.io/biocontainers/bioconductor-pipeframe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pipeframe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pipeframe/container.yaml"
updated_at: "2024-08-04 03:11:37.492320"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pipeframe"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pipeframe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pipeframe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pipeframe", "latest": {"1.18.0--r43hdfd78af_0": "sha256:1ec5e9d0d0d94a6feedde05228e20782380f9e3f9ad7cd33d8b0feb3dd675077"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a4f15c26b109902bce1611a1d1c2a5a2bc0c837f45532123fdd42cc8890910e2", "1.14.0--r42hdfd78af_0": "sha256:6f41636d0900719215e5622392e2fda7fb29e5d11390d75e58972e52653ca7f6", "1.10.0--r41hdfd78af_0": "sha256:5cc2455dc1cf3299eb655ac3e3247aa414ab40dc9119b9d3222fd8f8be068184", "1.16.0--r43hdfd78af_0": "sha256:acc4acf0b7eb1447e4e18c98893a89fa29ca55b3c91edc2895f36575dfca6ef1", "1.18.0--r43hdfd78af_0": "sha256:1ec5e9d0d0d94a6feedde05228e20782380f9e3f9ad7cd33d8b0feb3dd675077"}, "docker": "quay.io/biocontainers/bioconductor-pipeframe", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pipeframe.
shpc-registry automated BioContainers addition for bioconductor-pipeframe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pipeframe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pipeframe:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pipeframe/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pipeframe/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pipeframe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pipeframe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pipeframe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pipeframe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pipeframe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pipeframe-inspect-deffile:

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