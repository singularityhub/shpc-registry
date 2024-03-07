---
layout: container
name:  "quay.io/biocontainers/bioconductor-lipidr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lipidr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lipidr/container.yaml"
updated_at: "2024-03-07 00:06:33.468838"
latest: "2.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lipidr"

versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.12.0--r42hdfd78af_0"
 - "2.14.1--r43hdfd78af_0"
 - "2.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lipidr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lipidr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lipidr", "latest": {"2.16.0--r43hdfd78af_0": "sha256:1dd6f3c4c96ea4ed509694c6a03024cd92c8d0340d5b48bfa3a11bd235b447f3"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:4e41e52e87ca47d541599b364f496304f160df7e9723675dca301c24cf36c5fd", "2.12.0--r42hdfd78af_0": "sha256:453eb80d1ef2d7e99af0410d281bbf72e7686e2417a0d0bda3e63135a275b35c", "2.14.1--r43hdfd78af_0": "sha256:84d1b4f34813c3c135bcd39df9ebc051ef08ed087d7b97c527e99f1c70583268", "2.16.0--r43hdfd78af_0": "sha256:1dd6f3c4c96ea4ed509694c6a03024cd92c8d0340d5b48bfa3a11bd235b447f3"}, "docker": "quay.io/biocontainers/bioconductor-lipidr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lipidr.
shpc-registry automated BioContainers addition for bioconductor-lipidr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lipidr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lipidr:2.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lipidr/2.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lipidr/2.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lipidr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lipidr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lipidr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lipidr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lipidr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lipidr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lipidr

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