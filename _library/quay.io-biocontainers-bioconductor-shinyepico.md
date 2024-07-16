---
layout: container
name:  "quay.io/biocontainers/bioconductor-shinyepico"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-shinyepico/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-shinyepico/container.yaml"
updated_at: "2024-07-16 02:55:11.808016"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-shinyepico"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-shinyepico"
config: {"url": "https://biocontainers.pro/tools/bioconductor-shinyepico", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-shinyepico", "latest": {"1.10.0--r43hdfd78af_0": "sha256:2fa779799b554442b663a06fa0f9da0be56b8664afd00c24bb331d7370c759b3"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:29d963d769cffa712512d7d23e4975cb147084801f0bc6d75f32a35914692095", "1.6.0--r42hdfd78af_0": "sha256:670cb39396128fd1a6bafa1049e21fa092a74307317d4d9b4f6753db20ff0fe6", "1.8.0--r43hdfd78af_0": "sha256:b52fb17ebb7f4924806970dcde3024f3b75ae057f55d5831d9dd849f194d30db", "1.10.0--r43hdfd78af_0": "sha256:2fa779799b554442b663a06fa0f9da0be56b8664afd00c24bb331d7370c759b3"}, "docker": "quay.io/biocontainers/bioconductor-shinyepico", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-shinyepico.
shpc-registry automated BioContainers addition for bioconductor-shinyepico
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-shinyepico
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-shinyepico:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-shinyepico/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-shinyepico/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-shinyepico-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shinyepico-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shinyepico-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-shinyepico-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-shinyepico-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-shinyepico-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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