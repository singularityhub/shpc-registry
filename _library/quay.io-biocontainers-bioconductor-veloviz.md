---
layout: container
name:  "quay.io/biocontainers/bioconductor-veloviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-veloviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-veloviz/container.yaml"
updated_at: "2024-01-23 03:09:22.861882"
latest: "1.8.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-veloviz"
aliases:
 - "glpsol"
versions:
 - "1.0.0--r41hc247a5b_2"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_2"
 - "1.6.0--r43hf17093f_0"
 - "1.8.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-veloviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-veloviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-veloviz", "latest": {"1.8.0--r43hf17093f_0": "sha256:77bf5aee19d5fb317feb53c8beeed8d3e5f50e3734796ab27afa2c78e347d0ac"}, "tags": {"1.0.0--r41hc247a5b_2": "sha256:773acab824a6e8f966c76cb7fc8bf53447ce7a1ab6f0238dab0ad54bc49a33b7", "1.4.0--r42hc247a5b_0": "sha256:893f3de9188cbf1f68515bfa7d6e088bdcbbdfc86c3b6f2ff4811444c8ed2aaa", "1.4.0--r42hf17093f_2": "sha256:580b008799d4bf5e82ea50aa03258ec74c7b34e660fe8298ae7cc42092ad843d", "1.6.0--r43hf17093f_0": "sha256:57348066700b76d621ec19b3de20b0a3693a2c0377680f6d20cbe1584b50d50e", "1.8.0--r43hf17093f_0": "sha256:77bf5aee19d5fb317feb53c8beeed8d3e5f50e3734796ab27afa2c78e347d0ac"}, "docker": "quay.io/biocontainers/bioconductor-veloviz", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-veloviz.
shpc-registry automated BioContainers addition for bioconductor-veloviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-veloviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-veloviz:1.8.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-veloviz/1.8.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-veloviz/1.8.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-veloviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-veloviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-veloviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-veloviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-veloviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-veloviz-inspect-deffile:

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