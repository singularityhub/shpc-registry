---
layout: container
name:  "quay.io/biocontainers/bioconductor-titancna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-titancna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-titancna/container.yaml"
updated_at: "2025-04-15 03:50:37.805951"
latest: "1.44.0--r44h3df3fcb_1"
container_url: "https://biocontainers.pro/tools/bioconductor-titancna"

versions:
 - "1.32.0--r41hc0cfd56_2"
 - "1.36.0--r42hc0cfd56_0"
 - "1.36.0--r42ha9d7317_1"
 - "1.38.0--r43ha9d7317_0"
 - "1.40.0--r43ha9d7317_0"
 - "1.44.0--r44h3df3fcb_0"
 - "1.44.0--r44h3df3fcb_1"
description: "shpc-registry automated BioContainers addition for bioconductor-titancna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-titancna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-titancna", "latest": {"1.44.0--r44h3df3fcb_1": "sha256:fefaa87d9fa7edf58f2b29dee40b896061f758369eea0472419ab65070d4ff7c"}, "tags": {"1.32.0--r41hc0cfd56_2": "sha256:274cb17823262d460c301873afe9381d09ddf214947007a516acaf4966579a2d", "1.36.0--r42hc0cfd56_0": "sha256:1231f62e1bf1818f06d24f20b677b5ca922ca7878546b37d0809643ee748bea9", "1.36.0--r42ha9d7317_1": "sha256:56ad42ef82635ac04c38c07ccad03ebbf9fa6e979b0c36bc144c531ce8a58a34", "1.38.0--r43ha9d7317_0": "sha256:064832671c6ca8bf0927de6c7779d5d0132644c2afd97a83d37714f53cfd5a9c", "1.40.0--r43ha9d7317_0": "sha256:aeb52273370fe3d16e9c6ccbdff9a32a2578a57609d6e7dcbbc96eb0e917d7cd", "1.44.0--r44h3df3fcb_0": "sha256:93e5ba49b821ab84078636ef59259c0a5a3f1010957bfd75fd907dd3f76f1fb2", "1.44.0--r44h3df3fcb_1": "sha256:fefaa87d9fa7edf58f2b29dee40b896061f758369eea0472419ab65070d4ff7c"}, "docker": "quay.io/biocontainers/bioconductor-titancna"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-titancna.
shpc-registry automated BioContainers addition for bioconductor-titancna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-titancna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-titancna:1.44.0--r44h3df3fcb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-titancna/1.44.0--r44h3df3fcb_1
$ module help quay.io/biocontainers/bioconductor-titancna/1.44.0--r44h3df3fcb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-titancna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-titancna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-titancna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-titancna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-titancna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-titancna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-titancna

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