---
layout: container
name:  "quay.io/biocontainers/stainwarpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stainwarpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stainwarpy/container.yaml"
updated_at: "2026-02-28 04:30:35.713917"
latest: "0.2.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/stainwarpy"
aliases:
 - "ojph_compress"
 - "ojph_expand"
 - "stainwarpy"
 - "typer"
 - "tiff2fsspec"
 - "tiffcomment"
 - "cbrunsli"
 - "dbrunsli"
 - "imagecodecs"
 - "zfp"
 - "zopfli"
 - "zopflipng"
 - "JxrDecApp"
 - "JxrEncApp"
 - "imageio_download_bin"
 - "imageio_remove_bin"
 - "lsm2bin"
 - "tifffile"
 - "SvtAv1EncApp"
 - "dav1d"
 - "aomdec"
 - "aomenc"
 - "markdown-it"
 - "pygmentize"
 - "numpy-config"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
versions:
 - "0.2.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for stainwarpy"
config: {"url": "https://biocontainers.pro/tools/stainwarpy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for stainwarpy", "latest": {"0.2.4--pyhdfd78af_0": "sha256:bc9f20c31618ca55dfd5d499ff01e8d0dceb7ad4c39d6ddbe7662f237cfaf30a"}, "tags": {"0.2.4--pyhdfd78af_0": "sha256:bc9f20c31618ca55dfd5d499ff01e8d0dceb7ad4c39d6ddbe7662f237cfaf30a"}, "docker": "quay.io/biocontainers/stainwarpy", "aliases": {"ojph_compress": "/usr/local/bin/ojph_compress", "ojph_expand": "/usr/local/bin/ojph_expand", "stainwarpy": "/usr/local/bin/stainwarpy", "typer": "/usr/local/bin/typer", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "tiffcomment": "/usr/local/bin/tiffcomment", "cbrunsli": "/usr/local/bin/cbrunsli", "dbrunsli": "/usr/local/bin/dbrunsli", "imagecodecs": "/usr/local/bin/imagecodecs", "zfp": "/usr/local/bin/zfp", "zopfli": "/usr/local/bin/zopfli", "zopflipng": "/usr/local/bin/zopflipng", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "imageio_download_bin": "/usr/local/bin/imageio_download_bin", "imageio_remove_bin": "/usr/local/bin/imageio_remove_bin", "lsm2bin": "/usr/local/bin/lsm2bin", "tifffile": "/usr/local/bin/tifffile", "SvtAv1EncApp": "/usr/local/bin/SvtAv1EncApp", "dav1d": "/usr/local/bin/dav1d", "aomdec": "/usr/local/bin/aomdec", "aomenc": "/usr/local/bin/aomenc", "markdown-it": "/usr/local/bin/markdown-it", "pygmentize": "/usr/local/bin/pygmentize", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stainwarpy.
singularity registry hpc automated addition for stainwarpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stainwarpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stainwarpy:0.2.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stainwarpy/0.2.4--pyhdfd78af_0
$ module help quay.io/biocontainers/stainwarpy/0.2.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stainwarpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stainwarpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stainwarpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stainwarpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stainwarpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stainwarpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ojph_compress

```bash
$ singularity exec <container> /usr/local/bin/ojph_compress
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ojph_expand

```bash
$ singularity exec <container> /usr/local/bin/ojph_expand
$ podman run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ojph_expand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stainwarpy

```bash
$ singularity exec <container> /usr/local/bin/stainwarpy
$ podman run --it --rm --entrypoint /usr/local/bin/stainwarpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stainwarpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### imageio_download_bin

```bash
$ singularity exec <container> /usr/local/bin/imageio_download_bin
$ podman run --it --rm --entrypoint /usr/local/bin/imageio_download_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imageio_download_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imageio_remove_bin

```bash
$ singularity exec <container> /usr/local/bin/imageio_remove_bin
$ podman run --it --rm --entrypoint /usr/local/bin/imageio_remove_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imageio_remove_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### SvtAv1EncApp

```bash
$ singularity exec <container> /usr/local/bin/SvtAv1EncApp
$ podman run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dav1d

```bash
$ singularity exec <container> /usr/local/bin/dav1d
$ podman run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomdec

```bash
$ singularity exec <container> /usr/local/bin/aomdec
$ podman run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomenc

```bash
$ singularity exec <container> /usr/local/bin/aomenc
$ podman run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
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