---
layout: container
name:  "quay.io/biocontainers/bioconductor-hopach"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hopach/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hopach/container.yaml"
updated_at: "2025-04-06 03:51:20.281725"
latest: "2.66.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hopach"

versions:
 - "2.54.0--r41hc0cfd56_2"
 - "2.58.0--r42hc0cfd56_0"
 - "2.58.0--r42ha9d7317_1"
 - "2.60.0--r43ha9d7317_0"
 - "2.62.0--r43ha9d7317_0"
 - "2.66.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hopach"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hopach", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hopach", "latest": {"2.66.0--r44h3df3fcb_0": "sha256:2a6098869899a67349eb333ac47b9d195f6efae11450cbcd7a195d2e0fabfeac"}, "tags": {"2.54.0--r41hc0cfd56_2": "sha256:a9ada561104f5a197859106c33e5f516830d3e3a3b5611382cc851179ef083c1", "2.58.0--r42hc0cfd56_0": "sha256:2927cdcb00fb64ab8434f33f3437e26e58fa9679af9bcd2e7cf68ac92d140bef", "2.58.0--r42ha9d7317_1": "sha256:d506269b56ea4b3156184f8b407022400776cfd88898a86e9f2f410e3d0e1503", "2.60.0--r43ha9d7317_0": "sha256:ba303758fe18960a61f7e7f4d01e8ef5b0df524e1dc3c774fe8838e4cea443a5", "2.62.0--r43ha9d7317_0": "sha256:b817c173d876f7f324f518ebdd764563cba62263bdcbfe2e1aa08729c1ed160a", "2.66.0--r44h3df3fcb_0": "sha256:2a6098869899a67349eb333ac47b9d195f6efae11450cbcd7a195d2e0fabfeac"}, "docker": "quay.io/biocontainers/bioconductor-hopach"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hopach.
shpc-registry automated BioContainers addition for bioconductor-hopach
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hopach
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hopach:2.66.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hopach/2.66.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-hopach/2.66.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hopach-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hopach-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hopach-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hopach-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hopach-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hopach-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hopach

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