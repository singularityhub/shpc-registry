---
layout: container
name:  "quay.io/biocontainers/bioconductor-cma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cma/container.yaml"
updated_at: "2025-04-05 03:00:42.281200"
latest: "1.64.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cma"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.64.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cma", "latest": {"1.64.0--r44hdfd78af_0": "sha256:971cce69dd9e74e217cba202b6d6ff0256d5eed09bc3a946164e4d83e62b75cd"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:f4a42a8593f1a8bfea726902a12e253bdee67edddc01a72050a6daa56431c309", "1.56.0--r42hdfd78af_0": "sha256:d1592a27eda9860d02778f2342346fd3902cb732ba9e61c1477b0dd3933a356a", "1.58.0--r43hdfd78af_0": "sha256:ceab2fab81d4fd3ee589496ea8deac927a070948005c820ecd8ff436934c014f", "1.60.0--r43hdfd78af_0": "sha256:220d40eca9cea11debe7422bc2a3918ca0885145f190849ed26ca5eb4a858d55", "1.64.0--r44hdfd78af_0": "sha256:971cce69dd9e74e217cba202b6d6ff0256d5eed09bc3a946164e4d83e62b75cd"}, "docker": "quay.io/biocontainers/bioconductor-cma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cma.
shpc-registry automated BioContainers addition for bioconductor-cma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cma:1.64.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cma/1.64.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cma/1.64.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cma

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