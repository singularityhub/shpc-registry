---
layout: container
name:  "quay.io/biocontainers/bioconductor-leukemiaseset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-leukemiaseset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-leukemiaseset/container.yaml"
updated_at: "2023-02-17 03:17:20.446942"
latest: "1.34.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-leukemiaseset"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-leukemiaseset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-leukemiaseset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-leukemiaseset", "latest": {"1.34.0--r42hdfd78af_0": "sha256:f432cfb52dc68b51a1954580bd3371ea23c981193bbadc7e9e3fcb035dffddc9"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:2405678e612b4c233154d10c8f4e72e140ec1828caeb3a92e009ce48f1e7fbc2", "1.34.0--r42hdfd78af_0": "sha256:f432cfb52dc68b51a1954580bd3371ea23c981193bbadc7e9e3fcb035dffddc9"}, "docker": "quay.io/biocontainers/bioconductor-leukemiaseset"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-leukemiaseset.
shpc-registry automated BioContainers addition for bioconductor-leukemiaseset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-leukemiaseset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-leukemiaseset:1.34.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-leukemiaseset/1.34.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-leukemiaseset/1.34.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-leukemiaseset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-leukemiaseset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-leukemiaseset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-leukemiaseset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-leukemiaseset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-leukemiaseset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-leukemiaseset

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