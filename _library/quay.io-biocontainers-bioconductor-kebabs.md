---
layout: container
name:  "quay.io/biocontainers/bioconductor-kebabs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-kebabs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-kebabs/container.yaml"
updated_at: "2024-09-10 03:17:08.295869"
latest: "1.36.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-kebabs"

versions:
 - "1.28.1--r41hc247a5b_1"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_1"
 - "1.34.0--r43hf17093f_0"
 - "1.36.0--r43hf17093f_0"
 - "1.36.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-kebabs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-kebabs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-kebabs", "latest": {"1.36.0--r43hf17093f_1": "sha256:0dd0cc7e26ee145de1f1a9682fe2336f3dadcb0b2e9d2a7624235da59dd7a694"}, "tags": {"1.28.1--r41hc247a5b_1": "sha256:1ceac9bd98886901de84774fb4b20c9cb4604e6e07ee967151f109ac1aa0c19f", "1.32.0--r42hc247a5b_0": "sha256:4f413595317e84316088a05a3574dc3134968a3c79a79d249b23ea4521e24d52", "1.32.0--r42hf17093f_1": "sha256:1d5062018458ee7e71536791bad07e3c438310adac09d6dabd2d36370863fde2", "1.34.0--r43hf17093f_0": "sha256:324312ab6adfe95fd4c3f1d049d7655d6da202f66804ec99814fa10c732ad24f", "1.36.0--r43hf17093f_0": "sha256:a98c1c63fc14ddc9bbef6abf000d2dacc46946f94e8bf2b4f9c8cbd634c0293f", "1.36.0--r43hf17093f_1": "sha256:0dd0cc7e26ee145de1f1a9682fe2336f3dadcb0b2e9d2a7624235da59dd7a694"}, "docker": "quay.io/biocontainers/bioconductor-kebabs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-kebabs.
shpc-registry automated BioContainers addition for bioconductor-kebabs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-kebabs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-kebabs:1.36.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-kebabs/1.36.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-kebabs/1.36.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-kebabs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kebabs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kebabs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-kebabs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-kebabs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-kebabs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-kebabs

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