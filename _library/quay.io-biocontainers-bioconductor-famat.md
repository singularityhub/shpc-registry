---
layout: container
name:  "quay.io/biocontainers/bioconductor-famat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-famat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-famat/container.yaml"
updated_at: "2024-08-19 03:15:21.088630"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-famat"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-famat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-famat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-famat", "latest": {"1.12.0--r43hdfd78af_0": "sha256:6ff9366df16313fbd89a4da33b522808dd0b38dd88d399424ddc0abce91b69dc"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:a6fae9aa818ac1cca6ba724f07c9222a86a3992ba1c6969e5677804fdd6385b9", "1.8.0--r42hdfd78af_0": "sha256:e64d9df0b904b5d528363edcae81189f224c1f3115256f21d25f2effd770b0a4", "1.10.0--r43hdfd78af_0": "sha256:6b43518ca6e73896248228951d0df45691b51af08f7ce2f9c52333349c7246a5", "1.12.0--r43hdfd78af_0": "sha256:6ff9366df16313fbd89a4da33b522808dd0b38dd88d399424ddc0abce91b69dc"}, "docker": "quay.io/biocontainers/bioconductor-famat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-famat.
shpc-registry automated BioContainers addition for bioconductor-famat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-famat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-famat:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-famat/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-famat/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-famat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-famat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-famat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-famat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-famat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-famat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-famat

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