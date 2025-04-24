---
layout: container
name:  "quay.io/biocontainers/bioconductor-phyloseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phyloseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phyloseq/container.yaml"
updated_at: "2025-04-24 03:37:31.692298"
latest: "1.50.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phyloseq"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.50.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phyloseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phyloseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phyloseq", "latest": {"1.50.0--r44hdfd78af_0": "sha256:c9120b7e9faa87cea8c7cccfb13de0eb7d67bfe14f30d40c167e82d006dcbfab"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:8fc624578f508204af5738683a7388f896e8484b2edf41f077466baf70d3d739", "1.42.0--r42hdfd78af_0": "sha256:1c50bd93eb4e71cf44fb8b1bc24167c5551b18456061f41f0fab7ac448dbafc8", "1.44.0--r43hdfd78af_0": "sha256:11b021338600e7c27ec71977226b560fc4b577ae535ff23cc0242062c9c64420", "1.46.0--r43hdfd78af_0": "sha256:0c02efeec8dcfabcc970d9fe3cae374d72796945e0392f022c79f608441ab668", "1.50.0--r44hdfd78af_0": "sha256:c9120b7e9faa87cea8c7cccfb13de0eb7d67bfe14f30d40c167e82d006dcbfab"}, "docker": "quay.io/biocontainers/bioconductor-phyloseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phyloseq.
shpc-registry automated BioContainers addition for bioconductor-phyloseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phyloseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phyloseq:1.50.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phyloseq/1.50.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phyloseq/1.50.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phyloseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phyloseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phyloseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phyloseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phyloseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phyloseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phyloseq

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