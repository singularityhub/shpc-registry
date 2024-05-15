---
layout: container
name:  "quay.io/biocontainers/bioconductor-deconvr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deconvr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deconvr/container.yaml"
updated_at: "2024-05-15 03:00:00.371633"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-deconvr"

versions:
 - "1.0.1--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-deconvr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deconvr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deconvr", "latest": {"1.8.0--r43hdfd78af_0": "sha256:1dbe5672296f5edf58e295dddafdce4999e38cb4445e0ce9d630b630913d18e6"}, "tags": {"1.0.1--r41hdfd78af_0": "sha256:e7122044a349bfbb6e78f82acec25d8b96f9d3a0259991cde5de364800263332", "1.4.0--r42hdfd78af_0": "sha256:d7fcb4fac882317ec6494a5c70f8bf9d32fa4ef4b627cf3682dee5a836a93ae1", "1.6.0--r43hdfd78af_0": "sha256:c55a30e1d216abc93738538ad975e602c007a4098848c2805c68608735aa8e61", "1.8.0--r43hdfd78af_0": "sha256:1dbe5672296f5edf58e295dddafdce4999e38cb4445e0ce9d630b630913d18e6"}, "docker": "quay.io/biocontainers/bioconductor-deconvr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deconvr.
shpc-registry automated BioContainers addition for bioconductor-deconvr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deconvr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deconvr:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deconvr/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-deconvr/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deconvr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deconvr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deconvr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deconvr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deconvr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deconvr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-deconvr

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