---
layout: container
name:  "quay.io/biocontainers/deepsvr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepsvr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deepsvr/container.yaml"
updated_at: "2025-03-30 03:16:35.195514"
latest: "0.1.0--py_0"
container_url: "https://biocontainers.pro/tools/deepsvr"
aliases:
 - "bam-readcount"
 - "convert_zero_one_based"
 - "deepsvr"
 - "pbr"
 - "theano-cache"
 - "theano-nose"
 - "mako-render"
 - "perl5.22.0"
 - "tensorboard"
 - "c2ph"
 - "pstruct"
 - "qhelpconverter"
 - "protoc"
versions:
 - "0.1.0--py_0"
description: "shpc-registry automated BioContainers addition for deepsvr"
config: {"url": "https://biocontainers.pro/tools/deepsvr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepsvr", "latest": {"0.1.0--py_0": "sha256:2d1394d03b1aad83163774a5952f8383b5c9bd72c78312b84fbe2b61e8840060"}, "tags": {"0.1.0--py_0": "sha256:2d1394d03b1aad83163774a5952f8383b5c9bd72c78312b84fbe2b61e8840060"}, "docker": "quay.io/biocontainers/deepsvr", "aliases": {"bam-readcount": "/usr/local/bin/bam-readcount", "convert_zero_one_based": "/usr/local/bin/convert_zero_one_based", "deepsvr": "/usr/local/bin/deepsvr", "pbr": "/usr/local/bin/pbr", "theano-cache": "/usr/local/bin/theano-cache", "theano-nose": "/usr/local/bin/theano-nose", "mako-render": "/usr/local/bin/mako-render", "perl5.22.0": "/usr/local/bin/perl5.22.0", "tensorboard": "/usr/local/bin/tensorboard", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "qhelpconverter": "/usr/local/bin/qhelpconverter", "protoc": "/usr/local/bin/protoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepsvr.
shpc-registry automated BioContainers addition for deepsvr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepsvr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepsvr:0.1.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepsvr/0.1.0--py_0
$ module help quay.io/biocontainers/deepsvr/0.1.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepsvr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepsvr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepsvr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepsvr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepsvr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepsvr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam-readcount

```bash
$ singularity exec <container> /usr/local/bin/bam-readcount
$ podman run --it --rm --entrypoint /usr/local/bin/bam-readcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam-readcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_zero_one_based

```bash
$ singularity exec <container> /usr/local/bin/convert_zero_one_based
$ podman run --it --rm --entrypoint /usr/local/bin/convert_zero_one_based   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_zero_one_based   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deepsvr

```bash
$ singularity exec <container> /usr/local/bin/deepsvr
$ podman run --it --rm --entrypoint /usr/local/bin/deepsvr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepsvr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbr

```bash
$ singularity exec <container> /usr/local/bin/pbr
$ podman run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tensorboard

```bash
$ singularity exec <container> /usr/local/bin/tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc

```bash
$ singularity exec <container> /usr/local/bin/protoc
$ podman run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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