---
layout: container
name:  "quay.io/biocontainers/bioconductor-dss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dss/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dss/container.yaml"
updated_at: "2024-11-16 02:56:30.640728"
latest: "2.48.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-dss"

versions:
 - "2.42.0--r41hc0cfd56_2"
 - "2.46.0--r42hc0cfd56_0"
 - "2.46.0--r42ha9d7317_1"
 - "2.48.0--r43ha9d7317_0"
 - "2.48.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-dss"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dss", "latest": {"2.48.0--r43ha9d7317_1": "sha256:a1579ce52fa77cd078b5886690f90283e310b090951e423b54c3e1972c024747"}, "tags": {"2.42.0--r41hc0cfd56_2": "sha256:9d2d24749288e234b41083354fa98cd8edc12778d8f8c70b82761b7aa11d0f14", "2.46.0--r42hc0cfd56_0": "sha256:da0704c6f3692c1abf3cc96a48d60dcb55ff7fdc2f656fcb600d9051b770e73d", "2.46.0--r42ha9d7317_1": "sha256:74ae38e691e25d9081e86946e55285dee946284f947235e2db3c3f5278b939d7", "2.48.0--r43ha9d7317_0": "sha256:bb08ce92870c01cd65247be3c806b1c864c3bc4a5cdb921a785b701d1370f944", "2.48.0--r43ha9d7317_1": "sha256:a1579ce52fa77cd078b5886690f90283e310b090951e423b54c3e1972c024747"}, "docker": "quay.io/biocontainers/bioconductor-dss"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dss.
shpc-registry automated BioContainers addition for bioconductor-dss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dss:2.48.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dss/2.48.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-dss/2.48.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dss

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