---
layout: container
name:  "quay.io/biocontainers/bioconductor-qpgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qpgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qpgraph/container.yaml"
updated_at: "2024-11-01 03:39:33.339196"
latest: "2.36.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-qpgraph"

versions:
 - "2.28.2--r41hc0cfd56_0"
 - "2.32.0--r42hc0cfd56_0"
 - "2.32.0--r42ha9d7317_1"
 - "2.34.2--r43ha9d7317_0"
 - "2.36.0--r43ha9d7317_0"
 - "2.36.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-qpgraph"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qpgraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qpgraph", "latest": {"2.36.0--r43ha9d7317_1": "sha256:b84f1fb46e9031e7ede17184b1790fa31f2df86582c6d295de4e81810298b1f6"}, "tags": {"2.28.2--r41hc0cfd56_0": "sha256:18fb1092f84b0cc109752555579b89973af1b33dbf16edb5aec874cc85b1da9e", "2.32.0--r42hc0cfd56_0": "sha256:501140b6cf1a67e2afde2d9cce227568a724e9b981abb14c2771887542a92251", "2.32.0--r42ha9d7317_1": "sha256:b5389b0febd95529d99cc63986745163e10bcf48e46a6644fe7b5ef804b63200", "2.34.2--r43ha9d7317_0": "sha256:4198cbe8cab6e9365968adc29e9282df1f4e123c7eb93f931ea5423a3cc634f6", "2.36.0--r43ha9d7317_0": "sha256:c2a7417bc4fdf3571c3f9f4b0039bd16848187cb5d03258ccc1a509d88cfbc9b", "2.36.0--r43ha9d7317_1": "sha256:b84f1fb46e9031e7ede17184b1790fa31f2df86582c6d295de4e81810298b1f6"}, "docker": "quay.io/biocontainers/bioconductor-qpgraph"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qpgraph.
shpc-registry automated BioContainers addition for bioconductor-qpgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qpgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qpgraph:2.36.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qpgraph/2.36.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-qpgraph/2.36.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qpgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qpgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qpgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qpgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qpgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qpgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-qpgraph

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