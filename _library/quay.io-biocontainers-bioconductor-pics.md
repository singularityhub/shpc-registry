---
layout: container
name:  "quay.io/biocontainers/bioconductor-pics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pics/container.yaml"
updated_at: "2024-02-20 02:56:27.697162"
latest: "2.44.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pics"

versions:
 - "2.38.0--r41hc0cfd56_2"
 - "2.42.0--r42hc0cfd56_0"
 - "2.42.0--r42ha9d7317_1"
 - "2.44.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pics", "latest": {"2.44.0--r43ha9d7317_0": "sha256:e2a9745872fba2ea3ec1ca108d2239df5ae67663df9e89c1715cb885137cd11c"}, "tags": {"2.38.0--r41hc0cfd56_2": "sha256:d81d349d8a1d1e1badc5c0a3b0f48f67ce8be3e81de0deac249a27f15edcba05", "2.42.0--r42hc0cfd56_0": "sha256:fe6f37da031525ed1ee6b745f1636846161cbe78955f6f37020b9c8e35704062", "2.42.0--r42ha9d7317_1": "sha256:ff73af2dc5488570eef2936840f051842a8d8ba1e828f33925743b5be052bc92", "2.44.0--r43ha9d7317_0": "sha256:e2a9745872fba2ea3ec1ca108d2239df5ae67663df9e89c1715cb885137cd11c"}, "docker": "quay.io/biocontainers/bioconductor-pics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pics.
shpc-registry automated BioContainers addition for bioconductor-pics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pics:2.44.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pics/2.44.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-pics/2.44.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pics

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