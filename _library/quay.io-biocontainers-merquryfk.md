---
layout: container
name:  "quay.io/biocontainers/merquryfk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/merquryfk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/merquryfk/container.yaml"
updated_at: "2025-10-21 03:29:18.091123"
latest: "1.1.3--h71df26d_0"
container_url: "https://biocontainers.pro/tools/merquryfk"
aliases:
 - "ASMplot"
 - "CNplot"
 - "FastK"
 - "Fastcp"
 - "Fastmerge"
 - "Fastmv"
 - "Fastrm"
 - "HAPmaker"
 - "HAPplot"
 - "Haplex"
 - "Histex"
 - "Homex"
 - "KatComp"
 - "KatGC"
 - "Logex"
 - "MerquryFK"
 - "PloidyPlot"
 - "Profex"
 - "Symmex"
 - "Tabex"
 - "Vennex"
 - "pcre2posix_test"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.0--h4ef89c6_1"
 - "1.1.1--h4ef89c6_0"
 - "1.1.1--h71df26d_1"
 - "1.1.2--h71df26d_0"
 - "1.1.3--h71df26d_0"
description: "singularity registry hpc automated addition for merquryfk"
config: {"url": "https://biocontainers.pro/tools/merquryfk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for merquryfk", "latest": {"1.1.3--h71df26d_0": "sha256:fb3fac1cb5e121f6d9365595e719fdf0ae9dce42953a1ae0ee27b9b2ecb7fe65"}, "tags": {"1.0.0--h4ef89c6_1": "sha256:9c3fa6a6f3755992f93fc303cf4233bce1aef75ecb5e10be7c6dca50d136905d", "1.1.1--h4ef89c6_0": "sha256:0a91dcc5e9ab91637653bdea97f007a0f10c7379826a11d88a11f045a539392e", "1.1.1--h71df26d_1": "sha256:7a831c46cb4f25de04cb750237ab4786abbb556a6b9778b88670451707885b7a", "1.1.2--h71df26d_0": "sha256:5f36a489e62c81d0584236cb0b90c8ad11c318ad14dfb89caa461770aad629ec", "1.1.3--h71df26d_0": "sha256:fb3fac1cb5e121f6d9365595e719fdf0ae9dce42953a1ae0ee27b9b2ecb7fe65"}, "docker": "quay.io/biocontainers/merquryfk", "aliases": {"ASMplot": "/usr/local/bin/ASMplot", "CNplot": "/usr/local/bin/CNplot", "FastK": "/usr/local/bin/FastK", "Fastcp": "/usr/local/bin/Fastcp", "Fastmerge": "/usr/local/bin/Fastmerge", "Fastmv": "/usr/local/bin/Fastmv", "Fastrm": "/usr/local/bin/Fastrm", "HAPmaker": "/usr/local/bin/HAPmaker", "HAPplot": "/usr/local/bin/HAPplot", "Haplex": "/usr/local/bin/Haplex", "Histex": "/usr/local/bin/Histex", "Homex": "/usr/local/bin/Homex", "KatComp": "/usr/local/bin/KatComp", "KatGC": "/usr/local/bin/KatGC", "Logex": "/usr/local/bin/Logex", "MerquryFK": "/usr/local/bin/MerquryFK", "PloidyPlot": "/usr/local/bin/PloidyPlot", "Profex": "/usr/local/bin/Profex", "Symmex": "/usr/local/bin/Symmex", "Tabex": "/usr/local/bin/Tabex", "Vennex": "/usr/local/bin/Vennex", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/merquryfk.
singularity registry hpc automated addition for merquryfk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/merquryfk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/merquryfk:1.1.3--h71df26d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/merquryfk/1.1.3--h71df26d_0
$ module help quay.io/biocontainers/merquryfk/1.1.3--h71df26d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### merquryfk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### merquryfk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### merquryfk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### merquryfk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### merquryfk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### merquryfk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ASMplot

```bash
$ singularity exec <container> /usr/local/bin/ASMplot
$ podman run --it --rm --entrypoint /usr/local/bin/ASMplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ASMplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CNplot

```bash
$ singularity exec <container> /usr/local/bin/CNplot
$ podman run --it --rm --entrypoint /usr/local/bin/CNplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CNplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastK

```bash
$ singularity exec <container> /usr/local/bin/FastK
$ podman run --it --rm --entrypoint /usr/local/bin/FastK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastcp

```bash
$ singularity exec <container> /usr/local/bin/Fastcp
$ podman run --it --rm --entrypoint /usr/local/bin/Fastcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastmerge

```bash
$ singularity exec <container> /usr/local/bin/Fastmerge
$ podman run --it --rm --entrypoint /usr/local/bin/Fastmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastmv

```bash
$ singularity exec <container> /usr/local/bin/Fastmv
$ podman run --it --rm --entrypoint /usr/local/bin/Fastmv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastmv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastrm

```bash
$ singularity exec <container> /usr/local/bin/Fastrm
$ podman run --it --rm --entrypoint /usr/local/bin/Fastrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HAPmaker

```bash
$ singularity exec <container> /usr/local/bin/HAPmaker
$ podman run --it --rm --entrypoint /usr/local/bin/HAPmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HAPmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HAPplot

```bash
$ singularity exec <container> /usr/local/bin/HAPplot
$ podman run --it --rm --entrypoint /usr/local/bin/HAPplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HAPplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Haplex

```bash
$ singularity exec <container> /usr/local/bin/Haplex
$ podman run --it --rm --entrypoint /usr/local/bin/Haplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Haplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Histex

```bash
$ singularity exec <container> /usr/local/bin/Histex
$ podman run --it --rm --entrypoint /usr/local/bin/Histex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Histex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Homex

```bash
$ singularity exec <container> /usr/local/bin/Homex
$ podman run --it --rm --entrypoint /usr/local/bin/Homex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Homex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KatComp

```bash
$ singularity exec <container> /usr/local/bin/KatComp
$ podman run --it --rm --entrypoint /usr/local/bin/KatComp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KatComp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KatGC

```bash
$ singularity exec <container> /usr/local/bin/KatGC
$ podman run --it --rm --entrypoint /usr/local/bin/KatGC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KatGC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Logex

```bash
$ singularity exec <container> /usr/local/bin/Logex
$ podman run --it --rm --entrypoint /usr/local/bin/Logex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Logex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MerquryFK

```bash
$ singularity exec <container> /usr/local/bin/MerquryFK
$ podman run --it --rm --entrypoint /usr/local/bin/MerquryFK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MerquryFK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PloidyPlot

```bash
$ singularity exec <container> /usr/local/bin/PloidyPlot
$ podman run --it --rm --entrypoint /usr/local/bin/PloidyPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PloidyPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Profex

```bash
$ singularity exec <container> /usr/local/bin/Profex
$ podman run --it --rm --entrypoint /usr/local/bin/Profex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Profex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Symmex

```bash
$ singularity exec <container> /usr/local/bin/Symmex
$ podman run --it --rm --entrypoint /usr/local/bin/Symmex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Symmex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Tabex

```bash
$ singularity exec <container> /usr/local/bin/Tabex
$ podman run --it --rm --entrypoint /usr/local/bin/Tabex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Tabex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Vennex

```bash
$ singularity exec <container> /usr/local/bin/Vennex
$ podman run --it --rm --entrypoint /usr/local/bin/Vennex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Vennex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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