---
layout: container
name:  "quay.io/biocontainers/defense-finder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/defense-finder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/defense-finder/container.yaml"
updated_at: "2024-11-13 04:37:30.478413"
latest: "1.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/defense-finder"
aliases:
 - "defense-finder"
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
 - "1.0.9--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_0"
 - "1.2.1--pyhdfd78af_0"
 - "1.2.2--pyhdfd78af_0"
 - "1.2.2--pyhdfd78af_1"
 - "1.3.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for defense-finder"
config: {"url": "https://biocontainers.pro/tools/defense-finder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for defense-finder", "latest": {"1.3.0--pyhdfd78af_0": "sha256:9850280ff5c3a23db4b3064d3d73873a015dd9e4878b286d59077412e58d36a7"}, "tags": {"1.0.9--pyhdfd78af_0": "sha256:17364186d96289f09be4e3295ffd78c39f84a1d8db70bad3efac94ad65b2e43e", "1.1.1--pyhdfd78af_0": "sha256:341237c1e0f908839c5f0be29bb2748f08750e66008e12f571a007d616e16900", "1.2.0--pyhdfd78af_0": "sha256:5ba30d2d8099fbbdef8147945b57a27e3e95e8ade8582b0170606d38553fb2a1", "1.2.1--pyhdfd78af_0": "sha256:11e49b8272572e9b8604737fffe5137fcaee8b830acd112ac740cb118f77ba71", "1.2.2--pyhdfd78af_0": "sha256:36a2d65684b337b7dca59ea172cebb00adf564000b4fbd578b2f9f4d39894679", "1.2.2--pyhdfd78af_1": "sha256:a35b11d2030adffa76ed90b527bdbc652519b340b649644fa35958fd1cc4be2b", "1.3.0--pyhdfd78af_0": "sha256:9850280ff5c3a23db4b3064d3d73873a015dd9e4878b286d59077412e58d36a7"}, "docker": "quay.io/biocontainers/defense-finder", "aliases": {"defense-finder": "/usr/local/bin/defense-finder", "macsyconfig": "/usr/local/bin/macsyconfig", "macsydata": "/usr/local/bin/macsydata", "macsyfinder": "/usr/local/bin/macsyfinder", "macsymerge": "/usr/local/bin/macsymerge", "macsyprofile": "/usr/local/bin/macsyprofile", "macsysplit": "/usr/local/bin/macsysplit", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev", "esl-alistat": "/usr/local/bin/esl-alistat", "esl-compalign": "/usr/local/bin/esl-compalign", "esl-compstruct": "/usr/local/bin/esl-compstruct", "esl-construct": "/usr/local/bin/esl-construct", "esl-histplot": "/usr/local/bin/esl-histplot", "esl-mask": "/usr/local/bin/esl-mask", "esl-selectn": "/usr/local/bin/esl-selectn", "esl-seqrange": "/usr/local/bin/esl-seqrange", "esl-seqstat": "/usr/local/bin/esl-seqstat", "esl-sfetch": "/usr/local/bin/esl-sfetch", "esl-shuffle": "/usr/local/bin/esl-shuffle", "esl-ssdraw": "/usr/local/bin/esl-ssdraw", "esl-translate": "/usr/local/bin/esl-translate", "esl-weight": "/usr/local/bin/esl-weight", "esl-afetch": "/usr/local/bin/esl-afetch", "esl-reformat": "/usr/local/bin/esl-reformat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/defense-finder.
singularity registry hpc automated addition for defense-finder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/defense-finder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/defense-finder:1.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/defense-finder/1.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/defense-finder/1.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### defense-finder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### defense-finder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### defense-finder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### defense-finder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### defense-finder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### defense-finder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### defense-finder

```bash
$ singularity exec <container> /usr/local/bin/defense-finder
$ podman run --it --rm --entrypoint /usr/local/bin/defense-finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/defense-finder   -v ${PWD} -w ${PWD} <container> -c " $@"
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