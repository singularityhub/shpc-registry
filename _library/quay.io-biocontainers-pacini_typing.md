---
layout: container
name:  "quay.io/biocontainers/pacini_typing"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pacini_typing/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pacini_typing/container.yaml"
updated_at: "2025-02-27 03:07:19.483025"
latest: "1.6.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pacini_typing"
aliases:
 - "Pacini-typing"
 - "pacini_typing"
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
 - "just-top-hits"
 - "systematic-mutations"
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
versions:
 - "1.6.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pacini_typing"
config: {"url": "https://biocontainers.pro/tools/pacini_typing", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pacini_typing", "latest": {"1.6.4--pyhdfd78af_0": "sha256:ae817f2537bee4e54e679e7f7831bcd812e60441fa99a5ca41c28a1a268fd916"}, "tags": {"1.6.4--pyhdfd78af_0": "sha256:ae817f2537bee4e54e679e7f7831bcd812e60441fa99a5ca41c28a1a268fd916"}, "docker": "quay.io/biocontainers/pacini_typing", "aliases": {"Pacini-typing": "/usr/local/bin/Pacini-typing", "pacini_typing": "/usr/local/bin/pacini_typing", "kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info", "just-top-hits": "/usr/local/bin/just-top-hits", "systematic-mutations": "/usr/local/bin/systematic-mutations", "archive-ncbinlp": "/usr/local/bin/archive-ncbinlp", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy", "args2slice": "/usr/local/bin/args2slice", "asn2ref": "/usr/local/bin/asn2ref", "blst2gm": "/usr/local/bin/blst2gm", "cit2pmid": "/usr/local/bin/cit2pmid", "combine-uid-lists": "/usr/local/bin/combine-uid-lists", "difference-uid-lists": "/usr/local/bin/difference-uid-lists", "download-pmc": "/usr/local/bin/download-pmc", "ds2pme": "/usr/local/bin/ds2pme", "fetch-local": "/usr/local/bin/fetch-local", "fetch-nmcds": "/usr/local/bin/fetch-nmcds", "fetch-pmc": "/usr/local/bin/fetch-pmc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pacini_typing.
singularity registry hpc automated addition for pacini_typing
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pacini_typing
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pacini_typing:1.6.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pacini_typing/1.6.4--pyhdfd78af_0
$ module help quay.io/biocontainers/pacini_typing/1.6.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pacini_typing-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pacini_typing-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pacini_typing-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pacini_typing-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pacini_typing-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pacini_typing-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Pacini-typing

```bash
$ singularity exec <container> /usr/local/bin/Pacini-typing
$ podman run --it --rm --entrypoint /usr/local/bin/Pacini-typing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Pacini-typing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pacini_typing

```bash
$ singularity exec <container> /usr/local/bin/pacini_typing
$ podman run --it --rm --entrypoint /usr/local/bin/pacini_typing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pacini_typing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
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