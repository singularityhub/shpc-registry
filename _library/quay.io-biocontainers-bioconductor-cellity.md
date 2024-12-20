---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellity/container.yaml"
updated_at: "2024-12-20 02:55:08.520515"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellity"

versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellity"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellity", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellity", "latest": {"1.30.0--r43hdfd78af_0": "sha256:642a90f367e01c8a58873ca910ca41fbd69c92d176d141750bff44fbf775d4a6"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:dc6dd07a0ee050009ec300529d0a07d058524dc680a98797e29369ef56f4b70e", "1.26.0--r42hdfd78af_0": "sha256:aea72047292032f0eadfd907f0ee9f67ea6a02d18bb7c5b8595a549ab5e3ec62", "1.28.0--r43hdfd78af_0": "sha256:f369099bd4c8166d82e604df0397ec214695d0338fd4b961e55d85d9148e9f54", "1.30.0--r43hdfd78af_0": "sha256:642a90f367e01c8a58873ca910ca41fbd69c92d176d141750bff44fbf775d4a6"}, "docker": "quay.io/biocontainers/bioconductor-cellity"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellity.
shpc-registry automated BioContainers addition for bioconductor-cellity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellity:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellity/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellity/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cellity

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