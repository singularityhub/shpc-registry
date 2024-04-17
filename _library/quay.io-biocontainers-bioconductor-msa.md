---
layout: container
name:  "quay.io/biocontainers/bioconductor-msa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msa/container.yaml"
updated_at: "2024-04-17 02:40:35.622145"
latest: "1.34.0--r43hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msa"

versions:
 - "1.26.0--r41hc247a5b_2"
 - "1.30.0--r42hc247a5b_0"
 - "1.30.0--r42hc247a5b_1"
 - "1.32.0--r43hc247a5b_0"
 - "1.34.0--r43hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msa", "latest": {"1.34.0--r43hc247a5b_0": "sha256:a35a2e1ac26772a07cba7c03a900df5f61bb0a30bbf89d2a38a0aa213f426e48"}, "tags": {"1.26.0--r41hc247a5b_2": "sha256:7c94ab18562bc0a0f6e2e437de96762cd64a4fb7c43506c3de843053270d050d", "1.30.0--r42hc247a5b_0": "sha256:338215b63cf25ceb6fb11ad911846ebdfe4d2f66c1e1fcf4aa807525d8c67475", "1.30.0--r42hc247a5b_1": "sha256:1eaa4f52abcd0ab6312124bfa72a6d5e36e424163d76abc8d100edcc511dec2f", "1.32.0--r43hc247a5b_0": "sha256:968bdb852b428537f5268d4728d4bf77ae77858e835e5b21fb97965daded4b1d", "1.34.0--r43hc247a5b_0": "sha256:a35a2e1ac26772a07cba7c03a900df5f61bb0a30bbf89d2a38a0aa213f426e48"}, "docker": "quay.io/biocontainers/bioconductor-msa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msa.
shpc-registry automated BioContainers addition for bioconductor-msa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msa:1.34.0--r43hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msa/1.34.0--r43hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-msa/1.34.0--r43hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msa

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