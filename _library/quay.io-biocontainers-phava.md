---
layout: container
name:  "quay.io/biocontainers/phava"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phava/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phava/container.yaml"
updated_at: "2026-02-03 05:02:03.652110"
latest: "0.2.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/phava"
aliases:
 - "gawk-5.3.0"
 - "gawkbug"
 - "phava"
 - "aria2c"
 - "annot-tsv"
 - "xmlget"
 - "xmltext"
 - "aaindexextract"
 - "abiview"
 - "acdgalaxy"
 - "acdlog"
 - "acdpretty"
 - "acdtable"
 - "acdtrace"
 - "acdvalid"
 - "aligncopy"
 - "aligncopypair"
 - "antigenic"
 - "assemblyget"
 - "backtranambig"
 - "backtranseq"
 - "banana"
 - "biosed"
 - "btwisted"
 - "cachedas"
 - "cachedbfetch"
 - "cacheebeyesearch"
 - "cacheensembl"
versions:
 - "0.2.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for phava"
config: {"url": "https://biocontainers.pro/tools/phava", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phava", "latest": {"0.2.3--pyhdfd78af_0": "sha256:8d468e3a30146d174a9671633c0803a32b24ff5c341b1d11cabf48a8d0f91af9"}, "tags": {"0.2.3--pyhdfd78af_0": "sha256:8d468e3a30146d174a9671633c0803a32b24ff5c341b1d11cabf48a8d0f91af9"}, "docker": "quay.io/biocontainers/phava", "aliases": {"gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "gawkbug": "/usr/local/bin/gawkbug", "phava": "/usr/local/bin/phava", "aria2c": "/usr/local/bin/aria2c", "annot-tsv": "/usr/local/bin/annot-tsv", "xmlget": "/usr/local/bin/xmlget", "xmltext": "/usr/local/bin/xmltext", "aaindexextract": "/usr/local/bin/aaindexextract", "abiview": "/usr/local/bin/abiview", "acdgalaxy": "/usr/local/bin/acdgalaxy", "acdlog": "/usr/local/bin/acdlog", "acdpretty": "/usr/local/bin/acdpretty", "acdtable": "/usr/local/bin/acdtable", "acdtrace": "/usr/local/bin/acdtrace", "acdvalid": "/usr/local/bin/acdvalid", "aligncopy": "/usr/local/bin/aligncopy", "aligncopypair": "/usr/local/bin/aligncopypair", "antigenic": "/usr/local/bin/antigenic", "assemblyget": "/usr/local/bin/assemblyget", "backtranambig": "/usr/local/bin/backtranambig", "backtranseq": "/usr/local/bin/backtranseq", "banana": "/usr/local/bin/banana", "biosed": "/usr/local/bin/biosed", "btwisted": "/usr/local/bin/btwisted", "cachedas": "/usr/local/bin/cachedas", "cachedbfetch": "/usr/local/bin/cachedbfetch", "cacheebeyesearch": "/usr/local/bin/cacheebeyesearch", "cacheensembl": "/usr/local/bin/cacheensembl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phava.
singularity registry hpc automated addition for phava
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phava
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phava:0.2.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phava/0.2.3--pyhdfd78af_0
$ module help quay.io/biocontainers/phava/0.2.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phava-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phava-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phava-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phava-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phava-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phava-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phava

```bash
$ singularity exec <container> /usr/local/bin/phava
$ podman run --it --rm --entrypoint /usr/local/bin/phava   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phava   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlget

```bash
$ singularity exec <container> /usr/local/bin/xmlget
$ podman run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmltext

```bash
$ singularity exec <container> /usr/local/bin/xmltext
$ podman run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abiview

```bash
$ singularity exec <container> /usr/local/bin/abiview
$ podman run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdgalaxy

```bash
$ singularity exec <container> /usr/local/bin/acdgalaxy
$ podman run --it --rm --entrypoint /usr/local/bin/acdgalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdgalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdlog

```bash
$ singularity exec <container> /usr/local/bin/acdlog
$ podman run --it --rm --entrypoint /usr/local/bin/acdlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdpretty

```bash
$ singularity exec <container> /usr/local/bin/acdpretty
$ podman run --it --rm --entrypoint /usr/local/bin/acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdtable

```bash
$ singularity exec <container> /usr/local/bin/acdtable
$ podman run --it --rm --entrypoint /usr/local/bin/acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdtrace

```bash
$ singularity exec <container> /usr/local/bin/acdtrace
$ podman run --it --rm --entrypoint /usr/local/bin/acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdvalid

```bash
$ singularity exec <container> /usr/local/bin/acdvalid
$ podman run --it --rm --entrypoint /usr/local/bin/acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aligncopy

```bash
$ singularity exec <container> /usr/local/bin/aligncopy
$ podman run --it --rm --entrypoint /usr/local/bin/aligncopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aligncopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aligncopypair

```bash
$ singularity exec <container> /usr/local/bin/aligncopypair
$ podman run --it --rm --entrypoint /usr/local/bin/aligncopypair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aligncopypair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### antigenic

```bash
$ singularity exec <container> /usr/local/bin/antigenic
$ podman run --it --rm --entrypoint /usr/local/bin/antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assemblyget

```bash
$ singularity exec <container> /usr/local/bin/assemblyget
$ podman run --it --rm --entrypoint /usr/local/bin/assemblyget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assemblyget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### backtranambig

```bash
$ singularity exec <container> /usr/local/bin/backtranambig
$ podman run --it --rm --entrypoint /usr/local/bin/backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### backtranseq

```bash
$ singularity exec <container> /usr/local/bin/backtranseq
$ podman run --it --rm --entrypoint /usr/local/bin/backtranseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/backtranseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### banana

```bash
$ singularity exec <container> /usr/local/bin/banana
$ podman run --it --rm --entrypoint /usr/local/bin/banana   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/banana   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biosed

```bash
$ singularity exec <container> /usr/local/bin/biosed
$ podman run --it --rm --entrypoint /usr/local/bin/biosed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biosed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### btwisted

```bash
$ singularity exec <container> /usr/local/bin/btwisted
$ podman run --it --rm --entrypoint /usr/local/bin/btwisted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/btwisted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cachedas

```bash
$ singularity exec <container> /usr/local/bin/cachedas
$ podman run --it --rm --entrypoint /usr/local/bin/cachedas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cachedas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cachedbfetch

```bash
$ singularity exec <container> /usr/local/bin/cachedbfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cachedbfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cachedbfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacheebeyesearch

```bash
$ singularity exec <container> /usr/local/bin/cacheebeyesearch
$ podman run --it --rm --entrypoint /usr/local/bin/cacheebeyesearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacheebeyesearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacheensembl

```bash
$ singularity exec <container> /usr/local/bin/cacheensembl
$ podman run --it --rm --entrypoint /usr/local/bin/cacheensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacheensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
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