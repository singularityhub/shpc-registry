---
layout: container
name:  "quay.io/biocontainers/bioconductor-flames"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flames/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flames/container.yaml"
updated_at: "2025-02-14 02:41:55.901458"
latest: "1.8.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flames"

versions:
 - "1.0.2--r41hc247a5b_2"
 - "1.3.4--r42hc247a5b_0"
 - "1.3.4--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
 - "1.8.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flames"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flames", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flames", "latest": {"1.8.0--r43hf17093f_0": "sha256:059d0a832c057646cd327bfc03e39645ff68a3ee85c55af9ba3c3b64193ce76d"}, "tags": {"1.0.2--r41hc247a5b_2": "sha256:ab2aa45994b7945338a56f90d80e77eac1332ea66f88bd25097e05c535d96f87", "1.3.4--r42hc247a5b_0": "sha256:bd8ad9146cb8f6b85d9d6a35a652dd6fbd0bf19d5095a2c3c45b89963d88bf0e", "1.3.4--r42hf17093f_1": "sha256:9574e1d0d89b2186da009b79c89ffed0047080df74ee27d9978bba76d825eb3a", "1.6.0--r43hf17093f_0": "sha256:5c523d50399e8d4176fa7f9f5f0a85d2f48422658b89fade0c0039ffc3049928", "1.8.0--r43hf17093f_0": "sha256:059d0a832c057646cd327bfc03e39645ff68a3ee85c55af9ba3c3b64193ce76d"}, "docker": "quay.io/biocontainers/bioconductor-flames"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flames.
shpc-registry automated BioContainers addition for bioconductor-flames
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flames
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flames:1.8.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flames/1.8.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-flames/1.8.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flames-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flames-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flames-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flames-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flames-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flames-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flames

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