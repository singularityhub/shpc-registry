---
layout: container
name:  "quay.io/biocontainers/bioconductor-bumpymatrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bumpymatrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bumpymatrix/container.yaml"
updated_at: "2025-05-18 03:50:25.572913"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bumpymatrix"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bumpymatrix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bumpymatrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bumpymatrix", "latest": {"1.14.0--r44hdfd78af_0": "sha256:c3644400a1ac12f228dfe4f8562bdd4f9f80d4f45b85f486b6c037219d29ccfd"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:b3d766bd1b8b4a452e8f9fa13dd97208f7a3100b91b3c1276a6a3ff8efd85281", "1.6.0--r42hdfd78af_0": "sha256:c4757a1c5a00b36d3f8b8974a3b8b7132aa71adff22e20572b053e21b9c62b69", "1.8.0--r43hdfd78af_0": "sha256:172fc034ee8f93ba28a36d451be10832cac82b673e0cc44eeb42cd13d30bb714", "1.10.0--r43hdfd78af_0": "sha256:2eb718351c4d6286d18db40792d26bf060d9b05bfefc3fe493d525e392801832", "1.14.0--r44hdfd78af_0": "sha256:c3644400a1ac12f228dfe4f8562bdd4f9f80d4f45b85f486b6c037219d29ccfd"}, "docker": "quay.io/biocontainers/bioconductor-bumpymatrix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bumpymatrix.
shpc-registry automated BioContainers addition for bioconductor-bumpymatrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bumpymatrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bumpymatrix:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bumpymatrix/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bumpymatrix/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bumpymatrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bumpymatrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bumpymatrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bumpymatrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bumpymatrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bumpymatrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bumpymatrix

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