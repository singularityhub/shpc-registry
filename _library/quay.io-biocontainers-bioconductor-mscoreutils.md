---
layout: container
name:  "quay.io/biocontainers/bioconductor-mscoreutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mscoreutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mscoreutils/container.yaml"
updated_at: "2025-09-16 03:02:47.695438"
latest: "1.18.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-mscoreutils"

versions:
 - "1.6.2--r41hc247a5b_0"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_1"
 - "1.12.0--r43hf17093f_0"
 - "1.14.1--r43hf17093f_0"
 - "1.14.1--r43hf17093f_1"
 - "1.18.0--r44he5774e6_0"
 - "1.18.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-mscoreutils"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mscoreutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mscoreutils", "latest": {"1.18.0--r44he5774e6_1": "sha256:a122551a9db27fa84d0af95e4f18cae0f48dc6c7135dec6934d48125bc1f10ac"}, "tags": {"1.6.2--r41hc247a5b_0": "sha256:27e654ec2ffcf65573f539bbf0d203a93b154bac6a51a4161f24ca5eb7c6f150", "1.10.0--r42hc247a5b_0": "sha256:b991342ba20d3f7157de11f4f344ae9dea5140e9d2f54b616117ccd055625cc1", "1.10.0--r42hf17093f_1": "sha256:4c1890ac0cbcef98dcf491f31d1ef79adaad8a25690a8cf862074e81fe4fe5a6", "1.12.0--r43hf17093f_0": "sha256:a4b338e5d1b5914e1ebfaf4979e6ec742ed0eb518dbad2d7dd6a0820690b2c4d", "1.14.1--r43hf17093f_0": "sha256:7a75e4d9e3d3e841fe08de0cf334fb6a68dbb0838a294280f203a498da8d6147", "1.14.1--r43hf17093f_1": "sha256:1de7585ffbd429731d23a5644e2cb15558776fc1439a7144578cfec94f2ee398", "1.18.0--r44he5774e6_0": "sha256:636cfe6492289d6eb405b63b907d3f39164ec613ebc3b209dae2a915b9d1f810", "1.18.0--r44he5774e6_1": "sha256:a122551a9db27fa84d0af95e4f18cae0f48dc6c7135dec6934d48125bc1f10ac"}, "docker": "quay.io/biocontainers/bioconductor-mscoreutils"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mscoreutils.
shpc-registry automated BioContainers addition for bioconductor-mscoreutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mscoreutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mscoreutils:1.18.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mscoreutils/1.18.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-mscoreutils/1.18.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mscoreutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mscoreutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mscoreutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mscoreutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mscoreutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mscoreutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mscoreutils

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