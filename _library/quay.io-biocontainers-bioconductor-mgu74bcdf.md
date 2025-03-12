---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74bcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74bcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74bcdf/container.yaml"
updated_at: "2025-03-12 03:11:43.553211"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74bcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74bcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74bcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74bcdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:5ab278ad545c5e74384aeccb6ed881e9c512aebb1d2fabebde7cb441a525077a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:15ba9a4f4c29f0e406f14a5f8c716ab8d4f1f9c7553a46893e0ef058ad1e843d", "2.18.0--r42hdfd78af_10": "sha256:05dc2f4c03c355d9f635450d0cbb922a0eb8f62281b491595f0fe07b7c747f44", "2.18.0--r43hdfd78af_11": "sha256:93c264f353fa32d58ce0eaaac388f7f24d5df5479f7b7827ff76f746f62c3fe9", "2.18.0--r43hdfd78af_12": "sha256:f2b07dedd0baf5a662a8f3817e389dd1754b7041586f8b12edfac09574087ed7", "2.18.0--r44hdfd78af_13": "sha256:5ab278ad545c5e74384aeccb6ed881e9c512aebb1d2fabebde7cb441a525077a"}, "docker": "quay.io/biocontainers/bioconductor-mgu74bcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74bcdf.
shpc-registry automated BioContainers addition for bioconductor-mgu74bcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bcdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74bcdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mgu74bcdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74bcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74bcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74bcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74bcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74bcdf

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