---
layout: container
name:  "quay.io/biocontainers/anchorwave"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/anchorwave/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/anchorwave/container.yaml"
updated_at: "2022-10-27 01:11:28.639950"
latest: "1.0.1--hd03093a_1"
container_url: "https://biocontainers.pro/tools/anchorwave"
aliases:
 - "anchorwave"
 - "anchorwave_avx2"
 - "anchorwave_avx512"
 - "anchorwave_sse2"
 - "anchorwave_sse4.1"
 - "bulk-counts"
 - "configure"
 - "gmap.nosimd"
 - "gmap_cat"
 - "gmapl.nosimd"
 - "gsnap.nosimd"
 - "gsnapl.nosimd"
 - "indexdb_cat"
 - "sc-counts"
 - "trindex"
 - "velocity-counts"
versions:
 - "1.0.1--hd03093a_1"
description: "shpc-registry automated BioContainers addition for anchorwave"
config: {"url": "https://biocontainers.pro/tools/anchorwave", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for anchorwave", "latest": {"1.0.1--hd03093a_1": "sha256:e3dadaa9e1be9595a12bca26ec63781261af6f2cb17b3658c55694d392308a1c"}, "tags": {"1.0.1--hd03093a_1": "sha256:e3dadaa9e1be9595a12bca26ec63781261af6f2cb17b3658c55694d392308a1c"}, "docker": "quay.io/biocontainers/anchorwave", "aliases": {"anchorwave": "/usr/local/bin/anchorwave", "anchorwave_avx2": "/usr/local/bin/anchorwave_avx2", "anchorwave_avx512": "/usr/local/bin/anchorwave_avx512", "anchorwave_sse2": "/usr/local/bin/anchorwave_sse2", "anchorwave_sse4.1": "/usr/local/bin/anchorwave_sse4.1", "bulk-counts": "/usr/local/bin/bulk-counts", "configure": "/usr/local/bin/configure", "gmap.nosimd": "/usr/local/bin/gmap.nosimd", "gmap_cat": "/usr/local/bin/gmap_cat", "gmapl.nosimd": "/usr/local/bin/gmapl.nosimd", "gsnap.nosimd": "/usr/local/bin/gsnap.nosimd", "gsnapl.nosimd": "/usr/local/bin/gsnapl.nosimd", "indexdb_cat": "/usr/local/bin/indexdb_cat", "sc-counts": "/usr/local/bin/sc-counts", "trindex": "/usr/local/bin/trindex", "velocity-counts": "/usr/local/bin/velocity-counts"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/anchorwave.
shpc-registry automated BioContainers addition for anchorwave
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/anchorwave
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/anchorwave:1.0.1--hd03093a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/anchorwave/1.0.1--hd03093a_1
$ module help quay.io/biocontainers/anchorwave/1.0.1--hd03093a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### anchorwave-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### anchorwave-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### anchorwave-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### anchorwave-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### anchorwave-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### anchorwave-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anchorwave

```bash
$ singularity exec <container> /usr/local/bin/anchorwave
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_avx2

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_avx2
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_avx512

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_avx512
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_sse2

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_sse2
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_sse2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_sse2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anchorwave_sse4.1

```bash
$ singularity exec <container> /usr/local/bin/anchorwave_sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/anchorwave_sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anchorwave_sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bulk-counts

```bash
$ singularity exec <container> /usr/local/bin/bulk-counts
$ podman run --it --rm --entrypoint /usr/local/bin/bulk-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bulk-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### configure

```bash
$ singularity exec <container> /usr/local/bin/configure
$ podman run --it --rm --entrypoint /usr/local/bin/configure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/configure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_cat

```bash
$ singularity exec <container> /usr/local/bin/gmap_cat
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_cat

```bash
$ singularity exec <container> /usr/local/bin/indexdb_cat
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sc-counts

```bash
$ singularity exec <container> /usr/local/bin/sc-counts
$ podman run --it --rm --entrypoint /usr/local/bin/sc-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sc-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trindex

```bash
$ singularity exec <container> /usr/local/bin/trindex
$ podman run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velocity-counts

```bash
$ singularity exec <container> /usr/local/bin/velocity-counts
$ podman run --it --rm --entrypoint /usr/local/bin/velocity-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velocity-counts   -v ${PWD} -w ${PWD} <container> -c " $@"
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