---
layout: container
name:  "quay.io/biocontainers/automappa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/automappa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/automappa/container.yaml"
updated_at: "2024-11-21 03:16:41.172792"
latest: "2.1.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/automappa"
aliases:
 - "automappa"
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
 - "dash-generate-components"
 - "dash-update-components"
 - "editorconfig"
 - "gdown"
 - "js-beautify"
 - "renderer"
 - "rsync-ssl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "doesitcache"
 - "flask"
 - "diamond"
 - "ipython3"
 - "parsort"
 - "ipython"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "numba"
 - "pycc"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
 - "env_parallel.dash"
 - "env_parallel.fish"
 - "env_parallel.ksh"
 - "env_parallel.mksh"
versions:
 - "2.1.0--pyh5e36f6f_0"
description: "singularity registry hpc automated addition for automappa"
config: {"url": "https://biocontainers.pro/tools/automappa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for automappa", "latest": {"2.1.0--pyh5e36f6f_0": "sha256:a36de99781d7a478599094f166e090d6b578be6a86386a20becbe13fe0dcf553"}, "tags": {"2.1.0--pyh5e36f6f_0": "sha256:a36de99781d7a478599094f166e090d6b578be6a86386a20becbe13fe0dcf553"}, "docker": "quay.io/biocontainers/automappa", "aliases": {"automappa": "/usr/local/bin/automappa", "autometa-bedtools-genomecov": "/usr/local/bin/autometa-bedtools-genomecov", "autometa-benchmark": "/usr/local/bin/autometa-benchmark", "autometa-binning": "/usr/local/bin/autometa-binning", "autometa-binning-ldm": "/usr/local/bin/autometa-binning-ldm", "autometa-binning-ldm-loginfo": "/usr/local/bin/autometa-binning-ldm-loginfo", "autometa-binning-summary": "/usr/local/bin/autometa-binning-summary", "autometa-config": "/usr/local/bin/autometa-config", "autometa-coverage": "/usr/local/bin/autometa-coverage", "autometa-download-dataset": "/usr/local/bin/autometa-download-dataset", "autometa-hmmsearch-filter": "/usr/local/bin/autometa-hmmsearch-filter", "autometa-kmers": "/usr/local/bin/autometa-kmers", "autometa-length-filter": "/usr/local/bin/autometa-length-filter", "autometa-markers": "/usr/local/bin/autometa-markers", "autometa-orfs": "/usr/local/bin/autometa-orfs", "autometa-taxonomy": "/usr/local/bin/autometa-taxonomy", "autometa-taxonomy-lca": "/usr/local/bin/autometa-taxonomy-lca", "autometa-taxonomy-majority-vote": "/usr/local/bin/autometa-taxonomy-majority-vote", "autometa-unclustered-recruitment": "/usr/local/bin/autometa-unclustered-recruitment", "autometa-update-databases": "/usr/local/bin/autometa-update-databases", "dash-generate-components": "/usr/local/bin/dash-generate-components", "dash-update-components": "/usr/local/bin/dash-update-components", "editorconfig": "/usr/local/bin/editorconfig", "gdown": "/usr/local/bin/gdown", "js-beautify": "/usr/local/bin/js-beautify", "renderer": "/usr/local/bin/renderer", "rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "doesitcache": "/usr/local/bin/doesitcache", "flask": "/usr/local/bin/flask", "diamond": "/usr/local/bin/diamond", "ipython3": "/usr/local/bin/ipython3", "parsort": "/usr/local/bin/parsort", "ipython": "/usr/local/bin/ipython", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/automappa.
singularity registry hpc automated addition for automappa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/automappa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/automappa:2.1.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/automappa/2.1.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/automappa/2.1.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### automappa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### automappa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### automappa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### automappa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### automappa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### automappa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### automappa

```bash
$ singularity exec <container> /usr/local/bin/automappa
$ podman run --it --rm --entrypoint /usr/local/bin/automappa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/automappa   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dash-generate-components

```bash
$ singularity exec <container> /usr/local/bin/dash-generate-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-update-components

```bash
$ singularity exec <container> /usr/local/bin/dash-update-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### editorconfig

```bash
$ singularity exec <container> /usr/local/bin/editorconfig
$ podman run --it --rm --entrypoint /usr/local/bin/editorconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/editorconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdown

```bash
$ singularity exec <container> /usr/local/bin/gdown
$ podman run --it --rm --entrypoint /usr/local/bin/gdown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdown   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### js-beautify

```bash
$ singularity exec <container> /usr/local/bin/js-beautify
$ podman run --it --rm --entrypoint /usr/local/bin/js-beautify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/js-beautify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renderer

```bash
$ singularity exec <container> /usr/local/bin/renderer
$ podman run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.csh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.csh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.dash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.dash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.fish

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.fish
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.mksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.mksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
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