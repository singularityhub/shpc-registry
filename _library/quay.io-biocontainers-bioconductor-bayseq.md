---
layout: container
name:  "quay.io/biocontainers/bioconductor-bayseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bayseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bayseq/container.yaml"
updated_at: "2024-12-08 03:48:36.254645"
latest: "2.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bayseq"

versions:
 - "2.28.0--r41hdfd78af_0"
 - "2.31.0--r42hdfd78af_1"
 - "2.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bayseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bayseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bayseq", "latest": {"2.36.0--r43hdfd78af_0": "sha256:c25fa2ae9627ae348a3c0e200797b4576df4e247a86887636e745177f1d90e53"}, "tags": {"2.28.0--r41hdfd78af_0": "sha256:4f9f06df6f015e4396a839109c890110b4689437f18d18dc9afc3adc8a8e19e8", "2.31.0--r42hdfd78af_1": "sha256:5e6ef92ecef1a1fb68ce0a2872aac53354ae708d1220b5cf4b913d636bc6635b", "2.36.0--r43hdfd78af_0": "sha256:c25fa2ae9627ae348a3c0e200797b4576df4e247a86887636e745177f1d90e53"}, "docker": "quay.io/biocontainers/bioconductor-bayseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bayseq.
shpc-registry automated BioContainers addition for bioconductor-bayseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bayseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bayseq:2.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bayseq/2.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bayseq/2.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bayseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bayseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bayseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bayseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bayseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bayseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bayseq

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