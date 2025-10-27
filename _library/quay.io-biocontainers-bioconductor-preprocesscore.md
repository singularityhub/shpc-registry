---
layout: container
name:  "quay.io/biocontainers/bioconductor-preprocesscore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-preprocesscore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-preprocesscore/container.yaml"
updated_at: "2025-10-27 04:09:27.303112"
latest: "1.68.0--r44h3df3fcb_1"
container_url: "https://biocontainers.pro/tools/bioconductor-preprocesscore"

versions:
 - "1.56.0--r41hc0cfd56_3"
 - "1.60.0--r42hc0cfd56_0"
 - "1.60.2--r42hc0cfd56_0"
 - "1.60.2--r42ha9d7317_2"
 - "1.62.1--r43ha9d7317_1"
 - "1.64.0--r43ha9d7317_1"
 - "1.64.0--r43ha9d7317_2"
 - "1.68.0--r44h3df3fcb_0"
 - "1.68.0--r44h3df3fcb_1"
description: "shpc-registry automated BioContainers addition for bioconductor-preprocesscore"
config: {"url": "https://biocontainers.pro/tools/bioconductor-preprocesscore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-preprocesscore", "latest": {"1.68.0--r44h3df3fcb_1": "sha256:48d295375c271915f9f625b86019713fd3502b3f5276f60aa6f7a9da772f88b4"}, "tags": {"1.56.0--r41hc0cfd56_3": "sha256:04f16830ab80ff8d1b47df3698ff59af740b2e9da59e15cc4f910da054a7c7b7", "1.60.0--r42hc0cfd56_0": "sha256:d87a72c772626795a2de52db4663c25e790d2e2eb9f9f0f793663f9ea51c939a", "1.60.2--r42hc0cfd56_0": "sha256:45e93a3bc9e4d6eb0e0b62a61d3b630ff18f6fb0f00e952b9b5dd50560d712de", "1.60.2--r42ha9d7317_2": "sha256:150ab94d9b7de05dfa14e79858be93d4d5a8195a063ec4a4ac3ef9cefbfed344", "1.62.1--r43ha9d7317_1": "sha256:c8f70886b49ca56f2ef3754c136f7e9566f41a5a9d2782a7c1709b4b31881bc2", "1.64.0--r43ha9d7317_1": "sha256:0a02e61b085425c027cc637657dc44e4e1ef4009da208e9de89a09772f408e6c", "1.64.0--r43ha9d7317_2": "sha256:85ebb3beb73c3996c2da44ce375f44a5861feb5cfcf57b2b6390edfb8ec360d8", "1.68.0--r44h3df3fcb_0": "sha256:ed5241e09e473920d01cab86cfd95a3ac920f689f44f37169272b825063f69fa", "1.68.0--r44h3df3fcb_1": "sha256:48d295375c271915f9f625b86019713fd3502b3f5276f60aa6f7a9da772f88b4"}, "docker": "quay.io/biocontainers/bioconductor-preprocesscore"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-preprocesscore.
shpc-registry automated BioContainers addition for bioconductor-preprocesscore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-preprocesscore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-preprocesscore:1.68.0--r44h3df3fcb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-preprocesscore/1.68.0--r44h3df3fcb_1
$ module help quay.io/biocontainers/bioconductor-preprocesscore/1.68.0--r44h3df3fcb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-preprocesscore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-preprocesscore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-preprocesscore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-preprocesscore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-preprocesscore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-preprocesscore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-preprocesscore

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