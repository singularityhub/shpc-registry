---
layout: container
name:  "quay.io/biocontainers/bioconductor-iseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iseq/container.yaml"
updated_at: "2024-08-04 03:09:12.725756"
latest: "1.54.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-iseq"

versions:
 - "1.46.0--r41hc0cfd56_2"
 - "1.50.0--r42hc0cfd56_0"
 - "1.50.0--r42ha9d7317_2"
 - "1.52.0--r43ha9d7317_0"
 - "1.54.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-iseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iseq", "latest": {"1.54.0--r43ha9d7317_1": "sha256:0217cc7293af47ace3e582b6cfdc8f7aec10cfced9fad934c40acf47654f38a3"}, "tags": {"1.46.0--r41hc0cfd56_2": "sha256:7f21aa5ab2325326d8596e860745b710cc0c556e21676c64755ef4072ef06fdf", "1.50.0--r42hc0cfd56_0": "sha256:7751d775c2a4aaa94d1b160df93bed60202ac62391b68e0955b7b19508bb54b0", "1.50.0--r42ha9d7317_2": "sha256:a8fc196c4e2656d2964bc9068e1d86188cac0161c60015ba94c6710104955836", "1.52.0--r43ha9d7317_0": "sha256:29352cfdc534ecd4fecf0fbb08ad2f5cd520ee8f66052dbaee599f12193a3f39", "1.54.0--r43ha9d7317_1": "sha256:0217cc7293af47ace3e582b6cfdc8f7aec10cfced9fad934c40acf47654f38a3"}, "docker": "quay.io/biocontainers/bioconductor-iseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iseq.
shpc-registry automated BioContainers addition for bioconductor-iseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iseq:1.54.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iseq/1.54.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-iseq/1.54.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-iseq

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