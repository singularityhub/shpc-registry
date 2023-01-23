---
layout: container
name:  "quay.io/biocontainers/gmap-fusion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmap-fusion/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gmap-fusion/container.yaml"
updated_at: "2023-01-23 02:51:02.968589"
latest: "0.4.0--2"
container_url: "https://biocontainers.pro/tools/gmap-fusion"
aliases:
 - "GMAP-fusion"
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
 - "gmap_compress"
 - "gmap_process"
 - "gmap_reassemble"
 - "gmap_uncompress"
 - "gmapindex"
 - "gmapl"
 - "gmapl.sse42"
 - "gsnap"
 - "gsnap.sse42"
 - "gsnapl"
 - "gsnapl.sse42"
 - "gtf_genes"
 - "gtf_introns"
 - "gtf_splicesites"
 - "gtf_transcript_splicesites"
 - "gvf_iit"
 - "iit_dump"
 - "iit_get"
 - "iit_store"
 - "md_coords"
 - "psl_genes"
 - "psl_introns"
 - "psl_splicesites"
 - "sam_sort"
 - "snpindex"
 - "trindex"
 - "vcf_iit"
 - "gmap"
 - "db_archive"
 - "db_checkpoint"
 - "db_deadlock"
 - "db_dump"
 - "db_hotbackup"
 - "db_load"
 - "db_log_verify"
 - "db_printlog"
 - "db_recover"
versions:
 - "0.4.0--2"
description: "shpc-registry automated BioContainers addition for gmap-fusion"
config: {"url": "https://biocontainers.pro/tools/gmap-fusion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gmap-fusion", "latest": {"0.4.0--2": "sha256:40465100fd9563473496cc6d56e303b77cc691079a934db0e1b65b4a3f677e4f"}, "tags": {"0.4.0--2": "sha256:40465100fd9563473496cc6d56e303b77cc691079a934db0e1b65b4a3f677e4f"}, "docker": "quay.io/biocontainers/gmap-fusion", "aliases": {"GMAP-fusion": "/usr/local/bin/GMAP-fusion", "atoiindex": "/usr/local/bin/atoiindex", "cmetindex": "/usr/local/bin/cmetindex", "cpuid": "/usr/local/bin/cpuid", "dbsnp_iit": "/usr/local/bin/dbsnp_iit", "ensembl_genes": "/usr/local/bin/ensembl_genes", "fa_coords": "/usr/local/bin/fa_coords", "get-genome": "/usr/local/bin/get-genome", "gff3_genes": "/usr/local/bin/gff3_genes", "gff3_introns": "/usr/local/bin/gff3_introns", "gff3_splicesites": "/usr/local/bin/gff3_splicesites", "gmap.sse42": "/usr/local/bin/gmap.sse42", "gmap_build": "/usr/local/bin/gmap_build", "gmap_compress": "/usr/local/bin/gmap_compress", "gmap_process": "/usr/local/bin/gmap_process", "gmap_reassemble": "/usr/local/bin/gmap_reassemble", "gmap_uncompress": "/usr/local/bin/gmap_uncompress", "gmapindex": "/usr/local/bin/gmapindex", "gmapl": "/usr/local/bin/gmapl", "gmapl.sse42": "/usr/local/bin/gmapl.sse42", "gsnap": "/usr/local/bin/gsnap", "gsnap.sse42": "/usr/local/bin/gsnap.sse42", "gsnapl": "/usr/local/bin/gsnapl", "gsnapl.sse42": "/usr/local/bin/gsnapl.sse42", "gtf_genes": "/usr/local/bin/gtf_genes", "gtf_introns": "/usr/local/bin/gtf_introns", "gtf_splicesites": "/usr/local/bin/gtf_splicesites", "gtf_transcript_splicesites": "/usr/local/bin/gtf_transcript_splicesites", "gvf_iit": "/usr/local/bin/gvf_iit", "iit_dump": "/usr/local/bin/iit_dump", "iit_get": "/usr/local/bin/iit_get", "iit_store": "/usr/local/bin/iit_store", "md_coords": "/usr/local/bin/md_coords", "psl_genes": "/usr/local/bin/psl_genes", "psl_introns": "/usr/local/bin/psl_introns", "psl_splicesites": "/usr/local/bin/psl_splicesites", "sam_sort": "/usr/local/bin/sam_sort", "snpindex": "/usr/local/bin/snpindex", "trindex": "/usr/local/bin/trindex", "vcf_iit": "/usr/local/bin/vcf_iit", "gmap": "/usr/local/bin/gmap", "db_archive": "/usr/local/bin/db_archive", "db_checkpoint": "/usr/local/bin/db_checkpoint", "db_deadlock": "/usr/local/bin/db_deadlock", "db_dump": "/usr/local/bin/db_dump", "db_hotbackup": "/usr/local/bin/db_hotbackup", "db_load": "/usr/local/bin/db_load", "db_log_verify": "/usr/local/bin/db_log_verify", "db_printlog": "/usr/local/bin/db_printlog", "db_recover": "/usr/local/bin/db_recover"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmap-fusion.
shpc-registry automated BioContainers addition for gmap-fusion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmap-fusion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmap-fusion:0.4.0--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmap-fusion/0.4.0--2
$ module help quay.io/biocontainers/gmap-fusion/0.4.0--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmap-fusion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmap-fusion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmap-fusion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmap-fusion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmap-fusion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmap-fusion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GMAP-fusion

```bash
$ singularity exec <container> /usr/local/bin/GMAP-fusion
$ podman run --it --rm --entrypoint /usr/local/bin/GMAP-fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMAP-fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gmap_compress

```bash
$ singularity exec <container> /usr/local/bin/gmap_compress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_process

```bash
$ singularity exec <container> /usr/local/bin/gmap_process
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_process   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_process   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_reassemble

```bash
$ singularity exec <container> /usr/local/bin/gmap_reassemble
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_uncompress

```bash
$ singularity exec <container> /usr/local/bin/gmap_uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gsnapl

```bash
$ singularity exec <container> /usr/local/bin/gsnapl
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl.sse42

```bash
$ singularity exec <container> /usr/local/bin/gsnapl.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_genes

```bash
$ singularity exec <container> /usr/local/bin/gtf_genes
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_introns

```bash
$ singularity exec <container> /usr/local/bin/gtf_introns
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_splicesites

```bash
$ singularity exec <container> /usr/local/bin/gtf_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_transcript_splicesites

```bash
$ singularity exec <container> /usr/local/bin/gtf_transcript_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_transcript_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_transcript_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvf_iit

```bash
$ singularity exec <container> /usr/local/bin/gvf_iit
$ podman run --it --rm --entrypoint /usr/local/bin/gvf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gvf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iit_dump

```bash
$ singularity exec <container> /usr/local/bin/iit_dump
$ podman run --it --rm --entrypoint /usr/local/bin/iit_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iit_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iit_get

```bash
$ singularity exec <container> /usr/local/bin/iit_get
$ podman run --it --rm --entrypoint /usr/local/bin/iit_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iit_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iit_store

```bash
$ singularity exec <container> /usr/local/bin/iit_store
$ podman run --it --rm --entrypoint /usr/local/bin/iit_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iit_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md_coords

```bash
$ singularity exec <container> /usr/local/bin/md_coords
$ podman run --it --rm --entrypoint /usr/local/bin/md_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_genes

```bash
$ singularity exec <container> /usr/local/bin/psl_genes
$ podman run --it --rm --entrypoint /usr/local/bin/psl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_introns

```bash
$ singularity exec <container> /usr/local/bin/psl_introns
$ podman run --it --rm --entrypoint /usr/local/bin/psl_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_splicesites

```bash
$ singularity exec <container> /usr/local/bin/psl_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/psl_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_sort

```bash
$ singularity exec <container> /usr/local/bin/sam_sort
$ podman run --it --rm --entrypoint /usr/local/bin/sam_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpindex

```bash
$ singularity exec <container> /usr/local/bin/snpindex
$ podman run --it --rm --entrypoint /usr/local/bin/snpindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trindex

```bash
$ singularity exec <container> /usr/local/bin/trindex
$ podman run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_iit

```bash
$ singularity exec <container> /usr/local/bin/vcf_iit
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap

```bash
$ singularity exec <container> /usr/local/bin/gmap
$ podman run --it --rm --entrypoint /usr/local/bin/gmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_archive

```bash
$ singularity exec <container> /usr/local/bin/db_archive
$ podman run --it --rm --entrypoint /usr/local/bin/db_archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_checkpoint

```bash
$ singularity exec <container> /usr/local/bin/db_checkpoint
$ podman run --it --rm --entrypoint /usr/local/bin/db_checkpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_checkpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_deadlock

```bash
$ singularity exec <container> /usr/local/bin/db_deadlock
$ podman run --it --rm --entrypoint /usr/local/bin/db_deadlock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_deadlock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_dump

```bash
$ singularity exec <container> /usr/local/bin/db_dump
$ podman run --it --rm --entrypoint /usr/local/bin/db_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_hotbackup

```bash
$ singularity exec <container> /usr/local/bin/db_hotbackup
$ podman run --it --rm --entrypoint /usr/local/bin/db_hotbackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_hotbackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_load

```bash
$ singularity exec <container> /usr/local/bin/db_load
$ podman run --it --rm --entrypoint /usr/local/bin/db_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_log_verify

```bash
$ singularity exec <container> /usr/local/bin/db_log_verify
$ podman run --it --rm --entrypoint /usr/local/bin/db_log_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_log_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_printlog

```bash
$ singularity exec <container> /usr/local/bin/db_printlog
$ podman run --it --rm --entrypoint /usr/local/bin/db_printlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_printlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_recover

```bash
$ singularity exec <container> /usr/local/bin/db_recover
$ podman run --it --rm --entrypoint /usr/local/bin/db_recover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_recover   -v ${PWD} -w ${PWD} <container> -c " $@"
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