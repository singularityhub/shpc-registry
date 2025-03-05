---
layout: container
name:  "quay.io/biocontainers/bioconductor-decipher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-decipher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-decipher/container.yaml"
updated_at: "2025-03-05 03:39:08.637774"
latest: "3.2.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-decipher"

versions:
 - "2.8.1--r351h470a237_0"
 - "2.26.0--r42hc0cfd56_0"
 - "2.22.0--r41hc0cfd56_2"
 - "2.20.0--r41hd029910_0"
 - "2.18.1--r40hd029910_0"
 - "2.16.0--r40h037d062_0"
 - "2.26.0--r42ha9d7317_1"
 - "2.28.0--r43ha9d7317_0"
 - "2.30.0--r43ha9d7317_0"
 - "2.30.0--r43ha9d7317_1"
 - "3.2.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-decipher"
config: {"url": "https://biocontainers.pro/tools/bioconductor-decipher", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-decipher", "latest": {"3.2.0--r44h3df3fcb_0": "sha256:1911b48b7b82d821fbdbfbdef0c5dd640dc945c94d84d618502763b768fcbfeb"}, "tags": {"2.8.1--r351h470a237_0": "sha256:3635172330f8bafce5894111fb0ef15d78ee0b777dbb6d530cf5995dd8a9a786", "2.26.0--r42hc0cfd56_0": "sha256:f530b5a51cfe81b40302ec8aaf7bedb4899675df6c82d99dacd3f642e0a2317a", "2.22.0--r41hc0cfd56_2": "sha256:4c163b7d3a021c7b9d8898f76770708e504130c42452e19ba0d1808acef226a9", "2.20.0--r41hd029910_0": "sha256:59a295ceafe6eb665bacadc0a999c218eb6a1c4a0fb3f22c75e773fd4b988337", "2.18.1--r40hd029910_0": "sha256:607916366c78040b5cc3f7eb976664f1d573dd97393ea1d2919cfea5c8b2513b", "2.16.0--r40h037d062_0": "sha256:73d0eaf1d2d22e481edf2f754b6b46114cfa6613c77801f2dbb6e2edb972c9e5", "2.26.0--r42ha9d7317_1": "sha256:4b02a88c64614d6e2b3bb4ad5e54e1d3510cc8168e31cc59b37c7bb302c2d311", "2.28.0--r43ha9d7317_0": "sha256:b961fe3a13d00d4d34c8d6fc0a752114abcef32939336c459d623092af94c0fa", "2.30.0--r43ha9d7317_0": "sha256:c83040bf1952ef77b4a305a88223188a3d2678e3f274f57df6c30d7f216a8c89", "2.30.0--r43ha9d7317_1": "sha256:458b197ba4e074092c0c0c93cea3bae9bb7d58f2bf8c4f4968442df9f546351a", "3.2.0--r44h3df3fcb_0": "sha256:1911b48b7b82d821fbdbfbdef0c5dd640dc945c94d84d618502763b768fcbfeb"}, "docker": "quay.io/biocontainers/bioconductor-decipher"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-decipher.
shpc-registry automated BioContainers addition for bioconductor-decipher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-decipher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-decipher:3.2.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-decipher/3.2.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-decipher/3.2.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-decipher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-decipher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-decipher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-decipher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-decipher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-decipher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-decipher

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