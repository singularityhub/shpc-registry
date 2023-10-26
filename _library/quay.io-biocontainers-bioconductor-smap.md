---
layout: container
name:  "quay.io/biocontainers/bioconductor-smap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-smap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-smap/container.yaml"
updated_at: "2023-10-26 04:11:54.729833"
latest: "1.64.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-smap"

versions:
 - "1.58.0--r41hc0cfd56_2"
 - "1.62.0--r42hc0cfd56_0"
 - "1.62.0--r42ha9d7317_2"
 - "1.64.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-smap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-smap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-smap", "latest": {"1.64.0--r43ha9d7317_0": "sha256:5059398ce3e8f5d7fad38650fabb7dc3fab0d60e25adba1d27bc45cb56d05cef"}, "tags": {"1.58.0--r41hc0cfd56_2": "sha256:1384d46caf273511d77051fef7fede290dcaa7178e378d81c8fb9fefd153ddbc", "1.62.0--r42hc0cfd56_0": "sha256:f551e7ec16a6a7009cb0c4ffebfc3558e6024d8f64419d77832f037974bf7173", "1.62.0--r42ha9d7317_2": "sha256:626cba736f5809bd61d4db87650f5215bc61dff5b5920e89700b79ab5f588a28", "1.64.0--r43ha9d7317_0": "sha256:5059398ce3e8f5d7fad38650fabb7dc3fab0d60e25adba1d27bc45cb56d05cef"}, "docker": "quay.io/biocontainers/bioconductor-smap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-smap.
shpc-registry automated BioContainers addition for bioconductor-smap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-smap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-smap:1.64.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-smap/1.64.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-smap/1.64.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-smap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-smap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-smap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-smap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-smap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-smap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-smap

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