---
layout: container
name:  "quay.io/biocontainers/autometa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/autometa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/autometa/container.yaml"
updated_at: "2023-06-20 03:06:43.327439"
latest: "2.2.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/autometa"
aliases:
 - "autometa"
 - "autometa-bedtools-genomecov"
 - "autometa-benchmark"
 - "autometa-binning"
 - "autometa-binning-ldm"
 - "autometa-binning-ldm-loginfo"
 - "autometa-binning-summary"
 - "autometa-config"
 - "autometa-coverage"
 - "autometa-download-dataset"
 - "autometa-hmmsearch-filter"
 - "autometa-kmers"
 - "autometa-length-filter"
 - "autometa-markers"
 - "autometa-orfs"
 - "autometa-taxonomy"
 - "autometa-taxonomy-lca"
 - "autometa-taxonomy-majority-vote"
 - "autometa-unclustered-recruitment"
 - "autometa-update-databases"
 - "gdown"
 - "rsync-ssl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "doesitcache"
 - "ipython3"
 - "diamond"
 - "parsort"
versions:
 - "2.1.0--pyh5e36f6f_0"
 - "2.2.0--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for autometa"
config: {"url": "https://biocontainers.pro/tools/autometa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for autometa", "latest": {"2.2.0--pyh7cba7a3_0": "sha256:3ee6969901c532b8736bc8bfd16739695751da870487ef8b6747be0a477df689"}, "tags": {"2.1.0--pyh5e36f6f_0": "sha256:0218a75e97b25934b22058e8cea1317a6c1affd0972682d4e8c44550cb1ad9e4", "2.2.0--pyh7cba7a3_0": "sha256:3ee6969901c532b8736bc8bfd16739695751da870487ef8b6747be0a477df689"}, "docker": "quay.io/biocontainers/autometa", "aliases": {"autometa": "/usr/local/bin/autometa", "autometa-bedtools-genomecov": "/usr/local/bin/autometa-bedtools-genomecov", "autometa-benchmark": "/usr/local/bin/autometa-benchmark", "autometa-binning": "/usr/local/bin/autometa-binning", "autometa-binning-ldm": "/usr/local/bin/autometa-binning-ldm", "autometa-binning-ldm-loginfo": "/usr/local/bin/autometa-binning-ldm-loginfo", "autometa-binning-summary": "/usr/local/bin/autometa-binning-summary", "autometa-config": "/usr/local/bin/autometa-config", "autometa-coverage": "/usr/local/bin/autometa-coverage", "autometa-download-dataset": "/usr/local/bin/autometa-download-dataset", "autometa-hmmsearch-filter": "/usr/local/bin/autometa-hmmsearch-filter", "autometa-kmers": "/usr/local/bin/autometa-kmers", "autometa-length-filter": "/usr/local/bin/autometa-length-filter", "autometa-markers": "/usr/local/bin/autometa-markers", "autometa-orfs": "/usr/local/bin/autometa-orfs", "autometa-taxonomy": "/usr/local/bin/autometa-taxonomy", "autometa-taxonomy-lca": "/usr/local/bin/autometa-taxonomy-lca", "autometa-taxonomy-majority-vote": "/usr/local/bin/autometa-taxonomy-majority-vote", "autometa-unclustered-recruitment": "/usr/local/bin/autometa-unclustered-recruitment", "autometa-update-databases": "/usr/local/bin/autometa-update-databases", "gdown": "/usr/local/bin/gdown", "rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "doesitcache": "/usr/local/bin/doesitcache", "ipython3": "/usr/local/bin/ipython3", "diamond": "/usr/local/bin/diamond", "parsort": "/usr/local/bin/parsort"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/autometa.
shpc-registry automated BioContainers addition for autometa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/autometa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/autometa:2.2.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/autometa/2.2.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/autometa/2.2.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autometa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autometa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autometa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autometa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autometa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autometa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autometa

```bash
$ singularity exec <container> /usr/local/bin/autometa
$ podman run --it --rm --entrypoint /usr/local/bin/autometa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-bedtools-genomecov

```bash
$ singularity exec <container> /usr/local/bin/autometa-bedtools-genomecov
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-bedtools-genomecov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-bedtools-genomecov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-benchmark

```bash
$ singularity exec <container> /usr/local/bin/autometa-benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-binning

```bash
$ singularity exec <container> /usr/local/bin/autometa-binning
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-binning   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-binning   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-binning-ldm

```bash
$ singularity exec <container> /usr/local/bin/autometa-binning-ldm
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-binning-ldm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-binning-ldm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-binning-ldm-loginfo

```bash
$ singularity exec <container> /usr/local/bin/autometa-binning-ldm-loginfo
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-binning-ldm-loginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-binning-ldm-loginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-binning-summary

```bash
$ singularity exec <container> /usr/local/bin/autometa-binning-summary
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-binning-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-binning-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-config

```bash
$ singularity exec <container> /usr/local/bin/autometa-config
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-coverage

```bash
$ singularity exec <container> /usr/local/bin/autometa-coverage
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-download-dataset

```bash
$ singularity exec <container> /usr/local/bin/autometa-download-dataset
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-download-dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-download-dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-hmmsearch-filter

```bash
$ singularity exec <container> /usr/local/bin/autometa-hmmsearch-filter
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-hmmsearch-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-hmmsearch-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-kmers

```bash
$ singularity exec <container> /usr/local/bin/autometa-kmers
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-length-filter

```bash
$ singularity exec <container> /usr/local/bin/autometa-length-filter
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-length-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-length-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-markers

```bash
$ singularity exec <container> /usr/local/bin/autometa-markers
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-markers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-markers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-orfs

```bash
$ singularity exec <container> /usr/local/bin/autometa-orfs
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-taxonomy

```bash
$ singularity exec <container> /usr/local/bin/autometa-taxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-taxonomy-lca

```bash
$ singularity exec <container> /usr/local/bin/autometa-taxonomy-lca
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-taxonomy-lca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-taxonomy-lca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-taxonomy-majority-vote

```bash
$ singularity exec <container> /usr/local/bin/autometa-taxonomy-majority-vote
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-taxonomy-majority-vote   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-taxonomy-majority-vote   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-unclustered-recruitment

```bash
$ singularity exec <container> /usr/local/bin/autometa-unclustered-recruitment
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-unclustered-recruitment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-unclustered-recruitment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autometa-update-databases

```bash
$ singularity exec <container> /usr/local/bin/autometa-update-databases
$ podman run --it --rm --entrypoint /usr/local/bin/autometa-update-databases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autometa-update-databases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdown

```bash
$ singularity exec <container> /usr/local/bin/gdown
$ podman run --it --rm --entrypoint /usr/local/bin/gdown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdown   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync

```bash
$ singularity exec <container> /usr/local/bin/rsync
$ podman run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh128sum

```bash
$ singularity exec <container> /usr/local/bin/xxh128sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh32sum

```bash
$ singularity exec <container> /usr/local/bin/xxh32sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh64sum

```bash
$ singularity exec <container> /usr/local/bin/xxh64sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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