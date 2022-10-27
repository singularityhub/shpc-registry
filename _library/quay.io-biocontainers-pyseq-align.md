---
layout: container
name:  "quay.io/biocontainers/pyseq-align"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyseq-align/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pyseq-align/container.yaml"
updated_at: "2022-10-27 00:58:21.895512"
latest: "1.0.2--py37h8902056_1"
container_url: "https://biocontainers.pro/tools/pyseq-align"

versions:
 - "1.0.2--py37h8902056_1"
description: "shpc-registry automated BioContainers addition for pyseq-align"
config: {"url": "https://biocontainers.pro/tools/pyseq-align", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyseq-align", "latest": {"1.0.2--py37h8902056_1": "sha256:c73c1742fc1b767f7a9695e79ad8e94de1902382c63efc0dce9bd124e99032f0"}, "tags": {"1.0.2--py37h8902056_1": "sha256:c73c1742fc1b767f7a9695e79ad8e94de1902382c63efc0dce9bd124e99032f0"}, "docker": "quay.io/biocontainers/pyseq-align"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyseq-align.
shpc-registry automated BioContainers addition for pyseq-align
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyseq-align
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyseq-align:1.0.2--py37h8902056_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyseq-align/1.0.2--py37h8902056_1
$ module help quay.io/biocontainers/pyseq-align/1.0.2--py37h8902056_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyseq-align-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyseq-align-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyseq-align-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyseq-align-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyseq-align-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyseq-align-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pyseq-align

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