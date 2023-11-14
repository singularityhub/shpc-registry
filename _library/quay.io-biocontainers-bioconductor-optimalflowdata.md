---
layout: container
name:  "quay.io/biocontainers/bioconductor-optimalflowdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-optimalflowdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-optimalflowdata/container.yaml"
updated_at: "2023-11-14 02:49:35.169739"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-optimalflowdata"

versions:
 - "1.6.0--r41hdfd78af_1"
 - "1.10.0--r42hdfd78af_0"
 - "1.9.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-optimalflowdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-optimalflowdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-optimalflowdata", "latest": {"1.12.0--r43hdfd78af_0": "sha256:5eefc5eda248b2fd4ee555d6c95bc0423e6a55b8fdc14a7ef4ec5988d8474a60"}, "tags": {"1.6.0--r41hdfd78af_1": "sha256:4d4e5c9c64d83d143b6381b132a31af5d36b4c08838f083c1d8cd4f7dd75c80b", "1.10.0--r42hdfd78af_0": "sha256:89f9784c5a7296269fbae3715ac89b305f2c0e6b0a9b88739671eced198f04d9", "1.9.0--r42hdfd78af_0": "sha256:cbe8a36d98004baecf4c9da32936c0ffe4a81517739e2a5f691587888948f8e0", "1.12.0--r43hdfd78af_0": "sha256:5eefc5eda248b2fd4ee555d6c95bc0423e6a55b8fdc14a7ef4ec5988d8474a60"}, "docker": "quay.io/biocontainers/bioconductor-optimalflowdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-optimalflowdata.
shpc-registry automated BioContainers addition for bioconductor-optimalflowdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-optimalflowdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-optimalflowdata:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-optimalflowdata/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-optimalflowdata/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-optimalflowdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-optimalflowdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-optimalflowdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-optimalflowdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-optimalflowdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-optimalflowdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-optimalflowdata

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