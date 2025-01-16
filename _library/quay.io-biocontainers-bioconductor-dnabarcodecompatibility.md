---
layout: container
name:  "quay.io/biocontainers/bioconductor-dnabarcodecompatibility"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dnabarcodecompatibility/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dnabarcodecompatibility/container.yaml"
updated_at: "2025-01-16 03:27:13.763484"
latest: "1.22.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dnabarcodecompatibility"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dnabarcodecompatibility"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dnabarcodecompatibility", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dnabarcodecompatibility", "latest": {"1.22.0--r44he5774e6_0": "sha256:1fa062065847178696f7b28ea71e0a3f60e72d765470a36b5a22b693d160a63c"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:ca15e279d05f7933c34b8a073ddc86c680da31a6eda83d4aa9942e3d540d120a", "1.14.0--r42hdfd78af_0": "sha256:19dabcf77222e4936d317c8b26dfcb01a6da5028cc1428b5782652291da16b17", "1.10.0--r41hdfd78af_0": "sha256:cedc8bed43f9bfe0ed05fa318278472a7f616f5170f7233860bfd754a2b856d8", "1.16.0--r43hdfd78af_0": "sha256:f505f0fc4c227ac5ddff7db4abfcbaf915e3f99a44853ac03344b7e1f417a463", "1.18.0--r43hdfd78af_0": "sha256:dc3b2fccc6c0ac5998c4eeaec4d496bbe661693061d5744d911152c3107a4d82", "1.22.0--r44he5774e6_0": "sha256:1fa062065847178696f7b28ea71e0a3f60e72d765470a36b5a22b693d160a63c"}, "docker": "quay.io/biocontainers/bioconductor-dnabarcodecompatibility", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dnabarcodecompatibility.
shpc-registry automated BioContainers addition for bioconductor-dnabarcodecompatibility
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dnabarcodecompatibility
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dnabarcodecompatibility:1.22.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dnabarcodecompatibility/1.22.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-dnabarcodecompatibility/1.22.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dnabarcodecompatibility-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dnabarcodecompatibility-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dnabarcodecompatibility-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dnabarcodecompatibility-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dnabarcodecompatibility-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dnabarcodecompatibility-inspect-deffile:

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