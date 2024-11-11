---
layout: container
name:  "quay.io/biocontainers/bioconductor-spikeli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spikeli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spikeli/container.yaml"
updated_at: "2024-11-11 03:22:35.330257"
latest: "2.62.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spikeli"

versions:
 - "2.54.0--r41hdfd78af_0"
 - "2.58.0--r42hdfd78af_0"
 - "2.60.0--r43hdfd78af_0"
 - "2.62.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spikeli"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spikeli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spikeli", "latest": {"2.62.0--r43hdfd78af_0": "sha256:1be99f451723d1040c01a3ade543ef4ee24a7a22a1fab08b80f3909458343107"}, "tags": {"2.54.0--r41hdfd78af_0": "sha256:93bb96bcbb331d11f56071a27a63e25ff1136b93aeee1fead3d08262080b4c29", "2.58.0--r42hdfd78af_0": "sha256:a69261648f7de1f0a2cc3e42fde2f4e935b853cf9f5345cc62d0f8855bc4b8b9", "2.60.0--r43hdfd78af_0": "sha256:cedddd519fdb21a6513b41d6131a009189cb06d2345d4ed761280aadb42bc7b6", "2.62.0--r43hdfd78af_0": "sha256:1be99f451723d1040c01a3ade543ef4ee24a7a22a1fab08b80f3909458343107"}, "docker": "quay.io/biocontainers/bioconductor-spikeli"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spikeli.
shpc-registry automated BioContainers addition for bioconductor-spikeli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spikeli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spikeli:2.62.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spikeli/2.62.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spikeli/2.62.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spikeli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spikeli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spikeli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spikeli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spikeli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spikeli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spikeli

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