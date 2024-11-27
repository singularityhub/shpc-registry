---
layout: container
name:  "quay.io/biocontainers/bioconductor-farms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-farms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-farms/container.yaml"
updated_at: "2024-11-27 03:27:06.797343"
latest: "1.52.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-farms"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-farms"
config: {"url": "https://biocontainers.pro/tools/bioconductor-farms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-farms", "latest": {"1.52.0--r43hdfd78af_0": "sha256:74071ca6077f9300e022a88b1aff97edc5991b6c1b2bed88ebbc9571135a1daa"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:67fa02480be15b9f6292540ce0f8febc9d95232a20d277d2666f63d106fd3e27", "1.50.0--r42hdfd78af_0": "sha256:410219aea74d24cef5948434c6ec2713cfd93bddc7bda00bb489c86caaa45e43", "1.52.0--r43hdfd78af_0": "sha256:74071ca6077f9300e022a88b1aff97edc5991b6c1b2bed88ebbc9571135a1daa"}, "docker": "quay.io/biocontainers/bioconductor-farms"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-farms.
shpc-registry automated BioContainers addition for bioconductor-farms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-farms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-farms:1.52.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-farms/1.52.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-farms/1.52.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-farms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-farms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-farms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-farms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-farms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-farms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-farms

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