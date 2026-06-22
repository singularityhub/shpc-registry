---
layout: container
name:  "quay.io/biocontainers/perl-crypt-openssl-bignum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-crypt-openssl-bignum/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-crypt-openssl-bignum/container.yaml"
updated_at: "2026-06-22 02:42:45.355236"
latest: "0.09--pl5321hd474d78_0"
container_url: "https://biocontainers.pro/tools/perl-crypt-openssl-bignum"

versions:
 - "0.09--pl5321hd474d78_0"
description: "singularity registry hpc automated addition for perl-crypt-openssl-bignum"
config: {"url": "https://biocontainers.pro/tools/perl-crypt-openssl-bignum", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-crypt-openssl-bignum", "latest": {"0.09--pl5321hd474d78_0": "sha256:db9f98268360c700e36fdda139e620011c3772f4ee704a049c06b50515ed1b4b"}, "tags": {"0.09--pl5321hd474d78_0": "sha256:db9f98268360c700e36fdda139e620011c3772f4ee704a049c06b50515ed1b4b"}, "docker": "quay.io/biocontainers/perl-crypt-openssl-bignum"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-crypt-openssl-bignum.
singularity registry hpc automated addition for perl-crypt-openssl-bignum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-crypt-openssl-bignum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-crypt-openssl-bignum:0.09--pl5321hd474d78_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-crypt-openssl-bignum/0.09--pl5321hd474d78_0
$ module help quay.io/biocontainers/perl-crypt-openssl-bignum/0.09--pl5321hd474d78_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-crypt-openssl-bignum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-crypt-openssl-bignum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-crypt-openssl-bignum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-crypt-openssl-bignum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-crypt-openssl-bignum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-crypt-openssl-bignum-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-crypt-openssl-bignum

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