---
layout: container
name:  "quay.io/biocontainers/pneumo-typer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pneumo-typer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pneumo-typer/container.yaml"
updated_at: "2025-04-14 03:50:39.582840"
latest: "1.0.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pneumo-typer"
aliases:
 - "blastn_vdb"
 - "faToNib"
 - "gfClient"
 - "nibFrag"
 - "pneumo-typer"
 - "pslPretty"
 - "pslReps"
 - "pslSort"
 - "tblastn_vdb"
 - "gfServer"
 - "twoBitToFa"
 - "blat"
 - "twoBitInfo"
 - "uuid"
 - "uuid-config"
 - "faToTwoBit"
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
versions:
 - "1.0.1--hdfd78af_0"
 - "1.0.1--hdfd78af_3"
 - "1.0.3--hdfd78af_0"
description: "singularity registry hpc automated addition for pneumo-typer"
config: {"url": "https://biocontainers.pro/tools/pneumo-typer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pneumo-typer", "latest": {"1.0.3--hdfd78af_0": "sha256:92bbad9a73db47762b3ad40ef3bd6a3ecf7e65b3c60622904fd87ed39e59ab0e"}, "tags": {"1.0.1--hdfd78af_0": "sha256:f8247e39ae40c12c44552a3a5590d6143fc47a1c2b52ec1cad58f7ae0c646fc8", "1.0.1--hdfd78af_3": "sha256:fa2c1338648d49fe2102686d02fc9e0eaf9ec7566e6b7e0f0ad9e2f5a6ca9ca3", "1.0.3--hdfd78af_0": "sha256:92bbad9a73db47762b3ad40ef3bd6a3ecf7e65b3c60622904fd87ed39e59ab0e"}, "docker": "quay.io/biocontainers/pneumo-typer", "aliases": {"blastn_vdb": "/usr/local/bin/blastn_vdb", "faToNib": "/usr/local/bin/faToNib", "gfClient": "/usr/local/bin/gfClient", "nibFrag": "/usr/local/bin/nibFrag", "pneumo-typer": "/usr/local/bin/pneumo-typer", "pslPretty": "/usr/local/bin/pslPretty", "pslReps": "/usr/local/bin/pslReps", "pslSort": "/usr/local/bin/pslSort", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "gfServer": "/usr/local/bin/gfServer", "twoBitToFa": "/usr/local/bin/twoBitToFa", "blat": "/usr/local/bin/blat", "twoBitInfo": "/usr/local/bin/twoBitInfo", "uuid": "/usr/local/bin/uuid", "uuid-config": "/usr/local/bin/uuid-config", "faToTwoBit": "/usr/local/bin/faToTwoBit", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search", "bp_find-blast-matches": "/usr/local/bin/bp_find-blast-matches", "bp_gccalc": "/usr/local/bin/bp_gccalc", "bp_genbank2gff3": "/usr/local/bin/bp_genbank2gff3", "bp_index": "/usr/local/bin/bp_index", "bp_local_taxonomydb_query": "/usr/local/bin/bp_local_taxonomydb_query", "bp_make_mrna_protein": "/usr/local/bin/bp_make_mrna_protein", "bp_mask_by_search": "/usr/local/bin/bp_mask_by_search", "bp_mrtrans": "/usr/local/bin/bp_mrtrans", "bp_mutate": "/usr/local/bin/bp_mutate", "bp_nexus2nh": "/usr/local/bin/bp_nexus2nh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pneumo-typer.
singularity registry hpc automated addition for pneumo-typer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pneumo-typer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pneumo-typer:1.0.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pneumo-typer/1.0.3--hdfd78af_0
$ module help quay.io/biocontainers/pneumo-typer/1.0.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pneumo-typer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pneumo-typer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pneumo-typer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pneumo-typer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pneumo-typer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pneumo-typer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToNib

```bash
$ singularity exec <container> /usr/local/bin/faToNib
$ podman run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfClient

```bash
$ singularity exec <container> /usr/local/bin/gfClient
$ podman run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nibFrag

```bash
$ singularity exec <container> /usr/local/bin/nibFrag
$ podman run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pneumo-typer

```bash
$ singularity exec <container> /usr/local/bin/pneumo-typer
$ podman run --it --rm --entrypoint /usr/local/bin/pneumo-typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pneumo-typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslPretty

```bash
$ singularity exec <container> /usr/local/bin/pslPretty
$ podman run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslReps

```bash
$ singularity exec <container> /usr/local/bin/pslReps
$ podman run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslSort

```bash
$ singularity exec <container> /usr/local/bin/pslSort
$ podman run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blat

```bash
$ singularity exec <container> /usr/local/bin/blat
$ podman run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitInfo

```bash
$ singularity exec <container> /usr/local/bin/twoBitInfo
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid

```bash
$ singularity exec <container> /usr/local/bin/uuid
$ podman run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid-config

```bash
$ singularity exec <container> /usr/local/bin/uuid-config
$ podman run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
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