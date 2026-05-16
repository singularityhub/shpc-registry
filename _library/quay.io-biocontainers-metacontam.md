---
layout: container
name:  "quay.io/biocontainers/metacontam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metacontam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metacontam/container.yaml"
updated_at: "2026-05-16 05:46:56.256594"
latest: "0.0.1--py314hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metacontam"
aliases:
 - "bracken"
 - "bracken-build"
 - "combine_bracken_outputs.py"
 - "est_abundance.py"
 - "generate_kmer_distribution.py"
 - "k2"
 - "kmer2read_distr"
 - "metacontam"
 - "xxh3sum"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "rsync-ssl"
 - "rsync"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
 - "pair-at-a-time"
 - "print-missing-subranges"
 - "sort-by-length"
 - "xcommon.sh"
 - "xfetch"
 - "xfetch.ini"
 - "xfilter"
 - "xinfo"
 - "xlink"
 - "xlink.ini"
 - "xsearch"
versions:
 - "0.0.1--py314hdfd78af_0"
description: "singularity registry hpc automated addition for metacontam"
config: {"url": "https://biocontainers.pro/tools/metacontam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metacontam", "latest": {"0.0.1--py314hdfd78af_0": "sha256:efe3344dd4fd86a1c1789c244ff45f8ee2f167cc6b35911f07b5e1bc8e148aad"}, "tags": {"0.0.1--py314hdfd78af_0": "sha256:efe3344dd4fd86a1c1789c244ff45f8ee2f167cc6b35911f07b5e1bc8e148aad"}, "docker": "quay.io/biocontainers/metacontam", "aliases": {"bracken": "/usr/local/bin/bracken", "bracken-build": "/usr/local/bin/bracken-build", "combine_bracken_outputs.py": "/usr/local/bin/combine_bracken_outputs.py", "est_abundance.py": "/usr/local/bin/est_abundance.py", "generate_kmer_distribution.py": "/usr/local/bin/generate_kmer_distribution.py", "k2": "/usr/local/bin/k2", "kmer2read_distr": "/usr/local/bin/kmer2read_distr", "metacontam": "/usr/local/bin/metacontam", "xxh3sum": "/usr/local/bin/xxh3sum", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo", "xlink": "/usr/local/bin/xlink", "xlink.ini": "/usr/local/bin/xlink.ini", "xsearch": "/usr/local/bin/xsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metacontam.
singularity registry hpc automated addition for metacontam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metacontam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metacontam:0.0.1--py314hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metacontam/0.0.1--py314hdfd78af_0
$ module help quay.io/biocontainers/metacontam/0.0.1--py314hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metacontam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metacontam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metacontam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metacontam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metacontam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metacontam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bracken

```bash
$ singularity exec <container> /usr/local/bin/bracken
$ podman run --it --rm --entrypoint /usr/local/bin/bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bracken-build

```bash
$ singularity exec <container> /usr/local/bin/bracken-build
$ podman run --it --rm --entrypoint /usr/local/bin/bracken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bracken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_bracken_outputs.py

```bash
$ singularity exec <container> /usr/local/bin/combine_bracken_outputs.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_bracken_outputs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_bracken_outputs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### est_abundance.py

```bash
$ singularity exec <container> /usr/local/bin/est_abundance.py
$ podman run --it --rm --entrypoint /usr/local/bin/est_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/est_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_kmer_distribution.py

```bash
$ singularity exec <container> /usr/local/bin/generate_kmer_distribution.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_kmer_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_kmer_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k2

```bash
$ singularity exec <container> /usr/local/bin/k2
$ podman run --it --rm --entrypoint /usr/local/bin/k2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer2read_distr

```bash
$ singularity exec <container> /usr/local/bin/kmer2read_distr
$ podman run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metacontam

```bash
$ singularity exec <container> /usr/local/bin/metacontam
$ podman run --it --rm --entrypoint /usr/local/bin/metacontam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metacontam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2

```bash
$ singularity exec <container> /usr/local/bin/kraken2
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-build

```bash
$ singularity exec <container> /usr/local/bin/kraken2-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-inspect

```bash
$ singularity exec <container> /usr/local/bin/kraken2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/pair-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-missing-subranges

```bash
$ singularity exec <container> /usr/local/bin/print-missing-subranges
$ podman run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-by-length

```bash
$ singularity exec <container> /usr/local/bin/sort-by-length
$ podman run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/xcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch

```bash
$ singularity exec <container> /usr/local/bin/xfetch
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch.ini

```bash
$ singularity exec <container> /usr/local/bin/xfetch.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfilter

```bash
$ singularity exec <container> /usr/local/bin/xfilter
$ podman run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xinfo

```bash
$ singularity exec <container> /usr/local/bin/xinfo
$ podman run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink

```bash
$ singularity exec <container> /usr/local/bin/xlink
$ podman run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink.ini

```bash
$ singularity exec <container> /usr/local/bin/xlink.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsearch

```bash
$ singularity exec <container> /usr/local/bin/xsearch
$ podman run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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