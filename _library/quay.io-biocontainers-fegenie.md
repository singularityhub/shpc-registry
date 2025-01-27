---
layout: container
name:  "quay.io/biocontainers/fegenie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fegenie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fegenie/container.yaml"
updated_at: "2025-01-27 07:10:38.768160"
latest: "1.2--py311r40hdfd78af_3"
container_url: "https://biocontainers.pro/tools/fegenie"
aliases:
 - "FeGenie.py"
 - "aggregateBinDepths.pl"
 - "aggregateContigOverlapsByBin.pl"
 - "contigOverlaps"
 - "jgi_summarize_bam_contig_depths"
 - "merge_depths.pl"
 - "metabat"
 - "metabat1"
 - "metabat2"
 - "runMetaBat.sh"
 - "pandoc-server"
 - "diamond"
 - "prodigal"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
versions:
 - "1.2--py310r40hdfd78af_1"
 - "1.2--py311r40hdfd78af_2"
 - "1.2--py311r40hdfd78af_3"
description: "shpc-registry automated BioContainers addition for fegenie"
config: {"url": "https://biocontainers.pro/tools/fegenie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fegenie", "latest": {"1.2--py311r40hdfd78af_3": "sha256:08ffd70da8a9dd27f3585f72a392c84e219219a972d80f8cb5d777e9da1971e3"}, "tags": {"1.2--py310r40hdfd78af_1": "sha256:17eb874ab13962a0dc74b77e19803744772ef64791d2d6a3926c2843bab1c002", "1.2--py311r40hdfd78af_2": "sha256:7da1b107bb1b1cfe4c59cac2550827f8f6c24efa092098c6d7811631c7df224c", "1.2--py311r40hdfd78af_3": "sha256:08ffd70da8a9dd27f3585f72a392c84e219219a972d80f8cb5d777e9da1971e3"}, "docker": "quay.io/biocontainers/fegenie", "aliases": {"FeGenie.py": "/usr/local/bin/FeGenie.py", "aggregateBinDepths.pl": "/usr/local/bin/aggregateBinDepths.pl", "aggregateContigOverlapsByBin.pl": "/usr/local/bin/aggregateContigOverlapsByBin.pl", "contigOverlaps": "/usr/local/bin/contigOverlaps", "jgi_summarize_bam_contig_depths": "/usr/local/bin/jgi_summarize_bam_contig_depths", "merge_depths.pl": "/usr/local/bin/merge_depths.pl", "metabat": "/usr/local/bin/metabat", "metabat1": "/usr/local/bin/metabat1", "metabat2": "/usr/local/bin/metabat2", "runMetaBat.sh": "/usr/local/bin/runMetaBat.sh", "pandoc-server": "/usr/local/bin/pandoc-server", "diamond": "/usr/local/bin/diamond", "prodigal": "/usr/local/bin/prodigal", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fegenie.
shpc-registry automated BioContainers addition for fegenie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fegenie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fegenie:1.2--py311r40hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fegenie/1.2--py311r40hdfd78af_3
$ module help quay.io/biocontainers/fegenie/1.2--py311r40hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fegenie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fegenie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fegenie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fegenie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fegenie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fegenie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FeGenie.py

```bash
$ singularity exec <container> /usr/local/bin/FeGenie.py
$ podman run --it --rm --entrypoint /usr/local/bin/FeGenie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FeGenie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregateBinDepths.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateBinDepths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregateContigOverlapsByBin.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateContigOverlapsByBin.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contigOverlaps

```bash
$ singularity exec <container> /usr/local/bin/contigOverlaps
$ podman run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jgi_summarize_bam_contig_depths

```bash
$ singularity exec <container> /usr/local/bin/jgi_summarize_bam_contig_depths
$ podman run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_depths.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_depths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_depths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_depths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat

```bash
$ singularity exec <container> /usr/local/bin/metabat
$ podman run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat1

```bash
$ singularity exec <container> /usr/local/bin/metabat1
$ podman run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat2

```bash
$ singularity exec <container> /usr/local/bin/metabat2
$ podman run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMetaBat.sh

```bash
$ singularity exec <container> /usr/local/bin/runMetaBat.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
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