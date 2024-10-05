---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgamethylation450k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgamethylation450k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgamethylation450k/container.yaml"
updated_at: "2024-10-05 03:04:28.406663"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgamethylation450k"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcgamethylation450k"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgamethylation450k", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgamethylation450k", "latest": {"1.38.0--r43hdfd78af_0": "sha256:b5306e9da779df88f6c8358caf4f61f2f4c63cc85ab1c7cb333d03ac3dff43be"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:52e8265bb114fa1b72e55d800a0feb8f48e28aaa2659684cf6889ce731a66ef2", "1.33.0--r42hdfd78af_0": "sha256:02a820af2df6a84fc58d06725bc9b95c5571f271c0cabec2c07efa06f2d28909", "1.36.0--r43hdfd78af_0": "sha256:4dd5ee9391ff59707816e22426d19e78c51d83f9a20f6482c32b17bb28137471", "1.38.0--r43hdfd78af_0": "sha256:b5306e9da779df88f6c8358caf4f61f2f4c63cc85ab1c7cb333d03ac3dff43be"}, "docker": "quay.io/biocontainers/bioconductor-tcgamethylation450k"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgamethylation450k.
shpc-registry automated BioContainers addition for bioconductor-tcgamethylation450k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgamethylation450k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgamethylation450k:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgamethylation450k/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcgamethylation450k/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgamethylation450k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgamethylation450k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgamethylation450k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgamethylation450k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgamethylation450k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgamethylation450k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tcgamethylation450k

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