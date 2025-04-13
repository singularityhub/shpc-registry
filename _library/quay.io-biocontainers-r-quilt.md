---
layout: container
name:  "quay.io/biocontainers/r-quilt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-quilt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-quilt/container.yaml"
updated_at: "2025-04-13 04:09:52.172149"
latest: "2.0.1--r44h503566f_1"
container_url: "https://biocontainers.pro/tools/r-quilt"
aliases:
 - "rsync-ssl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "ace2sam"
 - "blast2sam.pl"
versions:
 - "1.0.3--r41h37595e4_1"
 - "1.0.3--r42h37595e4_2"
 - "1.0.4--r42h06b5641_1"
 - "1.0.4--r43h06b5641_2"
 - "1.0.5--r43h06b5641_0"
 - "2.0.0--r43hdbdd923_2"
 - "2.0.1--r43hdbdd923_0"
 - "2.0.1--r44h503566f_1"
description: "shpc-registry automated BioContainers addition for r-quilt"
config: {"url": "https://biocontainers.pro/tools/r-quilt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-quilt", "latest": {"2.0.1--r44h503566f_1": "sha256:b4b199a831e4a3ab717021e9590f94e288134c172f9d41d11f49fb4c3dc11a6a"}, "tags": {"1.0.3--r41h37595e4_1": "sha256:4ec3832600d461ffee36114ed456f8803099dc7bd7b72f3a1e2488dca438a6d8", "1.0.3--r42h37595e4_2": "sha256:43a24b0514a9bb760b0807a47374d0e5075c0d67230de33596442b492c7b89b8", "1.0.4--r42h06b5641_1": "sha256:98dcce673878992becc18bc82902c85ad47a388077369ffe7982c06ee564541c", "1.0.4--r43h06b5641_2": "sha256:70a42844d82cd0c5bb8dd8ad1c3f537f7a6527b5cf8986a8c8d7cc12f810fc72", "1.0.5--r43h06b5641_0": "sha256:53f513cd3325c6f890bc71a60624e2f2b16e182d16cde38ff5ead7bef868657d", "2.0.0--r43hdbdd923_2": "sha256:43322e829dca64581ed73751aae9631315bacdf6b6aa38d11853c232041c6f0d", "2.0.1--r43hdbdd923_0": "sha256:b2c0604023befc78c0fb9d7ce26301d03f48aac0eca3e0fe81b3d7a0d061b074", "2.0.1--r44h503566f_1": "sha256:b4b199a831e4a3ab717021e9590f94e288134c172f9d41d11f49fb4c3dc11a6a"}, "docker": "quay.io/biocontainers/r-quilt", "aliases": {"rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-quilt.
shpc-registry automated BioContainers addition for r-quilt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-quilt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-quilt:2.0.1--r44h503566f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-quilt/2.0.1--r44h503566f_1
$ module help quay.io/biocontainers/r-quilt/2.0.1--r44h503566f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-quilt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-quilt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-quilt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-quilt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-quilt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-quilt-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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