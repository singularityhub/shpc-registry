---
layout: container
name:  "quay.io/biocontainers/bioconductor-grohmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-grohmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-grohmm/container.yaml"
updated_at: "2025-04-17 03:07:33.469691"
latest: "1.36.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-grohmm"

versions:
 - "1.28.0--r41hc0cfd56_2"
 - "1.32.0--r42hc0cfd56_0"
 - "1.32.0--r42ha9d7317_1"
 - "1.34.0--r43ha9d7317_0"
 - "1.36.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-grohmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-grohmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-grohmm", "latest": {"1.36.0--r43ha9d7317_0": "sha256:62d8096ced7eabc6f892ac5b043e2609f47e7d8b5c456602015c66b394755094"}, "tags": {"1.28.0--r41hc0cfd56_2": "sha256:562e3045ce67119223be37fdc69bac8f2c41c27249a01596135de0be37d1d167", "1.32.0--r42hc0cfd56_0": "sha256:5c52599b9ad2a67bd4f4616c5cad8266575c230726fd4c3c403be2c80da39dc8", "1.32.0--r42ha9d7317_1": "sha256:921e5a9376468c0a28458bcb18cdf9fea9a68f342912de6f936f4f3d11c08e14", "1.34.0--r43ha9d7317_0": "sha256:71d8b898646e8815bf30e6b8afa1d27c6496a6014e029cc4deea27057415f071", "1.36.0--r43ha9d7317_0": "sha256:62d8096ced7eabc6f892ac5b043e2609f47e7d8b5c456602015c66b394755094"}, "docker": "quay.io/biocontainers/bioconductor-grohmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-grohmm.
shpc-registry automated BioContainers addition for bioconductor-grohmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-grohmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-grohmm:1.36.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-grohmm/1.36.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-grohmm/1.36.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-grohmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grohmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grohmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-grohmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-grohmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-grohmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-grohmm

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