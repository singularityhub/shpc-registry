---
layout: container
name:  "quay.io/biocontainers/bioconductor-edger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-edger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-edger/container.yaml"
updated_at: "2025-11-01 03:27:33.587293"
latest: "4.0.2--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-edger"

versions:
 - "3.36.0--r41hc247a5b_2"
 - "3.40.0--r42hc247a5b_0"
 - "3.40.0--r42hf17093f_1"
 - "3.42.4--r43hf17093f_0"
 - "4.0.2--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-edger"
config: {"url": "https://biocontainers.pro/tools/bioconductor-edger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-edger", "latest": {"4.0.2--r43hf17093f_0": "sha256:bf370d508da5675424680437c052d2dcfc7a3d89270aa7e03bcce89ceaca767a"}, "tags": {"3.36.0--r41hc247a5b_2": "sha256:fd4131e86260ead320c0fa1bf1de50c50c018f8ee3dfe1a7626af42f0860b9e8", "3.40.0--r42hc247a5b_0": "sha256:e6ec9c69f2b6bd609b7fd42a2cf9cb346e0f35e1a9a49a3aaaf08365e03956cf", "3.40.0--r42hf17093f_1": "sha256:b180a5d2102bdc1693b5c7a219aee157e163ffc1a99273225920b8a4eda11ab7", "3.42.4--r43hf17093f_0": "sha256:1ef04bf29136877807b1665114748ff8e84de704a57a5a11e03efa7722584d36", "4.0.2--r43hf17093f_0": "sha256:bf370d508da5675424680437c052d2dcfc7a3d89270aa7e03bcce89ceaca767a"}, "docker": "quay.io/biocontainers/bioconductor-edger"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-edger.
shpc-registry automated BioContainers addition for bioconductor-edger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-edger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-edger:4.0.2--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-edger/4.0.2--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-edger/4.0.2--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-edger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-edger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-edger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-edger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-edger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-edger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-edger

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