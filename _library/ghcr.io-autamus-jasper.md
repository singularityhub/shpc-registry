---
layout: container
name:  "ghcr.io/autamus/jasper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/jasper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/jasper/container.yaml"
updated_at: "2024-04-04 03:47:19.878408"
latest: "20210822.2247"
container_url: "https://github.com/orgs/autamus/packages/container/package/jasper"
aliases:
 - "jasper"
 - "jpegtran"
versions:
 - "2.0.32"
 - "2.0.33"
 - "latest"
 - "20210822.2247"
description: "JasPer is a collection of software (i.e., a library and application programs) for the coding and manipulation of images."
config: {"docker": "ghcr.io/autamus/jasper", "url": "https://github.com/orgs/autamus/packages/container/package/jasper", "maintainer": "@vsoch", "description": "JasPer is a collection of software (i.e., a library and application programs) for the coding and manipulation of images.", "latest": {"20210822.2247": "sha256:3daa467e6540c4687cdba590c74ef74feb866e5f2a8145bc592f4b89869d393c"}, "tags": {"2.0.32": "sha256:b6859fabe2d63ee45a5c3ff5aa3adeac11c3faf85a4e087c0abcc61e43e41f03", "2.0.33": "sha256:a675864cf6035dbf891e3af7f2b3c70e4c8e3e03c6cf5570dbe3ea259b68886d", "latest": "sha256:31ff2e3442c909eeb41ae66b5c2c3b92674275a53620430bd1f5d50953b99809", "20210822.2247": "sha256:3daa467e6540c4687cdba590c74ef74feb866e5f2a8145bc592f4b89869d393c"}, "aliases": {"jasper": "/opt/view/bin/jasper", "jpegtran": "/opt/view/bin/jpegtran"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/jasper.
JasPer is a collection of software (i.e., a library and application programs) for the coding and manipulation of images.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/jasper
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/jasper:20210822.2247
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/jasper/20210822.2247
$ module help ghcr.io/autamus/jasper/20210822.2247
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jasper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jasper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jasper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jasper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jasper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jasper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jasper

```bash
$ singularity exec <container> /opt/view/bin/jasper
$ podman run --it --rm --entrypoint /opt/view/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpegtran

```bash
$ singularity exec <container> /opt/view/bin/jpegtran
$ podman run --it --rm --entrypoint /opt/view/bin/jpegtran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jpegtran   -v ${PWD} -w ${PWD} <container> -c " $@"
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