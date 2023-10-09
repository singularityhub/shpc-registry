---
layout: container
name:  "quay.io/biocontainers/bioconductor-gosim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gosim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gosim/container.yaml"
updated_at: "2023-10-09 02:37:58.350620"
latest: "1.38.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gosim"

versions:
 - "1.32.0--r41hc247a5b_2"
 - "1.36.0--r42hc247a5b_0"
 - "1.36.0--r42hf17093f_1"
 - "1.38.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gosim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gosim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gosim", "latest": {"1.38.0--r43hf17093f_0": "sha256:73d3d444cde5b2fb2d5da7383916f449f1e4b2eaea2da56e3eb730e654c6d803"}, "tags": {"1.32.0--r41hc247a5b_2": "sha256:968367630f629bd22d276c36bfc7336604d223c5de49640730f18740ec62f3a9", "1.36.0--r42hc247a5b_0": "sha256:f42ecebe76d80e2b8a2c906d07cb7899273ac7211df79935f05b3a109155a0b3", "1.36.0--r42hf17093f_1": "sha256:ce045e53c5b807adee02f0b6e860d35327690e2f36893a499f762b364d93ee26", "1.38.0--r43hf17093f_0": "sha256:73d3d444cde5b2fb2d5da7383916f449f1e4b2eaea2da56e3eb730e654c6d803"}, "docker": "quay.io/biocontainers/bioconductor-gosim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gosim.
shpc-registry automated BioContainers addition for bioconductor-gosim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gosim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gosim:1.38.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gosim/1.38.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-gosim/1.38.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gosim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gosim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gosim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gosim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gosim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gosim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gosim

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