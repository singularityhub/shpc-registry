---
layout: container
name:  "quay.io/biocontainers/bioconductor-wppi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-wppi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-wppi/container.yaml"
updated_at: "2025-01-10 03:07:31.920327"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-wppi"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-wppi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-wppi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-wppi", "latest": {"1.10.0--r43hdfd78af_0": "sha256:2a2e70c4864186948be2a2b953d9731901df3808d7e5bebb4585095b604d791c"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:77dd5c3c251ed6890643aa7351c69a856b1d1645556b0394b4c0df2b3fb3733d", "1.6.0--r42hdfd78af_0": "sha256:158108464c0799d8b1b361cde151109c0e7c6c6509a8a9dd823369e62438d573", "1.8.0--r43hdfd78af_0": "sha256:4bed4701ab9776609d651218c5ec08f19b25bd11999c341bc44ee38a8bfbcd59", "1.10.0--r43hdfd78af_0": "sha256:2a2e70c4864186948be2a2b953d9731901df3808d7e5bebb4585095b604d791c"}, "docker": "quay.io/biocontainers/bioconductor-wppi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-wppi.
shpc-registry automated BioContainers addition for bioconductor-wppi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-wppi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-wppi:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-wppi/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-wppi/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-wppi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wppi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wppi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-wppi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-wppi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-wppi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-wppi

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