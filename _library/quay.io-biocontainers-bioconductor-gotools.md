---
layout: container
name:  "quay.io/biocontainers/bioconductor-gotools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gotools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gotools/container.yaml"
updated_at: "2024-01-06 02:45:22.173126"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gotools"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gotools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gotools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gotools", "latest": {"1.74.0--r43hdfd78af_0": "sha256:1c47a58c67eb863af0238a0797c4272554642fd39faebcbc136bf6170346493b"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:d967fc8b1b3eab8964f35b55dfe2ea7200c6814f04620642ca4caae25e7a50c5", "1.72.0--r42hdfd78af_0": "sha256:c1760931424192f47535f89191bd5327b377103534d53c063dd1f0d1b6f04b0d", "1.74.0--r43hdfd78af_0": "sha256:1c47a58c67eb863af0238a0797c4272554642fd39faebcbc136bf6170346493b"}, "docker": "quay.io/biocontainers/bioconductor-gotools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gotools.
shpc-registry automated BioContainers addition for bioconductor-gotools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gotools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gotools:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gotools/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gotools/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gotools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gotools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gotools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gotools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gotools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gotools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gotools

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