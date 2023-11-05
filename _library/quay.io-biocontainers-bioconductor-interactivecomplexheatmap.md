---
layout: container
name:  "quay.io/biocontainers/bioconductor-interactivecomplexheatmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-interactivecomplexheatmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-interactivecomplexheatmap/container.yaml"
updated_at: "2023-11-05 02:48:57.406578"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-interactivecomplexheatmap"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-interactivecomplexheatmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-interactivecomplexheatmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-interactivecomplexheatmap", "latest": {"1.8.0--r43hdfd78af_0": "sha256:be9f0004c4bad81d5e69ec9a7ac0baf14716143dd8c0b0b28ba5c1efd7605bb7"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:9e93d082392ea753e1a74868750486ccd3d18f10da8bef222719ef93b3f45f01", "1.6.0--r42hdfd78af_0": "sha256:0a7ff47299e0423427603d3c888781e1134a911269c21a5f4e16381e88120bf6", "1.8.0--r43hdfd78af_0": "sha256:be9f0004c4bad81d5e69ec9a7ac0baf14716143dd8c0b0b28ba5c1efd7605bb7"}, "docker": "quay.io/biocontainers/bioconductor-interactivecomplexheatmap", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-interactivecomplexheatmap.
shpc-registry automated BioContainers addition for bioconductor-interactivecomplexheatmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-interactivecomplexheatmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-interactivecomplexheatmap:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-interactivecomplexheatmap/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-interactivecomplexheatmap/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-interactivecomplexheatmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interactivecomplexheatmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interactivecomplexheatmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-interactivecomplexheatmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-interactivecomplexheatmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-interactivecomplexheatmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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