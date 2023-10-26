---
layout: container
name:  "quay.io/biocontainers/advntr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/advntr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/advntr/container.yaml"
updated_at: "2023-10-26 03:09:20.732684"
latest: "1.5.0--py36hd5865be_0"
container_url: "https://biocontainers.pro/tools/advntr"
aliases:
 - "adVNTR-Filtering"
 - "advntr"
 - "unit2"
 - "theano-cache"
 - "theano-nose"
 - "freeze_graph"
 - "mako-render"
 - "tf_upgrade_v2"
 - "muscle"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
versions:
 - "1.4.1--py27h20e14e4_2"
 - "1.5.0--py36hd5865be_0"
description: "shpc-registry automated BioContainers addition for advntr"
config: {"url": "https://biocontainers.pro/tools/advntr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for advntr", "latest": {"1.5.0--py36hd5865be_0": "sha256:29fec9d9b419bbd63a5e48aea4979807078d74b70b8d5bef4e6c1cd6a9a637c5"}, "tags": {"1.4.1--py27h20e14e4_2": "sha256:0b569503b0f7a84ffaccd92ad555bdcaf38b9dc30a8d5dd1a2918e124aaec70d", "1.5.0--py36hd5865be_0": "sha256:29fec9d9b419bbd63a5e48aea4979807078d74b70b8d5bef4e6c1cd6a9a637c5"}, "docker": "quay.io/biocontainers/advntr", "aliases": {"adVNTR-Filtering": "/usr/local/bin/adVNTR-Filtering", "advntr": "/usr/local/bin/advntr", "unit2": "/usr/local/bin/unit2", "theano-cache": "/usr/local/bin/theano-cache", "theano-nose": "/usr/local/bin/theano-nose", "freeze_graph": "/usr/local/bin/freeze_graph", "mako-render": "/usr/local/bin/mako-render", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2", "muscle": "/usr/local/bin/muscle", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/advntr.
shpc-registry automated BioContainers addition for advntr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/advntr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/advntr:1.5.0--py36hd5865be_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/advntr/1.5.0--py36hd5865be_0
$ module help quay.io/biocontainers/advntr/1.5.0--py36hd5865be_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### advntr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### advntr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### advntr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### advntr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### advntr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### advntr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adVNTR-Filtering

```bash
$ singularity exec <container> /usr/local/bin/adVNTR-Filtering
$ podman run --it --rm --entrypoint /usr/local/bin/adVNTR-Filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adVNTR-Filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### advntr

```bash
$ singularity exec <container> /usr/local/bin/advntr
$ podman run --it --rm --entrypoint /usr/local/bin/advntr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/advntr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unit2

```bash
$ singularity exec <container> /usr/local/bin/unit2
$ podman run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-cache

```bash
$ singularity exec <container> /usr/local/bin/theano-cache
$ podman run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-nose

```bash
$ singularity exec <container> /usr/local/bin/theano-nose
$ podman run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freeze_graph

```bash
$ singularity exec <container> /usr/local/bin/freeze_graph
$ podman run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tflite_convert

```bash
$ singularity exec <container> /usr/local/bin/tflite_convert
$ podman run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saved_model_cli

```bash
$ singularity exec <container> /usr/local/bin/saved_model_cli
$ podman run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco

```bash
$ singularity exec <container> /usr/local/bin/toco
$ podman run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
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