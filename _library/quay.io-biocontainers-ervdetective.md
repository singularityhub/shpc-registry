---
layout: container
name:  "quay.io/biocontainers/ervdetective"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ervdetective/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ervdetective/container.yaml"
updated_at: "2024-11-15 02:36:05.643078"
latest: "1.0.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ervdetective"
aliases:
 - "ervdetective"
 - "genometools-config"
 - "gt"
 - "just-first-key"
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
 - "gm2ranges"
versions:
 - "1.0.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for ervdetective"
config: {"url": "https://biocontainers.pro/tools/ervdetective", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ervdetective", "latest": {"1.0.8--pyhdfd78af_0": "sha256:575e0e4ae18235dbe60c735f3e478030a50107be8f181a699ca3465d08ae44bc"}, "tags": {"1.0.8--pyhdfd78af_0": "sha256:575e0e4ae18235dbe60c735f3e478030a50107be8f181a699ca3465d08ae44bc"}, "docker": "quay.io/biocontainers/ervdetective", "aliases": {"ervdetective": "/usr/local/bin/ervdetective", "genometools-config": "/usr/local/bin/genometools-config", "gt": "/usr/local/bin/gt", "just-first-key": "/usr/local/bin/just-first-key", "archive-ncbinlp": "/usr/local/bin/archive-ncbinlp", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy", "args2slice": "/usr/local/bin/args2slice", "asn2ref": "/usr/local/bin/asn2ref", "blst2gm": "/usr/local/bin/blst2gm", "cit2pmid": "/usr/local/bin/cit2pmid", "combine-uid-lists": "/usr/local/bin/combine-uid-lists", "difference-uid-lists": "/usr/local/bin/difference-uid-lists", "download-pmc": "/usr/local/bin/download-pmc", "ds2pme": "/usr/local/bin/ds2pme", "fetch-local": "/usr/local/bin/fetch-local", "fetch-nmcds": "/usr/local/bin/fetch-nmcds", "fetch-pmc": "/usr/local/bin/fetch-pmc", "fetch-taxonomy": "/usr/local/bin/fetch-taxonomy", "filter-genbank": "/usr/local/bin/filter-genbank", "filter-record": "/usr/local/bin/filter-record", "gbf2fsa": "/usr/local/bin/gbf2fsa", "gbf2ref": "/usr/local/bin/gbf2ref", "gm2ranges": "/usr/local/bin/gm2ranges"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ervdetective.
singularity registry hpc automated addition for ervdetective
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ervdetective
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ervdetective:1.0.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ervdetective/1.0.8--pyhdfd78af_0
$ module help quay.io/biocontainers/ervdetective/1.0.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ervdetective-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ervdetective-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ervdetective-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ervdetective-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ervdetective-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ervdetective-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ervdetective

```bash
$ singularity exec <container> /usr/local/bin/ervdetective
$ podman run --it --rm --entrypoint /usr/local/bin/ervdetective   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ervdetective   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genometools-config

```bash
$ singularity exec <container> /usr/local/bin/genometools-config
$ podman run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gt

```bash
$ singularity exec <container> /usr/local/bin/gt
$ podman run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### just-first-key

```bash
$ singularity exec <container> /usr/local/bin/just-first-key
$ podman run --it --rm --entrypoint /usr/local/bin/just-first-key   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/just-first-key   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gm2ranges

```bash
$ singularity exec <container> /usr/local/bin/gm2ranges
$ podman run --it --rm --entrypoint /usr/local/bin/gm2ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gm2ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
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