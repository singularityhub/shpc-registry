---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqlogo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqlogo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqlogo/container.yaml"
updated_at: "2025-09-24 03:32:15.293210"
latest: "1.72.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqlogo"

versions:
 - "1.60.0--r41hdfd78af_0"
 - "1.64.0--r42hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
 - "1.72.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqlogo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqlogo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqlogo", "latest": {"1.72.0--r44hdfd78af_0": "sha256:93b4ccacf97bf59932c1f77a147932ad497924158740406ed35765706c5e83bb"}, "tags": {"1.60.0--r41hdfd78af_0": "sha256:1a5e29c8e58bd3c51c763ee58530227e0a7783bc6214d4df3267df68ef047550", "1.64.0--r42hdfd78af_0": "sha256:6ad4e5b22ebc1ab4e982c12c98ecc778832f595d505606168a8f519f3ad24a09", "1.66.0--r43hdfd78af_0": "sha256:af2aae9debf381d7580105af2a9a78c8acb2d7c427704b148e5b4b15552327fc", "1.68.0--r43hdfd78af_0": "sha256:1fae4df94b7deeac509c7b30f83ad72adcfe5e59abf161376a588367e008d7b4", "1.72.0--r44hdfd78af_0": "sha256:93b4ccacf97bf59932c1f77a147932ad497924158740406ed35765706c5e83bb"}, "docker": "quay.io/biocontainers/bioconductor-seqlogo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqlogo.
shpc-registry automated BioContainers addition for bioconductor-seqlogo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqlogo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqlogo:1.72.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqlogo/1.72.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqlogo/1.72.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqlogo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqlogo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqlogo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqlogo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqlogo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqlogo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqlogo

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