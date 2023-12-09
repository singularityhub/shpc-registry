---
layout: container
name:  "quay.io/biocontainers/bioconductor-bluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bluster/container.yaml"
updated_at: "2023-12-09 03:04:57.442797"
latest: "1.10.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bluster"
aliases:
 - "glpsol"
versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bluster"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bluster", "latest": {"1.10.0--r43hf17093f_0": "sha256:73c2deef951d6f9171bb9d7759a457e543a4bfdc279e59511b19b32c5e51553b"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:fcb086716e9c7006fb46c9d012b59dacf803d5d60745487b99cbe2a1d532598e", "1.8.0--r42hc247a5b_0": "sha256:896f02361ee91fd38eb21e603100453092fb44b1d6901cb2d35eea610644478d", "1.8.0--r42hf17093f_1": "sha256:e468676d9d530d5c7a404269becdc9fd034b244d48d648fe3e2d09f8559408b0", "1.10.0--r43hf17093f_0": "sha256:73c2deef951d6f9171bb9d7759a457e543a4bfdc279e59511b19b32c5e51553b"}, "docker": "quay.io/biocontainers/bioconductor-bluster", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bluster.
shpc-registry automated BioContainers addition for bioconductor-bluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bluster:1.10.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bluster/1.10.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-bluster/1.10.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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