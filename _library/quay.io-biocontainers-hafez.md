---
layout: container
name:  "quay.io/biocontainers/hafez"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hafez/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hafez/container.yaml"
updated_at: "2025-04-11 03:42:25.702977"
latest: "1.0.4--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/hafez"
aliases:
 - "a3m_database_extract"
 - "a3m_database_filter"
 - "a3m_database_reduce"
 - "a3m_extract"
 - "a3m_reduce"
 - "cstranslate"
 - "ffindex_apply"
 - "ffindex_build"
 - "ffindex_from_fasta"
 - "ffindex_from_fasta_with_split"
 - "ffindex_get"
 - "ffindex_modify"
 - "ffindex_order"
 - "ffindex_reduce"
 - "ffindex_unpack"
 - "hafeZ.py"
 - "hhalign"
 - "hhalign_omp"
 - "hhblits"
 - "hhblits_ca3m"
 - "hhblits_omp"
 - "hhconsensus"
 - "hhfilter"
 - "hhmake"
 - "hhsearch"
 - "hhsearch_omp"
 - "ldc-build-runtime"
 - "ldc-profdata"
 - "ldc-prune-cache"
 - "ldc2"
 - "ldmd2"
 - "mosdepth"
 - "sambamba"
 - "filter-table"
 - "kmutate.sh"
 - "runhmm.sh"
 - "spdi2prod"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "summarizecoverage.sh"
 - "alltoall.sh"
 - "analyzesketchresults.sh"
versions:
 - "1.0.2--pyh5e36f6f_0"
 - "1.0.3--pyh7cba7a3_0"
 - "1.0.4--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for hafez"
config: {"url": "https://biocontainers.pro/tools/hafez", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hafez", "latest": {"1.0.4--pyh7cba7a3_0": "sha256:dd481c1e6304855a45e7eb314f8fc678e868dd9978c4c5132f32060a45efe6f4"}, "tags": {"1.0.2--pyh5e36f6f_0": "sha256:e8cd8b4c86e8c1df6d72ba0c3d6394587d5ec87b97b6b1cf3723153333f81049", "1.0.3--pyh7cba7a3_0": "sha256:85da51b188fd186e2addd5111d94bdc63ecdd62cd2705ceda70a9c7617c926c1", "1.0.4--pyh7cba7a3_0": "sha256:dd481c1e6304855a45e7eb314f8fc678e868dd9978c4c5132f32060a45efe6f4"}, "docker": "quay.io/biocontainers/hafez", "aliases": {"a3m_database_extract": "/usr/local/bin/a3m_database_extract", "a3m_database_filter": "/usr/local/bin/a3m_database_filter", "a3m_database_reduce": "/usr/local/bin/a3m_database_reduce", "a3m_extract": "/usr/local/bin/a3m_extract", "a3m_reduce": "/usr/local/bin/a3m_reduce", "cstranslate": "/usr/local/bin/cstranslate", "ffindex_apply": "/usr/local/bin/ffindex_apply", "ffindex_build": "/usr/local/bin/ffindex_build", "ffindex_from_fasta": "/usr/local/bin/ffindex_from_fasta", "ffindex_from_fasta_with_split": "/usr/local/bin/ffindex_from_fasta_with_split", "ffindex_get": "/usr/local/bin/ffindex_get", "ffindex_modify": "/usr/local/bin/ffindex_modify", "ffindex_order": "/usr/local/bin/ffindex_order", "ffindex_reduce": "/usr/local/bin/ffindex_reduce", "ffindex_unpack": "/usr/local/bin/ffindex_unpack", "hafeZ.py": "/usr/local/bin/hafeZ.py", "hhalign": "/usr/local/bin/hhalign", "hhalign_omp": "/usr/local/bin/hhalign_omp", "hhblits": "/usr/local/bin/hhblits", "hhblits_ca3m": "/usr/local/bin/hhblits_ca3m", "hhblits_omp": "/usr/local/bin/hhblits_omp", "hhconsensus": "/usr/local/bin/hhconsensus", "hhfilter": "/usr/local/bin/hhfilter", "hhmake": "/usr/local/bin/hhmake", "hhsearch": "/usr/local/bin/hhsearch", "hhsearch_omp": "/usr/local/bin/hhsearch_omp", "ldc-build-runtime": "/usr/local/bin/ldc-build-runtime", "ldc-profdata": "/usr/local/bin/ldc-profdata", "ldc-prune-cache": "/usr/local/bin/ldc-prune-cache", "ldc2": "/usr/local/bin/ldc2", "ldmd2": "/usr/local/bin/ldmd2", "mosdepth": "/usr/local/bin/mosdepth", "sambamba": "/usr/local/bin/sambamba", "filter-table": "/usr/local/bin/filter-table", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "spdi2prod": "/usr/local/bin/spdi2prod", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hafez.
shpc-registry automated BioContainers addition for hafez
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hafez
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hafez:1.0.4--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hafez/1.0.4--pyh7cba7a3_0
$ module help quay.io/biocontainers/hafez/1.0.4--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hafez-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hafez-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hafez-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hafez-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hafez-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hafez-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### a3m_database_extract

```bash
$ singularity exec <container> /usr/local/bin/a3m_database_extract
$ podman run --it --rm --entrypoint /usr/local/bin/a3m_database_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a3m_database_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a3m_database_filter

```bash
$ singularity exec <container> /usr/local/bin/a3m_database_filter
$ podman run --it --rm --entrypoint /usr/local/bin/a3m_database_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a3m_database_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a3m_database_reduce

```bash
$ singularity exec <container> /usr/local/bin/a3m_database_reduce
$ podman run --it --rm --entrypoint /usr/local/bin/a3m_database_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a3m_database_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a3m_extract

```bash
$ singularity exec <container> /usr/local/bin/a3m_extract
$ podman run --it --rm --entrypoint /usr/local/bin/a3m_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a3m_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a3m_reduce

```bash
$ singularity exec <container> /usr/local/bin/a3m_reduce
$ podman run --it --rm --entrypoint /usr/local/bin/a3m_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a3m_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cstranslate

```bash
$ singularity exec <container> /usr/local/bin/cstranslate
$ podman run --it --rm --entrypoint /usr/local/bin/cstranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cstranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_apply

```bash
$ singularity exec <container> /usr/local/bin/ffindex_apply
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_apply   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_apply   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_build

```bash
$ singularity exec <container> /usr/local/bin/ffindex_build
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_from_fasta

```bash
$ singularity exec <container> /usr/local/bin/ffindex_from_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_from_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_from_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_from_fasta_with_split

```bash
$ singularity exec <container> /usr/local/bin/ffindex_from_fasta_with_split
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_from_fasta_with_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_from_fasta_with_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_get

```bash
$ singularity exec <container> /usr/local/bin/ffindex_get
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_modify

```bash
$ singularity exec <container> /usr/local/bin/ffindex_modify
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_modify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_modify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_order

```bash
$ singularity exec <container> /usr/local/bin/ffindex_order
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_order   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_order   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_reduce

```bash
$ singularity exec <container> /usr/local/bin/ffindex_reduce
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffindex_unpack

```bash
$ singularity exec <container> /usr/local/bin/ffindex_unpack
$ podman run --it --rm --entrypoint /usr/local/bin/ffindex_unpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffindex_unpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hafeZ.py

```bash
$ singularity exec <container> /usr/local/bin/hafeZ.py
$ podman run --it --rm --entrypoint /usr/local/bin/hafeZ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hafeZ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhalign

```bash
$ singularity exec <container> /usr/local/bin/hhalign
$ podman run --it --rm --entrypoint /usr/local/bin/hhalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhalign_omp

```bash
$ singularity exec <container> /usr/local/bin/hhalign_omp
$ podman run --it --rm --entrypoint /usr/local/bin/hhalign_omp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhalign_omp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhblits

```bash
$ singularity exec <container> /usr/local/bin/hhblits
$ podman run --it --rm --entrypoint /usr/local/bin/hhblits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhblits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhblits_ca3m

```bash
$ singularity exec <container> /usr/local/bin/hhblits_ca3m
$ podman run --it --rm --entrypoint /usr/local/bin/hhblits_ca3m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhblits_ca3m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhblits_omp

```bash
$ singularity exec <container> /usr/local/bin/hhblits_omp
$ podman run --it --rm --entrypoint /usr/local/bin/hhblits_omp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhblits_omp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhconsensus

```bash
$ singularity exec <container> /usr/local/bin/hhconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/hhconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhfilter

```bash
$ singularity exec <container> /usr/local/bin/hhfilter
$ podman run --it --rm --entrypoint /usr/local/bin/hhfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhmake

```bash
$ singularity exec <container> /usr/local/bin/hhmake
$ podman run --it --rm --entrypoint /usr/local/bin/hhmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhsearch

```bash
$ singularity exec <container> /usr/local/bin/hhsearch
$ podman run --it --rm --entrypoint /usr/local/bin/hhsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hhsearch_omp

```bash
$ singularity exec <container> /usr/local/bin/hhsearch_omp
$ podman run --it --rm --entrypoint /usr/local/bin/hhsearch_omp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hhsearch_omp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-build-runtime

```bash
$ singularity exec <container> /usr/local/bin/ldc-build-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-profdata

```bash
$ singularity exec <container> /usr/local/bin/ldc-profdata
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-prune-cache

```bash
$ singularity exec <container> /usr/local/bin/ldc-prune-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc2

```bash
$ singularity exec <container> /usr/local/bin/ldc2
$ podman run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldmd2

```bash
$ singularity exec <container> /usr/local/bin/ldmd2
$ podman run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sambamba

```bash
$ singularity exec <container> /usr/local/bin/sambamba
$ podman run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-table

```bash
$ singularity exec <container> /usr/local/bin/filter-table
$ podman run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2prod

```bash
$ singularity exec <container> /usr/local/bin/spdi2prod
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerposition.sh

```bash
$ singularity exec <container> /usr/local/bin/kmerposition.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformatpb.sh

```bash
$ singularity exec <container> /usr/local/bin/reformatpb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizecoverage.sh

```bash
$ singularity exec <container> /usr/local/bin/summarizecoverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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