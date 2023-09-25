---
layout: container
name:  "quay.io/biocontainers/bioconductor-correp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-correp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-correp/container.yaml"
updated_at: "2023-09-25 03:12:24.388088"
latest: "1.66.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-correp"

versions:
 - "1.60.0--r41hdfd78af_0"
 - "1.64.0--r42hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-correp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-correp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-correp", "latest": {"1.66.0--r43hdfd78af_0": "sha256:20fd214792ab00f8b843383324c90c3346bec6803441a6bf61a21dd35d73b9c2"}, "tags": {"1.60.0--r41hdfd78af_0": "sha256:7819421d528af2e441b8e88bf8fa4ff50e2d98b611c86a37f401f5c11c4deb9a", "1.64.0--r42hdfd78af_0": "sha256:94734a46ec13e45e5dbe40a7f5256f822a299487b353a537b57da227c593afb0", "1.66.0--r43hdfd78af_0": "sha256:20fd214792ab00f8b843383324c90c3346bec6803441a6bf61a21dd35d73b9c2"}, "docker": "quay.io/biocontainers/bioconductor-correp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-correp.
shpc-registry automated BioContainers addition for bioconductor-correp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-correp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-correp:1.66.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-correp/1.66.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-correp/1.66.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-correp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-correp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-correp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-correp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-correp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-correp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-correp

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