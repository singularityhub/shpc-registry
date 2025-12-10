---
layout: container
name:  "quay.io/biocontainers/regain-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/regain-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/regain-cli/container.yaml"
updated_at: "2025-12-10 04:11:30.427813"
latest: "1.7.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/regain-cli"
aliases:
 - "amrfinder_index"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
 - "mutate"
 - "pair-at-a-time"
 - "print-missing-subranges"
 - "regain"
 - "sort-by-length"
 - "stx.prot"
 - "stxtyper"
 - "test_stxtyper.sh"
 - "xcommon.sh"
 - "xfetch"
 - "xfetch.ini"
 - "xfilter"
 - "xinfo"
 - "xlink"
 - "xlink.ini"
 - "xsearch"
 - "amrfinder_update"
 - "dna_mutation"
 - "fasta2parts"
 - "amr_report"
 - "amrfinder"
 - "fasta_extract"
 - "gff_check"
 - "fasta_check"
 - "pandoc-lua"
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
 - "just-top-hits"
 - "systematic-mutations"
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
versions:
 - "1.6.2--pyhdfd78af_0"
 - "1.7.1--pyhdfd78af_0"
 - "1.6.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for regain-cli"
config: {"url": "https://biocontainers.pro/tools/regain-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for regain-cli", "latest": {"1.7.1--pyhdfd78af_0": "sha256:8d82cbcd5eebb44999c09a2e74156b94d50982b9b28b8a04e15c1ba27654e9a9"}, "tags": {"1.6.2--pyhdfd78af_0": "sha256:fa6cfcaab71eea4fb15cc8290e9237b6a7905bc1a148e6aff38730c714ab12b4", "1.7.1--pyhdfd78af_0": "sha256:8d82cbcd5eebb44999c09a2e74156b94d50982b9b28b8a04e15c1ba27654e9a9", "1.6.3--pyhdfd78af_0": "sha256:5f914d4e20aed077d01c422c2a41ee74b9aa44761b529000b097c21a442f840f"}, "docker": "quay.io/biocontainers/regain-cli", "aliases": {"amrfinder_index": "/usr/local/bin/amrfinder_index", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "mutate": "/usr/local/bin/mutate", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "regain": "/usr/local/bin/regain", "sort-by-length": "/usr/local/bin/sort-by-length", "stx.prot": "/usr/local/bin/stx.prot", "stxtyper": "/usr/local/bin/stxtyper", "test_stxtyper.sh": "/usr/local/bin/test_stxtyper.sh", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo", "xlink": "/usr/local/bin/xlink", "xlink.ini": "/usr/local/bin/xlink.ini", "xsearch": "/usr/local/bin/xsearch", "amrfinder_update": "/usr/local/bin/amrfinder_update", "dna_mutation": "/usr/local/bin/dna_mutation", "fasta2parts": "/usr/local/bin/fasta2parts", "amr_report": "/usr/local/bin/amr_report", "amrfinder": "/usr/local/bin/amrfinder", "fasta_extract": "/usr/local/bin/fasta_extract", "gff_check": "/usr/local/bin/gff_check", "fasta_check": "/usr/local/bin/fasta_check", "pandoc-lua": "/usr/local/bin/pandoc-lua", "bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info", "just-top-hits": "/usr/local/bin/just-top-hits", "systematic-mutations": "/usr/local/bin/systematic-mutations", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy", "args2slice": "/usr/local/bin/args2slice", "asn2ref": "/usr/local/bin/asn2ref", "blst2gm": "/usr/local/bin/blst2gm", "cit2pmid": "/usr/local/bin/cit2pmid", "combine-uid-lists": "/usr/local/bin/combine-uid-lists", "difference-uid-lists": "/usr/local/bin/difference-uid-lists", "download-pmc": "/usr/local/bin/download-pmc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/regain-cli.
singularity registry hpc automated addition for regain-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/regain-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/regain-cli:1.7.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/regain-cli/1.7.1--pyhdfd78af_0
$ module help quay.io/biocontainers/regain-cli/1.7.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### regain-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### regain-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### regain-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### regain-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### regain-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### regain-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amrfinder_index

```bash
$ singularity exec <container> /usr/local/bin/amrfinder_index
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutate

```bash
$ singularity exec <container> /usr/local/bin/mutate
$ podman run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/pair-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-missing-subranges

```bash
$ singularity exec <container> /usr/local/bin/print-missing-subranges
$ podman run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### regain

```bash
$ singularity exec <container> /usr/local/bin/regain
$ podman run --it --rm --entrypoint /usr/local/bin/regain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/regain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-by-length

```bash
$ singularity exec <container> /usr/local/bin/sort-by-length
$ podman run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stx.prot

```bash
$ singularity exec <container> /usr/local/bin/stx.prot
$ podman run --it --rm --entrypoint /usr/local/bin/stx.prot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stx.prot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stxtyper

```bash
$ singularity exec <container> /usr/local/bin/stxtyper
$ podman run --it --rm --entrypoint /usr/local/bin/stxtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stxtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_stxtyper.sh

```bash
$ singularity exec <container> /usr/local/bin/test_stxtyper.sh
$ podman run --it --rm --entrypoint /usr/local/bin/test_stxtyper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_stxtyper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/xcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch

```bash
$ singularity exec <container> /usr/local/bin/xfetch
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch.ini

```bash
$ singularity exec <container> /usr/local/bin/xfetch.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfilter

```bash
$ singularity exec <container> /usr/local/bin/xfilter
$ podman run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xinfo

```bash
$ singularity exec <container> /usr/local/bin/xinfo
$ podman run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink

```bash
$ singularity exec <container> /usr/local/bin/xlink
$ podman run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink.ini

```bash
$ singularity exec <container> /usr/local/bin/xlink.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsearch

```bash
$ singularity exec <container> /usr/local/bin/xsearch
$ podman run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder_update

```bash
$ singularity exec <container> /usr/local/bin/amrfinder_update
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dna_mutation

```bash
$ singularity exec <container> /usr/local/bin/dna_mutation
$ podman run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2parts

```bash
$ singularity exec <container> /usr/local/bin/fasta2parts
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amr_report

```bash
$ singularity exec <container> /usr/local/bin/amr_report
$ podman run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder

```bash
$ singularity exec <container> /usr/local/bin/amrfinder
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_extract

```bash
$ singularity exec <container> /usr/local/bin/fasta_extract
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_check

```bash
$ singularity exec <container> /usr/local/bin/gff_check
$ podman run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_check

```bash
$ singularity exec <container> /usr/local/bin/fasta_check
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
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