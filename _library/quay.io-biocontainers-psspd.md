---
layout: container
name:  "quay.io/biocontainers/psspd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psspd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psspd/container.yaml"
updated_at: "2026-10-10 19:50:46.797914"
latest: "1.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/psspd"
aliases:
 - "amplicon3_core"
 - "archive-peptide"
 - "cittest"
 - "combine-uids"
 - "compare-uids"
 - "exclude-uids"
 - "filter-records"
 - "gene2tbl"
 - "gff3_exons"
 - "gpf2info"
 - "gtf_exons"
 - "intersect-uids"
 - "long_seq_tm_test"
 - "ntdpal"
 - "ntthal"
 - "oligotm"
 - "primer3_core"
 - "primer3_masker"
 - "psspd"
 - "rcommon.sh"
 - "split-records"
 - "test-repeat"
 - "uniq-count"
 - "uniq-count-rank"
 - "gmap_cat"
 - "indexdb_cat"
 - "gmap.nosimd"
 - "gmapl.nosimd"
 - "gsnap.nosimd"
 - "gsnapl.nosimd"
 - "trindex"
 - "atoiindex"
 - "cmetindex"
 - "cpuid"
 - "dbsnp_iit"
 - "ensembl_genes"
 - "fa_coords"
 - "get-genome"
 - "gff3_genes"
 - "gff3_introns"
 - "gff3_splicesites"
 - "gmap.sse42"
 - "gmap_build"
 - "gmap_process"
 - "gmapindex"
 - "gmapl"
 - "gmapl.sse42"
 - "gsnap"
 - "gsnap.sse42"
versions:
 - "1.1.1--hdfd78af_0"
description: "singularity registry hpc automated addition for psspd"
config: {"url": "https://biocontainers.pro/tools/psspd", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for psspd", "latest": {"1.1.1--hdfd78af_0": "sha256:75208f083d7fabfd66caa6f5e25dc9e7169cbf65384bc527811fc77b657d0b7b"}, "tags": {"1.1.1--hdfd78af_0": "sha256:75208f083d7fabfd66caa6f5e25dc9e7169cbf65384bc527811fc77b657d0b7b"}, "docker": "quay.io/biocontainers/psspd", "aliases": {"amplicon3_core": "/usr/local/bin/amplicon3_core", "archive-peptide": "/usr/local/bin/archive-peptide", "cittest": "/usr/local/bin/cittest", "combine-uids": "/usr/local/bin/combine-uids", "compare-uids": "/usr/local/bin/compare-uids", "exclude-uids": "/usr/local/bin/exclude-uids", "filter-records": "/usr/local/bin/filter-records", "gene2tbl": "/usr/local/bin/gene2tbl", "gff3_exons": "/usr/local/bin/gff3_exons", "gpf2info": "/usr/local/bin/gpf2info", "gtf_exons": "/usr/local/bin/gtf_exons", "intersect-uids": "/usr/local/bin/intersect-uids", "long_seq_tm_test": "/usr/local/bin/long_seq_tm_test", "ntdpal": "/usr/local/bin/ntdpal", "ntthal": "/usr/local/bin/ntthal", "oligotm": "/usr/local/bin/oligotm", "primer3_core": "/usr/local/bin/primer3_core", "primer3_masker": "/usr/local/bin/primer3_masker", "psspd": "/usr/local/bin/psspd", "rcommon.sh": "/usr/local/bin/rcommon.sh", "split-records": "/usr/local/bin/split-records", "test-repeat": "/usr/local/bin/test-repeat", "uniq-count": "/usr/local/bin/uniq-count", "uniq-count-rank": "/usr/local/bin/uniq-count-rank", "gmap_cat": "/usr/local/bin/gmap_cat", "indexdb_cat": "/usr/local/bin/indexdb_cat", "gmap.nosimd": "/usr/local/bin/gmap.nosimd", "gmapl.nosimd": "/usr/local/bin/gmapl.nosimd", "gsnap.nosimd": "/usr/local/bin/gsnap.nosimd", "gsnapl.nosimd": "/usr/local/bin/gsnapl.nosimd", "trindex": "/usr/local/bin/trindex", "atoiindex": "/usr/local/bin/atoiindex", "cmetindex": "/usr/local/bin/cmetindex", "cpuid": "/usr/local/bin/cpuid", "dbsnp_iit": "/usr/local/bin/dbsnp_iit", "ensembl_genes": "/usr/local/bin/ensembl_genes", "fa_coords": "/usr/local/bin/fa_coords", "get-genome": "/usr/local/bin/get-genome", "gff3_genes": "/usr/local/bin/gff3_genes", "gff3_introns": "/usr/local/bin/gff3_introns", "gff3_splicesites": "/usr/local/bin/gff3_splicesites", "gmap.sse42": "/usr/local/bin/gmap.sse42", "gmap_build": "/usr/local/bin/gmap_build", "gmap_process": "/usr/local/bin/gmap_process", "gmapindex": "/usr/local/bin/gmapindex", "gmapl": "/usr/local/bin/gmapl", "gmapl.sse42": "/usr/local/bin/gmapl.sse42", "gsnap": "/usr/local/bin/gsnap", "gsnap.sse42": "/usr/local/bin/gsnap.sse42"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psspd.
singularity registry hpc automated addition for psspd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psspd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psspd:1.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psspd/1.1.1--hdfd78af_0
$ module help quay.io/biocontainers/psspd/1.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psspd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psspd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psspd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psspd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psspd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psspd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amplicon3_core

```bash
$ singularity exec <container> /usr/local/bin/amplicon3_core
$ podman run --it --rm --entrypoint /usr/local/bin/amplicon3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicon3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-peptide

```bash
$ singularity exec <container> /usr/local/bin/archive-peptide
$ podman run --it --rm --entrypoint /usr/local/bin/archive-peptide   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-peptide   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cittest

```bash
$ singularity exec <container> /usr/local/bin/cittest
$ podman run --it --rm --entrypoint /usr/local/bin/cittest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cittest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine-uids

```bash
$ singularity exec <container> /usr/local/bin/combine-uids
$ podman run --it --rm --entrypoint /usr/local/bin/combine-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-uids

```bash
$ singularity exec <container> /usr/local/bin/compare-uids
$ podman run --it --rm --entrypoint /usr/local/bin/compare-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exclude-uids

```bash
$ singularity exec <container> /usr/local/bin/exclude-uids
$ podman run --it --rm --entrypoint /usr/local/bin/exclude-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exclude-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-records

```bash
$ singularity exec <container> /usr/local/bin/filter-records
$ podman run --it --rm --entrypoint /usr/local/bin/filter-records   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-records   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2tbl

```bash
$ singularity exec <container> /usr/local/bin/gene2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gene2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_exons

```bash
$ singularity exec <container> /usr/local/bin/gff3_exons
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_exons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_exons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpf2info

```bash
$ singularity exec <container> /usr/local/bin/gpf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gpf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_exons

```bash
$ singularity exec <container> /usr/local/bin/gtf_exons
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_exons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_exons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersect-uids

```bash
$ singularity exec <container> /usr/local/bin/intersect-uids
$ podman run --it --rm --entrypoint /usr/local/bin/intersect-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersect-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### long_seq_tm_test

```bash
$ singularity exec <container> /usr/local/bin/long_seq_tm_test
$ podman run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntdpal

```bash
$ singularity exec <container> /usr/local/bin/ntdpal
$ podman run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntthal

```bash
$ singularity exec <container> /usr/local/bin/ntthal
$ podman run --it --rm --entrypoint /usr/local/bin/ntthal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntthal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oligotm

```bash
$ singularity exec <container> /usr/local/bin/oligotm
$ podman run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primer3_core

```bash
$ singularity exec <container> /usr/local/bin/primer3_core
$ podman run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primer3_masker

```bash
$ singularity exec <container> /usr/local/bin/primer3_masker
$ podman run --it --rm --entrypoint /usr/local/bin/primer3_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primer3_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psspd

```bash
$ singularity exec <container> /usr/local/bin/psspd
$ podman run --it --rm --entrypoint /usr/local/bin/psspd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psspd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/rcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-records

```bash
$ singularity exec <container> /usr/local/bin/split-records
$ podman run --it --rm --entrypoint /usr/local/bin/split-records   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-records   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-repeat

```bash
$ singularity exec <container> /usr/local/bin/test-repeat
$ podman run --it --rm --entrypoint /usr/local/bin/test-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-repeat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-count

```bash
$ singularity exec <container> /usr/local/bin/uniq-count
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-count-rank

```bash
$ singularity exec <container> /usr/local/bin/uniq-count-rank
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-count-rank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-count-rank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_cat

```bash
$ singularity exec <container> /usr/local/bin/gmap_cat
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_cat

```bash
$ singularity exec <container> /usr/local/bin/indexdb_cat
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trindex

```bash
$ singularity exec <container> /usr/local/bin/trindex
$ podman run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### atoiindex

```bash
$ singularity exec <container> /usr/local/bin/atoiindex
$ podman run --it --rm --entrypoint /usr/local/bin/atoiindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atoiindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmetindex

```bash
$ singularity exec <container> /usr/local/bin/cmetindex
$ podman run --it --rm --entrypoint /usr/local/bin/cmetindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmetindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuid

```bash
$ singularity exec <container> /usr/local/bin/cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbsnp_iit

```bash
$ singularity exec <container> /usr/local/bin/dbsnp_iit
$ podman run --it --rm --entrypoint /usr/local/bin/dbsnp_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbsnp_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ensembl_genes

```bash
$ singularity exec <container> /usr/local/bin/ensembl_genes
$ podman run --it --rm --entrypoint /usr/local/bin/ensembl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ensembl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fa_coords

```bash
$ singularity exec <container> /usr/local/bin/fa_coords
$ podman run --it --rm --entrypoint /usr/local/bin/fa_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fa_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-genome

```bash
$ singularity exec <container> /usr/local/bin/get-genome
$ podman run --it --rm --entrypoint /usr/local/bin/get-genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_genes

```bash
$ singularity exec <container> /usr/local/bin/gff3_genes
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_introns

```bash
$ singularity exec <container> /usr/local/bin/gff3_introns
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_splicesites

```bash
$ singularity exec <container> /usr/local/bin/gff3_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap.sse42

```bash
$ singularity exec <container> /usr/local/bin/gmap.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_build

```bash
$ singularity exec <container> /usr/local/bin/gmap_build
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_process

```bash
$ singularity exec <container> /usr/local/bin/gmap_process
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_process   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_process   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapindex

```bash
$ singularity exec <container> /usr/local/bin/gmapindex
$ podman run --it --rm --entrypoint /usr/local/bin/gmapindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl

```bash
$ singularity exec <container> /usr/local/bin/gmapl
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl.sse42

```bash
$ singularity exec <container> /usr/local/bin/gmapl.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap

```bash
$ singularity exec <container> /usr/local/bin/gsnap
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap.sse42

```bash
$ singularity exec <container> /usr/local/bin/gsnap.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
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