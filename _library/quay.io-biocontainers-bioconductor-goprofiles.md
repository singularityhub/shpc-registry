---
layout: container
name:  "quay.io/biocontainers/bioconductor-goprofiles"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-goprofiles/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-goprofiles/container.yaml"
updated_at: "2025-02-03 02:55:13.928679"
latest: "1.68.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-goprofiles"

versions:
 - "1.56.0--r41hdfd78af_0"
 - "1.60.0--r42hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.64.0--r43hdfd78af_0"
 - "1.68.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-goprofiles"
config: {"url": "https://biocontainers.pro/tools/bioconductor-goprofiles", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-goprofiles", "latest": {"1.68.0--r44hdfd78af_0": "sha256:b9d14a569ac1c42b608dd6f28ea1d54da2620281465d9266ec06f67903bac1f9"}, "tags": {"1.56.0--r41hdfd78af_0": "sha256:8032f09a688e87df8872fd76a722b3a6b60f44d6a213163ffb8475cc937b12d4", "1.60.0--r42hdfd78af_0": "sha256:202bd69642bc71fcf6a9d16dc19046e1295509425bfcb25f256a4549c81b01ca", "1.62.0--r43hdfd78af_0": "sha256:a6846fe6d22f5cbeb7bfebdb733e98de06d64297311b392c60e777417fb09f7d", "1.64.0--r43hdfd78af_0": "sha256:f2f5b627b1dd65bd9a98989d7ee954b79be66726c345bb40bc2f163a8473f3ea", "1.68.0--r44hdfd78af_0": "sha256:b9d14a569ac1c42b608dd6f28ea1d54da2620281465d9266ec06f67903bac1f9"}, "docker": "quay.io/biocontainers/bioconductor-goprofiles"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-goprofiles.
shpc-registry automated BioContainers addition for bioconductor-goprofiles
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-goprofiles
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-goprofiles:1.68.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-goprofiles/1.68.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-goprofiles/1.68.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-goprofiles-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-goprofiles-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-goprofiles-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-goprofiles-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-goprofiles-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-goprofiles-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-goprofiles

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