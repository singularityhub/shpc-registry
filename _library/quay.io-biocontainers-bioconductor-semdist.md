---
layout: container
name:  "quay.io/biocontainers/bioconductor-semdist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-semdist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-semdist/container.yaml"
updated_at: "2024-12-11 03:19:22.248266"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-semdist"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-semdist"
config: {"url": "https://biocontainers.pro/tools/bioconductor-semdist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-semdist", "latest": {"1.36.0--r43hdfd78af_0": "sha256:3ff47050f80aba1c9a3fd769b9d71539db73b8e52049c9cd3a91cd1c441abfec"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:e988ab96f76f18f55c90e1d0fb74a028a325d45399ea82f7c41c8f31435ae25f", "1.32.0--r42hdfd78af_0": "sha256:22d0f097718f22199245c800be2384a0f1ede439c2056f807da442a3764eb944", "1.34.0--r43hdfd78af_0": "sha256:41d4e30dcd9fa24c16ee620ff5b55e6fc5a2ce82cdac88d9cf81b848d5a25465", "1.36.0--r43hdfd78af_0": "sha256:3ff47050f80aba1c9a3fd769b9d71539db73b8e52049c9cd3a91cd1c441abfec"}, "docker": "quay.io/biocontainers/bioconductor-semdist"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-semdist.
shpc-registry automated BioContainers addition for bioconductor-semdist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-semdist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-semdist:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-semdist/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-semdist/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-semdist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-semdist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-semdist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-semdist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-semdist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-semdist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-semdist

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