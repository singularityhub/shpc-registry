---
layout: container
name:  "quay.io/biocontainers/bioconductor-spiky"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spiky/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spiky/container.yaml"
updated_at: "2025-05-26 11:47:06.727112"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spiky"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spiky"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spiky", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spiky", "latest": {"1.12.0--r44hdfd78af_0": "sha256:7a4b9a1864d743c3d8df3d8ea25dfe9065492516c543a673d3b917279d216cce"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:22c2562868ab821d876a8a00179971de12f129724d0ccd72a9c40a4d32b77f0f", "1.4.0--r42hdfd78af_0": "sha256:102b1f5c0cde79383ba1e1196de723e304ed053ef7bc0baf1af8cdd0d726a3a2", "1.6.0--r43hdfd78af_0": "sha256:b4ce224029ca213a45ada7b304a6410d52863ef9ffb7b07024ae27e71ee29b84", "1.8.0--r43hdfd78af_0": "sha256:1bb82cf97de986db5d77262bbef4abed646079e578ae46080b950aa9ebd27c6b", "1.12.0--r44hdfd78af_0": "sha256:7a4b9a1864d743c3d8df3d8ea25dfe9065492516c543a673d3b917279d216cce"}, "docker": "quay.io/biocontainers/bioconductor-spiky"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spiky.
shpc-registry automated BioContainers addition for bioconductor-spiky
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spiky
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spiky:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spiky/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spiky/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spiky-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spiky-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spiky-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spiky-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spiky-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spiky-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spiky

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