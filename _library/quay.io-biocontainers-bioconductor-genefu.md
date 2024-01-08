---
layout: container
name:  "quay.io/biocontainers/bioconductor-genefu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genefu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genefu/container.yaml"
updated_at: "2024-01-08 03:10:05.806057"
latest: "2.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genefu"

versions:
 - "2.26.0--r41hdfd78af_0"
 - "2.30.0--r42hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genefu"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genefu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genefu", "latest": {"2.34.0--r43hdfd78af_0": "sha256:13ea3dcec3825272762346d0c4357218d0afa12f47ec05bbabcac3777c218d66"}, "tags": {"2.26.0--r41hdfd78af_0": "sha256:3186faac563ab6ba6db044d2fb9b0885c53cb1a6c50d9a8ef4d480fdb978e98f", "2.30.0--r42hdfd78af_0": "sha256:aff83f2b8b04362afb3ec6092f89e5579b552bb2bf7accea44099030e816b227", "2.32.0--r43hdfd78af_0": "sha256:4097e61ff6aecac20bb86e8a40217f71679d6d0255d37faa32b52221e142b2f2", "2.34.0--r43hdfd78af_0": "sha256:13ea3dcec3825272762346d0c4357218d0afa12f47ec05bbabcac3777c218d66"}, "docker": "quay.io/biocontainers/bioconductor-genefu"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genefu.
shpc-registry automated BioContainers addition for bioconductor-genefu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genefu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genefu:2.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genefu/2.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genefu/2.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genefu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genefu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genefu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genefu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genefu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genefu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genefu

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