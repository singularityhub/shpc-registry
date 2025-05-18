---
layout: container
name:  "quay.io/biocontainers/pangwes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pangwes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pangwes/container.yaml"
updated_at: "2025-05-18 03:22:17.031285"
latest: "0.3.0_alpha--h9948957_1"
container_url: "https://biocontainers.pro/tools/pangwes"
aliases:
 - "SpydrPick"
 - "cuttlefish"
 - "gfa1_parser"
 - "gwes_plot.r"
 - "unitig_distance"
 - "hb-info"
 - "tjbench"
versions:
 - "0.2.0_alpha--h4ac6f70_0"
 - "0.3.0_alpha--h4ac6f70_0"
 - "0.3.0_alpha--h9948957_1"
description: "singularity registry hpc automated addition for pangwes"
config: {"url": "https://biocontainers.pro/tools/pangwes", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pangwes", "latest": {"0.3.0_alpha--h9948957_1": "sha256:587a399c2dc63a4cb287850953adb7ee0db3f28f7bb85c3e84216e4d227de864"}, "tags": {"0.2.0_alpha--h4ac6f70_0": "sha256:b2d7d39eeee3e12ba9e52606c40cb76e884a44f0dc8a89051a8e00fbe3c85908", "0.3.0_alpha--h4ac6f70_0": "sha256:e98ba7713bbc4c42ab14d5b5f8af7b103d74b5808375b24173f4b91de07786f3", "0.3.0_alpha--h9948957_1": "sha256:587a399c2dc63a4cb287850953adb7ee0db3f28f7bb85c3e84216e4d227de864"}, "docker": "quay.io/biocontainers/pangwes", "aliases": {"SpydrPick": "/usr/local/bin/SpydrPick", "cuttlefish": "/usr/local/bin/cuttlefish", "gfa1_parser": "/usr/local/bin/gfa1_parser", "gwes_plot.r": "/usr/local/bin/gwes_plot.r", "unitig_distance": "/usr/local/bin/unitig_distance", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pangwes.
singularity registry hpc automated addition for pangwes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pangwes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pangwes:0.3.0_alpha--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pangwes/0.3.0_alpha--h9948957_1
$ module help quay.io/biocontainers/pangwes/0.3.0_alpha--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pangwes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pangwes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pangwes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pangwes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pangwes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pangwes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SpydrPick

```bash
$ singularity exec <container> /usr/local/bin/SpydrPick
$ podman run --it --rm --entrypoint /usr/local/bin/SpydrPick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpydrPick   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuttlefish

```bash
$ singularity exec <container> /usr/local/bin/cuttlefish
$ podman run --it --rm --entrypoint /usr/local/bin/cuttlefish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuttlefish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa1_parser

```bash
$ singularity exec <container> /usr/local/bin/gfa1_parser
$ podman run --it --rm --entrypoint /usr/local/bin/gfa1_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa1_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gwes_plot.r

```bash
$ singularity exec <container> /usr/local/bin/gwes_plot.r
$ podman run --it --rm --entrypoint /usr/local/bin/gwes_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gwes_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unitig_distance

```bash
$ singularity exec <container> /usr/local/bin/unitig_distance
$ podman run --it --rm --entrypoint /usr/local/bin/unitig_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unitig_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
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