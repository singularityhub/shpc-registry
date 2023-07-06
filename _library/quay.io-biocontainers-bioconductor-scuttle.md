---
layout: container
name:  "quay.io/biocontainers/bioconductor-scuttle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scuttle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scuttle/container.yaml"
updated_at: "2023-07-06 06:58:38.301404"
latest: "1.8.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-scuttle"

versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-scuttle"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scuttle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scuttle", "latest": {"1.8.0--r42hf17093f_1": "sha256:9c326597115d7610f25acff1ffb3e8d2c96808fea62c17537a8cbbf6ca909bd3"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:ea539dbb54472123fddc2403600b90a210e75922f97b467e4816b0fc8b830a8e", "1.8.0--r42hc247a5b_0": "sha256:bf089e4a3db722bfa369f9c36d4dd61191c1a0548e4b0e34a7b709738a11cd6f", "1.8.0--r42hf17093f_1": "sha256:9c326597115d7610f25acff1ffb3e8d2c96808fea62c17537a8cbbf6ca909bd3"}, "docker": "quay.io/biocontainers/bioconductor-scuttle"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scuttle.
shpc-registry automated BioContainers addition for bioconductor-scuttle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scuttle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scuttle:1.8.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scuttle/1.8.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-scuttle/1.8.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scuttle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scuttle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scuttle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scuttle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scuttle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scuttle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scuttle

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