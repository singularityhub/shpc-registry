---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotationhub"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotationhub/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotationhub/container.yaml"
updated_at: "2025-01-21 03:27:31.845558"
latest: "3.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotationhub"

versions:
 - "3.2.0--r41hdfd78af_0"
 - "3.6.0--r42hdfd78af_0"
 - "3.8.0--r43hdfd78af_0"
 - "3.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotationhub"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotationhub", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotationhub", "latest": {"3.10.0--r43hdfd78af_0": "sha256:856a2b0a4e1e252070c311a1b3e0b5b5706c482832f7a0a9b223f45e4f173607"}, "tags": {"3.2.0--r41hdfd78af_0": "sha256:03512824214ad768fbb83e71814e8ba339ff608257c73dcd818b93b45440345b", "3.6.0--r42hdfd78af_0": "sha256:fbc9d8102d1da40fa5a0a75a410b1f72c4a4f8e861ccfc1530d4a5dfa4d5c100", "3.8.0--r43hdfd78af_0": "sha256:8017f9e60d32be4f366b2e77f1e69de0b70b9b4df853e34737f34ada5f88a0b7", "3.10.0--r43hdfd78af_0": "sha256:856a2b0a4e1e252070c311a1b3e0b5b5706c482832f7a0a9b223f45e4f173607"}, "docker": "quay.io/biocontainers/bioconductor-annotationhub"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotationhub.
shpc-registry automated BioContainers addition for bioconductor-annotationhub
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationhub
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationhub:3.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotationhub/3.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotationhub/3.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotationhub-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationhub-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationhub-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotationhub-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotationhub-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotationhub-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-annotationhub

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