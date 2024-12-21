---
layout: container
name:  "quay.io/biocontainers/tadrep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tadrep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tadrep/container.yaml"
updated_at: "2024-12-21 03:06:03.575664"
latest: "0.9.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tadrep"
aliases:
 - "archspec"
 - "pgv-download-dataset"
 - "pgv-gui"
 - "pgv-mmseqs"
 - "pgv-mummer"
 - "pgv-pmauve"
 - "pgv-simpleplot"
 - "tadrep"
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
 - "gm2segs"
 - "ini2xml"
 - "jsonl2xml"
versions:
 - "0.9.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for tadrep"
config: {"url": "https://biocontainers.pro/tools/tadrep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tadrep", "latest": {"0.9.2--pyhdfd78af_0": "sha256:16f32a647c2ef06bf0f702ae6d2392711406094812891b4e0efa8d315e7c3936"}, "tags": {"0.9.2--pyhdfd78af_0": "sha256:16f32a647c2ef06bf0f702ae6d2392711406094812891b4e0efa8d315e7c3936"}, "docker": "quay.io/biocontainers/tadrep", "aliases": {"archspec": "/usr/local/bin/archspec", "pgv-download-dataset": "/usr/local/bin/pgv-download-dataset", "pgv-gui": "/usr/local/bin/pgv-gui", "pgv-mmseqs": "/usr/local/bin/pgv-mmseqs", "pgv-mummer": "/usr/local/bin/pgv-mummer", "pgv-pmauve": "/usr/local/bin/pgv-pmauve", "pgv-simpleplot": "/usr/local/bin/pgv-simpleplot", "tadrep": "/usr/local/bin/tadrep", "archive-ncbinlp": "/usr/local/bin/archive-ncbinlp", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy", "args2slice": "/usr/local/bin/args2slice", "asn2ref": "/usr/local/bin/asn2ref", "blst2gm": "/usr/local/bin/blst2gm", "cit2pmid": "/usr/local/bin/cit2pmid", "combine-uid-lists": "/usr/local/bin/combine-uid-lists", "difference-uid-lists": "/usr/local/bin/difference-uid-lists", "download-pmc": "/usr/local/bin/download-pmc", "ds2pme": "/usr/local/bin/ds2pme", "fetch-local": "/usr/local/bin/fetch-local", "fetch-nmcds": "/usr/local/bin/fetch-nmcds", "fetch-pmc": "/usr/local/bin/fetch-pmc", "fetch-taxonomy": "/usr/local/bin/fetch-taxonomy", "filter-genbank": "/usr/local/bin/filter-genbank", "filter-record": "/usr/local/bin/filter-record", "gbf2fsa": "/usr/local/bin/gbf2fsa", "gbf2ref": "/usr/local/bin/gbf2ref", "gm2ranges": "/usr/local/bin/gm2ranges", "gm2segs": "/usr/local/bin/gm2segs", "ini2xml": "/usr/local/bin/ini2xml", "jsonl2xml": "/usr/local/bin/jsonl2xml"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tadrep.
singularity registry hpc automated addition for tadrep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tadrep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tadrep:0.9.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tadrep/0.9.2--pyhdfd78af_0
$ module help quay.io/biocontainers/tadrep/0.9.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tadrep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tadrep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tadrep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tadrep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tadrep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tadrep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-download-dataset

```bash
$ singularity exec <container> /usr/local/bin/pgv-download-dataset
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-download-dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-download-dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-gui

```bash
$ singularity exec <container> /usr/local/bin/pgv-gui
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-mmseqs

```bash
$ singularity exec <container> /usr/local/bin/pgv-mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-mummer

```bash
$ singularity exec <container> /usr/local/bin/pgv-mummer
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-pmauve

```bash
$ singularity exec <container> /usr/local/bin/pgv-pmauve
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-pmauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-pmauve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgv-simpleplot

```bash
$ singularity exec <container> /usr/local/bin/pgv-simpleplot
$ podman run --it --rm --entrypoint /usr/local/bin/pgv-simpleplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgv-simpleplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tadrep

```bash
$ singularity exec <container> /usr/local/bin/tadrep
$ podman run --it --rm --entrypoint /usr/local/bin/tadrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tadrep   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gm2segs

```bash
$ singularity exec <container> /usr/local/bin/gm2segs
$ podman run --it --rm --entrypoint /usr/local/bin/gm2segs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gm2segs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ini2xml

```bash
$ singularity exec <container> /usr/local/bin/ini2xml
$ podman run --it --rm --entrypoint /usr/local/bin/ini2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ini2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonl2xml

```bash
$ singularity exec <container> /usr/local/bin/jsonl2xml
$ podman run --it --rm --entrypoint /usr/local/bin/jsonl2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonl2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
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