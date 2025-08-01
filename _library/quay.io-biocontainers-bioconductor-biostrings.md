---
layout: container
name:  "quay.io/biocontainers/bioconductor-biostrings"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biostrings/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biostrings/container.yaml"
updated_at: "2025-08-01 04:02:13.817670"
latest: "2.74.0--r44h3df3fcb_1"
container_url: "https://biocontainers.pro/tools/bioconductor-biostrings"

versions:
 - "2.62.0--r41hc0cfd56_2"
 - "2.66.0--r42ha9d7317_1"
 - "2.68.1--r43ha9d7317_0"
 - "2.70.1--r43ha9d7317_1"
 - "2.70.1--r43ha9d7317_2"
 - "2.74.0--r44h3df3fcb_0"
 - "2.74.0--r44h3df3fcb_1"
description: "shpc-registry automated BioContainers addition for bioconductor-biostrings"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biostrings", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biostrings", "latest": {"2.74.0--r44h3df3fcb_1": "sha256:64436a372e8bde3cfa7398b45b4fc596ad208e7b066767daa99661d36d0990a3"}, "tags": {"2.62.0--r41hc0cfd56_2": "sha256:38a4ef4ef521d979079946abc64b32a68ae0ffced7c4174cfc6c8df2a7026473", "2.66.0--r42ha9d7317_1": "sha256:5a30715087643148d41b2d599d67b6690f2f7e20580bebc4ade439c6a7016cf7", "2.68.1--r43ha9d7317_0": "sha256:d0ef41fcb1bb394b604cb1bc485141fd41359d50ac67e97433e037bf564a960b", "2.70.1--r43ha9d7317_1": "sha256:e05faadf46356026a96243641aa1798113538cd4ad1eeddd1423fb6794de89a5", "2.70.1--r43ha9d7317_2": "sha256:f22854008dc80c64f7142713407f424523a7180550dab7d9781391ef49e0bb86", "2.74.0--r44h3df3fcb_0": "sha256:3894d358fb5156ce4995d9e0ce6f341bd3dc825ceaf4942ee16f1df6c4a28fbe", "2.74.0--r44h3df3fcb_1": "sha256:64436a372e8bde3cfa7398b45b4fc596ad208e7b066767daa99661d36d0990a3"}, "docker": "quay.io/biocontainers/bioconductor-biostrings"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biostrings.
shpc-registry automated BioContainers addition for bioconductor-biostrings
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biostrings
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biostrings:2.74.0--r44h3df3fcb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biostrings/2.74.0--r44h3df3fcb_1
$ module help quay.io/biocontainers/bioconductor-biostrings/2.74.0--r44h3df3fcb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biostrings-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biostrings-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biostrings-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biostrings-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biostrings-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biostrings-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biostrings

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