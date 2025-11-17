---
layout: container
name:  "quay.io/biocontainers/scrubby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scrubby/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scrubby/container.yaml"
updated_at: "2025-11-17 04:54:45.540255"
latest: "0.2.1--h715e4b3_0"
container_url: "https://biocontainers.pro/tools/scrubby"
aliases:
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
 - "just-top-hits"
 - "scrubby"
 - "strobealign"
 - "systematic-mutations"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "rsync-ssl"
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
 - "fetch-local"
 - "fetch-nmcds"
 - "fetch-pmc"
 - "fetch-taxonomy"
 - "filter-genbank"
 - "filter-record"
 - "gbf2fsa"
 - "gbf2ref"
versions:
 - "0.2.1--h715e4b3_0"
description: "singularity registry hpc automated addition for scrubby"
config: {"url": "https://biocontainers.pro/tools/scrubby", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for scrubby", "latest": {"0.2.1--h715e4b3_0": "sha256:cf76bdd409c58022ef5001b38ee43c4e40dd2f7c6fc016814bdb47ebf1cb2536"}, "tags": {"0.2.1--h715e4b3_0": "sha256:cf76bdd409c58022ef5001b38ee43c4e40dd2f7c6fc016814bdb47ebf1cb2536"}, "docker": "quay.io/biocontainers/scrubby", "aliases": {"bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info", "just-top-hits": "/usr/local/bin/just-top-hits", "scrubby": "/usr/local/bin/scrubby", "strobealign": "/usr/local/bin/strobealign", "systematic-mutations": "/usr/local/bin/systematic-mutations", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "rsync-ssl": "/usr/local/bin/rsync-ssl", "archive-ncbinlp": "/usr/local/bin/archive-ncbinlp", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy", "args2slice": "/usr/local/bin/args2slice", "asn2ref": "/usr/local/bin/asn2ref", "blst2gm": "/usr/local/bin/blst2gm", "cit2pmid": "/usr/local/bin/cit2pmid", "combine-uid-lists": "/usr/local/bin/combine-uid-lists", "difference-uid-lists": "/usr/local/bin/difference-uid-lists", "download-pmc": "/usr/local/bin/download-pmc", "ds2pme": "/usr/local/bin/ds2pme", "fetch-local": "/usr/local/bin/fetch-local", "fetch-nmcds": "/usr/local/bin/fetch-nmcds", "fetch-pmc": "/usr/local/bin/fetch-pmc", "fetch-taxonomy": "/usr/local/bin/fetch-taxonomy", "filter-genbank": "/usr/local/bin/filter-genbank", "filter-record": "/usr/local/bin/filter-record", "gbf2fsa": "/usr/local/bin/gbf2fsa", "gbf2ref": "/usr/local/bin/gbf2ref"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scrubby.
singularity registry hpc automated addition for scrubby
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scrubby
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scrubby:0.2.1--h715e4b3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scrubby/0.2.1--h715e4b3_0
$ module help quay.io/biocontainers/scrubby/0.2.1--h715e4b3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scrubby-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scrubby-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scrubby-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scrubby-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scrubby-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scrubby-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### scrubby

```bash
$ singularity exec <container> /usr/local/bin/scrubby
$ podman run --it --rm --entrypoint /usr/local/bin/scrubby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scrubby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strobealign

```bash
$ singularity exec <container> /usr/local/bin/strobealign
$ podman run --it --rm --entrypoint /usr/local/bin/strobealign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strobealign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### systematic-mutations

```bash
$ singularity exec <container> /usr/local/bin/systematic-mutations
$ podman run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2

```bash
$ singularity exec <container> /usr/local/bin/kraken2
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-build

```bash
$ singularity exec <container> /usr/local/bin/kraken2-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-inspect

```bash
$ singularity exec <container> /usr/local/bin/kraken2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fetch-local

```bash
$ singularity exec <container> /usr/local/bin/fetch-local
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-local   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-local   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-nmcds

```bash
$ singularity exec <container> /usr/local/bin/fetch-nmcds
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-pmc

```bash
$ singularity exec <container> /usr/local/bin/fetch-pmc
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-taxonomy

```bash
$ singularity exec <container> /usr/local/bin/fetch-taxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-genbank

```bash
$ singularity exec <container> /usr/local/bin/filter-genbank
$ podman run --it --rm --entrypoint /usr/local/bin/filter-genbank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-genbank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-record

```bash
$ singularity exec <container> /usr/local/bin/filter-record
$ podman run --it --rm --entrypoint /usr/local/bin/filter-record   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-record   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2fsa

```bash
$ singularity exec <container> /usr/local/bin/gbf2fsa
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2fsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2fsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2ref

```bash
$ singularity exec <container> /usr/local/bin/gbf2ref
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
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