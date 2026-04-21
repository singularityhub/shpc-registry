---
layout: container
name:  "quay.io/biocontainers/euktect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/euktect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/euktect/container.yaml"
updated_at: "2026-04-21 05:14:02.109588"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/euktect"
aliases:
 - "euktect-predict"
 - "euktect-refine"
 - "pygrun"
 - "sacremoses"
 - "datasets-cli"
 - "transformers-cli"
 - "huggingface-cli"
 - "SvtAv1DecApp"
 - "xxh3sum"
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "vpxdec"
 - "vpxenc"
 - "ffmpeg"
 - "ffprobe"
 - "h264dec"
 - "h264enc"
 - "x264"
 - "plasma-store-server"
 - "plasma_store"
 - "get_gprof"
 - "srptool"
 - "ninja"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
versions:
 - "1.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for euktect"
config: {"url": "https://biocontainers.pro/tools/euktect", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for euktect", "latest": {"1.0.0--pyhdfd78af_0": "sha256:e6c91d3a5681d15876af59cbb3519c86fd0381c7928dbfa5ca04563f90daabe1"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:e6c91d3a5681d15876af59cbb3519c86fd0381c7928dbfa5ca04563f90daabe1"}, "docker": "quay.io/biocontainers/euktect", "aliases": {"euktect-predict": "/usr/local/bin/euktect-predict", "euktect-refine": "/usr/local/bin/euktect-refine", "pygrun": "/usr/local/bin/pygrun", "sacremoses": "/usr/local/bin/sacremoses", "datasets-cli": "/usr/local/bin/datasets-cli", "transformers-cli": "/usr/local/bin/transformers-cli", "huggingface-cli": "/usr/local/bin/huggingface-cli", "SvtAv1DecApp": "/usr/local/bin/SvtAv1DecApp", "xxh3sum": "/usr/local/bin/xxh3sum", "asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "vpxdec": "/usr/local/bin/vpxdec", "vpxenc": "/usr/local/bin/vpxenc", "ffmpeg": "/usr/local/bin/ffmpeg", "ffprobe": "/usr/local/bin/ffprobe", "h264dec": "/usr/local/bin/h264dec", "h264enc": "/usr/local/bin/h264enc", "x264": "/usr/local/bin/x264", "plasma-store-server": "/usr/local/bin/plasma-store-server", "plasma_store": "/usr/local/bin/plasma_store", "get_gprof": "/usr/local/bin/get_gprof", "srptool": "/usr/local/bin/srptool", "ninja": "/usr/local/bin/ninja", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/euktect.
singularity registry hpc automated addition for euktect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/euktect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/euktect:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/euktect/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/euktect/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### euktect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### euktect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### euktect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### euktect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### euktect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### euktect-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### euktect-predict

```bash
$ singularity exec <container> /usr/local/bin/euktect-predict
$ podman run --it --rm --entrypoint /usr/local/bin/euktect-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/euktect-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### euktect-refine

```bash
$ singularity exec <container> /usr/local/bin/euktect-refine
$ podman run --it --rm --entrypoint /usr/local/bin/euktect-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/euktect-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygrun

```bash
$ singularity exec <container> /usr/local/bin/pygrun
$ podman run --it --rm --entrypoint /usr/local/bin/pygrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sacremoses

```bash
$ singularity exec <container> /usr/local/bin/sacremoses
$ podman run --it --rm --entrypoint /usr/local/bin/sacremoses   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sacremoses   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets-cli

```bash
$ singularity exec <container> /usr/local/bin/datasets-cli
$ podman run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformers-cli

```bash
$ singularity exec <container> /usr/local/bin/transformers-cli
$ podman run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SvtAv1DecApp

```bash
$ singularity exec <container> /usr/local/bin/SvtAv1DecApp
$ podman run --it --rm --entrypoint /usr/local/bin/SvtAv1DecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SvtAv1DecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Coding

```bash
$ singularity exec <container> /usr/local/bin/asn1Coding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Decoding

```bash
$ singularity exec <container> /usr/local/bin/asn1Decoding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Parser

```bash
$ singularity exec <container> /usr/local/bin/asn1Parser
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vpxdec

```bash
$ singularity exec <container> /usr/local/bin/vpxdec
$ podman run --it --rm --entrypoint /usr/local/bin/vpxdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vpxdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vpxenc

```bash
$ singularity exec <container> /usr/local/bin/vpxenc
$ podman run --it --rm --entrypoint /usr/local/bin/vpxenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vpxenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffmpeg

```bash
$ singularity exec <container> /usr/local/bin/ffmpeg
$ podman run --it --rm --entrypoint /usr/local/bin/ffmpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffmpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffprobe

```bash
$ singularity exec <container> /usr/local/bin/ffprobe
$ podman run --it --rm --entrypoint /usr/local/bin/ffprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h264dec

```bash
$ singularity exec <container> /usr/local/bin/h264dec
$ podman run --it --rm --entrypoint /usr/local/bin/h264dec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h264dec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h264enc

```bash
$ singularity exec <container> /usr/local/bin/h264enc
$ podman run --it --rm --entrypoint /usr/local/bin/h264enc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h264enc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x264

```bash
$ singularity exec <container> /usr/local/bin/x264
$ podman run --it --rm --entrypoint /usr/local/bin/x264   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x264   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma-store-server

```bash
$ singularity exec <container> /usr/local/bin/plasma-store-server
$ podman run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma_store

```bash
$ singularity exec <container> /usr/local/bin/plasma_store
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srptool

```bash
$ singularity exec <container> /usr/local/bin/srptool
$ podman run --it --rm --entrypoint /usr/local/bin/srptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ninja

```bash
$ singularity exec <container> /usr/local/bin/ninja
$ podman run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli-debug

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli-debug
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-serv

```bash
$ singularity exec <container> /usr/local/bin/gnutls-serv
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-hash

```bash
$ singularity exec <container> /usr/local/bin/nettle-hash
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
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