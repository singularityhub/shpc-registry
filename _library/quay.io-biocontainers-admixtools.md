---
layout: container
name:  "quay.io/biocontainers/admixtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/admixtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/admixtools/container.yaml"
updated_at: "2024-12-07 01:52:29.711109"
latest: "7.0.2--h6a739c9_4"
container_url: "https://biocontainers.pro/tools/admixtools"
aliases:
 - "convertf"
 - "dof4"
 - "dof4a"
 - "dowtjack"
 - "expfit.sh"
 - "gcount"
 - "getresult"
 - "grabpars"
 - "jackdiff"
 - "kimf"
 - "mergeit"
 - "mkpretty"
 - "numlines"
 - "qp3Pop"
 - "qp4diff"
 - "qpAdm"
 - "qpBound"
 - "qpDpart"
 - "qpDstat"
 - "qpF4ratio"
 - "qpGraph"
 - "qpWave"
 - "qpdslow"
 - "qpff3base"
 - "qpfmv"
 - "qpfstats"
 - "qpmix"
 - "qpreroot"
 - "rexpfit.r"
 - "rolloff"
 - "rolloffp"
 - "simpjack2"
 - "wtjack.pl"
 - "xtractcol"
 - "xtractcolv"
versions:
 - "7.0.2--h2469040_2"
 - "7.0.2--h6a739c9_4"
description: "shpc-registry automated BioContainers addition for admixtools"
config: {"url": "https://biocontainers.pro/tools/admixtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for admixtools", "latest": {"7.0.2--h6a739c9_4": "sha256:d36c4dd46423f3a03a643103b5c996c0179d328b5d013be490ca3060ca7cb47a"}, "tags": {"7.0.2--h2469040_2": "sha256:a5f678de46f4eaf6be870bd46f63a137cf8eec027d9c09e890a29e8b6e9c600b", "7.0.2--h6a739c9_4": "sha256:d36c4dd46423f3a03a643103b5c996c0179d328b5d013be490ca3060ca7cb47a"}, "docker": "quay.io/biocontainers/admixtools", "aliases": {"convertf": "/usr/local/bin/convertf", "dof4": "/usr/local/bin/dof4", "dof4a": "/usr/local/bin/dof4a", "dowtjack": "/usr/local/bin/dowtjack", "expfit.sh": "/usr/local/bin/expfit.sh", "gcount": "/usr/local/bin/gcount", "getresult": "/usr/local/bin/getresult", "grabpars": "/usr/local/bin/grabpars", "jackdiff": "/usr/local/bin/jackdiff", "kimf": "/usr/local/bin/kimf", "mergeit": "/usr/local/bin/mergeit", "mkpretty": "/usr/local/bin/mkpretty", "numlines": "/usr/local/bin/numlines", "qp3Pop": "/usr/local/bin/qp3Pop", "qp4diff": "/usr/local/bin/qp4diff", "qpAdm": "/usr/local/bin/qpAdm", "qpBound": "/usr/local/bin/qpBound", "qpDpart": "/usr/local/bin/qpDpart", "qpDstat": "/usr/local/bin/qpDstat", "qpF4ratio": "/usr/local/bin/qpF4ratio", "qpGraph": "/usr/local/bin/qpGraph", "qpWave": "/usr/local/bin/qpWave", "qpdslow": "/usr/local/bin/qpdslow", "qpff3base": "/usr/local/bin/qpff3base", "qpfmv": "/usr/local/bin/qpfmv", "qpfstats": "/usr/local/bin/qpfstats", "qpmix": "/usr/local/bin/qpmix", "qpreroot": "/usr/local/bin/qpreroot", "rexpfit.r": "/usr/local/bin/rexpfit.r", "rolloff": "/usr/local/bin/rolloff", "rolloffp": "/usr/local/bin/rolloffp", "simpjack2": "/usr/local/bin/simpjack2", "wtjack.pl": "/usr/local/bin/wtjack.pl", "xtractcol": "/usr/local/bin/xtractcol", "xtractcolv": "/usr/local/bin/xtractcolv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/admixtools.
shpc-registry automated BioContainers addition for admixtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/admixtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/admixtools:7.0.2--h6a739c9_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/admixtools/7.0.2--h6a739c9_4
$ module help quay.io/biocontainers/admixtools/7.0.2--h6a739c9_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### admixtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### admixtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### admixtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### admixtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### admixtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### admixtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convertf

```bash
$ singularity exec <container> /usr/local/bin/convertf
$ podman run --it --rm --entrypoint /usr/local/bin/convertf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dof4

```bash
$ singularity exec <container> /usr/local/bin/dof4
$ podman run --it --rm --entrypoint /usr/local/bin/dof4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dof4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dof4a

```bash
$ singularity exec <container> /usr/local/bin/dof4a
$ podman run --it --rm --entrypoint /usr/local/bin/dof4a   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dof4a   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dowtjack

```bash
$ singularity exec <container> /usr/local/bin/dowtjack
$ podman run --it --rm --entrypoint /usr/local/bin/dowtjack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dowtjack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### expfit.sh

```bash
$ singularity exec <container> /usr/local/bin/expfit.sh
$ podman run --it --rm --entrypoint /usr/local/bin/expfit.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/expfit.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcount

```bash
$ singularity exec <container> /usr/local/bin/gcount
$ podman run --it --rm --entrypoint /usr/local/bin/gcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getresult

```bash
$ singularity exec <container> /usr/local/bin/getresult
$ podman run --it --rm --entrypoint /usr/local/bin/getresult   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getresult   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grabpars

```bash
$ singularity exec <container> /usr/local/bin/grabpars
$ podman run --it --rm --entrypoint /usr/local/bin/grabpars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grabpars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jackdiff

```bash
$ singularity exec <container> /usr/local/bin/jackdiff
$ podman run --it --rm --entrypoint /usr/local/bin/jackdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jackdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kimf

```bash
$ singularity exec <container> /usr/local/bin/kimf
$ podman run --it --rm --entrypoint /usr/local/bin/kimf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kimf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeit

```bash
$ singularity exec <container> /usr/local/bin/mergeit
$ podman run --it --rm --entrypoint /usr/local/bin/mergeit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkpretty

```bash
$ singularity exec <container> /usr/local/bin/mkpretty
$ podman run --it --rm --entrypoint /usr/local/bin/mkpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numlines

```bash
$ singularity exec <container> /usr/local/bin/numlines
$ podman run --it --rm --entrypoint /usr/local/bin/numlines   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numlines   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qp3Pop

```bash
$ singularity exec <container> /usr/local/bin/qp3Pop
$ podman run --it --rm --entrypoint /usr/local/bin/qp3Pop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qp3Pop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qp4diff

```bash
$ singularity exec <container> /usr/local/bin/qp4diff
$ podman run --it --rm --entrypoint /usr/local/bin/qp4diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qp4diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpAdm

```bash
$ singularity exec <container> /usr/local/bin/qpAdm
$ podman run --it --rm --entrypoint /usr/local/bin/qpAdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpAdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpBound

```bash
$ singularity exec <container> /usr/local/bin/qpBound
$ podman run --it --rm --entrypoint /usr/local/bin/qpBound   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpBound   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpDpart

```bash
$ singularity exec <container> /usr/local/bin/qpDpart
$ podman run --it --rm --entrypoint /usr/local/bin/qpDpart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpDpart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpDstat

```bash
$ singularity exec <container> /usr/local/bin/qpDstat
$ podman run --it --rm --entrypoint /usr/local/bin/qpDstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpDstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpF4ratio

```bash
$ singularity exec <container> /usr/local/bin/qpF4ratio
$ podman run --it --rm --entrypoint /usr/local/bin/qpF4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpF4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpGraph

```bash
$ singularity exec <container> /usr/local/bin/qpGraph
$ podman run --it --rm --entrypoint /usr/local/bin/qpGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpWave

```bash
$ singularity exec <container> /usr/local/bin/qpWave
$ podman run --it --rm --entrypoint /usr/local/bin/qpWave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpWave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpdslow

```bash
$ singularity exec <container> /usr/local/bin/qpdslow
$ podman run --it --rm --entrypoint /usr/local/bin/qpdslow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpdslow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpff3base

```bash
$ singularity exec <container> /usr/local/bin/qpff3base
$ podman run --it --rm --entrypoint /usr/local/bin/qpff3base   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpff3base   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpfmv

```bash
$ singularity exec <container> /usr/local/bin/qpfmv
$ podman run --it --rm --entrypoint /usr/local/bin/qpfmv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpfmv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpfstats

```bash
$ singularity exec <container> /usr/local/bin/qpfstats
$ podman run --it --rm --entrypoint /usr/local/bin/qpfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpmix

```bash
$ singularity exec <container> /usr/local/bin/qpmix
$ podman run --it --rm --entrypoint /usr/local/bin/qpmix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpmix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpreroot

```bash
$ singularity exec <container> /usr/local/bin/qpreroot
$ podman run --it --rm --entrypoint /usr/local/bin/qpreroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qpreroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rexpfit.r

```bash
$ singularity exec <container> /usr/local/bin/rexpfit.r
$ podman run --it --rm --entrypoint /usr/local/bin/rexpfit.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rexpfit.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rolloff

```bash
$ singularity exec <container> /usr/local/bin/rolloff
$ podman run --it --rm --entrypoint /usr/local/bin/rolloff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rolloff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rolloffp

```bash
$ singularity exec <container> /usr/local/bin/rolloffp
$ podman run --it --rm --entrypoint /usr/local/bin/rolloffp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rolloffp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simpjack2

```bash
$ singularity exec <container> /usr/local/bin/simpjack2
$ podman run --it --rm --entrypoint /usr/local/bin/simpjack2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simpjack2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtjack.pl

```bash
$ singularity exec <container> /usr/local/bin/wtjack.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wtjack.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtjack.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtractcol

```bash
$ singularity exec <container> /usr/local/bin/xtractcol
$ podman run --it --rm --entrypoint /usr/local/bin/xtractcol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtractcol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtractcolv

```bash
$ singularity exec <container> /usr/local/bin/xtractcolv
$ podman run --it --rm --entrypoint /usr/local/bin/xtractcolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtractcolv   -v ${PWD} -w ${PWD} <container> -c " $@"
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