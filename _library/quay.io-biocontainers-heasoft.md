---
layout: container
name:  "quay.io/biocontainers/heasoft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/heasoft/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/heasoft/container.yaml"
updated_at: "2026-01-26 04:03:40.337127"
latest: "6.35.2--hedafe93_1"
container_url: "https://biocontainers.pro/tools/heasoft"
aliases:
 - "debugpy"
 - "debugpy-adapter"
 - "fits2bitmap"
 - "fitscheck"
 - "fitsdiff"
 - "fitsheader"
 - "fitsinfo"
 - "h2benchmark"
 - "ld"
 - "protoc-29.3.0"
 - "protoc-gen-upb"
 - "protoc-gen-upb-29.3.0"
 - "protoc-gen-upb_minitable"
 - "protoc-gen-upb_minitable-29.3.0"
 - "protoc-gen-upbdefs"
 - "protoc-gen-upbdefs-29.3.0"
 - "samp_hub"
 - "showtable"
 - "showtable-astropy"
 - "volint"
 - "wcslint"
 - "checksum-profile"
 - "elastishadow"
 - "h5fuse"
 - "dask"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
 - "mqtt5canary"
 - "curve_keygen"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "gflags_completions.sh"
 - "ipython3"
 - "ipython"
versions:
 - "6.35.1--hedafe93_0"
 - "6.35.1--hedafe93_1"
 - "6.35.2--hedafe93_0"
 - "6.35.2--hedafe93_1"
description: "singularity registry hpc automated addition for heasoft"
config: {"url": "https://biocontainers.pro/tools/heasoft", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for heasoft", "latest": {"6.35.2--hedafe93_1": "sha256:7b401e9248501bfa0d62e612c84d6ce84d283acd336d36b5651e0879690408be"}, "tags": {"6.35.1--hedafe93_0": "sha256:aa88c37a6fce696755d4895454999dfebdbdcf2f666bf3851fe5c3159edcd729", "6.35.1--hedafe93_1": "sha256:8389346bf6257140cd4a61cee8e0daed572c5c48b844abc641d59742ef2241ff", "6.35.2--hedafe93_0": "sha256:78c138c6331b22562310352b5272fe4fc4c1dd02ef52b4d9479c08fcb8e2a162", "6.35.2--hedafe93_1": "sha256:7b401e9248501bfa0d62e612c84d6ce84d283acd336d36b5651e0879690408be"}, "docker": "quay.io/biocontainers/heasoft", "aliases": {"debugpy": "/usr/local/bin/debugpy", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "fits2bitmap": "/usr/local/bin/fits2bitmap", "fitscheck": "/usr/local/bin/fitscheck", "fitsdiff": "/usr/local/bin/fitsdiff", "fitsheader": "/usr/local/bin/fitsheader", "fitsinfo": "/usr/local/bin/fitsinfo", "h2benchmark": "/usr/local/bin/h2benchmark", "ld": "/usr/local/bin/ld", "protoc-29.3.0": "/usr/local/bin/protoc-29.3.0", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upb-29.3.0": "/usr/local/bin/protoc-gen-upb-29.3.0", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "protoc-gen-upb_minitable-29.3.0": "/usr/local/bin/protoc-gen-upb_minitable-29.3.0", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "protoc-gen-upbdefs-29.3.0": "/usr/local/bin/protoc-gen-upbdefs-29.3.0", "samp_hub": "/usr/local/bin/samp_hub", "showtable": "/usr/local/bin/showtable", "showtable-astropy": "/usr/local/bin/showtable-astropy", "volint": "/usr/local/bin/volint", "wcslint": "/usr/local/bin/wcslint", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "h5fuse": "/usr/local/bin/h5fuse", "dask": "/usr/local/bin/dask", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary", "mqtt5canary": "/usr/local/bin/mqtt5canary", "curve_keygen": "/usr/local/bin/curve_keygen", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/heasoft.
singularity registry hpc automated addition for heasoft
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/heasoft
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/heasoft:6.35.2--hedafe93_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/heasoft/6.35.2--hedafe93_1
$ module help quay.io/biocontainers/heasoft/6.35.2--hedafe93_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### heasoft-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### heasoft-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### heasoft-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### heasoft-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### heasoft-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### heasoft-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fits2bitmap

```bash
$ singularity exec <container> /usr/local/bin/fits2bitmap
$ podman run --it --rm --entrypoint /usr/local/bin/fits2bitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fits2bitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitscheck

```bash
$ singularity exec <container> /usr/local/bin/fitscheck
$ podman run --it --rm --entrypoint /usr/local/bin/fitscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsdiff

```bash
$ singularity exec <container> /usr/local/bin/fitsdiff
$ podman run --it --rm --entrypoint /usr/local/bin/fitsdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsheader

```bash
$ singularity exec <container> /usr/local/bin/fitsheader
$ podman run --it --rm --entrypoint /usr/local/bin/fitsheader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsheader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsinfo

```bash
$ singularity exec <container> /usr/local/bin/fitsinfo
$ podman run --it --rm --entrypoint /usr/local/bin/fitsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld

```bash
$ singularity exec <container> /usr/local/bin/ld
$ podman run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samp_hub

```bash
$ singularity exec <container> /usr/local/bin/samp_hub
$ podman run --it --rm --entrypoint /usr/local/bin/samp_hub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samp_hub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### showtable

```bash
$ singularity exec <container> /usr/local/bin/showtable
$ podman run --it --rm --entrypoint /usr/local/bin/showtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/showtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### showtable-astropy

```bash
$ singularity exec <container> /usr/local/bin/showtable-astropy
$ podman run --it --rm --entrypoint /usr/local/bin/showtable-astropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/showtable-astropy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### volint

```bash
$ singularity exec <container> /usr/local/bin/volint
$ podman run --it --rm --entrypoint /usr/local/bin/volint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/volint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wcslint

```bash
$ singularity exec <container> /usr/local/bin/wcslint
$ podman run --it --rm --entrypoint /usr/local/bin/wcslint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wcslint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask

```bash
$ singularity exec <container> /usr/local/bin/dask
$ podman run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-run

```bash
$ singularity exec <container> /usr/local/bin/jupyter-run
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub5

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub5
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_app

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_app
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-contents

```bash
$ singularity exec <container> /usr/local/bin/orc-contents
$ podman run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-metadata

```bash
$ singularity exec <container> /usr/local/bin/orc-metadata
$ podman run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-statistics

```bash
$ singularity exec <container> /usr/local/bin/orc-statistics
$ podman run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
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