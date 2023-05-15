---
layout: container
name:  "quay.io/biocontainers/bioconductor-shortread"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-shortread/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-shortread/container.yaml"
updated_at: "2023-05-15 04:10:10.308689"
latest: "1.56.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-shortread"

versions:
 - "1.52.0--r41hc247a5b_2"
 - "1.56.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-shortread"
config: {"url": "https://biocontainers.pro/tools/bioconductor-shortread", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-shortread", "latest": {"1.56.0--r42hc247a5b_0": "sha256:d5eafad82984223bd84e7af53b29a1adbf9591e7db27630875774fe3b97e77ac"}, "tags": {"1.52.0--r41hc247a5b_2": "sha256:77cb697d362696e9e66c70ed1131bf515a713d42d304038d788e73b1b1b1927a", "1.56.0--r42hc247a5b_0": "sha256:d5eafad82984223bd84e7af53b29a1adbf9591e7db27630875774fe3b97e77ac"}, "docker": "quay.io/biocontainers/bioconductor-shortread"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-shortread.
shpc-registry automated BioContainers addition for bioconductor-shortread
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-shortread
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-shortread:1.56.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-shortread/1.56.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-shortread/1.56.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-shortread-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shortread-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shortread-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-shortread-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-shortread-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-shortread-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-shortread

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