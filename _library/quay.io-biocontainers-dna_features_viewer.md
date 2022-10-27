---
layout: container
name:  "quay.io/biocontainers/dna_features_viewer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dna_features_viewer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dna_features_viewer/container.yaml"
updated_at: "2022-10-27 00:27:04.641907"
latest: "3.1.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/dna_features_viewer"

versions:
 - "3.1.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for dna_features_viewer"
config: {"url": "https://biocontainers.pro/tools/dna_features_viewer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dna_features_viewer", "latest": {"3.1.1--pyh5e36f6f_0": "sha256:eeef07193d6c5ac4e4d31291fa6d6d8778c601a328055dc34dbf8b185db542a6"}, "tags": {"3.1.1--pyh5e36f6f_0": "sha256:eeef07193d6c5ac4e4d31291fa6d6d8778c601a328055dc34dbf8b185db542a6"}, "docker": "quay.io/biocontainers/dna_features_viewer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/dna_features_viewer.
shpc-registry automated BioContainers addition for dna_features_viewer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dna_features_viewer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dna_features_viewer:3.1.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dna_features_viewer/3.1.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/dna_features_viewer/3.1.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dna_features_viewer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dna_features_viewer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dna_features_viewer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dna_features_viewer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dna_features_viewer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dna_features_viewer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### dna_features_viewer

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