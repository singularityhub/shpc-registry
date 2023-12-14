---
layout: container
name:  "quay.io/biocontainers/bioconductor-segmenter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-segmenter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-segmenter/container.yaml"
updated_at: "2023-12-14 03:21:31.724191"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-segmenter"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-segmenter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-segmenter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-segmenter", "latest": {"1.6.0--r43hdfd78af_0": "sha256:72bd8cde76136eb6ceb8d46a79dd5ab63d67f4fe3b6329d1dd3bacdd335481c5"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:3897c7d0b7793ef5b8ccfc47c3156e9f2da14801cea3ee45b735e00e61c8bccd", "1.4.0--r42hdfd78af_0": "sha256:63b42aadfa441b66ea9ea3680d3455f0610bf3eeaa65dbf5708b4f0a771c71a1", "1.6.0--r43hdfd78af_0": "sha256:72bd8cde76136eb6ceb8d46a79dd5ab63d67f4fe3b6329d1dd3bacdd335481c5"}, "docker": "quay.io/biocontainers/bioconductor-segmenter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-segmenter.
shpc-registry automated BioContainers addition for bioconductor-segmenter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-segmenter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-segmenter:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-segmenter/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-segmenter/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-segmenter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-segmenter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-segmenter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-segmenter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-segmenter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-segmenter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-segmenter

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