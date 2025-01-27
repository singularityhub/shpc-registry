---
layout: container
name:  "quay.io/biocontainers/bioconductor-maqcsubsetilm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maqcsubsetilm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maqcsubsetilm/container.yaml"
updated_at: "2025-01-27 03:31:37.386124"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maqcsubsetilm"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maqcsubsetilm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maqcsubsetilm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maqcsubsetilm", "latest": {"1.40.0--r43hdfd78af_0": "sha256:587becab3dd98567a799b16448f3a5a1ffd47f0063cb2540bce610dfb0c7d6ef"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:e31b095c84a21901794d31aebce9107efe521e1b013312c91b307876c35261ee", "1.36.0--r42hdfd78af_0": "sha256:2b9724ef8aa17ced95b461311d466353ad6285081d1dd9ce312e2d18f8755dcc", "1.38.0--r43hdfd78af_0": "sha256:fdc36bd2964fe89bfd51dcb03ab6228fc40c87302d31a5c44f06207cde4b8991", "1.40.0--r43hdfd78af_0": "sha256:587becab3dd98567a799b16448f3a5a1ffd47f0063cb2540bce610dfb0c7d6ef"}, "docker": "quay.io/biocontainers/bioconductor-maqcsubsetilm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maqcsubsetilm.
shpc-registry automated BioContainers addition for bioconductor-maqcsubsetilm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maqcsubsetilm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maqcsubsetilm:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maqcsubsetilm/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-maqcsubsetilm/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maqcsubsetilm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maqcsubsetilm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maqcsubsetilm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maqcsubsetilm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maqcsubsetilm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maqcsubsetilm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maqcsubsetilm

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