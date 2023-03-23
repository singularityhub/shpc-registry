---
layout: container
name:  "quay.io/biocontainers/bioconductor-reactomepa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-reactomepa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-reactomepa/container.yaml"
updated_at: "2023-03-23 02:34:59.393034"
latest: "1.42.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-reactomepa"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-reactomepa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-reactomepa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-reactomepa", "latest": {"1.42.0--r42hdfd78af_0": "sha256:9e5333083924cccf0acee88f2dbc513a6bde131c380f967d4132ac3084aea185"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:4f795a4a1ac96bcf96f53002b811b2e7a379a690be9d3a7573ce5c5bc103a943", "1.42.0--r42hdfd78af_0": "sha256:9e5333083924cccf0acee88f2dbc513a6bde131c380f967d4132ac3084aea185"}, "docker": "quay.io/biocontainers/bioconductor-reactomepa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-reactomepa.
shpc-registry automated BioContainers addition for bioconductor-reactomepa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-reactomepa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-reactomepa:1.42.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-reactomepa/1.42.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-reactomepa/1.42.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-reactomepa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reactomepa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reactomepa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-reactomepa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-reactomepa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-reactomepa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-reactomepa

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