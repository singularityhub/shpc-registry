---
layout: container
name:  "quay.io/biocontainers/bugseq-porechop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bugseq-porechop/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bugseq-porechop/container.yaml"
updated_at: "2022-10-27 00:28:02.822950"
latest: "0.3.4pre--py37h96cfd12_2"
container_url: "https://biocontainers.pro/tools/bugseq-porechop"

versions:
 - "0.3.4pre--py37h96cfd12_2"
description: "shpc-registry automated BioContainers addition for bugseq-porechop"
config: {"url": "https://biocontainers.pro/tools/bugseq-porechop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bugseq-porechop", "latest": {"0.3.4pre--py37h96cfd12_2": "sha256:f95fb3004e6dd2f7364be4d9872a0deba3732382ed682a8c82aa554d4ecabf26"}, "tags": {"0.3.4pre--py37h96cfd12_2": "sha256:f95fb3004e6dd2f7364be4d9872a0deba3732382ed682a8c82aa554d4ecabf26"}, "docker": "quay.io/biocontainers/bugseq-porechop"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bugseq-porechop.
shpc-registry automated BioContainers addition for bugseq-porechop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bugseq-porechop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bugseq-porechop:0.3.4pre--py37h96cfd12_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bugseq-porechop/0.3.4pre--py37h96cfd12_2
$ module help quay.io/biocontainers/bugseq-porechop/0.3.4pre--py37h96cfd12_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bugseq-porechop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bugseq-porechop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bugseq-porechop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bugseq-porechop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bugseq-porechop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bugseq-porechop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bugseq-porechop

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