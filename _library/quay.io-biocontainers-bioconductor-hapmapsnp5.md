---
layout: container
name:  "quay.io/biocontainers/bioconductor-hapmapsnp5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hapmapsnp5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hapmapsnp5/container.yaml"
updated_at: "2024-04-29 02:49:04.751658"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hapmapsnp5"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.39.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hapmapsnp5"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hapmapsnp5", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hapmapsnp5", "latest": {"1.44.0--r43hdfd78af_0": "sha256:b96b0215a0818e77814498fdf8459b39fc84339b4ad5d855785787554a112a81"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:5393e45d5564dc2613060ecbe009c771b177d6ce2bc554292eea7736ebdcd9d7", "1.39.0--r42hdfd78af_0": "sha256:6a0b8cc388ab3185c92048dc7c679e086f4e90ebd5685e4afa08bc2de7731857", "1.42.0--r43hdfd78af_0": "sha256:c4105a4a0d9b661cc8dcbf47e0e47a0624d4940247a3154bce587c790f95903d", "1.44.0--r43hdfd78af_0": "sha256:b96b0215a0818e77814498fdf8459b39fc84339b4ad5d855785787554a112a81"}, "docker": "quay.io/biocontainers/bioconductor-hapmapsnp5"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hapmapsnp5.
shpc-registry automated BioContainers addition for bioconductor-hapmapsnp5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmapsnp5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmapsnp5:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hapmapsnp5/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hapmapsnp5/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hapmapsnp5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmapsnp5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmapsnp5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hapmapsnp5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hapmapsnp5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hapmapsnp5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hapmapsnp5

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