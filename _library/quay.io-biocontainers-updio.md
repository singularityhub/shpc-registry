---
layout: container
name:  "quay.io/biocontainers/updio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/updio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/updio/container.yaml"
updated_at: "2024-03-20 02:43:07.850030"
latest: "1.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/updio"
aliases:
 - "tab-to-vcf"
 - "updio"
 - "vcf-haplotypes"
 - "fill-aa"
 - "fill-an-ac"
 - "fill-fs"
 - "fill-ref-md5"
 - "vcf-annotate"
 - "vcf-compare"
 - "vcf-concat"
 - "vcf-consensus"
 - "vcf-contrast"
 - "vcf-convert"
 - "vcf-fix-newlines"
 - "vcf-fix-ploidy"
 - "vcf-indel-stats"
 - "vcf-isec"
 - "vcf-merge"
 - "vcf-phased-join"
 - "vcf-query"
 - "vcf-shuffle-cols"
 - "vcf-sort"
 - "vcf-stats"
 - "vcf-subset"
 - "vcf-to-tab"
 - "vcf-tstv"
 - "vcf-validator"
 - "htsfile"
versions:
 - "1.1.0--hdfd78af_0"
description: "singularity registry hpc automated addition for updio"
config: {"url": "https://biocontainers.pro/tools/updio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for updio", "latest": {"1.1.0--hdfd78af_0": "sha256:a2d5411ff8c89eb7f11885004f89ebc2cdd664fdc727759f887067866d138c15"}, "tags": {"1.1.0--hdfd78af_0": "sha256:a2d5411ff8c89eb7f11885004f89ebc2cdd664fdc727759f887067866d138c15"}, "docker": "quay.io/biocontainers/updio", "aliases": {"tab-to-vcf": "/usr/local/bin/tab-to-vcf", "updio": "/usr/local/bin/updio", "vcf-haplotypes": "/usr/local/bin/vcf-haplotypes", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert", "vcf-fix-newlines": "/usr/local/bin/vcf-fix-newlines", "vcf-fix-ploidy": "/usr/local/bin/vcf-fix-ploidy", "vcf-indel-stats": "/usr/local/bin/vcf-indel-stats", "vcf-isec": "/usr/local/bin/vcf-isec", "vcf-merge": "/usr/local/bin/vcf-merge", "vcf-phased-join": "/usr/local/bin/vcf-phased-join", "vcf-query": "/usr/local/bin/vcf-query", "vcf-shuffle-cols": "/usr/local/bin/vcf-shuffle-cols", "vcf-sort": "/usr/local/bin/vcf-sort", "vcf-stats": "/usr/local/bin/vcf-stats", "vcf-subset": "/usr/local/bin/vcf-subset", "vcf-to-tab": "/usr/local/bin/vcf-to-tab", "vcf-tstv": "/usr/local/bin/vcf-tstv", "vcf-validator": "/usr/local/bin/vcf-validator", "htsfile": "/usr/local/bin/htsfile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/updio.
singularity registry hpc automated addition for updio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/updio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/updio:1.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/updio/1.1.0--hdfd78af_0
$ module help quay.io/biocontainers/updio/1.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### updio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### updio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### updio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### updio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### updio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### updio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tab-to-vcf

```bash
$ singularity exec <container> /usr/local/bin/tab-to-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### updio

```bash
$ singularity exec <container> /usr/local/bin/updio
$ podman run --it --rm --entrypoint /usr/local/bin/updio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/updio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-haplotypes

```bash
$ singularity exec <container> /usr/local/bin/vcf-haplotypes
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-aa

```bash
$ singularity exec <container> /usr/local/bin/fill-aa
$ podman run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-an-ac

```bash
$ singularity exec <container> /usr/local/bin/fill-an-ac
$ podman run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-fs

```bash
$ singularity exec <container> /usr/local/bin/fill-fs
$ podman run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-ref-md5

```bash
$ singularity exec <container> /usr/local/bin/fill-ref-md5
$ podman run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-annotate

```bash
$ singularity exec <container> /usr/local/bin/vcf-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-compare

```bash
$ singularity exec <container> /usr/local/bin/vcf-compare
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-concat

```bash
$ singularity exec <container> /usr/local/bin/vcf-concat
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-consensus

```bash
$ singularity exec <container> /usr/local/bin/vcf-consensus
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-contrast

```bash
$ singularity exec <container> /usr/local/bin/vcf-contrast
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-convert

```bash
$ singularity exec <container> /usr/local/bin/vcf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-fix-newlines

```bash
$ singularity exec <container> /usr/local/bin/vcf-fix-newlines
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-fix-newlines   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-fix-newlines   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-fix-ploidy

```bash
$ singularity exec <container> /usr/local/bin/vcf-fix-ploidy
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-fix-ploidy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-fix-ploidy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-indel-stats

```bash
$ singularity exec <container> /usr/local/bin/vcf-indel-stats
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-indel-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-indel-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-isec

```bash
$ singularity exec <container> /usr/local/bin/vcf-isec
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-isec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-isec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-merge

```bash
$ singularity exec <container> /usr/local/bin/vcf-merge
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-phased-join

```bash
$ singularity exec <container> /usr/local/bin/vcf-phased-join
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-phased-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-phased-join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-query

```bash
$ singularity exec <container> /usr/local/bin/vcf-query
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-query   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-query   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-shuffle-cols

```bash
$ singularity exec <container> /usr/local/bin/vcf-shuffle-cols
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-shuffle-cols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-shuffle-cols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-sort

```bash
$ singularity exec <container> /usr/local/bin/vcf-sort
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-stats

```bash
$ singularity exec <container> /usr/local/bin/vcf-stats
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-subset

```bash
$ singularity exec <container> /usr/local/bin/vcf-subset
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-to-tab

```bash
$ singularity exec <container> /usr/local/bin/vcf-to-tab
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-to-tab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-to-tab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-tstv

```bash
$ singularity exec <container> /usr/local/bin/vcf-tstv
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-tstv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-tstv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-validator

```bash
$ singularity exec <container> /usr/local/bin/vcf-validator
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
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