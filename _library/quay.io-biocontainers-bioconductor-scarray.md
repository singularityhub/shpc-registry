---
layout: container
name:  "quay.io/biocontainers/bioconductor-scarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scarray/container.yaml"
updated_at: "2024-06-23 02:42:25.496343"
latest: "1.10.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scarray"

versions:
 - "1.2.1--r41hc247a5b_1"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.2--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scarray", "latest": {"1.10.0--r43hf17093f_0": "sha256:cb38b1cfc87e9de155cc35886e9cc47932e75e1fd341144e8489204d26b44707"}, "tags": {"1.2.1--r41hc247a5b_1": "sha256:e2242fdb22bb50e2eeaa7e74ee3ce99dc43bd2c31c987c95f3bc0ad33a808071", "1.6.0--r42hc247a5b_0": "sha256:ee9cb72b53328e0e6bd41a3b433c3bd95a3d83659a1cf84b311d73d0aef82cc9", "1.6.0--r42hf17093f_1": "sha256:cd4f706a64b6a07b9ccf23f30a0258c257bc893792e1adf29477b96d9e9c286e", "1.8.2--r43hf17093f_0": "sha256:c853dda0c59ba43b42bc55e896bd6a1a4248fb9f83d990a32a24ae7dea2bc0f8", "1.10.0--r43hf17093f_0": "sha256:cb38b1cfc87e9de155cc35886e9cc47932e75e1fd341144e8489204d26b44707"}, "docker": "quay.io/biocontainers/bioconductor-scarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scarray.
shpc-registry automated BioContainers addition for bioconductor-scarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scarray:1.10.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scarray/1.10.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-scarray/1.10.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scarray

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