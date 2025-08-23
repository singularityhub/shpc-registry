---
layout: container
name:  "quay.io/biocontainers/orthologer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orthologer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orthologer/container.yaml"
updated_at: "2025-08-23 03:22:59.556085"
latest: "3.7.1--py311hf097cbd_0"
container_url: "https://biocontainers.pro/tools/orthologer"
aliases:
 - "bash"
 - "bashbug"
 - "brhclus"
 - "build_import_file"
 - "cmpclus"
 - "evolrate"
 - "extractpairs"
 - "findbrh"
 - "getclus"
 - "getinpar"
 - "indexdb"
 - "mergeinpar"
 - "orthologer"
 - "orthomapper"
 - "splitgenes"
 - "statclus"
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
 - "just-top-hits"
 - "systematic-mutations"
 - "rsync-ssl"
 - "aria2c"
 - "rsync"
 - "gawk-5.3.0"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "archive-ncbinlp"
 - "archive-nihocc"
 - "archive-nmcds"
 - "archive-pmc"
 - "archive-taxonomy"
 - "args2slice"
 - "asn2ref"
 - "blst2gm"
 - "cit2pmid"
 - "combine-uid-lists"
 - "difference-uid-lists"
 - "download-pmc"
 - "ds2pme"
versions:
 - "3.3.2--hdbdd923_0"
 - "3.4.1--hdbdd923_0"
 - "3.5.0--hdbdd923_0"
 - "3.4.2--hdbdd923_0"
 - "3.5.0--h503566f_1"
 - "3.7.1--py311hf097cbd_0"
description: "singularity registry hpc automated addition for orthologer"
config: {"url": "https://biocontainers.pro/tools/orthologer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for orthologer", "latest": {"3.7.1--py311hf097cbd_0": "sha256:0070c14991c25c2d51003bcc0a0a45a79ee93b50f8978dc06ed289e9fdb0217d"}, "tags": {"3.3.2--hdbdd923_0": "sha256:6c844bf2348c886a4f3d67edb36b1ac293afcad320a0b15f56d2a6b394f2973e", "3.4.1--hdbdd923_0": "sha256:9cec8a5d1ffec5b143c65a6fe42c03ac73ed37eb173fb07fcd794522ec9413ae", "3.5.0--hdbdd923_0": "sha256:ea4bbd663fb06aa2f36f974ebf4c6735ae147deb176f411feb09f2df08c0f825", "3.4.2--hdbdd923_0": "sha256:eea2c7bbd1f46c71a6de8be7c5b18b303cecaef526c260f2b5e4bc3c16c29d7b", "3.5.0--h503566f_1": "sha256:b32d4805820234b80859addb5da7940dc39f8fe15c0d0ad21aa7b64a51566bf5", "3.7.1--py311hf097cbd_0": "sha256:0070c14991c25c2d51003bcc0a0a45a79ee93b50f8978dc06ed289e9fdb0217d"}, "docker": "quay.io/biocontainers/orthologer", "aliases": {"bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "brhclus": "/usr/local/bin/brhclus", "build_import_file": "/usr/local/bin/build_import_file", "cmpclus": "/usr/local/bin/cmpclus", "evolrate": "/usr/local/bin/evolrate", "extractpairs": "/usr/local/bin/extractpairs", "findbrh": "/usr/local/bin/findbrh", "getclus": "/usr/local/bin/getclus", "getinpar": "/usr/local/bin/getinpar", "indexdb": "/usr/local/bin/indexdb", "mergeinpar": "/usr/local/bin/mergeinpar", "orthologer": "/usr/local/bin/orthologer", "orthomapper": "/usr/local/bin/orthomapper", "splitgenes": "/usr/local/bin/splitgenes", "statclus": "/usr/local/bin/statclus", "bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info", "just-top-hits": "/usr/local/bin/just-top-hits", "systematic-mutations": "/usr/local/bin/systematic-mutations", "rsync-ssl": "/usr/local/bin/rsync-ssl", "aria2c": "/usr/local/bin/aria2c", "rsync": "/usr/local/bin/rsync", "gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "archive-ncbinlp": "/usr/local/bin/archive-ncbinlp", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy", "args2slice": "/usr/local/bin/args2slice", "asn2ref": "/usr/local/bin/asn2ref", "blst2gm": "/usr/local/bin/blst2gm", "cit2pmid": "/usr/local/bin/cit2pmid", "combine-uid-lists": "/usr/local/bin/combine-uid-lists", "difference-uid-lists": "/usr/local/bin/difference-uid-lists", "download-pmc": "/usr/local/bin/download-pmc", "ds2pme": "/usr/local/bin/ds2pme"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orthologer.
singularity registry hpc automated addition for orthologer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orthologer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orthologer:3.7.1--py311hf097cbd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orthologer/3.7.1--py311hf097cbd_0
$ module help quay.io/biocontainers/orthologer/3.7.1--py311hf097cbd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orthologer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orthologer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orthologer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orthologer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orthologer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orthologer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brhclus

```bash
$ singularity exec <container> /usr/local/bin/brhclus
$ podman run --it --rm --entrypoint /usr/local/bin/brhclus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brhclus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_import_file

```bash
$ singularity exec <container> /usr/local/bin/build_import_file
$ podman run --it --rm --entrypoint /usr/local/bin/build_import_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_import_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpclus

```bash
$ singularity exec <container> /usr/local/bin/cmpclus
$ podman run --it --rm --entrypoint /usr/local/bin/cmpclus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpclus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evolrate

```bash
$ singularity exec <container> /usr/local/bin/evolrate
$ podman run --it --rm --entrypoint /usr/local/bin/evolrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evolrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractpairs

```bash
$ singularity exec <container> /usr/local/bin/extractpairs
$ podman run --it --rm --entrypoint /usr/local/bin/extractpairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractpairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findbrh

```bash
$ singularity exec <container> /usr/local/bin/findbrh
$ podman run --it --rm --entrypoint /usr/local/bin/findbrh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findbrh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getclus

```bash
$ singularity exec <container> /usr/local/bin/getclus
$ podman run --it --rm --entrypoint /usr/local/bin/getclus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getclus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getinpar

```bash
$ singularity exec <container> /usr/local/bin/getinpar
$ podman run --it --rm --entrypoint /usr/local/bin/getinpar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getinpar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb

```bash
$ singularity exec <container> /usr/local/bin/indexdb
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeinpar

```bash
$ singularity exec <container> /usr/local/bin/mergeinpar
$ podman run --it --rm --entrypoint /usr/local/bin/mergeinpar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeinpar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthologer

```bash
$ singularity exec <container> /usr/local/bin/orthologer
$ podman run --it --rm --entrypoint /usr/local/bin/orthologer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthologer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthomapper

```bash
$ singularity exec <container> /usr/local/bin/orthomapper
$ podman run --it --rm --entrypoint /usr/local/bin/orthomapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthomapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitgenes

```bash
$ singularity exec <container> /usr/local/bin/splitgenes
$ podman run --it --rm --entrypoint /usr/local/bin/splitgenes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitgenes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statclus

```bash
$ singularity exec <container> /usr/local/bin/statclus
$ podman run --it --rm --entrypoint /usr/local/bin/statclus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statclus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsmp2info

```bash
$ singularity exec <container> /usr/local/bin/bsmp2info
$ podman run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fsa2xml

```bash
$ singularity exec <container> /usr/local/bin/fsa2xml
$ podman run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2info

```bash
$ singularity exec <container> /usr/local/bin/gbf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### just-top-hits

```bash
$ singularity exec <container> /usr/local/bin/just-top-hits
$ podman run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### systematic-mutations

```bash
$ singularity exec <container> /usr/local/bin/systematic-mutations
$ podman run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync

```bash
$ singularity exec <container> /usr/local/bin/rsync
$ podman run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh128sum

```bash
$ singularity exec <container> /usr/local/bin/xxh128sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh32sum

```bash
$ singularity exec <container> /usr/local/bin/xxh32sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh64sum

```bash
$ singularity exec <container> /usr/local/bin/xxh64sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-ncbinlp

```bash
$ singularity exec <container> /usr/local/bin/archive-ncbinlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-ncbinlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-ncbinlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nihocc

```bash
$ singularity exec <container> /usr/local/bin/archive-nihocc
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nihocc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nihocc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nmcds

```bash
$ singularity exec <container> /usr/local/bin/archive-nmcds
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pmc

```bash
$ singularity exec <container> /usr/local/bin/archive-pmc
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-taxonomy

```bash
$ singularity exec <container> /usr/local/bin/archive-taxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/archive-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### args2slice

```bash
$ singularity exec <container> /usr/local/bin/args2slice
$ podman run --it --rm --entrypoint /usr/local/bin/args2slice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/args2slice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2ref

```bash
$ singularity exec <container> /usr/local/bin/asn2ref
$ podman run --it --rm --entrypoint /usr/local/bin/asn2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2gm

```bash
$ singularity exec <container> /usr/local/bin/blst2gm
$ podman run --it --rm --entrypoint /usr/local/bin/blst2gm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2gm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cit2pmid

```bash
$ singularity exec <container> /usr/local/bin/cit2pmid
$ podman run --it --rm --entrypoint /usr/local/bin/cit2pmid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cit2pmid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine-uid-lists

```bash
$ singularity exec <container> /usr/local/bin/combine-uid-lists
$ podman run --it --rm --entrypoint /usr/local/bin/combine-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### difference-uid-lists

```bash
$ singularity exec <container> /usr/local/bin/difference-uid-lists
$ podman run --it --rm --entrypoint /usr/local/bin/difference-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/difference-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-pmc

```bash
$ singularity exec <container> /usr/local/bin/download-pmc
$ podman run --it --rm --entrypoint /usr/local/bin/download-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ds2pme

```bash
$ singularity exec <container> /usr/local/bin/ds2pme
$ podman run --it --rm --entrypoint /usr/local/bin/ds2pme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ds2pme   -v ${PWD} -w ${PWD} <container> -c " $@"
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