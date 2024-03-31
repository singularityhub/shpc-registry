---
layout: container
name:  "quay.io/biocontainers/bioconductor-droplettestfiles"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-droplettestfiles/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-droplettestfiles/container.yaml"
updated_at: "2024-03-31 02:30:57.158701"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-droplettestfiles"

versions:
 - "1.4.0--r41hdfd78af_1"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-droplettestfiles"
config: {"url": "https://biocontainers.pro/tools/bioconductor-droplettestfiles", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-droplettestfiles", "latest": {"1.12.0--r43hdfd78af_0": "sha256:607ee1102788c8539b1a44f7c32e5439cc60e398a27d49d762bb2591979d9d58"}, "tags": {"1.4.0--r41hdfd78af_1": "sha256:36e9970f718ea5b738253b6e6cbd40726eb415b685bb1d484631272f8ca038fd", "1.8.0--r42hdfd78af_0": "sha256:5819f5de05b608122db6e0e4ffb5efa4b51615d87a6645d57ba7742a69da496f", "1.10.0--r43hdfd78af_0": "sha256:feae2b8222c656dc1855cec631cc9b30979d5cab75f4f83fc0d38c9e4fa6dd14", "1.12.0--r43hdfd78af_0": "sha256:607ee1102788c8539b1a44f7c32e5439cc60e398a27d49d762bb2591979d9d58"}, "docker": "quay.io/biocontainers/bioconductor-droplettestfiles"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-droplettestfiles.
shpc-registry automated BioContainers addition for bioconductor-droplettestfiles
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-droplettestfiles
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-droplettestfiles:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-droplettestfiles/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-droplettestfiles/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-droplettestfiles-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-droplettestfiles-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-droplettestfiles-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-droplettestfiles-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-droplettestfiles-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-droplettestfiles-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-droplettestfiles

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