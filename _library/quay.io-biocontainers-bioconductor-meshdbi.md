---
layout: container
name:  "quay.io/biocontainers/bioconductor-meshdbi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-meshdbi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-meshdbi/container.yaml"
updated_at: "2023-10-04 03:17:46.138393"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-meshdbi"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-meshdbi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-meshdbi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-meshdbi", "latest": {"1.36.0--r43hdfd78af_0": "sha256:b2c847e4fc4523cd6da57081bd1f4ca86e44156b12945217b02cd738d8f3eebf"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:8248de8815ee7421bab1879701dfb9a0c7f22a69551820f7c60339ac037a0b92", "1.34.0--r42hdfd78af_0": "sha256:9500bafabaa9d9acb500264959175715304c39fce0ff40362c7ce20ff70854c7", "1.36.0--r43hdfd78af_0": "sha256:b2c847e4fc4523cd6da57081bd1f4ca86e44156b12945217b02cd738d8f3eebf"}, "docker": "quay.io/biocontainers/bioconductor-meshdbi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-meshdbi.
shpc-registry automated BioContainers addition for bioconductor-meshdbi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-meshdbi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-meshdbi:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-meshdbi/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-meshdbi/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-meshdbi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meshdbi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meshdbi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-meshdbi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-meshdbi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-meshdbi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-meshdbi

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