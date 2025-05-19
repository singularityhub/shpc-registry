---
layout: container
name:  "quay.io/biocontainers/bioconductor-transview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-transview/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-transview/container.yaml"
updated_at: "2025-05-19 03:55:23.775996"
latest: "1.46.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-transview"

versions:
 - "1.38.0--r41hc0cfd56_2"
 - "1.42.0--r42hc0cfd56_0"
 - "1.42.0--r42ha9d7317_1"
 - "1.44.0--r43ha9d7317_0"
 - "1.46.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-transview"
config: {"url": "https://biocontainers.pro/tools/bioconductor-transview", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-transview", "latest": {"1.46.0--r43ha9d7317_0": "sha256:8151241dde2da3e9e36f5f3ddf82952015bc058279508fa8538950a646aa5ef1"}, "tags": {"1.38.0--r41hc0cfd56_2": "sha256:ba1feae14587d25043c4e9c442d4582d13b655e966e4f620d979159791de16a6", "1.42.0--r42hc0cfd56_0": "sha256:baa5f7a57354da506faf3e99035900162d6a0beb0b15d92b68cff1e506d75480", "1.42.0--r42ha9d7317_1": "sha256:f403b62c5ed3b48cf815acb0376ac0387b9c20c29619fac2107bf0ec54532a4e", "1.44.0--r43ha9d7317_0": "sha256:e1fb1e1a050772a3af8e02c86487cdcb701036e38665773414e8badd9e7b1a6e", "1.46.0--r43ha9d7317_0": "sha256:8151241dde2da3e9e36f5f3ddf82952015bc058279508fa8538950a646aa5ef1"}, "docker": "quay.io/biocontainers/bioconductor-transview"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-transview.
shpc-registry automated BioContainers addition for bioconductor-transview
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-transview
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-transview:1.46.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-transview/1.46.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-transview/1.46.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-transview-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transview-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transview-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-transview-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-transview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-transview-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-transview

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