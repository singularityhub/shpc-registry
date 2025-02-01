---
layout: container
name:  "quay.io/biocontainers/bioconductor-clonality"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clonality/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clonality/container.yaml"
updated_at: "2025-02-01 03:31:22.440535"
latest: "1.47.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clonality"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.47.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clonality"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clonality", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clonality", "latest": {"1.47.0--r43hdfd78af_0": "sha256:aeeb01f5e45d5a903e59d5e865f37576ac322683b150391cc12d7c9b9137b12f"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:776ff8a567b0442049af0838a3606cbad86afe454b15acaf00e0428b166989a0", "1.46.0--r42hdfd78af_0": "sha256:89916c114571f5d6166124e0313a77d0e535857fd4b83c174bbaf96aa37e9c20", "1.47.0--r43hdfd78af_0": "sha256:aeeb01f5e45d5a903e59d5e865f37576ac322683b150391cc12d7c9b9137b12f"}, "docker": "quay.io/biocontainers/bioconductor-clonality"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clonality.
shpc-registry automated BioContainers addition for bioconductor-clonality
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clonality
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clonality:1.47.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clonality/1.47.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clonality/1.47.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clonality-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clonality-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clonality-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clonality-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clonality-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clonality-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clonality

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