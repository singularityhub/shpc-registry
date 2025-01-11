---
layout: container
name:  "quay.io/biocontainers/bioconductor-tfbstools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tfbstools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tfbstools/container.yaml"
updated_at: "2025-01-11 03:16:01.262893"
latest: "1.40.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-tfbstools"

versions:
 - "1.32.0--r41hc0cfd56_2"
 - "1.36.0--r42hc0cfd56_0"
 - "1.36.0--r42ha9d7317_1"
 - "1.38.0--r43ha9d7317_0"
 - "1.40.0--r43ha9d7317_0"
 - "1.40.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-tfbstools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tfbstools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tfbstools", "latest": {"1.40.0--r43ha9d7317_1": "sha256:9412260c85cf56def46cd80d8f16afdb5227c04fdaf7a63160d160940ad5c14d"}, "tags": {"1.32.0--r41hc0cfd56_2": "sha256:7b14058c71f3b8e599e2e44fafe43827f89e8b77a073af14d301bb3039bb8fd6", "1.36.0--r42hc0cfd56_0": "sha256:9135ff6d48db4f7faf3a7f7a5e7c72d32d2611ba6f19d821e1bbf47b17b1363a", "1.36.0--r42ha9d7317_1": "sha256:81f47222b23fcbd9dd5a3613d03998e997990287a4037c3f51ecd823f77c7456", "1.38.0--r43ha9d7317_0": "sha256:c4286af2167eb22bd5ffaa1a6972e0d2d92025c2007ca4ac1a0243c2996531ad", "1.40.0--r43ha9d7317_0": "sha256:e3ab64e301f7a6bc13a59e9b93fd18f35c18a01736f3e37b8bc86f8e4a586f26", "1.40.0--r43ha9d7317_1": "sha256:9412260c85cf56def46cd80d8f16afdb5227c04fdaf7a63160d160940ad5c14d"}, "docker": "quay.io/biocontainers/bioconductor-tfbstools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tfbstools.
shpc-registry automated BioContainers addition for bioconductor-tfbstools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tfbstools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tfbstools:1.40.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tfbstools/1.40.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-tfbstools/1.40.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tfbstools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfbstools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfbstools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tfbstools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tfbstools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tfbstools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tfbstools

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