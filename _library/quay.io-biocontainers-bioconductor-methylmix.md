---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylmix/container.yaml"
updated_at: "2025-12-23 04:05:49.440633"
latest: "2.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylmix"

versions:
 - "2.24.0--r41hdfd78af_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylmix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylmix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylmix", "latest": {"2.36.0--r44hdfd78af_0": "sha256:b9d55cd7cd979184c18553cfb3c2cd674809e89b50e59ff531d704e1deb59ab6"}, "tags": {"2.24.0--r41hdfd78af_0": "sha256:6424aa1a6941d1b32dad4fb21d2f54b52a1fdd4b756d23e8fa60babde5f0c511", "2.28.0--r42hdfd78af_0": "sha256:5e3c2a87cc067607f97e0d38cec59e239a1109747914af7483bf19bf5e0f54a0", "2.30.0--r43hdfd78af_0": "sha256:7b44f4e4fa5c0c92ee2947250e4f79aefba18ca2ec49277179aba2184cfd3f94", "2.32.0--r43hdfd78af_0": "sha256:8edf9553e6ab5c67380da2086357baf35cc7741a60b119f022ee5448998cdad0", "2.36.0--r44hdfd78af_0": "sha256:b9d55cd7cd979184c18553cfb3c2cd674809e89b50e59ff531d704e1deb59ab6"}, "docker": "quay.io/biocontainers/bioconductor-methylmix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylmix.
shpc-registry automated BioContainers addition for bioconductor-methylmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylmix:2.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylmix/2.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylmix/2.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylmix

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