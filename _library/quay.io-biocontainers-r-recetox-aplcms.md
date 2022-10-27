---
layout: container
name:  "quay.io/biocontainers/r-recetox-aplcms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-recetox-aplcms/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-recetox-aplcms/container.yaml"
updated_at: "2022-10-27 00:39:13.826623"
latest: "0.9.4--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-recetox-aplcms"
aliases:
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
versions:
 - "0.9.4--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-recetox-aplcms"
config: {"url": "https://biocontainers.pro/tools/r-recetox-aplcms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-recetox-aplcms", "latest": {"0.9.4--r41hdfd78af_0": "sha256:99b0b84eed1ed66dd9793caa02eeb5062ad1e543f32e1209835d2314ef41016e"}, "tags": {"0.9.4--r41hdfd78af_0": "sha256:99b0b84eed1ed66dd9793caa02eeb5062ad1e543f32e1209835d2314ef41016e"}, "docker": "quay.io/biocontainers/r-recetox-aplcms", "aliases": {"elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-recetox-aplcms.
shpc-registry automated BioContainers addition for r-recetox-aplcms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-recetox-aplcms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-recetox-aplcms:0.9.4--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-recetox-aplcms/0.9.4--r41hdfd78af_0
$ module help quay.io/biocontainers/r-recetox-aplcms/0.9.4--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-recetox-aplcms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-recetox-aplcms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-recetox-aplcms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-recetox-aplcms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-recetox-aplcms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-recetox-aplcms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
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