---
layout: container
name:  "quay.io/biocontainers/fanc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fanc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fanc/container.yaml"
updated_at: "2023-05-23 03:15:23.599523"
latest: "0.9.23b--py37h8902056_2"
container_url: "https://biocontainers.pro/tools/fanc"
aliases:
 - "calc-prorate"
 - "cheroot"
 - "cherryd"
 - "convert-regions"
 - "fanc"
 - "fancplot"
 - "gridmap_web"
 - "tiff2fsspec"
 - "tiffcomment"
 - "JxrDecApp"
 - "JxrEncApp"
 - "cbrunsli"
 - "dbrunsli"
 - "imagecodecs"
 - "lsm2bin"
 - "tifffile"
 - "zfp"
 - "zopfli"
 - "zopflipng"
versions:
 - "0.9.23b--py37h8902056_2"
description: "shpc-registry automated BioContainers addition for fanc"
config: {"url": "https://biocontainers.pro/tools/fanc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fanc", "latest": {"0.9.23b--py37h8902056_2": "sha256:e020b005bfffab0e8225bc06025050b3f1a14f8302713088a9f519be8b602e19"}, "tags": {"0.9.23b--py37h8902056_2": "sha256:e020b005bfffab0e8225bc06025050b3f1a14f8302713088a9f519be8b602e19"}, "docker": "quay.io/biocontainers/fanc", "aliases": {"calc-prorate": "/usr/local/bin/calc-prorate", "cheroot": "/usr/local/bin/cheroot", "cherryd": "/usr/local/bin/cherryd", "convert-regions": "/usr/local/bin/convert-regions", "fanc": "/usr/local/bin/fanc", "fancplot": "/usr/local/bin/fancplot", "gridmap_web": "/usr/local/bin/gridmap_web", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "tiffcomment": "/usr/local/bin/tiffcomment", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "cbrunsli": "/usr/local/bin/cbrunsli", "dbrunsli": "/usr/local/bin/dbrunsli", "imagecodecs": "/usr/local/bin/imagecodecs", "lsm2bin": "/usr/local/bin/lsm2bin", "tifffile": "/usr/local/bin/tifffile", "zfp": "/usr/local/bin/zfp", "zopfli": "/usr/local/bin/zopfli", "zopflipng": "/usr/local/bin/zopflipng"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fanc.
shpc-registry automated BioContainers addition for fanc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fanc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fanc:0.9.23b--py37h8902056_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fanc/0.9.23b--py37h8902056_2
$ module help quay.io/biocontainers/fanc/0.9.23b--py37h8902056_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fanc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fanc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fanc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fanc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fanc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fanc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### calc-prorate

```bash
$ singularity exec <container> /usr/local/bin/calc-prorate
$ podman run --it --rm --entrypoint /usr/local/bin/calc-prorate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calc-prorate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheroot

```bash
$ singularity exec <container> /usr/local/bin/cheroot
$ podman run --it --rm --entrypoint /usr/local/bin/cheroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cherryd

```bash
$ singularity exec <container> /usr/local/bin/cherryd
$ podman run --it --rm --entrypoint /usr/local/bin/cherryd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cherryd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-regions

```bash
$ singularity exec <container> /usr/local/bin/convert-regions
$ podman run --it --rm --entrypoint /usr/local/bin/convert-regions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-regions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fanc

```bash
$ singularity exec <container> /usr/local/bin/fanc
$ podman run --it --rm --entrypoint /usr/local/bin/fanc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fanc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fancplot

```bash
$ singularity exec <container> /usr/local/bin/fancplot
$ podman run --it --rm --entrypoint /usr/local/bin/fancplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fancplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gridmap_web

```bash
$ singularity exec <container> /usr/local/bin/gridmap_web
$ podman run --it --rm --entrypoint /usr/local/bin/gridmap_web   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gridmap_web   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcomment

```bash
$ singularity exec <container> /usr/local/bin/tiffcomment
$ podman run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrDecApp

```bash
$ singularity exec <container> /usr/local/bin/JxrDecApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrEncApp

```bash
$ singularity exec <container> /usr/local/bin/JxrEncApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbrunsli

```bash
$ singularity exec <container> /usr/local/bin/cbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbrunsli

```bash
$ singularity exec <container> /usr/local/bin/dbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagecodecs

```bash
$ singularity exec <container> /usr/local/bin/imagecodecs
$ podman run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsm2bin

```bash
$ singularity exec <container> /usr/local/bin/lsm2bin
$ podman run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tifffile

```bash
$ singularity exec <container> /usr/local/bin/tifffile
$ podman run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfp

```bash
$ singularity exec <container> /usr/local/bin/zfp
$ podman run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopfli

```bash
$ singularity exec <container> /usr/local/bin/zopfli
$ podman run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopflipng

```bash
$ singularity exec <container> /usr/local/bin/zopflipng
$ podman run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
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