---
layout: container
name:  "quay.io/biocontainers/bioconductor-blima"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-blima/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-blima/container.yaml"
updated_at: "2024-12-04 03:30:58.312794"
latest: "1.36.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-blima"

versions:
 - "1.28.0--r41hc247a5b_2"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_1"
 - "1.34.0--r43hf17093f_0"
 - "1.36.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-blima"
config: {"url": "https://biocontainers.pro/tools/bioconductor-blima", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-blima", "latest": {"1.36.0--r43hf17093f_0": "sha256:3b2d2ad164e3f414ac2039021af33e8a269b39491e82c447e66bb22bf6d9a054"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:6e43eeb54dd17e5557e1ada227ada0f312c11d79d8a6204ef9a007331f938c14", "1.32.0--r42hc247a5b_0": "sha256:da645990c16051fb4ae84dee558d2aefa07a1dfffa2884f0346bf7d6fb36af91", "1.32.0--r42hf17093f_1": "sha256:d6b1f74fb782ca3038da80f4cfd59805f63546d7ee38e3fcf4cd75e30acfd568", "1.34.0--r43hf17093f_0": "sha256:4b3704b059d47761139d2e248ef9fbf7a4fbf16576e238f5e5a48ff51be3f83b", "1.36.0--r43hf17093f_0": "sha256:3b2d2ad164e3f414ac2039021af33e8a269b39491e82c447e66bb22bf6d9a054"}, "docker": "quay.io/biocontainers/bioconductor-blima"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-blima.
shpc-registry automated BioContainers addition for bioconductor-blima
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-blima
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-blima:1.36.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-blima/1.36.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-blima/1.36.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-blima-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blima-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-blima-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-blima-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-blima-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-blima-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-blima

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