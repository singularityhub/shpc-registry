---
layout: container
name:  "quay.io/biocontainers/bioconductor-seq2pathway"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seq2pathway/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seq2pathway/container.yaml"
updated_at: "2023-07-26 03:24:05.267945"
latest: "1.30.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seq2pathway"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seq2pathway"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seq2pathway", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seq2pathway", "latest": {"1.30.0--r42hdfd78af_0": "sha256:ad453ec39c7ee36830c9328b324c55b529c150ac1c5dd3b4d98a0939341a9b09"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:c46890d76557e0713eb69e69c60bcf0920ca283e80e8bd0c3b45553af3e950b0", "1.30.0--r42hdfd78af_0": "sha256:ad453ec39c7ee36830c9328b324c55b529c150ac1c5dd3b4d98a0939341a9b09"}, "docker": "quay.io/biocontainers/bioconductor-seq2pathway"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seq2pathway.
shpc-registry automated BioContainers addition for bioconductor-seq2pathway
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seq2pathway
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seq2pathway:1.30.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seq2pathway/1.30.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seq2pathway/1.30.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seq2pathway-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seq2pathway-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seq2pathway-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seq2pathway-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seq2pathway-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seq2pathway-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seq2pathway

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