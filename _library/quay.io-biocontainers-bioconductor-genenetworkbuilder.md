---
layout: container
name:  "quay.io/biocontainers/bioconductor-genenetworkbuilder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genenetworkbuilder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genenetworkbuilder/container.yaml"
updated_at: "2023-10-31 02:35:27.636631"
latest: "1.42.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genenetworkbuilder"

versions:
 - "1.36.1--r41hc247a5b_1"
 - "1.40.0--r42hc247a5b_0"
 - "1.40.0--r42hf17093f_1"
 - "1.42.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genenetworkbuilder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genenetworkbuilder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genenetworkbuilder", "latest": {"1.42.0--r43hf17093f_0": "sha256:47fe86486494dfff9aa4aea399cc0896f7fc57ac4ef4e37c28e0b60a36619d9c"}, "tags": {"1.36.1--r41hc247a5b_1": "sha256:95d65d458abcfc62a64c59113bf7e1cbadeee8cdfdba850ff882897b0775354b", "1.40.0--r42hc247a5b_0": "sha256:5fc7bc961d6fa5310b21366b7d93987ffad8231375ed7f2ee7ce19f642368a00", "1.40.0--r42hf17093f_1": "sha256:c2cd81a9ddc878d1bf538465e2da7438e162dac65d2c05b447b8c2b64477394d", "1.42.0--r43hf17093f_0": "sha256:47fe86486494dfff9aa4aea399cc0896f7fc57ac4ef4e37c28e0b60a36619d9c"}, "docker": "quay.io/biocontainers/bioconductor-genenetworkbuilder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genenetworkbuilder.
shpc-registry automated BioContainers addition for bioconductor-genenetworkbuilder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genenetworkbuilder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genenetworkbuilder:1.42.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genenetworkbuilder/1.42.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-genenetworkbuilder/1.42.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genenetworkbuilder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genenetworkbuilder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genenetworkbuilder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genenetworkbuilder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genenetworkbuilder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genenetworkbuilder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genenetworkbuilder

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