---
layout: container
name:  "quay.io/biocontainers/new-fave"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/new-fave/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/new-fave/container.yaml"
updated_at: "2026-10-10 19:32:35.644346"
latest: "1.3.0"
container_url: "https://biocontainers.pro/tools/new-fave"
aliases:
 - "fasttrack"
 - "fave-extract"
 - "fave_recode"
 - "filetype"
 - "cffi-gen-src"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "out123"
 - "idna"
 - "lame"
 - "flac"
 - "metaflac"
 - "sndfile-cmp"
 - "sndfile-concat"
 - "sndfile-convert"
 - "sndfile-deinterleave"
 - "sndfile-info"
 - "sndfile-interleave"
 - "sndfile-metadata-get"
 - "sndfile-metadata-set"
 - "sndfile-play"
 - "sndfile-salvage"
 - "fc-genconf"
 - "numba"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
versions:
 - "1.3.0"
description: "singularity registry hpc automated addition for new-fave"
config: {"url": "https://biocontainers.pro/tools/new-fave", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for new-fave", "latest": {"1.3.0": "sha256:5911dc9f7b9c374b0b6af632964c64c0eeef56276c2e014ad2f95abe5f1cf0c9"}, "tags": {"1.3.0": "sha256:5911dc9f7b9c374b0b6af632964c64c0eeef56276c2e014ad2f95abe5f1cf0c9"}, "docker": "quay.io/biocontainers/new-fave", "aliases": {"fasttrack": "/usr/local/bin/fasttrack", "fave-extract": "/usr/local/bin/fave-extract", "fave_recode": "/usr/local/bin/fave_recode", "filetype": "/usr/local/bin/filetype", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "out123": "/usr/local/bin/out123", "idna": "/usr/local/bin/idna", "lame": "/usr/local/bin/lame", "flac": "/usr/local/bin/flac", "metaflac": "/usr/local/bin/metaflac", "sndfile-cmp": "/usr/local/bin/sndfile-cmp", "sndfile-concat": "/usr/local/bin/sndfile-concat", "sndfile-convert": "/usr/local/bin/sndfile-convert", "sndfile-deinterleave": "/usr/local/bin/sndfile-deinterleave", "sndfile-info": "/usr/local/bin/sndfile-info", "sndfile-interleave": "/usr/local/bin/sndfile-interleave", "sndfile-metadata-get": "/usr/local/bin/sndfile-metadata-get", "sndfile-metadata-set": "/usr/local/bin/sndfile-metadata-set", "sndfile-play": "/usr/local/bin/sndfile-play", "sndfile-salvage": "/usr/local/bin/sndfile-salvage", "fc-genconf": "/usr/local/bin/fc-genconf", "numba": "/usr/local/bin/numba", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/new-fave.
singularity registry hpc automated addition for new-fave
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/new-fave
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/new-fave:1.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/new-fave/1.3.0
$ module help quay.io/biocontainers/new-fave/1.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### new-fave-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### new-fave-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### new-fave-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### new-fave-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### new-fave-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### new-fave-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasttrack

```bash
$ singularity exec <container> /usr/local/bin/fasttrack
$ podman run --it --rm --entrypoint /usr/local/bin/fasttrack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttrack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fave-extract

```bash
$ singularity exec <container> /usr/local/bin/fave-extract
$ podman run --it --rm --entrypoint /usr/local/bin/fave-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fave-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fave_recode

```bash
$ singularity exec <container> /usr/local/bin/fave_recode
$ podman run --it --rm --entrypoint /usr/local/bin/fave_recode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fave_recode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filetype

```bash
$ singularity exec <container> /usr/local/bin/filetype
$ podman run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123

```bash
$ singularity exec <container> /usr/local/bin/mpg123
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-id3dump

```bash
$ singularity exec <container> /usr/local/bin/mpg123-id3dump
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-strip

```bash
$ singularity exec <container> /usr/local/bin/mpg123-strip
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### out123

```bash
$ singularity exec <container> /usr/local/bin/out123
$ podman run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lame

```bash
$ singularity exec <container> /usr/local/bin/lame
$ podman run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flac

```bash
$ singularity exec <container> /usr/local/bin/flac
$ podman run --it --rm --entrypoint /usr/local/bin/flac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaflac

```bash
$ singularity exec <container> /usr/local/bin/metaflac
$ podman run --it --rm --entrypoint /usr/local/bin/metaflac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaflac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-cmp

```bash
$ singularity exec <container> /usr/local/bin/sndfile-cmp
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-concat

```bash
$ singularity exec <container> /usr/local/bin/sndfile-concat
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-convert

```bash
$ singularity exec <container> /usr/local/bin/sndfile-convert
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-deinterleave

```bash
$ singularity exec <container> /usr/local/bin/sndfile-deinterleave
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-deinterleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-deinterleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-info

```bash
$ singularity exec <container> /usr/local/bin/sndfile-info
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-interleave

```bash
$ singularity exec <container> /usr/local/bin/sndfile-interleave
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-metadata-get

```bash
$ singularity exec <container> /usr/local/bin/sndfile-metadata-get
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-metadata-set

```bash
$ singularity exec <container> /usr/local/bin/sndfile-metadata-set
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-set   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-play

```bash
$ singularity exec <container> /usr/local/bin/sndfile-play
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-play   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-play   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-salvage

```bash
$ singularity exec <container> /usr/local/bin/sndfile-salvage
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-salvage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-salvage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
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