---
layout: container
name:  "quay.io/biocontainers/rdock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rdock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rdock/container.yaml"
updated_at: "2023-09-22 04:15:12.855491"
latest: "2013.1--pl5.22.0_1"
container_url: "https://biocontainers.pro/tools/rdock"
aliases:
 - "babel"
 - "ht_protocol_finder.pl"
 - "make_grid.csh"
 - "obchiral"
 - "rbcalcgrid"
 - "rbcavity"
 - "rbdock"
 - "rblist"
 - "rbmoegrid"
 - "run_rbdock.pl"
 - "run_rbscreen.pl"
 - "sdfield"
 - "sdfilter"
 - "sdmodify"
 - "sdreport"
 - "sdrmsd"
 - "sdsort"
 - "sdsplit"
 - "sdtether"
 - "obabel"
 - "obconformer"
 - "obdistgen"
 - "obenergy"
 - "obfit"
 - "obgen"
 - "obgrep"
 - "obminimize"
 - "obprobe"
 - "obprop"
versions:
 - "2013.1--pl5.22.0_1"
description: "shpc-registry automated BioContainers addition for rdock"
config: {"url": "https://biocontainers.pro/tools/rdock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rdock", "latest": {"2013.1--pl5.22.0_1": "sha256:601dd7a7deb3bd2886b1f0a0b52e0de66267dce163d8128c5252b39d41a7f3c5"}, "tags": {"2013.1--pl5.22.0_1": "sha256:601dd7a7deb3bd2886b1f0a0b52e0de66267dce163d8128c5252b39d41a7f3c5"}, "docker": "quay.io/biocontainers/rdock", "aliases": {"babel": "/usr/local/bin/babel", "ht_protocol_finder.pl": "/usr/local/bin/ht_protocol_finder.pl", "make_grid.csh": "/usr/local/bin/make_grid.csh", "obchiral": "/usr/local/bin/obchiral", "rbcalcgrid": "/usr/local/bin/rbcalcgrid", "rbcavity": "/usr/local/bin/rbcavity", "rbdock": "/usr/local/bin/rbdock", "rblist": "/usr/local/bin/rblist", "rbmoegrid": "/usr/local/bin/rbmoegrid", "run_rbdock.pl": "/usr/local/bin/run_rbdock.pl", "run_rbscreen.pl": "/usr/local/bin/run_rbscreen.pl", "sdfield": "/usr/local/bin/sdfield", "sdfilter": "/usr/local/bin/sdfilter", "sdmodify": "/usr/local/bin/sdmodify", "sdreport": "/usr/local/bin/sdreport", "sdrmsd": "/usr/local/bin/sdrmsd", "sdsort": "/usr/local/bin/sdsort", "sdsplit": "/usr/local/bin/sdsplit", "sdtether": "/usr/local/bin/sdtether", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize", "obprobe": "/usr/local/bin/obprobe", "obprop": "/usr/local/bin/obprop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rdock.
shpc-registry automated BioContainers addition for rdock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rdock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rdock:2013.1--pl5.22.0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rdock/2013.1--pl5.22.0_1
$ module help quay.io/biocontainers/rdock/2013.1--pl5.22.0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rdock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rdock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rdock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rdock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rdock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rdock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### babel

```bash
$ singularity exec <container> /usr/local/bin/babel
$ podman run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ht_protocol_finder.pl

```bash
$ singularity exec <container> /usr/local/bin/ht_protocol_finder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ht_protocol_finder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ht_protocol_finder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_grid.csh

```bash
$ singularity exec <container> /usr/local/bin/make_grid.csh
$ podman run --it --rm --entrypoint /usr/local/bin/make_grid.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_grid.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obchiral

```bash
$ singularity exec <container> /usr/local/bin/obchiral
$ podman run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbcalcgrid

```bash
$ singularity exec <container> /usr/local/bin/rbcalcgrid
$ podman run --it --rm --entrypoint /usr/local/bin/rbcalcgrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbcalcgrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbcavity

```bash
$ singularity exec <container> /usr/local/bin/rbcavity
$ podman run --it --rm --entrypoint /usr/local/bin/rbcavity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbcavity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbdock

```bash
$ singularity exec <container> /usr/local/bin/rbdock
$ podman run --it --rm --entrypoint /usr/local/bin/rbdock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbdock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rblist

```bash
$ singularity exec <container> /usr/local/bin/rblist
$ podman run --it --rm --entrypoint /usr/local/bin/rblist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rblist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbmoegrid

```bash
$ singularity exec <container> /usr/local/bin/rbmoegrid
$ podman run --it --rm --entrypoint /usr/local/bin/rbmoegrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbmoegrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_rbdock.pl

```bash
$ singularity exec <container> /usr/local/bin/run_rbdock.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_rbdock.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_rbdock.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_rbscreen.pl

```bash
$ singularity exec <container> /usr/local/bin/run_rbscreen.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_rbscreen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_rbscreen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdfield

```bash
$ singularity exec <container> /usr/local/bin/sdfield
$ podman run --it --rm --entrypoint /usr/local/bin/sdfield   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdfield   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdfilter

```bash
$ singularity exec <container> /usr/local/bin/sdfilter
$ podman run --it --rm --entrypoint /usr/local/bin/sdfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdmodify

```bash
$ singularity exec <container> /usr/local/bin/sdmodify
$ podman run --it --rm --entrypoint /usr/local/bin/sdmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdreport

```bash
$ singularity exec <container> /usr/local/bin/sdreport
$ podman run --it --rm --entrypoint /usr/local/bin/sdreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdrmsd

```bash
$ singularity exec <container> /usr/local/bin/sdrmsd
$ podman run --it --rm --entrypoint /usr/local/bin/sdrmsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdrmsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdsort

```bash
$ singularity exec <container> /usr/local/bin/sdsort
$ podman run --it --rm --entrypoint /usr/local/bin/sdsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdsplit

```bash
$ singularity exec <container> /usr/local/bin/sdsplit
$ podman run --it --rm --entrypoint /usr/local/bin/sdsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdtether

```bash
$ singularity exec <container> /usr/local/bin/sdtether
$ podman run --it --rm --entrypoint /usr/local/bin/sdtether   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdtether   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obabel

```bash
$ singularity exec <container> /usr/local/bin/obabel
$ podman run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obconformer

```bash
$ singularity exec <container> /usr/local/bin/obconformer
$ podman run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obdistgen

```bash
$ singularity exec <container> /usr/local/bin/obdistgen
$ podman run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obenergy

```bash
$ singularity exec <container> /usr/local/bin/obenergy
$ podman run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfit

```bash
$ singularity exec <container> /usr/local/bin/obfit
$ podman run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgen

```bash
$ singularity exec <container> /usr/local/bin/obgen
$ podman run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgrep

```bash
$ singularity exec <container> /usr/local/bin/obgrep
$ podman run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obminimize

```bash
$ singularity exec <container> /usr/local/bin/obminimize
$ podman run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprobe

```bash
$ singularity exec <container> /usr/local/bin/obprobe
$ podman run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprop

```bash
$ singularity exec <container> /usr/local/bin/obprop
$ podman run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
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