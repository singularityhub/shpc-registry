---
layout: container
name:  "quay.io/biocontainers/bioconductor-scpca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scpca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scpca/container.yaml"
updated_at: "2024-10-25 03:42:02.450819"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scpca"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scpca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scpca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scpca", "latest": {"1.16.0--r43hdfd78af_0": "sha256:c1098a2bb27d3dd5184edde3cf3d2a1f003cc6acd2b58c173ece194adba45c91"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a73c20cdf3ca1c6da8709eb9a5695238b6dff0a5f48e2732bc76ff9057e71db3", "1.12.0--r42hdfd78af_0": "sha256:881e0be5fb555af678c380dc62e50158f6dfc8c19dd1adc14fb165bf9316ba20", "1.14.0--r43hdfd78af_0": "sha256:66399af0965414b3aaf2a4c76e8db3cc1a38b354398de8ebdcc7d8846ffca4d7", "1.16.0--r43hdfd78af_0": "sha256:c1098a2bb27d3dd5184edde3cf3d2a1f003cc6acd2b58c173ece194adba45c91"}, "docker": "quay.io/biocontainers/bioconductor-scpca"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scpca.
shpc-registry automated BioContainers addition for bioconductor-scpca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scpca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scpca:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scpca/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scpca/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scpca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scpca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scpca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scpca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scpca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scpca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scpca

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