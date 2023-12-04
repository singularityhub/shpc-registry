---
layout: container
name:  "quay.io/biocontainers/bioconductor-xde"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xde/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xde/container.yaml"
updated_at: "2023-12-04 03:04:09.680844"
latest: "2.46.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xde"

versions:
 - "2.40.0--r41hc247a5b_2"
 - "2.44.0--r42hc247a5b_0"
 - "2.44.0--r42hf17093f_1"
 - "2.46.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xde"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xde", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xde", "latest": {"2.46.0--r43hf17093f_0": "sha256:2906f6a7f01d9a453fcb0feba703bb1552bf152861e97744cc984679fe27909a"}, "tags": {"2.40.0--r41hc247a5b_2": "sha256:18d5059127324925ae95f5aad649294a426bdacac7f55cba62ff92ec754e5490", "2.44.0--r42hc247a5b_0": "sha256:fbafa31d3882b685ae9df295f964a67f2d3a48c90b939d5bf624a3ea3b1582c1", "2.44.0--r42hf17093f_1": "sha256:7955bf9f1d8e6ccf11c5998084fb024a27222f90996bbeec82370ef26c30f47c", "2.46.0--r43hf17093f_0": "sha256:2906f6a7f01d9a453fcb0feba703bb1552bf152861e97744cc984679fe27909a"}, "docker": "quay.io/biocontainers/bioconductor-xde"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xde.
shpc-registry automated BioContainers addition for bioconductor-xde
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xde
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xde:2.46.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xde/2.46.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-xde/2.46.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xde-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xde-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xde-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xde-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xde-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xde-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xde

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