---
layout: container
name:  "quay.io/biocontainers/acms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/acms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/acms/container.yaml"
updated_at: "2025-02-16 02:57:13.741660"
latest: "1.3.0--pl5321h9948957_2"
container_url: "https://biocontainers.pro/tools/acms"
aliases:
 - "acmbuild"
 - "acmbuild_checkCompatibility"
 - "acmbuild_train"
 - "acmsearch"
 - "addRNAoptions.pl"
 - "gapc"
 - "ghc"
 - "ghc-8.10.7"
 - "ghc-pkg"
 - "ghc-pkg-8.10.7"
 - "ghci"
 - "ghci-8.10.7"
 - "hp2ps"
 - "hpc"
 - "hsc2hs"
 - "runghc"
 - "runghc-8.10.7"
 - "runhaskell"
versions:
 - "1.3.0--pl5321h4ac6f70_1"
 - "1.3.0--pl5321h9948957_2"
description: "singularity registry hpc automated addition for acms"
config: {"url": "https://biocontainers.pro/tools/acms", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for acms", "latest": {"1.3.0--pl5321h9948957_2": "sha256:3f6a1c89887bd1d02536e51deac651925d7479d2ca981fecbd45a2c027ccdde1"}, "tags": {"1.3.0--pl5321h4ac6f70_1": "sha256:d03b87ff7e995e55d2489df9b2bbc6f8961f2e8e9d65efa093b785c51b8ca00e", "1.3.0--pl5321h9948957_2": "sha256:3f6a1c89887bd1d02536e51deac651925d7479d2ca981fecbd45a2c027ccdde1"}, "docker": "quay.io/biocontainers/acms", "aliases": {"acmbuild": "/usr/local/bin/acmbuild", "acmbuild_checkCompatibility": "/usr/local/bin/acmbuild_checkCompatibility", "acmbuild_train": "/usr/local/bin/acmbuild_train", "acmsearch": "/usr/local/bin/acmsearch", "addRNAoptions.pl": "/usr/local/bin/addRNAoptions.pl", "gapc": "/usr/local/bin/gapc", "ghc": "/usr/local/bin/ghc", "ghc-8.10.7": "/usr/local/bin/ghc-8.10.7", "ghc-pkg": "/usr/local/bin/ghc-pkg", "ghc-pkg-8.10.7": "/usr/local/bin/ghc-pkg-8.10.7", "ghci": "/usr/local/bin/ghci", "ghci-8.10.7": "/usr/local/bin/ghci-8.10.7", "hp2ps": "/usr/local/bin/hp2ps", "hpc": "/usr/local/bin/hpc", "hsc2hs": "/usr/local/bin/hsc2hs", "runghc": "/usr/local/bin/runghc", "runghc-8.10.7": "/usr/local/bin/runghc-8.10.7", "runhaskell": "/usr/local/bin/runhaskell"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/acms.
singularity registry hpc automated addition for acms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/acms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/acms:1.3.0--pl5321h9948957_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/acms/1.3.0--pl5321h9948957_2
$ module help quay.io/biocontainers/acms/1.3.0--pl5321h9948957_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### acms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### acms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### acms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### acms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### acms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### acms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### acmbuild

```bash
$ singularity exec <container> /usr/local/bin/acmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/acmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acmbuild_checkCompatibility

```bash
$ singularity exec <container> /usr/local/bin/acmbuild_checkCompatibility
$ podman run --it --rm --entrypoint /usr/local/bin/acmbuild_checkCompatibility   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acmbuild_checkCompatibility   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acmbuild_train

```bash
$ singularity exec <container> /usr/local/bin/acmbuild_train
$ podman run --it --rm --entrypoint /usr/local/bin/acmbuild_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acmbuild_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acmsearch

```bash
$ singularity exec <container> /usr/local/bin/acmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/acmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addRNAoptions.pl

```bash
$ singularity exec <container> /usr/local/bin/addRNAoptions.pl
$ podman run --it --rm --entrypoint /usr/local/bin/addRNAoptions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addRNAoptions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gapc

```bash
$ singularity exec <container> /usr/local/bin/gapc
$ podman run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghc

```bash
$ singularity exec <container> /usr/local/bin/ghc
$ podman run --it --rm --entrypoint /usr/local/bin/ghc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghc-8.10.7

```bash
$ singularity exec <container> /usr/local/bin/ghc-8.10.7
$ podman run --it --rm --entrypoint /usr/local/bin/ghc-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghc-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghc-pkg

```bash
$ singularity exec <container> /usr/local/bin/ghc-pkg
$ podman run --it --rm --entrypoint /usr/local/bin/ghc-pkg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghc-pkg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghc-pkg-8.10.7

```bash
$ singularity exec <container> /usr/local/bin/ghc-pkg-8.10.7
$ podman run --it --rm --entrypoint /usr/local/bin/ghc-pkg-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghc-pkg-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghci

```bash
$ singularity exec <container> /usr/local/bin/ghci
$ podman run --it --rm --entrypoint /usr/local/bin/ghci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghci-8.10.7

```bash
$ singularity exec <container> /usr/local/bin/ghci-8.10.7
$ podman run --it --rm --entrypoint /usr/local/bin/ghci-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghci-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hp2ps

```bash
$ singularity exec <container> /usr/local/bin/hp2ps
$ podman run --it --rm --entrypoint /usr/local/bin/hp2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hp2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpc

```bash
$ singularity exec <container> /usr/local/bin/hpc
$ podman run --it --rm --entrypoint /usr/local/bin/hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsc2hs

```bash
$ singularity exec <container> /usr/local/bin/hsc2hs
$ podman run --it --rm --entrypoint /usr/local/bin/hsc2hs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsc2hs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runghc

```bash
$ singularity exec <container> /usr/local/bin/runghc
$ podman run --it --rm --entrypoint /usr/local/bin/runghc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runghc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runghc-8.10.7

```bash
$ singularity exec <container> /usr/local/bin/runghc-8.10.7
$ podman run --it --rm --entrypoint /usr/local/bin/runghc-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runghc-8.10.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhaskell

```bash
$ singularity exec <container> /usr/local/bin/runhaskell
$ podman run --it --rm --entrypoint /usr/local/bin/runhaskell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhaskell   -v ${PWD} -w ${PWD} <container> -c " $@"
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