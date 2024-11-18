---
layout: container
name:  "quay.io/biocontainers/bioconductor-mimosa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mimosa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mimosa/container.yaml"
updated_at: "2024-11-18 03:18:26.187069"
latest: "1.37.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mimosa"

versions:
 - "1.32.0--r41hc247a5b_2"
 - "1.36.0--r42hc247a5b_0"
 - "1.36.0--r42hf17093f_1"
 - "1.37.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mimosa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mimosa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mimosa", "latest": {"1.37.0--r43hf17093f_0": "sha256:ba215bca2d589d6dcbb76177a142916b8548f2301fffced40a56959a98f2c3cc"}, "tags": {"1.32.0--r41hc247a5b_2": "sha256:0e2ad68c2223c504159a7f9104a75be736e64960671c5492d5d6ae8f30b1a28e", "1.36.0--r42hc247a5b_0": "sha256:cc4545f4844c26e0b51dbad4292d2d7a7233ba95890564f9e9b509f87ecbce6c", "1.36.0--r42hf17093f_1": "sha256:91655672df86d932188e826f03550e373c95be423170e19a5a7cc56ffcfd6708", "1.37.0--r43hf17093f_0": "sha256:ba215bca2d589d6dcbb76177a142916b8548f2301fffced40a56959a98f2c3cc"}, "docker": "quay.io/biocontainers/bioconductor-mimosa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mimosa.
shpc-registry automated BioContainers addition for bioconductor-mimosa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mimosa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mimosa:1.37.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mimosa/1.37.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-mimosa/1.37.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mimosa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mimosa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mimosa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mimosa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mimosa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mimosa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mimosa

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