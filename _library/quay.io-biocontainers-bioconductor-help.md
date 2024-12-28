---
layout: container
name:  "quay.io/biocontainers/bioconductor-help"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-help/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-help/container.yaml"
updated_at: "2024-12-28 03:23:28.897948"
latest: "1.64.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-help"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.64.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-help"
config: {"url": "https://biocontainers.pro/tools/bioconductor-help", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-help", "latest": {"1.64.0--r44hdfd78af_0": "sha256:3d3fe97782db8409299cae89d51d7c52366a4f4cc8278f40542687616bd1c537"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:581c7fd7b9b6c1fe7c07cf24b626836ec89c758e4ecc8dd3b0d86b3b63fa75f8", "1.56.0--r42hdfd78af_0": "sha256:a8d57c8b5e7d7963f87d6a26bfdd0972eec9b20545b86539555766133f7ebe45", "1.58.0--r43hdfd78af_0": "sha256:44bbb97cbfa5f0ab855b06721c57132654983c08f45d4d1733b70e808113eab1", "1.60.0--r43hdfd78af_0": "sha256:b75bff2ff9c6b476e7d01dd7fd00ce6afed67f7d865374000f72a16fdf9ed042", "1.64.0--r44hdfd78af_0": "sha256:3d3fe97782db8409299cae89d51d7c52366a4f4cc8278f40542687616bd1c537"}, "docker": "quay.io/biocontainers/bioconductor-help"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-help.
shpc-registry automated BioContainers addition for bioconductor-help
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-help
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-help:1.64.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-help/1.64.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-help/1.64.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-help-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-help-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-help-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-help-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-help-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-help-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-help

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