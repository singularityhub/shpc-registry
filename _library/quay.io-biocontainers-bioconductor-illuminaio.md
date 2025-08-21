---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminaio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminaio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminaio/container.yaml"
updated_at: "2025-08-21 06:51:05.339253"
latest: "0.48.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminaio"

versions:
 - "0.36.0--r41hc0cfd56_2"
 - "0.40.0--r42hc0cfd56_0"
 - "0.40.0--r42ha9d7317_2"
 - "0.42.0--r43ha9d7317_0"
 - "0.44.0--r43ha9d7317_1"
 - "0.44.0--r43ha9d7317_2"
 - "0.48.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminaio"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminaio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminaio", "latest": {"0.48.0--r44h3df3fcb_0": "sha256:157ea9d335f42b247320f75f6feb1b1341d8d3d96d915d970299fc3f36edaa04"}, "tags": {"0.36.0--r41hc0cfd56_2": "sha256:9efc92f2fa72f18d6533e4ab7038eb611a548d2da10167cc44edcb0293b1e13b", "0.40.0--r42hc0cfd56_0": "sha256:6f9edfc017010bfc81b395869829915e6e8cb7f3584470b85440672210f36057", "0.40.0--r42ha9d7317_2": "sha256:049d5ee73cc527fcca0e61e5006e955b6f6533f01496163124729759e1df8478", "0.42.0--r43ha9d7317_0": "sha256:efef46e964fa3e8aa37a8b45cf545fe18e7f4ec138ea4a3e7424a482c2b7ec69", "0.44.0--r43ha9d7317_1": "sha256:518c8fd7805759045ee2775d99d25856a530c5ac9135d6ace2f1a71d58ed512d", "0.44.0--r43ha9d7317_2": "sha256:71926b4b2ff4c56bf860304d451411a41c5bd95539700c04b31768055b673c13", "0.48.0--r44h3df3fcb_0": "sha256:157ea9d335f42b247320f75f6feb1b1341d8d3d96d915d970299fc3f36edaa04"}, "docker": "quay.io/biocontainers/bioconductor-illuminaio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminaio.
shpc-registry automated BioContainers addition for bioconductor-illuminaio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminaio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminaio:0.48.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminaio/0.48.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-illuminaio/0.48.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminaio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminaio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminaio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminaio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminaio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminaio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminaio

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