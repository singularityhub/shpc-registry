---
layout: container
name:  "quay.io/biocontainers/hla-la"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hla-la/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hla-la/container.yaml"
updated_at: "2023-08-29 03:01:04.935705"
latest: "1.0.3--hdcf5f25_2"
container_url: "https://biocontainers.pro/tools/hla-la"
aliases:
 - "HLA-ASM.pl"
 - "HLA-LA.pl"
 - "picard"
 - "bp_aacomp"
 - "bp_bioflat_index"
 - "bp_biogetseq"
 - "bp_dbsplit"
 - "bp_extract_feature_seq"
 - "bp_fastam9_to_table"
 - "bp_fetch"
 - "bp_filter_search"
 - "bp_find-blast-matches"
versions:
 - "1.0.3--hd03093a_0"
 - "1.0.3--hd03093a_1"
 - "1.0.3--hdcf5f25_2"
description: "shpc-registry automated BioContainers addition for hla-la"
config: {"url": "https://biocontainers.pro/tools/hla-la", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hla-la", "latest": {"1.0.3--hdcf5f25_2": "sha256:219f5af455458a51d4d3562253fe61eee8f6f28419029828ebe715b69241f8a0"}, "tags": {"1.0.3--hd03093a_0": "sha256:15fd1f4c6d3dead02f82660a684c1186d9b96b37d3e9f8102ce82614fc059716", "1.0.3--hd03093a_1": "sha256:d2586b8356473aa8cb83a76fa675b18b0a9e6f4033f0a8b40bfe557e2df9c988", "1.0.3--hdcf5f25_2": "sha256:219f5af455458a51d4d3562253fe61eee8f6f28419029828ebe715b69241f8a0"}, "docker": "quay.io/biocontainers/hla-la", "aliases": {"HLA-ASM.pl": "/usr/local/bin/HLA-ASM.pl", "HLA-LA.pl": "/usr/local/bin/HLA-LA.pl", "picard": "/usr/local/bin/picard", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search", "bp_find-blast-matches": "/usr/local/bin/bp_find-blast-matches"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hla-la.
shpc-registry automated BioContainers addition for hla-la
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hla-la
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hla-la:1.0.3--hdcf5f25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hla-la/1.0.3--hdcf5f25_2
$ module help quay.io/biocontainers/hla-la/1.0.3--hdcf5f25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hla-la-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hla-la-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hla-la-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hla-la-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hla-la-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hla-la-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HLA-ASM.pl

```bash
$ singularity exec <container> /usr/local/bin/HLA-ASM.pl
$ podman run --it --rm --entrypoint /usr/local/bin/HLA-ASM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HLA-ASM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HLA-LA.pl

```bash
$ singularity exec <container> /usr/local/bin/HLA-LA.pl
$ podman run --it --rm --entrypoint /usr/local/bin/HLA-LA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HLA-LA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
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