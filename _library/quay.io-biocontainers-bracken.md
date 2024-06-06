---
layout: container
name:  "quay.io/biocontainers/bracken"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bracken/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bracken/container.yaml"
updated_at: "2024-06-06 02:53:38.954220"
latest: "2.9--py39h1f90b4d_0"
container_url: "https://biocontainers.pro/tools/bracken"
aliases:
 - "bracken"
 - "bracken-build"
 - "combine_bracken_outputs.py"
 - "est_abundance.py"
 - "generate_kmer_distribution.py"
 - "kmer2read_distr"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "rsync-ssl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "tar"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
versions:
 - "2.6.2--py39hc16433a_0"
 - "2.9--py39h1f90b4d_0"
 - "2.8--py310h0dbaff4_1"
 - "2.7--py310h30d9df9_0"
 - "2.6.2--py27hc30c61c_0"
description: "shpc-registry automated BioContainers addition for bracken"
config: {"url": "https://biocontainers.pro/tools/bracken", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bracken", "latest": {"2.9--py39h1f90b4d_0": "sha256:4451c195fd98e803a73e3a10827535524647be8467cd6529e2f59c4995dfa560"}, "tags": {"2.6.2--py39hc16433a_0": "sha256:d9f1cf7dc3630e00bb4689532b94db774cdf0c0855ac5a9c8c85a8f4301bc237", "2.9--py39h1f90b4d_0": "sha256:4451c195fd98e803a73e3a10827535524647be8467cd6529e2f59c4995dfa560", "2.8--py310h0dbaff4_1": "sha256:a90025a7544dce6e41e6a680bd1364ea10594a456933cc520d19ab975436ec3f", "2.7--py310h30d9df9_0": "sha256:d274711096f8d9016885ad9aaaf2502c5b56f307d2a74018c981309ea8a1e1c7", "2.6.2--py27hc30c61c_0": "sha256:19ed676ef28c3c07f17eb05fc276b500fdcb698adae68b73b76498907f13a7fb"}, "docker": "quay.io/biocontainers/bracken", "aliases": {"bracken": "/usr/local/bin/bracken", "bracken-build": "/usr/local/bin/bracken-build", "combine_bracken_outputs.py": "/usr/local/bin/combine_bracken_outputs.py", "est_abundance.py": "/usr/local/bin/est_abundance.py", "generate_kmer_distribution.py": "/usr/local/bin/generate_kmer_distribution.py", "kmer2read_distr": "/usr/local/bin/kmer2read_distr", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "tar": "/usr/local/bin/tar", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bracken.
shpc-registry automated BioContainers addition for bracken
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bracken
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bracken:2.9--py39h1f90b4d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bracken/2.9--py39h1f90b4d_0
$ module help quay.io/biocontainers/bracken/2.9--py39h1f90b4d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bracken-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bracken-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bracken-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bracken-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bracken-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bracken-inspect-deffile:

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


#### kmer2read_distr

```bash
$ singularity exec <container> /usr/local/bin/kmer2read_distr
$ podman run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
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