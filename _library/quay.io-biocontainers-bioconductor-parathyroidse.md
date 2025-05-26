---
layout: container
name:  "quay.io/biocontainers/bioconductor-parathyroidse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-parathyroidse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-parathyroidse/container.yaml"
updated_at: "2025-05-26 03:23:31.493566"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-parathyroidse"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-parathyroidse"
config: {"url": "https://biocontainers.pro/tools/bioconductor-parathyroidse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-parathyroidse", "latest": {"1.40.0--r43hdfd78af_0": "sha256:753621e0c980e21a6de02005f832ede71be09c8f43445cda3f547dd73a85dc90"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:70b8357a603ac392379203efec386bddfa2e6eb4a6c1f158f04f0f0bdecbca34", "1.36.0--r42hdfd78af_0": "sha256:d47f04cc51089ad3b5e85d1c9097585aab69719cba9281398e6351ca69cbe88b", "1.38.0--r43hdfd78af_0": "sha256:3ffc0f139e00bf68349a441b31798c83c31fdf3c29d7f0123d601e712519d3c2", "1.40.0--r43hdfd78af_0": "sha256:753621e0c980e21a6de02005f832ede71be09c8f43445cda3f547dd73a85dc90"}, "docker": "quay.io/biocontainers/bioconductor-parathyroidse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-parathyroidse.
shpc-registry automated BioContainers addition for bioconductor-parathyroidse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-parathyroidse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-parathyroidse:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-parathyroidse/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-parathyroidse/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-parathyroidse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-parathyroidse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-parathyroidse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-parathyroidse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-parathyroidse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-parathyroidse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-parathyroidse

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