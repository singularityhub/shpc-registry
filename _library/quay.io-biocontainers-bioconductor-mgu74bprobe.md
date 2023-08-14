---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74bprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74bprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74bprobe/container.yaml"
updated_at: "2023-08-14 03:08:17.246659"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74bprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74bprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74bprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74bprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:3b03844e7954cb33c7504ee481dbab0f0bf65e33e3bab5b366012842145b5ff7"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:adea9f4e37011cc88331f1a7901c0efdbd3d903b425bca81244ae09772116e90", "2.18.0--r42hdfd78af_10": "sha256:8f8f3031826c3b798b0d5ed9db5042578a1e3ace9b71a4ef25ed337bde0a7474", "2.18.0--r43hdfd78af_11": "sha256:3b03844e7954cb33c7504ee481dbab0f0bf65e33e3bab5b366012842145b5ff7"}, "docker": "quay.io/biocontainers/bioconductor-mgu74bprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74bprobe.
shpc-registry automated BioContainers addition for bioconductor-mgu74bprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74bprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-mgu74bprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74bprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74bprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74bprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74bprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74bprobe

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