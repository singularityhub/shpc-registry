---
layout: container
name:  "quay.io/biocontainers/bioconductor-screclassify"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-screclassify/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-screclassify/container.yaml"
updated_at: "2025-01-30 03:27:18.202461"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-screclassify"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-screclassify"
config: {"url": "https://biocontainers.pro/tools/bioconductor-screclassify", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-screclassify", "latest": {"1.12.0--r44hdfd78af_0": "sha256:989344ffa8116002d8414dd89eba17d38e2a45642073e2383e19578ea2576e92"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:5b4588ed667e1e9387fc6c481bc15e8c265e61619eb4cefb20c9bea668f8570f", "1.4.0--r42hdfd78af_0": "sha256:58cafa69a162add7a48d3c365dcc0e21176a9742e215133d8cfc7672d272c6d9", "1.6.0--r43hdfd78af_0": "sha256:8ad273d8837d3aad565070a3fc7c036cca7addeb1c173f634dbc7c239728ce0c", "1.8.0--r43hdfd78af_0": "sha256:2a470ebde0075135afa687c3ff71f6988add034d964859645b0d01285128432c", "1.12.0--r44hdfd78af_0": "sha256:989344ffa8116002d8414dd89eba17d38e2a45642073e2383e19578ea2576e92"}, "docker": "quay.io/biocontainers/bioconductor-screclassify"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-screclassify.
shpc-registry automated BioContainers addition for bioconductor-screclassify
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-screclassify
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-screclassify:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-screclassify/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-screclassify/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-screclassify-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screclassify-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screclassify-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-screclassify-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-screclassify-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-screclassify-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-screclassify

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