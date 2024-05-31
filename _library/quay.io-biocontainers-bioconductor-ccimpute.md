---
layout: container
name:  "quay.io/biocontainers/bioconductor-ccimpute"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ccimpute/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ccimpute/container.yaml"
updated_at: "2024-05-31 03:06:23.114612"
latest: "1.4.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ccimpute"

versions:
 - "1.0.0--r42hc247a5b_0"
 - "1.0.0--r42hf17093f_1"
 - "1.2.1--r43hf17093f_0"
 - "1.4.0--r43hf17093f_0"
description: "singularity registry hpc automated addition for bioconductor-ccimpute"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ccimpute", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-ccimpute", "latest": {"1.4.0--r43hf17093f_0": "sha256:8ed02694399293da29794eee31f24f492443b0d1727358d296ce24a747b91788"}, "tags": {"1.0.0--r42hc247a5b_0": "sha256:f40957655be9ef92a3730ac5d382e2d141bf2367267678d1c5550828efe394e0", "1.0.0--r42hf17093f_1": "sha256:f526c0d29141ff79c287829b4208929cd3f12a04bb4fccd72d014a8f67d16d5b", "1.2.1--r43hf17093f_0": "sha256:807e33fc4c0471fb55abaa3f27c06072e3aa1c75df7792b8af0170185b0548f8", "1.4.0--r43hf17093f_0": "sha256:8ed02694399293da29794eee31f24f492443b0d1727358d296ce24a747b91788"}, "docker": "quay.io/biocontainers/bioconductor-ccimpute"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ccimpute.
singularity registry hpc automated addition for bioconductor-ccimpute
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ccimpute
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ccimpute:1.4.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ccimpute/1.4.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-ccimpute/1.4.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ccimpute-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccimpute-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccimpute-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ccimpute-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ccimpute-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ccimpute-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ccimpute

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