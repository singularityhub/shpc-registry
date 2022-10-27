---
layout: container
name:  "quay.io/biocontainers/a5-miseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/a5-miseq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/a5-miseq/container.yaml"
updated_at: "2022-10-27 01:06:45.951762"
latest: "20160825--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/a5-miseq"
aliases:
 - "a5_pipeline.pl"
 - "aserver"
 - "autopoint"
 - "fc-cache"
 - "fc-cat"
 - "fc-conflist"
 - "fc-list"
 - "fc-match"
 - "fc-pattern"
 - "fc-query"
 - "fc-scan"
 - "fc-validate"
 - "gapplication"
 - "genbrk"
 - "gencfu"
 - "gencnval"
 - "gendict"
 - "genrb"
 - "h2ph"
 - "h2xs"
 - "hb-ot-shape-closure"
 - "hb-shape"
 - "hb-subset"
 - "hb-view"
 - "pack200"
 - "pal2rgb"
 - "pl2pm"
 - "rmic"
 - "rmid"
 - "rmiregistry"
versions:
 - "20160825--hdfd78af_2"
description: "A5-miseq is a pipeline for assembling dna sequence data generated on the illumina sequencing platform. this readme will take you through the steps necessary for running _a5-miseq_"
config: {"url": "https://biocontainers.pro/tools/a5-miseq", "maintainer": "@vsoch", "description": "A5-miseq is a pipeline for assembling dna sequence data generated on the illumina sequencing platform. this readme will take you through the steps necessary for running _a5-miseq_", "latest": {"20160825--hdfd78af_2": "sha256:48cb29db1d86d7b8018f1c83298a67717d50bb9a6ea0f1f72c2c67d077d2e2e5"}, "tags": {"20160825--hdfd78af_2": "sha256:48cb29db1d86d7b8018f1c83298a67717d50bb9a6ea0f1f72c2c67d077d2e2e5"}, "docker": "quay.io/biocontainers/a5-miseq", "aliases": {"a5_pipeline.pl": "/usr/local/bin/a5_pipeline.pl", "aserver": "/usr/local/bin/aserver", "autopoint": "/usr/local/bin/autopoint", "fc-cache": "/usr/local/bin/fc-cache", "fc-cat": "/usr/local/bin/fc-cat", "fc-conflist": "/usr/local/bin/fc-conflist", "fc-list": "/usr/local/bin/fc-list", "fc-match": "/usr/local/bin/fc-match", "fc-pattern": "/usr/local/bin/fc-pattern", "fc-query": "/usr/local/bin/fc-query", "fc-scan": "/usr/local/bin/fc-scan", "fc-validate": "/usr/local/bin/fc-validate", "gapplication": "/usr/local/bin/gapplication", "genbrk": "/usr/local/bin/genbrk", "gencfu": "/usr/local/bin/gencfu", "gencnval": "/usr/local/bin/gencnval", "gendict": "/usr/local/bin/gendict", "genrb": "/usr/local/bin/genrb", "h2ph": "/usr/local/bin/h2ph", "h2xs": "/usr/local/bin/h2xs", "hb-ot-shape-closure": "/usr/local/bin/hb-ot-shape-closure", "hb-shape": "/usr/local/bin/hb-shape", "hb-subset": "/usr/local/bin/hb-subset", "hb-view": "/usr/local/bin/hb-view", "pack200": "/usr/local/bin/pack200", "pal2rgb": "/usr/local/bin/pal2rgb", "pl2pm": "/usr/local/bin/pl2pm", "rmic": "/usr/local/bin/rmic", "rmid": "/usr/local/bin/rmid", "rmiregistry": "/usr/local/bin/rmiregistry"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/a5-miseq.
A5-miseq is a pipeline for assembling dna sequence data generated on the illumina sequencing platform. this readme will take you through the steps necessary for running _a5-miseq_
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/a5-miseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/a5-miseq:20160825--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/a5-miseq/20160825--hdfd78af_2
$ module help quay.io/biocontainers/a5-miseq/20160825--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### a5-miseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### a5-miseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### a5-miseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### a5-miseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### a5-miseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### a5-miseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### a5_pipeline.pl

```bash
$ singularity exec <container> /usr/local/bin/a5_pipeline.pl
$ podman run --it --rm --entrypoint /usr/local/bin/a5_pipeline.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a5_pipeline.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autopoint

```bash
$ singularity exec <container> /usr/local/bin/autopoint
$ podman run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-cache

```bash
$ singularity exec <container> /usr/local/bin/fc-cache
$ podman run --it --rm --entrypoint /usr/local/bin/fc-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-cat

```bash
$ singularity exec <container> /usr/local/bin/fc-cat
$ podman run --it --rm --entrypoint /usr/local/bin/fc-cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-conflist

```bash
$ singularity exec <container> /usr/local/bin/fc-conflist
$ podman run --it --rm --entrypoint /usr/local/bin/fc-conflist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-conflist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-list

```bash
$ singularity exec <container> /usr/local/bin/fc-list
$ podman run --it --rm --entrypoint /usr/local/bin/fc-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-match

```bash
$ singularity exec <container> /usr/local/bin/fc-match
$ podman run --it --rm --entrypoint /usr/local/bin/fc-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-pattern

```bash
$ singularity exec <container> /usr/local/bin/fc-pattern
$ podman run --it --rm --entrypoint /usr/local/bin/fc-pattern   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-pattern   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-query

```bash
$ singularity exec <container> /usr/local/bin/fc-query
$ podman run --it --rm --entrypoint /usr/local/bin/fc-query   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-query   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-scan

```bash
$ singularity exec <container> /usr/local/bin/fc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/fc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-validate

```bash
$ singularity exec <container> /usr/local/bin/fc-validate
$ podman run --it --rm --entrypoint /usr/local/bin/fc-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gapplication

```bash
$ singularity exec <container> /usr/local/bin/gapplication
$ podman run --it --rm --entrypoint /usr/local/bin/gapplication   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapplication   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbrk

```bash
$ singularity exec <container> /usr/local/bin/genbrk
$ podman run --it --rm --entrypoint /usr/local/bin/genbrk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbrk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gencfu

```bash
$ singularity exec <container> /usr/local/bin/gencfu
$ podman run --it --rm --entrypoint /usr/local/bin/gencfu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencfu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gencnval

```bash
$ singularity exec <container> /usr/local/bin/gencnval
$ podman run --it --rm --entrypoint /usr/local/bin/gencnval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencnval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gendict

```bash
$ singularity exec <container> /usr/local/bin/gendict
$ podman run --it --rm --entrypoint /usr/local/bin/gendict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gendict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genrb

```bash
$ singularity exec <container> /usr/local/bin/genrb
$ podman run --it --rm --entrypoint /usr/local/bin/genrb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genrb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2ph

```bash
$ singularity exec <container> /usr/local/bin/h2ph
$ podman run --it --rm --entrypoint /usr/local/bin/h2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2xs

```bash
$ singularity exec <container> /usr/local/bin/h2xs
$ podman run --it --rm --entrypoint /usr/local/bin/h2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-ot-shape-closure

```bash
$ singularity exec <container> /usr/local/bin/hb-ot-shape-closure
$ podman run --it --rm --entrypoint /usr/local/bin/hb-ot-shape-closure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-ot-shape-closure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-shape

```bash
$ singularity exec <container> /usr/local/bin/hb-shape
$ podman run --it --rm --entrypoint /usr/local/bin/hb-shape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-shape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-subset

```bash
$ singularity exec <container> /usr/local/bin/hb-subset
$ podman run --it --rm --entrypoint /usr/local/bin/hb-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-view

```bash
$ singularity exec <container> /usr/local/bin/hb-view
$ podman run --it --rm --entrypoint /usr/local/bin/hb-view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-view   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pack200

```bash
$ singularity exec <container> /usr/local/bin/pack200
$ podman run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pal2rgb

```bash
$ singularity exec <container> /usr/local/bin/pal2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/pal2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pal2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pl2pm

```bash
$ singularity exec <container> /usr/local/bin/pl2pm
$ podman run --it --rm --entrypoint /usr/local/bin/pl2pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pl2pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmic

```bash
$ singularity exec <container> /usr/local/bin/rmic
$ podman run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmid

```bash
$ singularity exec <container> /usr/local/bin/rmid
$ podman run --it --rm --entrypoint /usr/local/bin/rmid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmiregistry

```bash
$ singularity exec <container> /usr/local/bin/rmiregistry
$ podman run --it --rm --entrypoint /usr/local/bin/rmiregistry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmiregistry   -v ${PWD} -w ${PWD} <container> -c " $@"
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