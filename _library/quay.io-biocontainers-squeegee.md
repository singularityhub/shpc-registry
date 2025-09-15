---
layout: container
name:  "quay.io/biocontainers/squeegee"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/squeegee/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/squeegee/container.yaml"
updated_at: "2025-09-15 03:29:36.497737"
latest: "0.2.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/squeegee"
aliases:
 - "existDB"
 - "kmer-mask"
 - "kraken"
 - "kraken-build"
 - "kraken-filter"
 - "kraken-mpa-report"
 - "kraken-report"
 - "kraken-translate"
 - "mapMers"
 - "mapMers-depth"
 - "mt19937ar-test"
 - "positionDB"
 - "simple"
 - "squeegee"
 - "test-merStream"
 - "test-seqCache"
 - "test-seqStream"
 - "rsync-ssl"
 - "meryl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "tar"
 - "capnp"
 - "capnpc"
versions:
 - "0.2.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for squeegee"
config: {"url": "https://biocontainers.pro/tools/squeegee", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for squeegee", "latest": {"0.2.0--hdfd78af_0": "sha256:57e9d7d23a3edd00031d62968539ea71e2e01409a151d1264730da3b13b84025"}, "tags": {"0.2.0--hdfd78af_0": "sha256:57e9d7d23a3edd00031d62968539ea71e2e01409a151d1264730da3b13b84025"}, "docker": "quay.io/biocontainers/squeegee", "aliases": {"existDB": "/usr/local/bin/existDB", "kmer-mask": "/usr/local/bin/kmer-mask", "kraken": "/usr/local/bin/kraken", "kraken-build": "/usr/local/bin/kraken-build", "kraken-filter": "/usr/local/bin/kraken-filter", "kraken-mpa-report": "/usr/local/bin/kraken-mpa-report", "kraken-report": "/usr/local/bin/kraken-report", "kraken-translate": "/usr/local/bin/kraken-translate", "mapMers": "/usr/local/bin/mapMers", "mapMers-depth": "/usr/local/bin/mapMers-depth", "mt19937ar-test": "/usr/local/bin/mt19937ar-test", "positionDB": "/usr/local/bin/positionDB", "simple": "/usr/local/bin/simple", "squeegee": "/usr/local/bin/squeegee", "test-merStream": "/usr/local/bin/test-merStream", "test-seqCache": "/usr/local/bin/test-seqCache", "test-seqStream": "/usr/local/bin/test-seqStream", "rsync-ssl": "/usr/local/bin/rsync-ssl", "meryl": "/usr/local/bin/meryl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "tar": "/usr/local/bin/tar", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/squeegee.
shpc-registry automated BioContainers addition for squeegee
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/squeegee
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/squeegee:0.2.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/squeegee/0.2.0--hdfd78af_0
$ module help quay.io/biocontainers/squeegee/0.2.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### squeegee-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### squeegee-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### squeegee-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### squeegee-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### squeegee-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### squeegee-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### existDB

```bash
$ singularity exec <container> /usr/local/bin/existDB
$ podman run --it --rm --entrypoint /usr/local/bin/existDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/existDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer-mask

```bash
$ singularity exec <container> /usr/local/bin/kmer-mask
$ podman run --it --rm --entrypoint /usr/local/bin/kmer-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken

```bash
$ singularity exec <container> /usr/local/bin/kraken
$ podman run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-build

```bash
$ singularity exec <container> /usr/local/bin/kraken-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-filter

```bash
$ singularity exec <container> /usr/local/bin/kraken-filter
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-translate

```bash
$ singularity exec <container> /usr/local/bin/kraken-translate
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapMers

```bash
$ singularity exec <container> /usr/local/bin/mapMers
$ podman run --it --rm --entrypoint /usr/local/bin/mapMers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapMers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapMers-depth

```bash
$ singularity exec <container> /usr/local/bin/mapMers-depth
$ podman run --it --rm --entrypoint /usr/local/bin/mapMers-depth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapMers-depth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mt19937ar-test

```bash
$ singularity exec <container> /usr/local/bin/mt19937ar-test
$ podman run --it --rm --entrypoint /usr/local/bin/mt19937ar-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mt19937ar-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### positionDB

```bash
$ singularity exec <container> /usr/local/bin/positionDB
$ podman run --it --rm --entrypoint /usr/local/bin/positionDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/positionDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simple

```bash
$ singularity exec <container> /usr/local/bin/simple
$ podman run --it --rm --entrypoint /usr/local/bin/simple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### squeegee

```bash
$ singularity exec <container> /usr/local/bin/squeegee
$ podman run --it --rm --entrypoint /usr/local/bin/squeegee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/squeegee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-merStream

```bash
$ singularity exec <container> /usr/local/bin/test-merStream
$ podman run --it --rm --entrypoint /usr/local/bin/test-merStream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-merStream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-seqCache

```bash
$ singularity exec <container> /usr/local/bin/test-seqCache
$ podman run --it --rm --entrypoint /usr/local/bin/test-seqCache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-seqCache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-seqStream

```bash
$ singularity exec <container> /usr/local/bin/test-seqStream
$ podman run --it --rm --entrypoint /usr/local/bin/test-seqStream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-seqStream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl

```bash
$ singularity exec <container> /usr/local/bin/meryl
$ podman run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
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