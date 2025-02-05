---
layout: container
name:  "quay.io/biocontainers/quota_anchor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quota_anchor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quota_anchor/container.yaml"
updated_at: "2025-02-05 03:37:03.026793"
latest: "0.0.1b2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/quota_anchor"
aliases:
 - "anchorwave"
 - "anchorwave_avx2"
 - "anchorwave_avx512"
 - "anchorwave_sse2"
 - "anchorwave_sse4.1"
 - "gffread"
 - "gmap.nosimd"
 - "gmap_cat"
 - "gmapl.nosimd"
 - "gsnap.nosimd"
 - "gsnapl.nosimd"
 - "indexdb_cat"
 - "pal2nal.pl"
 - "quota_Anchor"
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
 - "gsnapl"
 - "gsnapl.sse42"
 - "gtf_genes"
 - "gtf_introns"
 - "gtf_splicesites"
 - "gtf_transcript_splicesites"
versions:
 - "0.0.1a0--pyhdfd78af_0"
 - "0.0.1a1--pyhdfd78af_0"
 - "0.0.1b2--pyhdfd78af_1"
description: "singularity registry hpc automated addition for quota_anchor"
config: {"url": "https://biocontainers.pro/tools/quota_anchor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for quota_anchor", "latest": {"0.0.1b2--pyhdfd78af_1": "sha256:d64d3e7f12732affe0247cd906a1ae1bd1d23614ac0be29c59c981c0a11115dd"}, "tags": {"0.0.1a0--pyhdfd78af_0": "sha256:ccd9381bdbb88b28f7770029c205c1fdb339b95a193e5370e597e8b2142732d5", "0.0.1a1--pyhdfd78af_0": "sha256:c49c9090e520f5be503d5daf58a524298011c1b61e9b9ab81be004a149f58e40", "0.0.1b2--pyhdfd78af_1": "sha256:d64d3e7f12732affe0247cd906a1ae1bd1d23614ac0be29c59c981c0a11115dd"}, "docker": "quay.io/biocontainers/quota_anchor", "aliases": {"anchorwave": "/usr/local/bin/anchorwave", "anchorwave_avx2": "/usr/local/bin/anchorwave_avx2", "anchorwave_avx512": "/usr/local/bin/anchorwave_avx512", "anchorwave_sse2": "/usr/local/bin/anchorwave_sse2", "anchorwave_sse4.1": "/usr/local/bin/anchorwave_sse4.1", "gffread": "/usr/local/bin/gffread", "gmap.nosimd": "/usr/local/bin/gmap.nosimd", "gmap_cat": "/usr/local/bin/gmap_cat", "gmapl.nosimd": "/usr/local/bin/gmapl.nosimd", "gsnap.nosimd": "/usr/local/bin/gsnap.nosimd", "gsnapl.nosimd": "/usr/local/bin/gsnapl.nosimd", "indexdb_cat": "/usr/local/bin/indexdb_cat", "pal2nal.pl": "/usr/local/bin/pal2nal.pl", "quota_Anchor": "/usr/local/bin/quota_Anchor", "trindex": "/usr/local/bin/trindex", "atoiindex": "/usr/local/bin/atoiindex", "cmetindex": "/usr/local/bin/cmetindex", "cpuid": "/usr/local/bin/cpuid", "dbsnp_iit": "/usr/local/bin/dbsnp_iit", "ensembl_genes": "/usr/local/bin/ensembl_genes", "fa_coords": "/usr/local/bin/fa_coords", "get-genome": "/usr/local/bin/get-genome", "gff3_genes": "/usr/local/bin/gff3_genes", "gff3_introns": "/usr/local/bin/gff3_introns", "gff3_splicesites": "/usr/local/bin/gff3_splicesites", "gmap.sse42": "/usr/local/bin/gmap.sse42", "gmap_build": "/usr/local/bin/gmap_build", "gmap_process": "/usr/local/bin/gmap_process", "gmapindex": "/usr/local/bin/gmapindex", "gmapl": "/usr/local/bin/gmapl", "gmapl.sse42": "/usr/local/bin/gmapl.sse42", "gsnap": "/usr/local/bin/gsnap", "gsnap.sse42": "/usr/local/bin/gsnap.sse42", "gsnapl": "/usr/local/bin/gsnapl", "gsnapl.sse42": "/usr/local/bin/gsnapl.sse42", "gtf_genes": "/usr/local/bin/gtf_genes", "gtf_introns": "/usr/local/bin/gtf_introns", "gtf_splicesites": "/usr/local/bin/gtf_splicesites", "gtf_transcript_splicesites": "/usr/local/bin/gtf_transcript_splicesites"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quota_anchor.
singularity registry hpc automated addition for quota_anchor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quota_anchor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quota_anchor:0.0.1b2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quota_anchor/0.0.1b2--pyhdfd78af_1
$ module help quay.io/biocontainers/quota_anchor/0.0.1b2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quota_anchor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quota_anchor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quota_anchor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quota_anchor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quota_anchor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quota_anchor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anchorwave

```bash
$ singularity exec <container> /usr/local/bin/anchorwave
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_avx2

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_avx2
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_avx512

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_avx512
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_sse2

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_sse2
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_sse2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_sse2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_sse4.1

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_cat

```bash
$ singularity exec <container> /usr/local/bin/gmap_cat
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### indexdb_cat

```bash
$ singularity exec <container> /usr/local/bin/indexdb_cat
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pal2nal.pl

```bash
$ singularity exec <container> /usr/local/bin/pal2nal.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quota_Anchor

```bash
$ singularity exec <container> /usr/local/bin/quota_Anchor
$ podman run --it --rm --entrypoint /usr/local/bin/quota_Anchor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quota_Anchor   -v ${PWD} -w ${PWD} <container> -c " $@"
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