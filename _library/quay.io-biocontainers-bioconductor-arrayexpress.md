---
layout: container
name:  "quay.io/biocontainers/bioconductor-arrayexpress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-arrayexpress/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-arrayexpress/container.yaml"
updated_at: "2024-01-10 08:29:27.863438"
latest: "1.62.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-arrayexpress"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.57.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-arrayexpress"
config: {"url": "https://biocontainers.pro/tools/bioconductor-arrayexpress", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-arrayexpress", "latest": {"1.62.0--r43hdfd78af_0": "sha256:c22771c84a1f860c5f096e6b76ae21f38a97069049defa750ea6402b2bee61ba"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:0673ae8333fb0d0f189f294154d272036c2dff69a3da1d380cc19cc77ef2e662", "1.57.0--r42hdfd78af_0": "sha256:4776a6852841fe065948b9a63b6449d855860f91e57d7f11063d9bc7f4918ab4", "1.60.0--r43hdfd78af_0": "sha256:41f2dbc6ba5702bc33940dfea73ad822fbfd53df817a68d1281ab0d61eef5367", "1.62.0--r43hdfd78af_0": "sha256:c22771c84a1f860c5f096e6b76ae21f38a97069049defa750ea6402b2bee61ba"}, "docker": "quay.io/biocontainers/bioconductor-arrayexpress"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-arrayexpress.
shpc-registry automated BioContainers addition for bioconductor-arrayexpress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-arrayexpress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-arrayexpress:1.62.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-arrayexpress/1.62.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-arrayexpress/1.62.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-arrayexpress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrayexpress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrayexpress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-arrayexpress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-arrayexpress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-arrayexpress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-arrayexpress

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