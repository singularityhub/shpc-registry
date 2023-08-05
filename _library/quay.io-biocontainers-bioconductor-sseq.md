---
layout: container
name:  "quay.io/biocontainers/bioconductor-sseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sseq/container.yaml"
updated_at: "2023-08-05 03:20:04.429964"
latest: "1.36.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sseq"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sseq", "latest": {"1.36.0--r42hdfd78af_0": "sha256:86ec576fbdff1ec003ef4f23bfb86af33a397d2ce924cf26bff4cbe0c3239005"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:e21c88b6c442fb2b13928341ab80c105aa481809de69b69382783d5ce9396c69", "1.36.0--r42hdfd78af_0": "sha256:86ec576fbdff1ec003ef4f23bfb86af33a397d2ce924cf26bff4cbe0c3239005"}, "docker": "quay.io/biocontainers/bioconductor-sseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sseq.
shpc-registry automated BioContainers addition for bioconductor-sseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sseq:1.36.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sseq/1.36.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sseq/1.36.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sseq

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