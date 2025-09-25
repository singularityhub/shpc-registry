---
layout: container
name:  "quay.io/biocontainers/bioconductor-scp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scp/container.yaml"
updated_at: "2025-09-25 08:06:32.263325"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scp"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scp", "latest": {"1.16.0--r44hdfd78af_0": "sha256:a27388c10f94c7bcfbf340314f5715d450026782ba868b27c96b433b24f7d907"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:08fc876994acb41e2b9ba675dfb6f56f1ae2abf010e0dd495b58b692762f0e4a", "1.8.0--r42hdfd78af_0": "sha256:031a6dc97c5fd60bac295d97e4ed909c31324b8d45dbed1dda1af4c7579801aa", "1.10.1--r43hdfd78af_0": "sha256:d918ae26181bcaa1195f23c2833086e1e752469415e5c7464bbfa37896df6015", "1.12.0--r43hdfd78af_0": "sha256:dc95d965823e43cbafc5d4dd144d85110ca016ebee9f86491461b10f087e34ca", "1.16.0--r44hdfd78af_0": "sha256:a27388c10f94c7bcfbf340314f5715d450026782ba868b27c96b433b24f7d907"}, "docker": "quay.io/biocontainers/bioconductor-scp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scp.
shpc-registry automated BioContainers addition for bioconductor-scp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scp:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scp/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scp/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scp

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