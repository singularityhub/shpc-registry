---
layout: container
name:  "quay.io/biocontainers/bioconductor-nparc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nparc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nparc/container.yaml"
updated_at: "2024-06-11 05:19:15.721366"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nparc"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nparc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nparc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nparc", "latest": {"1.14.0--r43hdfd78af_0": "sha256:cf9f72153c51ed4b05d66ca4696f1eed63d1792170a4ed644ede5cd8afdf2373"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:7a1e662e003082329d2d308f8d18cf91e7974c86255b4fb369bf399ec7ed1760", "1.10.0--r42hdfd78af_0": "sha256:b0d2ea4b81d05db754ca216aca677c5c018e14c884ff4dbb03c3db3f48ecd651", "1.12.0--r43hdfd78af_0": "sha256:ce843ab8909461a816dd74c692f119a07ca3cd7e18d3c7340be1046c8e0bb8c2", "1.14.0--r43hdfd78af_0": "sha256:cf9f72153c51ed4b05d66ca4696f1eed63d1792170a4ed644ede5cd8afdf2373"}, "docker": "quay.io/biocontainers/bioconductor-nparc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nparc.
shpc-registry automated BioContainers addition for bioconductor-nparc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nparc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nparc:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nparc/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nparc/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nparc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nparc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nparc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nparc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nparc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nparc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nparc

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