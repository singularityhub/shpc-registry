---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylpipe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylpipe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylpipe/container.yaml"
updated_at: "2024-01-04 02:39:45.749159"
latest: "1.36.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylpipe"

versions:
 - "1.27.0--r41h5c21468_1"
 - "1.32.0--r42hc0cfd56_0"
 - "1.32.0--r42ha9d7317_1"
 - "1.34.1--r43ha9d7317_0"
 - "1.36.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylpipe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylpipe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylpipe", "latest": {"1.36.0--r43ha9d7317_0": "sha256:115ad69a1c1f69803685b5a2e1ac04417f08ca43ee1a8a495654e219dd4026a6"}, "tags": {"1.27.0--r41h5c21468_1": "sha256:a06b7dffceaca9a426504ef830ea398e9d8e557799c17ca92d2d60b54f38988d", "1.32.0--r42hc0cfd56_0": "sha256:2c60894031057989d65b9154aabcbc4dc71fffc8b4ef5eda06b74e889cdee10e", "1.32.0--r42ha9d7317_1": "sha256:afd0386290b3d8dab522ecc73fc7d9c19bb489d326e20c7e47fea99b1c1179e6", "1.34.1--r43ha9d7317_0": "sha256:6e7cebb1680815d3322cfd7ae5db98a314ecacd34d03968fb35e9f248f3f5cc7", "1.36.0--r43ha9d7317_0": "sha256:115ad69a1c1f69803685b5a2e1ac04417f08ca43ee1a8a495654e219dd4026a6"}, "docker": "quay.io/biocontainers/bioconductor-methylpipe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylpipe.
shpc-registry automated BioContainers addition for bioconductor-methylpipe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylpipe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylpipe:1.36.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylpipe/1.36.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-methylpipe/1.36.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylpipe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylpipe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylpipe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylpipe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylpipe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylpipe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylpipe

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