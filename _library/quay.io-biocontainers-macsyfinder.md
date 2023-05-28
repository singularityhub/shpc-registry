---
layout: container
name:  "quay.io/biocontainers/macsyfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/macsyfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/macsyfinder/container.yaml"
updated_at: "2023-05-28 02:50:40.928274"
latest: "2.1.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/macsyfinder"
aliases:
 - "macsyconfig"
 - "macsydata"
 - "macsyfinder"
 - "macsymerge"
 - "macsyprofile"
 - "macsysplit"
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
 - "esl-weight"
 - "esl-afetch"
 - "esl-reformat"
versions:
 - "2.1--pyh7cba7a3_0"
 - "2.1.1--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for macsyfinder"
config: {"url": "https://biocontainers.pro/tools/macsyfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for macsyfinder", "latest": {"2.1.1--pyh7cba7a3_0": "sha256:7b864126df5c6f804ed0086a432f78bacf48dd37271ff5abe7b39347e8fa5aec"}, "tags": {"2.1--pyh7cba7a3_0": "sha256:fd961ced95ba3a908b9bd7d69913b3897a5bf20b34586243a2a6a5a0743e79ab", "2.1.1--pyh7cba7a3_0": "sha256:7b864126df5c6f804ed0086a432f78bacf48dd37271ff5abe7b39347e8fa5aec"}, "docker": "quay.io/biocontainers/macsyfinder", "aliases": {"macsyconfig": "/usr/local/bin/macsyconfig", "macsydata": "/usr/local/bin/macsydata", "macsyfinder": "/usr/local/bin/macsyfinder", "macsymerge": "/usr/local/bin/macsymerge", "macsyprofile": "/usr/local/bin/macsyprofile", "macsysplit": "/usr/local/bin/macsysplit", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev", "esl-alistat": "/usr/local/bin/esl-alistat", "esl-compalign": "/usr/local/bin/esl-compalign", "esl-compstruct": "/usr/local/bin/esl-compstruct", "esl-construct": "/usr/local/bin/esl-construct", "esl-histplot": "/usr/local/bin/esl-histplot", "esl-mask": "/usr/local/bin/esl-mask", "esl-selectn": "/usr/local/bin/esl-selectn", "esl-seqrange": "/usr/local/bin/esl-seqrange", "esl-seqstat": "/usr/local/bin/esl-seqstat", "esl-sfetch": "/usr/local/bin/esl-sfetch", "esl-shuffle": "/usr/local/bin/esl-shuffle", "esl-ssdraw": "/usr/local/bin/esl-ssdraw", "esl-translate": "/usr/local/bin/esl-translate", "esl-weight": "/usr/local/bin/esl-weight", "esl-afetch": "/usr/local/bin/esl-afetch", "esl-reformat": "/usr/local/bin/esl-reformat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/macsyfinder.
singularity registry hpc automated addition for macsyfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/macsyfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/macsyfinder:2.1.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/macsyfinder/2.1.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/macsyfinder/2.1.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### macsyfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### macsyfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### macsyfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### macsyfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### macsyfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### macsyfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### macsyconfig

```bash
$ singularity exec <container> /usr/local/bin/macsyconfig
$ podman run --it --rm --entrypoint /usr/local/bin/macsyconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macsyconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### macsydata

```bash
$ singularity exec <container> /usr/local/bin/macsydata
$ podman run --it --rm --entrypoint /usr/local/bin/macsydata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macsydata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### macsyfinder

```bash
$ singularity exec <container> /usr/local/bin/macsyfinder
$ podman run --it --rm --entrypoint /usr/local/bin/macsyfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macsyfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### macsymerge

```bash
$ singularity exec <container> /usr/local/bin/macsymerge
$ podman run --it --rm --entrypoint /usr/local/bin/macsymerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macsymerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### macsyprofile

```bash
$ singularity exec <container> /usr/local/bin/macsyprofile
$ podman run --it --rm --entrypoint /usr/local/bin/macsyprofile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macsyprofile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### macsysplit

```bash
$ singularity exec <container> /usr/local/bin/macsysplit
$ podman run --it --rm --entrypoint /usr/local/bin/macsysplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macsysplit   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### esl-weight

```bash
$ singularity exec <container> /usr/local/bin/esl-weight
$ podman run --it --rm --entrypoint /usr/local/bin/esl-weight   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-weight   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-afetch

```bash
$ singularity exec <container> /usr/local/bin/esl-afetch
$ podman run --it --rm --entrypoint /usr/local/bin/esl-afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-reformat

```bash
$ singularity exec <container> /usr/local/bin/esl-reformat
$ podman run --it --rm --entrypoint /usr/local/bin/esl-reformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-reformat   -v ${PWD} -w ${PWD} <container> -c " $@"
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