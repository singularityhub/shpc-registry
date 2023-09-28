---
layout: container
name:  "quay.io/biocontainers/bioconductor-motifstack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-motifstack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-motifstack/container.yaml"
updated_at: "2023-09-28 02:33:54.268503"
latest: "1.44.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-motifstack"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-motifstack"
config: {"url": "https://biocontainers.pro/tools/bioconductor-motifstack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-motifstack", "latest": {"1.44.1--r43hdfd78af_0": "sha256:9345723dc0c95c1a7b07992a6a2cd62a4b18a3396420103c506c82bae59eb79b"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:e00b080fe28dd4d7935ae911687935b35d00aac42b529fd6d9e604b47dc397ef", "1.42.0--r42hdfd78af_0": "sha256:fdd466405d5bc7d162cbcf8958dee6ba9131a4b3cb06fe5f24f24a9796703225", "1.44.1--r43hdfd78af_0": "sha256:9345723dc0c95c1a7b07992a6a2cd62a4b18a3396420103c506c82bae59eb79b"}, "docker": "quay.io/biocontainers/bioconductor-motifstack"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-motifstack.
shpc-registry automated BioContainers addition for bioconductor-motifstack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-motifstack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-motifstack:1.44.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-motifstack/1.44.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-motifstack/1.44.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-motifstack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifstack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifstack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-motifstack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-motifstack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-motifstack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-motifstack

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