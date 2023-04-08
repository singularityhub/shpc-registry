---
layout: container
name:  "quay.io/biocontainers/bioconductor-normqpcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-normqpcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-normqpcr/container.yaml"
updated_at: "2023-04-08 03:11:14.595885"
latest: "1.44.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-normqpcr"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-normqpcr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-normqpcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-normqpcr", "latest": {"1.44.0--r42hdfd78af_0": "sha256:c8d8b4248f6a294888c6c203f7d90f1c48eff0b4a3b488582856c578309981ed"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:fd2bec571b1adaec3036374602852ae01a83d979a4882a0ad47a202530a8e426", "1.44.0--r42hdfd78af_0": "sha256:c8d8b4248f6a294888c6c203f7d90f1c48eff0b4a3b488582856c578309981ed"}, "docker": "quay.io/biocontainers/bioconductor-normqpcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-normqpcr.
shpc-registry automated BioContainers addition for bioconductor-normqpcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-normqpcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-normqpcr:1.44.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-normqpcr/1.44.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-normqpcr/1.44.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-normqpcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normqpcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normqpcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-normqpcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-normqpcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-normqpcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-normqpcr

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