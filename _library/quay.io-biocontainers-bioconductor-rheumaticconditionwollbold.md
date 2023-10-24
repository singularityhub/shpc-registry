---
layout: container
name:  "quay.io/biocontainers/bioconductor-rheumaticconditionwollbold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rheumaticconditionwollbold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rheumaticconditionwollbold/container.yaml"
updated_at: "2023-10-24 02:54:48.735148"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rheumaticconditionwollbold"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rheumaticconditionwollbold"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rheumaticconditionwollbold", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rheumaticconditionwollbold", "latest": {"1.38.0--r43hdfd78af_0": "sha256:c9bc0f22c82df98d0cb6efc3840de9da27c87e53de4080e90b652f7e42cca927"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:8d80483382e46a5ec2a4fe5a62714fb8960cb24c0c34735fd8695fdf1da7ef09", "1.35.0--r42hdfd78af_0": "sha256:77d7cfefceff8453cb608811b2860814fb30d52a832bb6864dfd98a744b0ed21", "1.38.0--r43hdfd78af_0": "sha256:c9bc0f22c82df98d0cb6efc3840de9da27c87e53de4080e90b652f7e42cca927"}, "docker": "quay.io/biocontainers/bioconductor-rheumaticconditionwollbold"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rheumaticconditionwollbold.
shpc-registry automated BioContainers addition for bioconductor-rheumaticconditionwollbold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rheumaticconditionwollbold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rheumaticconditionwollbold:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rheumaticconditionwollbold/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rheumaticconditionwollbold/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rheumaticconditionwollbold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rheumaticconditionwollbold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rheumaticconditionwollbold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rheumaticconditionwollbold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rheumaticconditionwollbold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rheumaticconditionwollbold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rheumaticconditionwollbold

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