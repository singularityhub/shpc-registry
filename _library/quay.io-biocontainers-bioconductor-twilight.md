---
layout: container
name:  "quay.io/biocontainers/bioconductor-twilight"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-twilight/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-twilight/container.yaml"
updated_at: "2023-12-23 03:07:35.453279"
latest: "1.78.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-twilight"

versions:
 - "1.70.0--r41hc0cfd56_2"
 - "1.74.0--r42hc0cfd56_0"
 - "1.74.0--r42ha9d7317_1"
 - "1.76.0--r43ha9d7317_0"
 - "1.78.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-twilight"
config: {"url": "https://biocontainers.pro/tools/bioconductor-twilight", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-twilight", "latest": {"1.78.0--r43ha9d7317_0": "sha256:c20e9b1a587ccc6f536858c5f201040c71f0a48ad49f739a305feb063cf8613d"}, "tags": {"1.70.0--r41hc0cfd56_2": "sha256:85a3e35535a9c21b1c26e8118383160b96d6c1595e9da612df71a64317bee280", "1.74.0--r42hc0cfd56_0": "sha256:d71deb42fdee884471ae6ecaecded1e5b56953e918a8a5b827d22130d406514a", "1.74.0--r42ha9d7317_1": "sha256:d00cfc406ec0140ab23a7f14b9476c484c0bdd984babbe4ad6e85eb7312d4e4f", "1.76.0--r43ha9d7317_0": "sha256:24023e8a33a061d4581f9c08cefcb85122611426e7c582d98369c20dbb0a0d2d", "1.78.0--r43ha9d7317_0": "sha256:c20e9b1a587ccc6f536858c5f201040c71f0a48ad49f739a305feb063cf8613d"}, "docker": "quay.io/biocontainers/bioconductor-twilight"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-twilight.
shpc-registry automated BioContainers addition for bioconductor-twilight
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-twilight
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-twilight:1.78.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-twilight/1.78.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-twilight/1.78.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-twilight-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-twilight-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-twilight-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-twilight-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-twilight-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-twilight-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-twilight

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