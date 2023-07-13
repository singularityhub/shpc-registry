---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylscaper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylscaper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylscaper/container.yaml"
updated_at: "2023-07-13 03:30:05.205382"
latest: "1.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylscaper"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylscaper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylscaper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylscaper", "latest": {"1.6.0--r42hdfd78af_0": "sha256:7005edb2ca3892f56762cad8905b41e33004b8553a618ba8b04b02e9e49f74d2"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:acc9c9cf853dbeebfa7fdf02538e38bbf1279a6d2f6d0a5a8346cdbe049ad92d", "1.6.0--r42hdfd78af_0": "sha256:7005edb2ca3892f56762cad8905b41e33004b8553a618ba8b04b02e9e49f74d2"}, "docker": "quay.io/biocontainers/bioconductor-methylscaper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylscaper.
shpc-registry automated BioContainers addition for bioconductor-methylscaper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylscaper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylscaper:1.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylscaper/1.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylscaper/1.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylscaper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylscaper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylscaper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylscaper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylscaper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylscaper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylscaper

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