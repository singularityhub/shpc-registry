---
layout: container
name:  "quay.io/biocontainers/bioconductor-affxparser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affxparser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affxparser/container.yaml"
updated_at: "2024-12-19 04:30:43.409548"
latest: "1.74.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-affxparser"

versions:
 - "1.66.0--r41hc247a5b_2"
 - "1.70.0--r42hc247a5b_0"
 - "1.70.0--r42hf17093f_2"
 - "1.72.0--r43hf17093f_0"
 - "1.74.0--r43hf17093f_0"
 - "1.74.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-affxparser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affxparser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affxparser", "latest": {"1.74.0--r43hf17093f_1": "sha256:de695830bdd8faf6094fb441465a888d6c7d560e5da577e7879ee1731adc2569"}, "tags": {"1.66.0--r41hc247a5b_2": "sha256:12bd20c6e471d9ff385f4bdc90309eff7c2f8cec7c2a5ffba592d85c1e640d72", "1.70.0--r42hc247a5b_0": "sha256:5efb72c2040bce9cf426ffbc24d07356e1870076106726e0eafcc1ef2f4418bf", "1.70.0--r42hf17093f_2": "sha256:9fb86d47e04c550abca7e0c292d89b1d59802c6a55f2d7d22da78b0d410b7397", "1.72.0--r43hf17093f_0": "sha256:2b0dfad731c2b196985c30d5c6321739587dfa90d13b320c50fdf6e3d219e09b", "1.74.0--r43hf17093f_0": "sha256:221926e7d87a38f5375086dd88a9e2f47ae61ed6be2d890069d3b07d220c3431", "1.74.0--r43hf17093f_1": "sha256:de695830bdd8faf6094fb441465a888d6c7d560e5da577e7879ee1731adc2569"}, "docker": "quay.io/biocontainers/bioconductor-affxparser"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affxparser.
shpc-registry automated BioContainers addition for bioconductor-affxparser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affxparser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affxparser:1.74.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affxparser/1.74.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-affxparser/1.74.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affxparser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affxparser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affxparser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affxparser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affxparser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affxparser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affxparser

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