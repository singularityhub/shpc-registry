---
layout: container
name:  "quay.io/biocontainers/mummer2circos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mummer2circos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mummer2circos/container.yaml"
updated_at: "2025-11-22 03:38:12.626855"
latest: "1.4.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mummer2circos"
aliases:
 - "mummer2circos"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "gddiag"
 - "list.modules"
 - "test.modules"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "gdlib-config"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
 - "mummerplot"
 - "nucmer"
 - "promer"
 - "repeat-match"
 - "show-aligns"
 - "show-coords"
 - "show-diff"
 - "show-snps"
versions:
 - "1.4.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mummer2circos"
config: {"url": "https://biocontainers.pro/tools/mummer2circos", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mummer2circos", "latest": {"1.4.2--pyhdfd78af_0": "sha256:6664bf249fc4f2e377917dfc6b9a81178cd123fc3c10aa73b6a14a2dbbb2fe20"}, "tags": {"1.4.2--pyhdfd78af_0": "sha256:6664bf249fc4f2e377917dfc6b9a81178cd123fc3c10aa73b6a14a2dbbb2fe20"}, "docker": "quay.io/biocontainers/mummer2circos", "aliases": {"mummer2circos": "/usr/local/bin/mummer2circos", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "gddiag": "/usr/local/bin/gddiag", "list.modules": "/usr/local/bin/list.modules", "test.modules": "/usr/local/bin/test.modules", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "gdlib-config": "/usr/local/bin/gdlib-config", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot", "nucmer": "/usr/local/bin/nucmer", "promer": "/usr/local/bin/promer", "repeat-match": "/usr/local/bin/repeat-match", "show-aligns": "/usr/local/bin/show-aligns", "show-coords": "/usr/local/bin/show-coords", "show-diff": "/usr/local/bin/show-diff", "show-snps": "/usr/local/bin/show-snps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mummer2circos.
singularity registry hpc automated addition for mummer2circos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mummer2circos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mummer2circos:1.4.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mummer2circos/1.4.2--pyhdfd78af_0
$ module help quay.io/biocontainers/mummer2circos/1.4.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mummer2circos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mummer2circos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mummer2circos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mummer2circos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mummer2circos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mummer2circos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mummer2circos

```bash
$ singularity exec <container> /usr/local/bin/mummer2circos
$ podman run --it --rm --entrypoint /usr/local/bin/mummer2circos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer2circos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos

```bash
$ singularity exec <container> /usr/local/bin/circos
$ podman run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos.exe

```bash
$ singularity exec <container> /usr/local/bin/circos.exe
$ podman run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.bat

```bash
$ singularity exec <container> /usr/local/bin/compile.bat
$ podman run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.make

```bash
$ singularity exec <container> /usr/local/bin/compile.make
$ podman run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gddiag

```bash
$ singularity exec <container> /usr/local/bin/gddiag
$ podman run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list.modules

```bash
$ singularity exec <container> /usr/local/bin/list.modules
$ podman run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.modules

```bash
$ singularity exec <container> /usr/local/bin/test.modules
$ podman run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /usr/local/bin/mummerplot
$ podman run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucmer

```bash
$ singularity exec <container> /usr/local/bin/nucmer
$ podman run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promer

```bash
$ singularity exec <container> /usr/local/bin/promer
$ podman run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repeat-match

```bash
$ singularity exec <container> /usr/local/bin/repeat-match
$ podman run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-aligns

```bash
$ singularity exec <container> /usr/local/bin/show-aligns
$ podman run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-coords

```bash
$ singularity exec <container> /usr/local/bin/show-coords
$ podman run --it --rm --entrypoint /usr/local/bin/show-coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-diff

```bash
$ singularity exec <container> /usr/local/bin/show-diff
$ podman run --it --rm --entrypoint /usr/local/bin/show-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-snps

```bash
$ singularity exec <container> /usr/local/bin/show-snps
$ podman run --it --rm --entrypoint /usr/local/bin/show-snps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-snps   -v ${PWD} -w ${PWD} <container> -c " $@"
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