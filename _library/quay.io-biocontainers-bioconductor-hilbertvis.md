---
layout: container
name:  "quay.io/biocontainers/bioconductor-hilbertvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hilbertvis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hilbertvis/container.yaml"
updated_at: "2025-05-24 03:47:01.244101"
latest: "1.64.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hilbertvis"

versions:
 - "1.52.0--r41hc0cfd56_2"
 - "1.56.0--r42hc0cfd56_0"
 - "1.56.0--r42ha9d7317_2"
 - "1.58.0--r43ha9d7317_0"
 - "1.60.0--r43ha9d7317_1"
 - "1.60.0--r43ha9d7317_2"
 - "1.60.0--r43ha9d7317_3"
 - "1.64.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hilbertvis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hilbertvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hilbertvis", "latest": {"1.64.0--r44h3df3fcb_0": "sha256:c6edb089985a478d077b9ff3b092e3bcc1d7f4634cdea998876ef4ebb50fb85c"}, "tags": {"1.52.0--r41hc0cfd56_2": "sha256:19a62d20181ee7ac020ca946c2dacf60b179034ac48f95b5fe08c24f9d9942c8", "1.56.0--r42hc0cfd56_0": "sha256:5deea6811e2f1b16c907fd859a7ca6d06c7d8625c212ef25610babe1b4141ed7", "1.56.0--r42ha9d7317_2": "sha256:4e3ae7dea88c618a760468cfd8ff8d05d3b8175d35b14921aead54020e5aea0e", "1.58.0--r43ha9d7317_0": "sha256:dcc6ce407f7225bba54b1733707f5524c986137134f73989d03cc8d9c2c35401", "1.60.0--r43ha9d7317_1": "sha256:f50a91ceee00220c20f727924086ac8f4704e788f9ed70506b8387aa2422c0dc", "1.60.0--r43ha9d7317_2": "sha256:3a49279eb8e8626623bafce71f9b56f7e10ee39bf0db2e76dbc7556dd2bb3fd8", "1.60.0--r43ha9d7317_3": "sha256:4fc39d7e5864d4ce009b0e562fa81fbaca61412800b07e96ac33fc8b52910277", "1.64.0--r44h3df3fcb_0": "sha256:c6edb089985a478d077b9ff3b092e3bcc1d7f4634cdea998876ef4ebb50fb85c"}, "docker": "quay.io/biocontainers/bioconductor-hilbertvis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hilbertvis.
shpc-registry automated BioContainers addition for bioconductor-hilbertvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hilbertvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hilbertvis:1.64.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hilbertvis/1.64.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-hilbertvis/1.64.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hilbertvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hilbertvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hilbertvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hilbertvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hilbertvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hilbertvis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hilbertvis

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