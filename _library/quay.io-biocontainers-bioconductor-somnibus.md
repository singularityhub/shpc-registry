---
layout: container
name:  "quay.io/biocontainers/bioconductor-somnibus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-somnibus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-somnibus/container.yaml"
updated_at: "2025-03-24 03:45:37.141923"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-somnibus"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.7.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-somnibus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-somnibus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-somnibus", "latest": {"1.10.0--r43hdfd78af_0": "sha256:52576111cf93d66b3727b675cdaa2beb0da40b58edf99b95e69271c298329971"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:b09c4e79c1de51f2676486810edd5f823cef025962101212591e0ce058aa4fb7", "1.6.0--r42hdfd78af_0": "sha256:ee413c0b8f7e70a5cad96c7a3f1cec74b80fc15ee3ea64f21b541a1b52128c27", "1.7.0--r43hdfd78af_0": "sha256:acb8e70bc041c0d35fdf3187dce79b138b1beb375910781fa3a00e03618d1649", "1.10.0--r43hdfd78af_0": "sha256:52576111cf93d66b3727b675cdaa2beb0da40b58edf99b95e69271c298329971"}, "docker": "quay.io/biocontainers/bioconductor-somnibus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-somnibus.
shpc-registry automated BioContainers addition for bioconductor-somnibus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-somnibus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-somnibus:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-somnibus/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-somnibus/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-somnibus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-somnibus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-somnibus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-somnibus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-somnibus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-somnibus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-somnibus

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