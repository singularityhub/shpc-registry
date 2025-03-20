---
layout: container
name:  "quay.io/biocontainers/bioconductor-plier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plier/container.yaml"
updated_at: "2025-03-20 04:28:57.193373"
latest: "1.76.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-plier"

versions:
 - "1.64.0--r41hc247a5b_2"
 - "1.68.0--r42hc247a5b_0"
 - "1.68.0--r42hf17093f_1"
 - "1.70.0--r43hf17093f_0"
 - "1.72.0--r43hf17093f_0"
 - "1.76.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-plier"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plier", "latest": {"1.76.0--r44he5774e6_0": "sha256:a044262c8763af4172e8ff6ef39c8cd0b5bbc46ae22aba066ee962fd83c25d13"}, "tags": {"1.64.0--r41hc247a5b_2": "sha256:fa4633ab3af277edfe4106608abacdcccbb3d6532fa4ff60ce39b02870f769d7", "1.68.0--r42hc247a5b_0": "sha256:15f5125357a42e734a70e74c7f19473b119e9b4e09303d915f7e69822b245de7", "1.68.0--r42hf17093f_1": "sha256:5c025d4b0a145571a64593b75b8ac900cc1f11362f92c567ba62aaa98f53d2a5", "1.70.0--r43hf17093f_0": "sha256:826184b83d0392ff93d137533956799acaadb26930b103cceb1a902e8e3b22bb", "1.72.0--r43hf17093f_0": "sha256:1ef38f9e95f3bd37265dbe1a6d78ac77707ae00415257569d617e0e5120d3bb3", "1.76.0--r44he5774e6_0": "sha256:a044262c8763af4172e8ff6ef39c8cd0b5bbc46ae22aba066ee962fd83c25d13"}, "docker": "quay.io/biocontainers/bioconductor-plier"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plier.
shpc-registry automated BioContainers addition for bioconductor-plier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plier:1.76.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plier/1.76.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-plier/1.76.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-plier

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