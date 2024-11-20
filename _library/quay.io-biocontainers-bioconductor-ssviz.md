---
layout: container
name:  "quay.io/biocontainers/bioconductor-ssviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ssviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ssviz/container.yaml"
updated_at: "2024-11-20 03:04:04.713696"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ssviz"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ssviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ssviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ssviz", "latest": {"1.36.0--r43hdfd78af_0": "sha256:8ee3fc9546f007dbb655551f77b5329e46d346853d1de626a22b58f931b6925a"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:deab91391b862c7c85fce4d70b5b5446c51810ccd6963f70c3ba953d9519124b", "1.32.0--r42hdfd78af_0": "sha256:726cf5959c35520b76d67197023a0e522e23009689ba4f8d467077bddb9899af", "1.34.0--r43hdfd78af_0": "sha256:fa53bcc5bd3c9d876c7f91b7806c088a2d98873cef2d188aae79c94658fe5209", "1.36.0--r43hdfd78af_0": "sha256:8ee3fc9546f007dbb655551f77b5329e46d346853d1de626a22b58f931b6925a"}, "docker": "quay.io/biocontainers/bioconductor-ssviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ssviz.
shpc-registry automated BioContainers addition for bioconductor-ssviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ssviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ssviz:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ssviz/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ssviz/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ssviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ssviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ssviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ssviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ssviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ssviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ssviz

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