---
layout: container
name:  "quay.io/biocontainers/hla-asm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hla-asm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hla-asm/container.yaml"
updated_at: "2024-03-05 03:04:37.308766"
latest: "1.0.1--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hla-asm"
aliases:
 - "HLA-ASM.pl"
 - "findPath.pm"
 - "bp_aacomp"
 - "bp_bioflat_index"
 - "bp_biogetseq"
 - "bp_dbsplit"
 - "bp_extract_feature_seq"
 - "bp_fastam9_to_table"
 - "bp_fetch"
 - "bp_filter_search"
 - "bp_find-blast-matches"
 - "bp_gccalc"
 - "bp_genbank2gff3"
 - "bp_index"
 - "bp_local_taxonomydb_query"
 - "bp_make_mrna_protein"
 - "bp_mask_by_search"
 - "bp_mrtrans"
 - "bp_mutate"
 - "bp_nexus2nh"
 - "bp_nrdb"
 - "bp_oligo_count"
 - "bp_process_gadfly"
 - "bp_process_sgd"
 - "bp_revtrans-motif"
 - "bp_search2alnblocks"
 - "bp_search2gff"
versions:
 - "1.0.1--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for hla-asm"
config: {"url": "https://biocontainers.pro/tools/hla-asm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hla-asm", "latest": {"1.0.1--pl5321hdfd78af_0": "sha256:567cf55c0ca7d834508c8b4646eed8083b78290fcd06972828b32dfd77f01863"}, "tags": {"1.0.1--pl5321hdfd78af_0": "sha256:567cf55c0ca7d834508c8b4646eed8083b78290fcd06972828b32dfd77f01863"}, "docker": "quay.io/biocontainers/hla-asm", "aliases": {"HLA-ASM.pl": "/usr/local/bin/HLA-ASM.pl", "findPath.pm": "/usr/local/bin/findPath.pm", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search", "bp_find-blast-matches": "/usr/local/bin/bp_find-blast-matches", "bp_gccalc": "/usr/local/bin/bp_gccalc", "bp_genbank2gff3": "/usr/local/bin/bp_genbank2gff3", "bp_index": "/usr/local/bin/bp_index", "bp_local_taxonomydb_query": "/usr/local/bin/bp_local_taxonomydb_query", "bp_make_mrna_protein": "/usr/local/bin/bp_make_mrna_protein", "bp_mask_by_search": "/usr/local/bin/bp_mask_by_search", "bp_mrtrans": "/usr/local/bin/bp_mrtrans", "bp_mutate": "/usr/local/bin/bp_mutate", "bp_nexus2nh": "/usr/local/bin/bp_nexus2nh", "bp_nrdb": "/usr/local/bin/bp_nrdb", "bp_oligo_count": "/usr/local/bin/bp_oligo_count", "bp_process_gadfly": "/usr/local/bin/bp_process_gadfly", "bp_process_sgd": "/usr/local/bin/bp_process_sgd", "bp_revtrans-motif": "/usr/local/bin/bp_revtrans-motif", "bp_search2alnblocks": "/usr/local/bin/bp_search2alnblocks", "bp_search2gff": "/usr/local/bin/bp_search2gff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hla-asm.
singularity registry hpc automated addition for hla-asm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hla-asm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hla-asm:1.0.1--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hla-asm/1.0.1--pl5321hdfd78af_0
$ module help quay.io/biocontainers/hla-asm/1.0.1--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hla-asm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hla-asm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hla-asm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hla-asm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hla-asm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hla-asm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HLA-ASM.pl

```bash
$ singularity exec <container> /usr/local/bin/HLA-ASM.pl
$ podman run --it --rm --entrypoint /usr/local/bin/HLA-ASM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HLA-ASM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findPath.pm

```bash
$ singularity exec <container> /usr/local/bin/findPath.pm
$ podman run --it --rm --entrypoint /usr/local/bin/findPath.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findPath.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_dbsplit

```bash
$ singularity exec <container> /usr/local/bin/bp_dbsplit
$ podman run --it --rm --entrypoint /usr/local/bin/bp_dbsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_dbsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_extract_feature_seq

```bash
$ singularity exec <container> /usr/local/bin/bp_extract_feature_seq
$ podman run --it --rm --entrypoint /usr/local/bin/bp_extract_feature_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_extract_feature_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_fastam9_to_table

```bash
$ singularity exec <container> /usr/local/bin/bp_fastam9_to_table
$ podman run --it --rm --entrypoint /usr/local/bin/bp_fastam9_to_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_fastam9_to_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_fetch

```bash
$ singularity exec <container> /usr/local/bin/bp_fetch
$ podman run --it --rm --entrypoint /usr/local/bin/bp_fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_filter_search

```bash
$ singularity exec <container> /usr/local/bin/bp_filter_search
$ podman run --it --rm --entrypoint /usr/local/bin/bp_filter_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_filter_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_gccalc

```bash
$ singularity exec <container> /usr/local/bin/bp_gccalc
$ podman run --it --rm --entrypoint /usr/local/bin/bp_gccalc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_gccalc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_genbank2gff3

```bash
$ singularity exec <container> /usr/local/bin/bp_genbank2gff3
$ podman run --it --rm --entrypoint /usr/local/bin/bp_genbank2gff3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_genbank2gff3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_index

```bash
$ singularity exec <container> /usr/local/bin/bp_index
$ podman run --it --rm --entrypoint /usr/local/bin/bp_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_local_taxonomydb_query

```bash
$ singularity exec <container> /usr/local/bin/bp_local_taxonomydb_query
$ podman run --it --rm --entrypoint /usr/local/bin/bp_local_taxonomydb_query   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_local_taxonomydb_query   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_make_mrna_protein

```bash
$ singularity exec <container> /usr/local/bin/bp_make_mrna_protein
$ podman run --it --rm --entrypoint /usr/local/bin/bp_make_mrna_protein   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_make_mrna_protein   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_mask_by_search

```bash
$ singularity exec <container> /usr/local/bin/bp_mask_by_search
$ podman run --it --rm --entrypoint /usr/local/bin/bp_mask_by_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_mask_by_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_mrtrans

```bash
$ singularity exec <container> /usr/local/bin/bp_mrtrans
$ podman run --it --rm --entrypoint /usr/local/bin/bp_mrtrans   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_mrtrans   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_mutate

```bash
$ singularity exec <container> /usr/local/bin/bp_mutate
$ podman run --it --rm --entrypoint /usr/local/bin/bp_mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_nexus2nh

```bash
$ singularity exec <container> /usr/local/bin/bp_nexus2nh
$ podman run --it --rm --entrypoint /usr/local/bin/bp_nexus2nh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_nexus2nh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_nrdb

```bash
$ singularity exec <container> /usr/local/bin/bp_nrdb
$ podman run --it --rm --entrypoint /usr/local/bin/bp_nrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_nrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_oligo_count

```bash
$ singularity exec <container> /usr/local/bin/bp_oligo_count
$ podman run --it --rm --entrypoint /usr/local/bin/bp_oligo_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_oligo_count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_process_gadfly

```bash
$ singularity exec <container> /usr/local/bin/bp_process_gadfly
$ podman run --it --rm --entrypoint /usr/local/bin/bp_process_gadfly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_process_gadfly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_process_sgd

```bash
$ singularity exec <container> /usr/local/bin/bp_process_sgd
$ podman run --it --rm --entrypoint /usr/local/bin/bp_process_sgd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_process_sgd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_revtrans-motif

```bash
$ singularity exec <container> /usr/local/bin/bp_revtrans-motif
$ podman run --it --rm --entrypoint /usr/local/bin/bp_revtrans-motif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_revtrans-motif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2alnblocks

```bash
$ singularity exec <container> /usr/local/bin/bp_search2alnblocks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2alnblocks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2alnblocks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2gff

```bash
$ singularity exec <container> /usr/local/bin/bp_search2gff
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
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