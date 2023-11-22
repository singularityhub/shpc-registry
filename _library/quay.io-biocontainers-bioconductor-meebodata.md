---
layout: container
name:  "quay.io/biocontainers/bioconductor-meebodata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-meebodata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-meebodata/container.yaml"
updated_at: "2023-11-22 02:44:55.645182"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-meebodata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-meebodata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-meebodata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-meebodata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:592ae1ab97224d85ec06da263fd5e4eb76b2dac8ed8e5da1f04213db81ff8a08"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:83862cc70b8d3dc3eca4e8c57d3ce7f793a8be3bc686e2821cdaf9844fdb0081", "1.35.0--r42hdfd78af_0": "sha256:9835e3a8580204e1657be5d41505c49d66636252b0b6554e130768d47d04813f", "1.38.0--r43hdfd78af_0": "sha256:592ae1ab97224d85ec06da263fd5e4eb76b2dac8ed8e5da1f04213db81ff8a08"}, "docker": "quay.io/biocontainers/bioconductor-meebodata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-meebodata.
shpc-registry automated BioContainers addition for bioconductor-meebodata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-meebodata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-meebodata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-meebodata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-meebodata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-meebodata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meebodata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meebodata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-meebodata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-meebodata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-meebodata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-meebodata

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