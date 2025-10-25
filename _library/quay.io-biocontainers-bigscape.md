---
layout: container
name:  "quay.io/biocontainers/bigscape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bigscape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bigscape/container.yaml"
updated_at: "2025-10-25 03:26:08.626635"
latest: "1.1.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bigscape"
aliases:
 - "bigscape.py"
 - "matplotlib"
 - "FastTreeMP"
 - "FastTree"
 - "fasttree"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
 - "esl-alimanip"
 - "esl-alimap"
 - "esl-alimask"
 - "esl-alimerge"
 - "esl-alipid"
 - "esl-alirev"
 - "esl-alistat"
 - "esl-compalign"
 - "esl-compstruct"
 - "esl-construct"
 - "esl-histplot"
 - "esl-mask"
 - "esl-selectn"
 - "esl-seqrange"
 - "esl-seqstat"
 - "esl-sfetch"
 - "esl-shuffle"
 - "esl-ssdraw"
 - "esl-translate"
versions:
 - "1.1.5--pyhdfd78af_0"
 - "1.1.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bigscape"
config: {"url": "https://biocontainers.pro/tools/bigscape", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bigscape", "latest": {"1.1.6--pyhdfd78af_0": "sha256:a91ce287638c741b67217f2365e8fd3fb0f169e465d016583560c123358150f0"}, "tags": {"1.1.5--pyhdfd78af_0": "sha256:6ba1e973ce2640f664d05e56b8513de72c0fbeaaeb5ef2625b5571836bd5db72", "1.1.6--pyhdfd78af_0": "sha256:a91ce287638c741b67217f2365e8fd3fb0f169e465d016583560c123358150f0"}, "docker": "quay.io/biocontainers/bigscape", "aliases": {"bigscape.py": "/usr/local/bin/bigscape.py", "matplotlib": "/usr/local/bin/matplotlib", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev", "esl-alistat": "/usr/local/bin/esl-alistat", "esl-compalign": "/usr/local/bin/esl-compalign", "esl-compstruct": "/usr/local/bin/esl-compstruct", "esl-construct": "/usr/local/bin/esl-construct", "esl-histplot": "/usr/local/bin/esl-histplot", "esl-mask": "/usr/local/bin/esl-mask", "esl-selectn": "/usr/local/bin/esl-selectn", "esl-seqrange": "/usr/local/bin/esl-seqrange", "esl-seqstat": "/usr/local/bin/esl-seqstat", "esl-sfetch": "/usr/local/bin/esl-sfetch", "esl-shuffle": "/usr/local/bin/esl-shuffle", "esl-ssdraw": "/usr/local/bin/esl-ssdraw", "esl-translate": "/usr/local/bin/esl-translate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bigscape.
singularity registry hpc automated addition for bigscape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bigscape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bigscape:1.1.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bigscape/1.1.6--pyhdfd78af_0
$ module help quay.io/biocontainers/bigscape/1.1.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bigscape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bigscape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bigscape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bigscape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bigscape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bigscape-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigscape.py

```bash
$ singularity exec <container> /usr/local/bin/bigscape.py
$ podman run --it --rm --entrypoint /usr/local/bin/bigscape.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigscape.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matplotlib

```bash
$ singularity exec <container> /usr/local/bin/matplotlib
$ podman run --it --rm --entrypoint /usr/local/bin/matplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easel

```bash
$ singularity exec <container> /usr/local/bin/easel
$ podman run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mixdchlet

```bash
$ singularity exec <container> /usr/local/bin/esl-mixdchlet
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimanip

```bash
$ singularity exec <container> /usr/local/bin/esl-alimanip
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimap

```bash
$ singularity exec <container> /usr/local/bin/esl-alimap
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimask

```bash
$ singularity exec <container> /usr/local/bin/esl-alimask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimerge

```bash
$ singularity exec <container> /usr/local/bin/esl-alimerge
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alipid

```bash
$ singularity exec <container> /usr/local/bin/esl-alipid
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alirev

```bash
$ singularity exec <container> /usr/local/bin/esl-alirev
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alistat

```bash
$ singularity exec <container> /usr/local/bin/esl-alistat
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-compalign

```bash
$ singularity exec <container> /usr/local/bin/esl-compalign
$ podman run --it --rm --entrypoint /usr/local/bin/esl-compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-compstruct

```bash
$ singularity exec <container> /usr/local/bin/esl-compstruct
$ podman run --it --rm --entrypoint /usr/local/bin/esl-compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-construct

```bash
$ singularity exec <container> /usr/local/bin/esl-construct
$ podman run --it --rm --entrypoint /usr/local/bin/esl-construct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-construct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-histplot

```bash
$ singularity exec <container> /usr/local/bin/esl-histplot
$ podman run --it --rm --entrypoint /usr/local/bin/esl-histplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-histplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mask

```bash
$ singularity exec <container> /usr/local/bin/esl-mask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-selectn

```bash
$ singularity exec <container> /usr/local/bin/esl-selectn
$ podman run --it --rm --entrypoint /usr/local/bin/esl-selectn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-selectn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-seqrange

```bash
$ singularity exec <container> /usr/local/bin/esl-seqrange
$ podman run --it --rm --entrypoint /usr/local/bin/esl-seqrange   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-seqrange   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-seqstat

```bash
$ singularity exec <container> /usr/local/bin/esl-seqstat
$ podman run --it --rm --entrypoint /usr/local/bin/esl-seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-sfetch

```bash
$ singularity exec <container> /usr/local/bin/esl-sfetch
$ podman run --it --rm --entrypoint /usr/local/bin/esl-sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-shuffle

```bash
$ singularity exec <container> /usr/local/bin/esl-shuffle
$ podman run --it --rm --entrypoint /usr/local/bin/esl-shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-ssdraw

```bash
$ singularity exec <container> /usr/local/bin/esl-ssdraw
$ podman run --it --rm --entrypoint /usr/local/bin/esl-ssdraw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-ssdraw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-translate

```bash
$ singularity exec <container> /usr/local/bin/esl-translate
$ podman run --it --rm --entrypoint /usr/local/bin/esl-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
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