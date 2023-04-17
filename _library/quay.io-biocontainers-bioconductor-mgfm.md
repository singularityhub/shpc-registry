---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgfm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgfm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgfm/container.yaml"
updated_at: "2023-04-17 03:32:41.579713"
latest: "1.32.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mgfm"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mgfm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgfm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgfm", "latest": {"1.32.0--r42hdfd78af_0": "sha256:0222523e640b15f6a61c1e59edf98cbca1075459f20fd7ce8b25f436222cafa6"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:4814e0d8fcafe9f37bf104c10dadd1652e8da07ad8d628ea0641c01429906503", "1.32.0--r42hdfd78af_0": "sha256:0222523e640b15f6a61c1e59edf98cbca1075459f20fd7ce8b25f436222cafa6"}, "docker": "quay.io/biocontainers/bioconductor-mgfm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgfm.
shpc-registry automated BioContainers addition for bioconductor-mgfm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgfm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgfm:1.32.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgfm/1.32.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mgfm/1.32.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgfm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgfm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgfm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgfm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgfm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgfm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgfm

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