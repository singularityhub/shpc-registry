---
layout: container
name:  "quay.io/biocontainers/kyototycoon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kyototycoon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kyototycoon/container.yaml"
updated_at: "2024-01-18 02:37:11.309391"
latest: "20170410--h27c383b_4"
container_url: "https://biocontainers.pro/tools/kyototycoon"
aliases:
 - "kccachetest"
 - "kcdirmgr"
 - "kcdirtest"
 - "kcforestmgr"
 - "kcforesttest"
 - "kcgrasstest"
 - "kchashmgr"
 - "kchashtest"
 - "kclangctest"
 - "kcpolymgr"
 - "kcpolytest"
 - "kcprototest"
 - "kcstashtest"
 - "kctreemgr"
 - "kctreetest"
 - "kcutilmgr"
 - "kcutiltest"
 - "ktremotemgr"
 - "ktremotetest"
 - "ktserver"
 - "kttimedmgr"
 - "kttimedtest"
 - "ktutilmgr"
 - "ktutilserv"
 - "ktutiltest"
versions:
 - "2017.04.10--hd344e51_3"
 - "20170410--hf64b9f5_2"
 - "20170410--hd344e51_1"
 - "20170410--h896b458_0"
 - "20170410--h27c383b_4"
 - "20170410--hf64b9f5_3"
description: "shpc-registry automated BioContainers addition for kyototycoon"
config: {"url": "https://biocontainers.pro/tools/kyototycoon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kyototycoon", "latest": {"20170410--h27c383b_4": "sha256:63003a4d2a53e2b54e48a89130b2d1a74834ba647596877ab4e7873f5aa686c4"}, "tags": {"2017.04.10--hd344e51_3": "sha256:6651b8770a005a6cce1af51ae6dbeea7a73b8ba9dadd92249fa796d7dc6fbc0e", "20170410--hf64b9f5_2": "sha256:8f514fe6f5129d839b2d060cc58433dfac80f3f7d01cc9da7c450f9c577648ac", "20170410--hd344e51_1": "sha256:f814042945631d1bca3a97f1b46831c4c6a647a799c04ffe0d77ce7f88ce8d7c", "20170410--h896b458_0": "sha256:acda5ac9fdcfec966e0147031fe8ea4f02ada6dbdbd3b169273ed18377af6bdb", "20170410--h27c383b_4": "sha256:63003a4d2a53e2b54e48a89130b2d1a74834ba647596877ab4e7873f5aa686c4", "20170410--hf64b9f5_3": "sha256:344352d5edaa4ffba425ed21025b37449d41829380e619549b5d3cc30e6ea594"}, "docker": "quay.io/biocontainers/kyototycoon", "aliases": {"kccachetest": "/usr/local/bin/kccachetest", "kcdirmgr": "/usr/local/bin/kcdirmgr", "kcdirtest": "/usr/local/bin/kcdirtest", "kcforestmgr": "/usr/local/bin/kcforestmgr", "kcforesttest": "/usr/local/bin/kcforesttest", "kcgrasstest": "/usr/local/bin/kcgrasstest", "kchashmgr": "/usr/local/bin/kchashmgr", "kchashtest": "/usr/local/bin/kchashtest", "kclangctest": "/usr/local/bin/kclangctest", "kcpolymgr": "/usr/local/bin/kcpolymgr", "kcpolytest": "/usr/local/bin/kcpolytest", "kcprototest": "/usr/local/bin/kcprototest", "kcstashtest": "/usr/local/bin/kcstashtest", "kctreemgr": "/usr/local/bin/kctreemgr", "kctreetest": "/usr/local/bin/kctreetest", "kcutilmgr": "/usr/local/bin/kcutilmgr", "kcutiltest": "/usr/local/bin/kcutiltest", "ktremotemgr": "/usr/local/bin/ktremotemgr", "ktremotetest": "/usr/local/bin/ktremotetest", "ktserver": "/usr/local/bin/ktserver", "kttimedmgr": "/usr/local/bin/kttimedmgr", "kttimedtest": "/usr/local/bin/kttimedtest", "ktutilmgr": "/usr/local/bin/ktutilmgr", "ktutilserv": "/usr/local/bin/ktutilserv", "ktutiltest": "/usr/local/bin/ktutiltest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kyototycoon.
shpc-registry automated BioContainers addition for kyototycoon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kyototycoon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kyototycoon:20170410--h27c383b_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kyototycoon/20170410--h27c383b_4
$ module help quay.io/biocontainers/kyototycoon/20170410--h27c383b_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kyototycoon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kyototycoon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kyototycoon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kyototycoon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kyototycoon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kyototycoon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kccachetest

```bash
$ singularity exec <container> /usr/local/bin/kccachetest
$ podman run --it --rm --entrypoint /usr/local/bin/kccachetest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kccachetest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcdirmgr

```bash
$ singularity exec <container> /usr/local/bin/kcdirmgr
$ podman run --it --rm --entrypoint /usr/local/bin/kcdirmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcdirmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcdirtest

```bash
$ singularity exec <container> /usr/local/bin/kcdirtest
$ podman run --it --rm --entrypoint /usr/local/bin/kcdirtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcdirtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcforestmgr

```bash
$ singularity exec <container> /usr/local/bin/kcforestmgr
$ podman run --it --rm --entrypoint /usr/local/bin/kcforestmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcforestmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcforesttest

```bash
$ singularity exec <container> /usr/local/bin/kcforesttest
$ podman run --it --rm --entrypoint /usr/local/bin/kcforesttest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcforesttest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcgrasstest

```bash
$ singularity exec <container> /usr/local/bin/kcgrasstest
$ podman run --it --rm --entrypoint /usr/local/bin/kcgrasstest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcgrasstest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kchashmgr

```bash
$ singularity exec <container> /usr/local/bin/kchashmgr
$ podman run --it --rm --entrypoint /usr/local/bin/kchashmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kchashmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kchashtest

```bash
$ singularity exec <container> /usr/local/bin/kchashtest
$ podman run --it --rm --entrypoint /usr/local/bin/kchashtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kchashtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kclangctest

```bash
$ singularity exec <container> /usr/local/bin/kclangctest
$ podman run --it --rm --entrypoint /usr/local/bin/kclangctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kclangctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcpolymgr

```bash
$ singularity exec <container> /usr/local/bin/kcpolymgr
$ podman run --it --rm --entrypoint /usr/local/bin/kcpolymgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcpolymgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcpolytest

```bash
$ singularity exec <container> /usr/local/bin/kcpolytest
$ podman run --it --rm --entrypoint /usr/local/bin/kcpolytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcpolytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcprototest

```bash
$ singularity exec <container> /usr/local/bin/kcprototest
$ podman run --it --rm --entrypoint /usr/local/bin/kcprototest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcprototest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcstashtest

```bash
$ singularity exec <container> /usr/local/bin/kcstashtest
$ podman run --it --rm --entrypoint /usr/local/bin/kcstashtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcstashtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kctreemgr

```bash
$ singularity exec <container> /usr/local/bin/kctreemgr
$ podman run --it --rm --entrypoint /usr/local/bin/kctreemgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kctreemgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kctreetest

```bash
$ singularity exec <container> /usr/local/bin/kctreetest
$ podman run --it --rm --entrypoint /usr/local/bin/kctreetest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kctreetest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcutilmgr

```bash
$ singularity exec <container> /usr/local/bin/kcutilmgr
$ podman run --it --rm --entrypoint /usr/local/bin/kcutilmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcutilmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kcutiltest

```bash
$ singularity exec <container> /usr/local/bin/kcutiltest
$ podman run --it --rm --entrypoint /usr/local/bin/kcutiltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kcutiltest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktremotemgr

```bash
$ singularity exec <container> /usr/local/bin/ktremotemgr
$ podman run --it --rm --entrypoint /usr/local/bin/ktremotemgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktremotemgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktremotetest

```bash
$ singularity exec <container> /usr/local/bin/ktremotetest
$ podman run --it --rm --entrypoint /usr/local/bin/ktremotetest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktremotetest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktserver

```bash
$ singularity exec <container> /usr/local/bin/ktserver
$ podman run --it --rm --entrypoint /usr/local/bin/ktserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kttimedmgr

```bash
$ singularity exec <container> /usr/local/bin/kttimedmgr
$ podman run --it --rm --entrypoint /usr/local/bin/kttimedmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kttimedmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kttimedtest

```bash
$ singularity exec <container> /usr/local/bin/kttimedtest
$ podman run --it --rm --entrypoint /usr/local/bin/kttimedtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kttimedtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktutilmgr

```bash
$ singularity exec <container> /usr/local/bin/ktutilmgr
$ podman run --it --rm --entrypoint /usr/local/bin/ktutilmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktutilmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktutilserv

```bash
$ singularity exec <container> /usr/local/bin/ktutilserv
$ podman run --it --rm --entrypoint /usr/local/bin/ktutilserv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktutilserv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktutiltest

```bash
$ singularity exec <container> /usr/local/bin/ktutiltest
$ podman run --it --rm --entrypoint /usr/local/bin/ktutiltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktutiltest   -v ${PWD} -w ${PWD} <container> -c " $@"
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