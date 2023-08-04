---
layout: container
name:  "quay.io/biocontainers/bioconductor-gse159526"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gse159526/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gse159526/container.yaml"
updated_at: "2023-08-04 03:07:45.065158"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gse159526"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.3.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gse159526"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gse159526", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gse159526", "latest": {"1.6.0--r43hdfd78af_0": "sha256:b2560323828e98c61c0acab7c16f2812fe4e9a53d8ab98cec02e97714af3f6ad"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:ef757966338a4647fbbdde4bca81cf8094a91fca68a2d8ddcdde645642012ea2", "1.3.0--r42hdfd78af_0": "sha256:22f12c0eabbd88105c01f08f15a7c50c76e0ae46cbf72d5a3ec405ff616733e1", "1.6.0--r43hdfd78af_0": "sha256:b2560323828e98c61c0acab7c16f2812fe4e9a53d8ab98cec02e97714af3f6ad"}, "docker": "quay.io/biocontainers/bioconductor-gse159526"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gse159526.
shpc-registry automated BioContainers addition for bioconductor-gse159526
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gse159526
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gse159526:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gse159526/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gse159526/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gse159526-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gse159526-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gse159526-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gse159526-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gse159526-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gse159526-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gse159526

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