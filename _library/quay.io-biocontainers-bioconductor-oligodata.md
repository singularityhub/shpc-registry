---
layout: container
name:  "quay.io/biocontainers/bioconductor-oligodata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oligodata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oligodata/container.yaml"
updated_at: "2024-06-12 03:19:17.479425"
latest: "1.8.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-oligodata"

versions:
 - "1.8.0--r41hdfd78af_9"
 - "1.8.0--r42hdfd78af_10"
 - "1.8.0--r43hdfd78af_11"
 - "1.8.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-oligodata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oligodata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oligodata", "latest": {"1.8.0--r43hdfd78af_12": "sha256:5d4fea400da5cfdf3270834a5fb9fba0719e7df5a08d62d4020efffb04a3b9f5"}, "tags": {"1.8.0--r41hdfd78af_9": "sha256:5248fe1547c4a4453e1f9d61579b8dc3ade53e6c37e73c0b1ddb0a84a5da1625", "1.8.0--r42hdfd78af_10": "sha256:6b9a090d38bb639b02e027bfe5effb3e08862ad07a0a617e4b8c607c4ead6bd1", "1.8.0--r43hdfd78af_11": "sha256:ce75cacdddddc4a800cb8035bd4a5056436e68ffba6e6cb3a2e3fefbbce774c0", "1.8.0--r43hdfd78af_12": "sha256:5d4fea400da5cfdf3270834a5fb9fba0719e7df5a08d62d4020efffb04a3b9f5"}, "docker": "quay.io/biocontainers/bioconductor-oligodata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oligodata.
shpc-registry automated BioContainers addition for bioconductor-oligodata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oligodata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oligodata:1.8.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oligodata/1.8.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-oligodata/1.8.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oligodata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oligodata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oligodata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oligodata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oligodata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oligodata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-oligodata

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