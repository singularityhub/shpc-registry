---
layout: container
name:  "quay.io/biocontainers/bioconductor-isocorrectorgui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-isocorrectorgui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-isocorrectorgui/container.yaml"
updated_at: "2024-03-20 02:42:49.607871"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-isocorrectorgui"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-isocorrectorgui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-isocorrectorgui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-isocorrectorgui", "latest": {"1.18.0--r43hdfd78af_0": "sha256:d4b188bff7363ff3c50a8d4b589199ed4038c9ea835482404d1964e661272f0e"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:45b38cd2971442c6941f656e325a09c1ba252b4075da960d28ff7d9358ff6157", "1.14.0--r42hdfd78af_0": "sha256:3b8c16e939e7d8d903e9db6f6068cc1852bf954da2d0c4c31db370b810232360", "1.10.0--r41hdfd78af_0": "sha256:985f1717b15ed38ab143f3afe2f0e1acde0c21eb0bfd8b4205f3b0b4fae1e517", "1.16.0--r43hdfd78af_0": "sha256:4e80e3d2ab590537309c11510d5e59b2b95a74323edf0f29f989aa22fdecf15f", "1.18.0--r43hdfd78af_0": "sha256:d4b188bff7363ff3c50a8d4b589199ed4038c9ea835482404d1964e661272f0e"}, "docker": "quay.io/biocontainers/bioconductor-isocorrectorgui", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-isocorrectorgui.
shpc-registry automated BioContainers addition for bioconductor-isocorrectorgui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-isocorrectorgui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-isocorrectorgui:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-isocorrectorgui/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-isocorrectorgui/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-isocorrectorgui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isocorrectorgui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isocorrectorgui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-isocorrectorgui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-isocorrectorgui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-isocorrectorgui-inspect-deffile:

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