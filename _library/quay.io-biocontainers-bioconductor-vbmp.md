---
layout: container
name:  "quay.io/biocontainers/bioconductor-vbmp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vbmp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vbmp/container.yaml"
updated_at: "2024-01-22 02:56:03.574461"
latest: "1.70.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vbmp"

versions:
 - "1.62.0--r41hdfd78af_0"
 - "1.66.0--r42hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vbmp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vbmp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vbmp", "latest": {"1.70.0--r43hdfd78af_0": "sha256:d1f3388226912ee0831a3a2e877be5dd972dc25b800d88ed8c6086c85e6536c9"}, "tags": {"1.62.0--r41hdfd78af_0": "sha256:d3f7b8c7324913400b182de6a7f695fb6bf867f7fabec9acdbdfed3eca89d2db", "1.66.0--r42hdfd78af_0": "sha256:dc6e2255e22d6329cbb5902505a1070ab9b7c59e04c14f2752867c69638777c5", "1.68.0--r43hdfd78af_0": "sha256:7aca52bb953d7338163ec4f6fc5680f8aabb274f216e128b62a35894e1401206", "1.70.0--r43hdfd78af_0": "sha256:d1f3388226912ee0831a3a2e877be5dd972dc25b800d88ed8c6086c85e6536c9"}, "docker": "quay.io/biocontainers/bioconductor-vbmp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vbmp.
shpc-registry automated BioContainers addition for bioconductor-vbmp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vbmp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vbmp:1.70.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vbmp/1.70.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-vbmp/1.70.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vbmp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vbmp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vbmp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vbmp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vbmp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vbmp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vbmp

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