---
layout: container
name:  "quay.io/biocontainers/bioconductor-madseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-madseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-madseq/container.yaml"
updated_at: "2025-01-10 03:20:15.096937"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-madseq"
aliases:
 - "jags"
 - "wget"
versions:
 - "1.6.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-madseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-madseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-madseq", "latest": {"1.28.0--r43hdfd78af_0": "sha256:cf43b6638b920da23b62f00efb646b5cad34cc2031fbd87e0d6d950cee4b8616"}, "tags": {"1.6.1--r351_0": "sha256:2a385c5f272c51064945e13a1054ac36d0677735a19c85438ea5c76fd3754206", "1.24.0--r42hdfd78af_0": "sha256:018573516ab061dd24a723093dcfc7be02735ed3964698061360530378114386", "1.20.0--r41hdfd78af_0": "sha256:0865cc6447ff603bfdbdc2de05621015e0c76f6c844a7bc431806364e0c457aa", "1.18.0--r41hdfd78af_0": "sha256:cd2281d16e198338c098ba1d709ebb3ecc8705433f5486b173e81700b9ebff82", "1.16.0--r40hdfd78af_1": "sha256:4ac5b6bd5216740ca3fa9df5c069fa0532c3040aa0234a6476e0df815faa96f3", "1.14.0--r40_0": "sha256:89306d4ef01bbe83f17f10ae48fd72970597ad0f5dcb4a25d8516fcb2a75510c", "1.26.0--r43hdfd78af_0": "sha256:3e17ed671aa0b40a17ab4b0d45c1df2c3a575946f9d4e3b6b991922b3754ef1c", "1.28.0--r43hdfd78af_0": "sha256:cf43b6638b920da23b62f00efb646b5cad34cc2031fbd87e0d6d950cee4b8616"}, "docker": "quay.io/biocontainers/bioconductor-madseq", "aliases": {"jags": "/usr/local/bin/jags", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-madseq.
shpc-registry automated BioContainers addition for bioconductor-madseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-madseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-madseq:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-madseq/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-madseq/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-madseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-madseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-madseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-madseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-madseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-madseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jags

```bash
$ singularity exec <container> /usr/local/bin/jags
$ podman run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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