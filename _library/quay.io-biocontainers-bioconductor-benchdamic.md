---
layout: container
name:  "quay.io/biocontainers/bioconductor-benchdamic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-benchdamic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-benchdamic/container.yaml"
updated_at: "2025-10-27 03:47:37.453416"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-benchdamic"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-benchdamic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-benchdamic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-benchdamic", "latest": {"1.6.0--r43hdfd78af_0": "sha256:b0ffd3c0679440c1c015a3496a0f50b26f51a85263a8f3e0cc4e26e5ff883735"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:47b02bdd15d720b9cb5b3bde3507707cc11dbe2fc62928a2cc5fd0d2128e7016", "1.4.0--r42hdfd78af_0": "sha256:6290aa2f7553f1a93e6ce14cf5df95e8c3effa22a16335464a892f4c7e6d3701", "1.6.0--r43hdfd78af_0": "sha256:b0ffd3c0679440c1c015a3496a0f50b26f51a85263a8f3e0cc4e26e5ff883735"}, "docker": "quay.io/biocontainers/bioconductor-benchdamic"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-benchdamic.
shpc-registry automated BioContainers addition for bioconductor-benchdamic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-benchdamic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-benchdamic:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-benchdamic/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-benchdamic/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-benchdamic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-benchdamic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-benchdamic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-benchdamic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-benchdamic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-benchdamic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-benchdamic

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