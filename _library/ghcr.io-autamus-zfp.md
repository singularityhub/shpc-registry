---
layout: container
name:  "ghcr.io/autamus/zfp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/zfp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/zfp/container.yaml"
updated_at: "2024-04-27 03:10:49.334606"
latest: "0.5.5"
container_url: "https://github.com/orgs/autamus/packages/container/package/zfp"

versions:
 - "0.5.5"
 - "latest"
description: "zfp is a compressed number format for multidimensional floating-point and integer arrays."
config: {"docker": "ghcr.io/autamus/zfp", "url": "https://github.com/orgs/autamus/packages/container/package/zfp", "maintainer": "@vsoch", "description": "zfp is a compressed number format for multidimensional floating-point and integer arrays.", "latest": {"0.5.5": "sha256:95051afe1d3cf610dd9e260d9418b145aa52a1b8e8458380f36984ae23484cc3"}, "tags": {"0.5.5": "sha256:95051afe1d3cf610dd9e260d9418b145aa52a1b8e8458380f36984ae23484cc3", "latest": "sha256:95051afe1d3cf610dd9e260d9418b145aa52a1b8e8458380f36984ae23484cc3"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/zfp.
zfp is a compressed number format for multidimensional floating-point and integer arrays.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/zfp
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/zfp:0.5.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/zfp/0.5.5
$ module help ghcr.io/autamus/zfp/0.5.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zfp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zfp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zfp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zfp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zfp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zfp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### zfp

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