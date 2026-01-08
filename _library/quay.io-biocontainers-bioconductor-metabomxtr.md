---
layout: container
name:  "quay.io/biocontainers/bioconductor-metabomxtr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metabomxtr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metabomxtr/container.yaml"
updated_at: "2026-01-08 03:46:24.722895"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metabomxtr"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metabomxtr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metabomxtr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metabomxtr", "latest": {"1.40.0--r44hdfd78af_0": "sha256:ead21ffb9e39a90b92047c98ba3e6edd5dd0fe3432879115e7ffe63c690ad7e9"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:c99f395e67cec62dd51827ced2f5935c6e51b7191d9876e48ce3c4c6060242f4", "1.32.0--r42hdfd78af_0": "sha256:ae8e35d1eda63982308570f38d15a85590444700d651f3bb36d68de27c8b78e3", "1.34.0--r43hdfd78af_0": "sha256:8e36000272608247ae98c6397a081604176433d808c73e7bf5fead1bb69d5a73", "1.36.0--r43hdfd78af_0": "sha256:630028778731f5fa85952f26c8640cf74d3298329f77aade35828a8dc8b8b6a8", "1.40.0--r44hdfd78af_0": "sha256:ead21ffb9e39a90b92047c98ba3e6edd5dd0fe3432879115e7ffe63c690ad7e9"}, "docker": "quay.io/biocontainers/bioconductor-metabomxtr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metabomxtr.
shpc-registry automated BioContainers addition for bioconductor-metabomxtr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metabomxtr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metabomxtr:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metabomxtr/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metabomxtr/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metabomxtr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabomxtr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabomxtr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metabomxtr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metabomxtr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metabomxtr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metabomxtr

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