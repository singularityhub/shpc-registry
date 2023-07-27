---
layout: container
name:  "quay.io/biocontainers/bioconductor-pumadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pumadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pumadata/container.yaml"
updated_at: "2023-07-27 02:35:37.724226"
latest: "2.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pumadata"

versions:
 - "2.30.0--r41hdfd78af_1"
 - "2.34.0--r42hdfd78af_0"
 - "2.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pumadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pumadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pumadata", "latest": {"2.36.0--r43hdfd78af_0": "sha256:71f3aebf9dd9f82e750e41c456b933339a8662e48b6373674c0ce4ecccdac4b8"}, "tags": {"2.30.0--r41hdfd78af_1": "sha256:a5534063f74e9200146e190842422dd010ac20653e4772fd5829a831e0faf6b1", "2.34.0--r42hdfd78af_0": "sha256:a4b62ab186855b6d8577b2ec9d0be603c627551ee00d8ea2bff70b9961b1db1a", "2.36.0--r43hdfd78af_0": "sha256:71f3aebf9dd9f82e750e41c456b933339a8662e48b6373674c0ce4ecccdac4b8"}, "docker": "quay.io/biocontainers/bioconductor-pumadata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pumadata.
shpc-registry automated BioContainers addition for bioconductor-pumadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pumadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pumadata:2.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pumadata/2.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pumadata/2.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pumadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pumadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pumadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pumadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pumadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pumadata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pumadata

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