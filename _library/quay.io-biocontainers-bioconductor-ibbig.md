---
layout: container
name:  "quay.io/biocontainers/bioconductor-ibbig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ibbig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ibbig/container.yaml"
updated_at: "2025-02-23 03:36:34.317366"
latest: "1.50.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ibbig"

versions:
 - "1.38.0--r41hc0cfd56_2"
 - "1.42.0--r42hc0cfd56_0"
 - "1.42.0--r42ha9d7317_2"
 - "1.44.0--r43ha9d7317_0"
 - "1.46.0--r43ha9d7317_1"
 - "1.50.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ibbig"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ibbig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ibbig", "latest": {"1.50.0--r44h3df3fcb_0": "sha256:ca6640e8a73b1866bf6e86743a49fb4ededccdbb7019e51a56effbc22cbd04a2"}, "tags": {"1.38.0--r41hc0cfd56_2": "sha256:994235508f631d362eb2f2c55c57c9592c704d762059223a513155b83cd9853d", "1.42.0--r42hc0cfd56_0": "sha256:8adfd78d9444c1553b7abee5d2e36009c3cae8449910e9e914b940813565ab73", "1.42.0--r42ha9d7317_2": "sha256:f96b4e707d1a205e73b7e67c19f3c660944fd14742b2cefa02cf78a6c28e410b", "1.44.0--r43ha9d7317_0": "sha256:e6391efd1629eba0296da282dbaaba18c3dbe5f97cf1612cb9c543997d161375", "1.46.0--r43ha9d7317_1": "sha256:bfacb350bb72eca4f3b54e74293ba8d33869c3abd17529c67982fde48fb51c95", "1.50.0--r44h3df3fcb_0": "sha256:ca6640e8a73b1866bf6e86743a49fb4ededccdbb7019e51a56effbc22cbd04a2"}, "docker": "quay.io/biocontainers/bioconductor-ibbig"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ibbig.
shpc-registry automated BioContainers addition for bioconductor-ibbig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ibbig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ibbig:1.50.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ibbig/1.50.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-ibbig/1.50.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ibbig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ibbig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ibbig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ibbig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ibbig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ibbig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ibbig

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