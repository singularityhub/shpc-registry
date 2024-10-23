---
layout: container
name:  "quay.io/biocontainers/bioconductor-cocitestats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cocitestats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cocitestats/container.yaml"
updated_at: "2024-10-23 03:14:38.761644"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cocitestats"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cocitestats"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cocitestats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cocitestats", "latest": {"1.74.0--r43hdfd78af_0": "sha256:c85465c37ff83169fa8f18c03645aa609ede78c857fcb4b109eb3c2e5db7307a"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:b17092279c5d74b3857d71f158ed7bc1ea1e93336d17e85ef33a30f6b2ae214f", "1.70.0--r42hdfd78af_0": "sha256:aa56f8d132d61e1dfcdde174284d1720319e1961b98298cf8ca3898da18742e7", "1.72.0--r43hdfd78af_0": "sha256:604b90a5e452f9e9d07e0c8582817c39a0d96bf9b83c39b95473027b86aaf471", "1.74.0--r43hdfd78af_0": "sha256:c85465c37ff83169fa8f18c03645aa609ede78c857fcb4b109eb3c2e5db7307a"}, "docker": "quay.io/biocontainers/bioconductor-cocitestats"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cocitestats.
shpc-registry automated BioContainers addition for bioconductor-cocitestats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cocitestats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cocitestats:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cocitestats/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cocitestats/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cocitestats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cocitestats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cocitestats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cocitestats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cocitestats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cocitestats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cocitestats

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