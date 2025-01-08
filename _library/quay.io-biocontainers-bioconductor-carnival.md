---
layout: container
name:  "quay.io/biocontainers/bioconductor-carnival"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-carnival/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-carnival/container.yaml"
updated_at: "2025-01-08 07:06:03.577601"
latest: "2.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-carnival"
aliases:
 - "pandoc"
versions:
 - "2.4.0--r41hdfd78af_0"
 - "2.8.0--r42hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-carnival"
config: {"url": "https://biocontainers.pro/tools/bioconductor-carnival", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-carnival", "latest": {"2.16.0--r44hdfd78af_0": "sha256:481dc367730b01e19cc126f04eda89fac39b31f57a8df2ae33e4e4e2efa7a899"}, "tags": {"2.4.0--r41hdfd78af_0": "sha256:b6a8510407cbfe91fe07ba619a1f15ab22b3253261ebd7cae827db989a29cb46", "2.8.0--r42hdfd78af_0": "sha256:b34523325b711cf734675b49b8f48f0afc65bbc6b52380b2db16543bb51ef71c", "2.10.0--r43hdfd78af_0": "sha256:fe532a47833ada8c4745e801e4936f0791231ccf70994d2e6df330a226d5af27", "2.12.0--r43hdfd78af_0": "sha256:f0ba61f68a3ea714143ff2e0ee105ae4e7c5f37cb9f8f1aa52c07dffa91c9aa6", "2.16.0--r44hdfd78af_0": "sha256:481dc367730b01e19cc126f04eda89fac39b31f57a8df2ae33e4e4e2efa7a899"}, "docker": "quay.io/biocontainers/bioconductor-carnival", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-carnival.
shpc-registry automated BioContainers addition for bioconductor-carnival
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-carnival
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-carnival:2.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-carnival/2.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-carnival/2.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-carnival-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-carnival-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-carnival-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-carnival-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-carnival-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-carnival-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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