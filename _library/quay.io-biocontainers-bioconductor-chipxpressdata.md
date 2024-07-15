---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipxpressdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipxpressdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipxpressdata/container.yaml"
updated_at: "2024-07-15 03:23:20.375741"
latest: "1.36.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipxpressdata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.35.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipxpressdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipxpressdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipxpressdata", "latest": {"1.36.0--r42hdfd78af_0": "sha256:25b5d7a1b89137a62609715adbd0d4ce45f3608cba33eda391caf4324b9209ce"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:82d1ce53d58e1ef8a884c19d719d46302e1b22272dc6bd7222fbfed48cd49ee0", "1.36.0--r42hdfd78af_0": "sha256:25b5d7a1b89137a62609715adbd0d4ce45f3608cba33eda391caf4324b9209ce", "1.35.0--r42hdfd78af_0": "sha256:276059e2475ce92f529967d4df3bfc13caee58c7d893cfaa336bc144713ffedb"}, "docker": "quay.io/biocontainers/bioconductor-chipxpressdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipxpressdata.
shpc-registry automated BioContainers addition for bioconductor-chipxpressdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipxpressdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipxpressdata:1.36.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipxpressdata/1.36.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipxpressdata/1.36.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipxpressdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipxpressdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipxpressdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipxpressdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipxpressdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipxpressdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chipxpressdata

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