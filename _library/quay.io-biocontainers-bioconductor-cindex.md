---
layout: container
name:  "quay.io/biocontainers/bioconductor-cindex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cindex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cindex/container.yaml"
updated_at: "2024-03-23 02:54:49.125106"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cindex"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cindex"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cindex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cindex", "latest": {"1.30.0--r43hdfd78af_0": "sha256:b89cf91a53666224850d3dad7bb704642e9a08eeaff84e0e62fdd33925729886"}, "tags": {"1.8.0--r351_0": "sha256:6df66f2813ab9dbca4629a7c6f547f1bf1179d8638cf0849e6527679f82328d0", "1.26.0--r42hdfd78af_0": "sha256:243da5ab680bcf3624bc3ae9b14bf7a0522971b6af9398a0ffb09373dbf90ef7", "1.22.0--r41hdfd78af_0": "sha256:3835c7c7033853c46e44fb22f90e2de7ae8faec646f9f1f12cc32638e63e5d1c", "1.20.0--r41hdfd78af_0": "sha256:a2659653fc8cd35c01f1409ee553ce5f0d27fb75ee72cbaa5942109914422e9e", "1.18.0--r40hdfd78af_1": "sha256:4266ab83c62a80059f5315c439dee2f3faf354b86055e4718572f1f68be4cda3", "1.16.0--r40_0": "sha256:1d1c9fd3eac12aa43451b93c812a01ce3aadcad48125559c3223620eb4802fa5", "1.28.0--r43hdfd78af_0": "sha256:33ed4c507b1d1d277646d18ca6c697b4046156d4e76600c5e71b245c7ad74a0d", "1.30.0--r43hdfd78af_0": "sha256:b89cf91a53666224850d3dad7bb704642e9a08eeaff84e0e62fdd33925729886"}, "docker": "quay.io/biocontainers/bioconductor-cindex", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cindex.
shpc-registry automated BioContainers addition for bioconductor-cindex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cindex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cindex:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cindex/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cindex/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cindex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cindex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cindex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cindex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cindex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cindex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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