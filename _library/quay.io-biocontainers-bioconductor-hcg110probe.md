---
layout: container
name:  "quay.io/biocontainers/bioconductor-hcg110probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hcg110probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hcg110probe/container.yaml"
updated_at: "2023-01-21 03:10:02.366327"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-hcg110probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-hcg110probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hcg110probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hcg110probe", "latest": {"2.18.0--r42hdfd78af_10": "sha256:b00c31f6645d4bb5f9fcbfb5e308dcf6154310197bc273ec6a601e7e76a8a23e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c095c6486a3461aa4041e87d145c5a98914e0cf014135a6dc596aa0c48aae56b", "2.18.0--r42hdfd78af_10": "sha256:b00c31f6645d4bb5f9fcbfb5e308dcf6154310197bc273ec6a601e7e76a8a23e"}, "docker": "quay.io/biocontainers/bioconductor-hcg110probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hcg110probe.
shpc-registry automated BioContainers addition for bioconductor-hcg110probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hcg110probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hcg110probe:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hcg110probe/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-hcg110probe/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hcg110probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hcg110probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hcg110probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hcg110probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hcg110probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hcg110probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hcg110probe

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