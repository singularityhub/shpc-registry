---
layout: container
name:  "quay.io/biocontainers/krakenuniq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/krakenuniq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/krakenuniq/container.yaml"
updated_at: "2023-05-02 03:00:29.202105"
latest: "1.0.3--pl5321h19e8d03_1"
container_url: "https://biocontainers.pro/tools/krakenuniq"
aliases:
 - "build_taxdb"
 - "krakenuniq"
 - "krakenuniq-build"
 - "krakenuniq-download"
 - "krakenuniq-extract-reads"
 - "krakenuniq-filter"
 - "krakenuniq-mpa-report"
 - "krakenuniq-report"
 - "krakenuniq-translate"
 - "read_merger.pl"
 - "rsync-ssl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "tar"
 - "jellyfish"
 - "idn2"
 - "lwp-download"
versions:
 - "1.0.1a--pl5321h19e8d03_1"
 - "1.0.2--pl5321h19e8d03_0"
 - "1.0.3--pl5321h19e8d03_0"
 - "1.0.3--pl5321h19e8d03_1"
description: "shpc-registry automated BioContainers addition for krakenuniq"
config: {"url": "https://biocontainers.pro/tools/krakenuniq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for krakenuniq", "latest": {"1.0.3--pl5321h19e8d03_1": "sha256:0151dc5f74af96a4ed7517efaca66fa233762c14b255ce2d959752a61ecf6c9b"}, "tags": {"1.0.1a--pl5321h19e8d03_1": "sha256:6e3e0ae1accf6002e746fe4bb3de8e81bcb206ceeaf5ee59f0cb299c4a90d11e", "1.0.2--pl5321h19e8d03_0": "sha256:a3c562fab4cb3de4be59b1ed2106486bf1560d0ca2dc2c8ee5c3caf723cb50ab", "1.0.3--pl5321h19e8d03_0": "sha256:5bf112a0169a5b4747d8d939f56b1dc923fdddc73d3eccb6dc64351e761dd16e", "1.0.3--pl5321h19e8d03_1": "sha256:0151dc5f74af96a4ed7517efaca66fa233762c14b255ce2d959752a61ecf6c9b"}, "docker": "quay.io/biocontainers/krakenuniq", "aliases": {"build_taxdb": "/usr/local/bin/build_taxdb", "krakenuniq": "/usr/local/bin/krakenuniq", "krakenuniq-build": "/usr/local/bin/krakenuniq-build", "krakenuniq-download": "/usr/local/bin/krakenuniq-download", "krakenuniq-extract-reads": "/usr/local/bin/krakenuniq-extract-reads", "krakenuniq-filter": "/usr/local/bin/krakenuniq-filter", "krakenuniq-mpa-report": "/usr/local/bin/krakenuniq-mpa-report", "krakenuniq-report": "/usr/local/bin/krakenuniq-report", "krakenuniq-translate": "/usr/local/bin/krakenuniq-translate", "read_merger.pl": "/usr/local/bin/read_merger.pl", "rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "tar": "/usr/local/bin/tar", "jellyfish": "/usr/local/bin/jellyfish", "idn2": "/usr/local/bin/idn2", "lwp-download": "/usr/local/bin/lwp-download"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/krakenuniq.
shpc-registry automated BioContainers addition for krakenuniq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/krakenuniq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/krakenuniq:1.0.3--pl5321h19e8d03_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/krakenuniq/1.0.3--pl5321h19e8d03_1
$ module help quay.io/biocontainers/krakenuniq/1.0.3--pl5321h19e8d03_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### krakenuniq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### krakenuniq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### krakenuniq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### krakenuniq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### krakenuniq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### krakenuniq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### build_taxdb

```bash
$ singularity exec <container> /usr/local/bin/build_taxdb
$ podman run --it --rm --entrypoint /usr/local/bin/build_taxdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_taxdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq-build

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq-build
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq-download

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq-download
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq-extract-reads

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq-extract-reads
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq-extract-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq-extract-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq-filter

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq-filter
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq-report

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq-report
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenuniq-translate

```bash
$ singularity exec <container> /usr/local/bin/krakenuniq-translate
$ podman run --it --rm --entrypoint /usr/local/bin/krakenuniq-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenuniq-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_merger.pl

```bash
$ singularity exec <container> /usr/local/bin/read_merger.pl
$ podman run --it --rm --entrypoint /usr/local/bin/read_merger.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_merger.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-download

```bash
$ singularity exec <container> /usr/local/bin/lwp-download
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
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