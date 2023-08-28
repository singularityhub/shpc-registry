---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtreemix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtreemix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtreemix/container.yaml"
updated_at: "2023-08-28 09:04:29.891924"
latest: "1.62.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtreemix"

versions:
 - "1.56.0--r41hc247a5b_2"
 - "1.60.0--r42hc247a5b_0"
 - "1.60.0--r42hf17093f_1"
 - "1.62.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtreemix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtreemix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtreemix", "latest": {"1.62.0--r43hf17093f_0": "sha256:853c9add0203959ad238bb1857096109d03d02faf697c375ad001dcd2ee20a5c"}, "tags": {"1.56.0--r41hc247a5b_2": "sha256:41f000b32e82c69425a948f7908085a3284845003363abbd10892cb5deed3c14", "1.60.0--r42hc247a5b_0": "sha256:ad5089f311eff740cee255604227bcdee5bf4e85aa1f81fec8969d991f772ecc", "1.60.0--r42hf17093f_1": "sha256:e104985392c30a90540a3d38b834c5b14a3281cf86f42f794c95e7d29c0973c7", "1.62.0--r43hf17093f_0": "sha256:853c9add0203959ad238bb1857096109d03d02faf697c375ad001dcd2ee20a5c"}, "docker": "quay.io/biocontainers/bioconductor-rtreemix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtreemix.
shpc-registry automated BioContainers addition for bioconductor-rtreemix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtreemix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtreemix:1.62.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtreemix/1.62.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-rtreemix/1.62.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtreemix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtreemix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtreemix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtreemix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtreemix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtreemix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtreemix

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