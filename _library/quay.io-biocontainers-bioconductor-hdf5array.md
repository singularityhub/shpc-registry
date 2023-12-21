---
layout: container
name:  "quay.io/biocontainers/bioconductor-hdf5array"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hdf5array/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hdf5array/container.yaml"
updated_at: "2023-12-21 02:42:45.777161"
latest: "1.30.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hdf5array"

versions:
 - "1.8.1--r351_0"
 - "1.26.0--r42h171f361_1"
 - "1.22.1--r41hc0cfd56_1"
 - "1.20.0--r41ha2fdcc6_1"
 - "1.18.1--r40hd029910_0"
 - "1.16.0--r40h037d062_0"
 - "1.26.0--r42h58c1800_2"
 - "1.28.1--r43ha9d7317_0"
 - "1.30.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hdf5array"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hdf5array", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hdf5array", "latest": {"1.30.0--r43ha9d7317_0": "sha256:81ea2296993670912f98f80ab3fe24143d04b60267ed26386376c98180e6f64e"}, "tags": {"1.8.1--r351_0": "sha256:4e27f447a5b20ea3799aaed016ff2733a5369820db29480abc48a3729e8382b0", "1.26.0--r42h171f361_1": "sha256:5ba35f6bbd5e85eb668105a6b83b44a4552a5918e61b8cad4f73b34b0cb440be", "1.22.1--r41hc0cfd56_1": "sha256:c742438075e837da0a76fc0a516697f4a2a7be998d58d105c541117719cb043a", "1.20.0--r41ha2fdcc6_1": "sha256:7c567bb7ad91c6b5ac19c8f90f5078831e892b31fb750b7f1d9219c4b1d797fc", "1.18.1--r40hd029910_0": "sha256:c620fb25254d5a79766eebc8454859665c5b6668fc83ecad8befb757efdfbfb2", "1.16.0--r40h037d062_0": "sha256:b2b0d190627aaf6c0df60fac5cd112249a0745c2b48f6ae66f6f177e11bdef17", "1.26.0--r42h58c1800_2": "sha256:2f3d64907bbc563659d8adc9a53f5b364b742f96c3869bce6a352f189f705434", "1.28.1--r43ha9d7317_0": "sha256:ec6b6d755f28ddab3a818c6e5e6fd3a4b5d22b78be67319bd46a868f8046d427", "1.30.0--r43ha9d7317_0": "sha256:81ea2296993670912f98f80ab3fe24143d04b60267ed26386376c98180e6f64e"}, "docker": "quay.io/biocontainers/bioconductor-hdf5array"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hdf5array.
shpc-registry automated BioContainers addition for bioconductor-hdf5array
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hdf5array
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hdf5array:1.30.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hdf5array/1.30.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-hdf5array/1.30.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hdf5array-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hdf5array-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hdf5array-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hdf5array-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hdf5array-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hdf5array-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hdf5array

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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