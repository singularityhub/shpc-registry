---
layout: container
name:  "quay.io/biocontainers/bioconductor-tronco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tronco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tronco/container.yaml"
updated_at: "2024-10-27 03:08:25.903591"
latest: "2.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tronco"

versions:
 - "2.26.0--r41hdfd78af_0"
 - "2.30.0--r42hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tronco"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tronco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tronco", "latest": {"2.34.0--r43hdfd78af_0": "sha256:8ad5fd6858f3e2e3893d6baa189e2efa6afcef091d2880a40911ef5fba5e2367"}, "tags": {"2.26.0--r41hdfd78af_0": "sha256:66b2cad56fb0163745fa2224d682100d6c3722d48f4e5056bdffaeb29e471f2e", "2.30.0--r42hdfd78af_0": "sha256:5eef2ac53bef5d74edf6be39d6fbbed8f6615309f26c7bf4248bea657e5b988b", "2.32.0--r43hdfd78af_0": "sha256:3effecd27e6252d356e79aef2c70afb63354df1cdace3809a7bb12ce91914a0c", "2.34.0--r43hdfd78af_0": "sha256:8ad5fd6858f3e2e3893d6baa189e2efa6afcef091d2880a40911ef5fba5e2367"}, "docker": "quay.io/biocontainers/bioconductor-tronco"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tronco.
shpc-registry automated BioContainers addition for bioconductor-tronco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tronco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tronco:2.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tronco/2.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tronco/2.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tronco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tronco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tronco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tronco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tronco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tronco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tronco

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