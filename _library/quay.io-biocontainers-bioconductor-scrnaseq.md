---
layout: container
name:  "quay.io/biocontainers/bioconductor-scrnaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scrnaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scrnaseq/container.yaml"
updated_at: "2023-09-15 02:46:48.922067"
latest: "2.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scrnaseq"

versions:
 - "2.8.0--r41hdfd78af_1"
 - "2.12.0--r42hdfd78af_0"
 - "2.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scrnaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scrnaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scrnaseq", "latest": {"2.14.0--r43hdfd78af_0": "sha256:dc2864793eb55d2ed6066226f3cc14dd64e05ebeec64708436ab25dc27182ec4"}, "tags": {"2.8.0--r41hdfd78af_1": "sha256:4709c7aec80879dfa98f424c0689d2c69882c08e0134e6243fe59fee0b0ad419", "2.12.0--r42hdfd78af_0": "sha256:b8a9898bc1c0ca81f24cbee1e637aeab41522ba5d9b8b98364a611d5b5a16b0f", "2.14.0--r43hdfd78af_0": "sha256:dc2864793eb55d2ed6066226f3cc14dd64e05ebeec64708436ab25dc27182ec4"}, "docker": "quay.io/biocontainers/bioconductor-scrnaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scrnaseq.
shpc-registry automated BioContainers addition for bioconductor-scrnaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scrnaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scrnaseq:2.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scrnaseq/2.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scrnaseq/2.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scrnaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scrnaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scrnaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scrnaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scrnaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scrnaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scrnaseq

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