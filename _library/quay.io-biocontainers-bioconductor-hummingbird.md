---
layout: container
name:  "quay.io/biocontainers/bioconductor-hummingbird"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hummingbird/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hummingbird/container.yaml"
updated_at: "2026-02-01 05:21:14.606070"
latest: "1.16.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hummingbird"

versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.0--r43hf17093f_0"
 - "1.12.0--r43hf17093f_0"
 - "1.16.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hummingbird"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hummingbird", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hummingbird", "latest": {"1.16.0--r44he5774e6_0": "sha256:948426b4396d25465baa942f5077ef581e37b8d93e5815f843198227bc2e347c"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:fcbfa9691dfad0dad2ff308bb91ffa807a0e0f4c161bb04e2a8902f738b857d1", "1.8.0--r42hc247a5b_0": "sha256:e09bc14e803707ceff8efd24a143b334b129c02c60c1d0a7fbd36ab014f4d0a0", "1.8.0--r42hf17093f_1": "sha256:3c1f2e1c7ffb6e49b98bdf0f0ca9554c165e42c410bf374272d8ec6a280470de", "1.10.0--r43hf17093f_0": "sha256:2c136c18b9787d58cc73cefb47e422eac85bae8020e7fadc89ee1ad7b1336df2", "1.12.0--r43hf17093f_0": "sha256:2a4545ec53c1861e37e1f0221266d313effb32c51c20d4b68dd08350765527e1", "1.16.0--r44he5774e6_0": "sha256:948426b4396d25465baa942f5077ef581e37b8d93e5815f843198227bc2e347c"}, "docker": "quay.io/biocontainers/bioconductor-hummingbird"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hummingbird.
shpc-registry automated BioContainers addition for bioconductor-hummingbird
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hummingbird
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hummingbird:1.16.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hummingbird/1.16.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-hummingbird/1.16.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hummingbird-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hummingbird-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hummingbird-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hummingbird-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hummingbird-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hummingbird-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hummingbird

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