---
layout: container
name:  "quay.io/biocontainers/platon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/platon/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/platon/container.yaml"
updated_at: "2022-10-27 00:43:03.305253"
latest: "1.6--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/platon"
aliases:
 - "delta2vcf"
 - "platon"
versions:
 - "1.6--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for platon"
config: {"url": "https://biocontainers.pro/tools/platon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for platon", "latest": {"1.6--pyhdfd78af_1": "sha256:09223057e5494cc75a342d646b59ffc82faa987fb2ab4b4470317ada1f7c567b"}, "tags": {"1.6--pyhdfd78af_1": "sha256:09223057e5494cc75a342d646b59ffc82faa987fb2ab4b4470317ada1f7c567b"}, "docker": "quay.io/biocontainers/platon", "aliases": {"delta2vcf": "/usr/local/bin/delta2vcf", "platon": "/usr/local/bin/platon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/platon.
shpc-registry automated BioContainers addition for platon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/platon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/platon:1.6--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/platon/1.6--pyhdfd78af_1
$ module help quay.io/biocontainers/platon/1.6--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### platon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### platon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### platon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### platon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### platon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### platon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delta2vcf

```bash
$ singularity exec <container> /usr/local/bin/delta2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### platon

```bash
$ singularity exec <container> /usr/local/bin/platon
$ podman run --it --rm --entrypoint /usr/local/bin/platon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/platon   -v ${PWD} -w ${PWD} <container> -c " $@"
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