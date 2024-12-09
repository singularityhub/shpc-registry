---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsreg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsreg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsreg/container.yaml"
updated_at: "2024-12-09 04:20:24.883298"
latest: "1.36.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsreg"

versions:
 - "1.28.0--r41hc247a5b_2"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_1"
 - "1.34.0--r43hf17093f_0"
 - "1.36.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsreg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsreg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsreg", "latest": {"1.36.0--r43hf17093f_0": "sha256:c15341035910d79271a6246a61c347512b178a0c7d2b3d5b6534d172e29a9463"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:50ed50eb3483a52e3fd877bcfd73859ec4f8c6aa1718089beea50f3534603651", "1.32.0--r42hc247a5b_0": "sha256:6432bc6a893aba262d70bd6525104760f32db4efc24d2a983eb2bcbf906dfdd8", "1.32.0--r42hf17093f_1": "sha256:509fa975e29593b1b28e62057d02e87b70a8137610e6e1db64593bbdc4705988", "1.34.0--r43hf17093f_0": "sha256:37daa1fcfcbf0f7642a7f28a4cb49cd698666294514c609801ae3585ec5fdac0", "1.36.0--r43hf17093f_0": "sha256:c15341035910d79271a6246a61c347512b178a0c7d2b3d5b6534d172e29a9463"}, "docker": "quay.io/biocontainers/bioconductor-gsreg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsreg.
shpc-registry automated BioContainers addition for bioconductor-gsreg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsreg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsreg:1.36.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsreg/1.36.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-gsreg/1.36.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsreg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsreg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsreg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsreg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsreg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsreg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gsreg

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