---
layout: container
name:  "quay.io/biocontainers/deeparg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deeparg/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deeparg/container.yaml"
updated_at: "2022-10-27 00:32:40.736519"
latest: "1.0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/deeparg"
aliases:
 - "deeparg"
 - "theano-test"
versions:
 - "1.0.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for deeparg"
config: {"url": "https://biocontainers.pro/tools/deeparg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deeparg", "latest": {"1.0.2--pyhdfd78af_1": "sha256:e832b2c8217b058b9fba5bd61be0c87f03721464bfb7bc7025ed100414b974bf"}, "tags": {"1.0.2--pyhdfd78af_1": "sha256:e832b2c8217b058b9fba5bd61be0c87f03721464bfb7bc7025ed100414b974bf"}, "docker": "quay.io/biocontainers/deeparg", "aliases": {"deeparg": "/usr/local/bin/deeparg", "theano-test": "/usr/local/bin/theano-test"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deeparg.
shpc-registry automated BioContainers addition for deeparg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deeparg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deeparg:1.0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deeparg/1.0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/deeparg/1.0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deeparg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deeparg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deeparg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deeparg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deeparg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deeparg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deeparg

```bash
$ singularity exec <container> /usr/local/bin/deeparg
$ podman run --it --rm --entrypoint /usr/local/bin/deeparg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deeparg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-test

```bash
$ singularity exec <container> /usr/local/bin/theano-test
$ podman run --it --rm --entrypoint /usr/local/bin/theano-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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