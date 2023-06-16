---
layout: container
name:  "quay.io/biocontainers/targetdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/targetdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/targetdb/container.yaml"
updated_at: "2023-06-16 02:50:03.151269"
latest: "1.3.1--pyh864c0ab_0"
container_url: "https://biocontainers.pro/tools/targetdb"
aliases:
 - "dpocket"
 - "ffmpeg"
 - "ffprobe"
 - "fpocket"
 - "h264dec"
 - "h264enc"
 - "hyper"
 - "imgcmp"
 - "imginfo"
 - "jasper"
 - "lame"
 - "mdpocket"
 - "opencv_annotation"
 - "opencv_interactive-calibration"
 - "opencv_version"
 - "opencv_visualisation"
 - "opencv_waldboost_detector"
 - "setup_vars_opencv4.sh"
 - "targetDB"
 - "target_DB"
 - "tmrdemo"
 - "tpocket"
 - "x264"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
 - "nettle-hash"
 - "nettle-lfib-stream"
 - "nettle-pbkdf2"
 - "ocsptool"
 - "pkcs1-conv"
 - "psktool"
versions:
 - "1.3.1--pyh864c0ab_0"
description: "shpc-registry automated BioContainers addition for targetdb"
config: {"url": "https://biocontainers.pro/tools/targetdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for targetdb", "latest": {"1.3.1--pyh864c0ab_0": "sha256:4a523b0f824316de7958ed1221b19ed581d71fb9ccef85fadc65e6a10c4ace46"}, "tags": {"1.3.1--pyh864c0ab_0": "sha256:4a523b0f824316de7958ed1221b19ed581d71fb9ccef85fadc65e6a10c4ace46"}, "docker": "quay.io/biocontainers/targetdb", "aliases": {"dpocket": "/usr/local/bin/dpocket", "ffmpeg": "/usr/local/bin/ffmpeg", "ffprobe": "/usr/local/bin/ffprobe", "fpocket": "/usr/local/bin/fpocket", "h264dec": "/usr/local/bin/h264dec", "h264enc": "/usr/local/bin/h264enc", "hyper": "/usr/local/bin/hyper", "imgcmp": "/usr/local/bin/imgcmp", "imginfo": "/usr/local/bin/imginfo", "jasper": "/usr/local/bin/jasper", "lame": "/usr/local/bin/lame", "mdpocket": "/usr/local/bin/mdpocket", "opencv_annotation": "/usr/local/bin/opencv_annotation", "opencv_interactive-calibration": "/usr/local/bin/opencv_interactive-calibration", "opencv_version": "/usr/local/bin/opencv_version", "opencv_visualisation": "/usr/local/bin/opencv_visualisation", "opencv_waldboost_detector": "/usr/local/bin/opencv_waldboost_detector", "setup_vars_opencv4.sh": "/usr/local/bin/setup_vars_opencv4.sh", "targetDB": "/usr/local/bin/targetDB", "target_DB": "/usr/local/bin/target_DB", "tmrdemo": "/usr/local/bin/tmrdemo", "tpocket": "/usr/local/bin/tpocket", "x264": "/usr/local/bin/x264", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv", "nettle-hash": "/usr/local/bin/nettle-hash", "nettle-lfib-stream": "/usr/local/bin/nettle-lfib-stream", "nettle-pbkdf2": "/usr/local/bin/nettle-pbkdf2", "ocsptool": "/usr/local/bin/ocsptool", "pkcs1-conv": "/usr/local/bin/pkcs1-conv", "psktool": "/usr/local/bin/psktool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/targetdb.
shpc-registry automated BioContainers addition for targetdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/targetdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/targetdb:1.3.1--pyh864c0ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/targetdb/1.3.1--pyh864c0ab_0
$ module help quay.io/biocontainers/targetdb/1.3.1--pyh864c0ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### targetdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### targetdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### targetdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### targetdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### targetdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### targetdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dpocket

```bash
$ singularity exec <container> /usr/local/bin/dpocket
$ podman run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fpocket

```bash
$ singularity exec <container> /usr/local/bin/fpocket
$ podman run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hyper

```bash
$ singularity exec <container> /usr/local/bin/hyper
$ podman run --it --rm --entrypoint /usr/local/bin/hyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imgcmp

```bash
$ singularity exec <container> /usr/local/bin/imgcmp
$ podman run --it --rm --entrypoint /usr/local/bin/imgcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imgcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imginfo

```bash
$ singularity exec <container> /usr/local/bin/imginfo
$ podman run --it --rm --entrypoint /usr/local/bin/imginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jasper

```bash
$ singularity exec <container> /usr/local/bin/jasper
$ podman run --it --rm --entrypoint /usr/local/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lame

```bash
$ singularity exec <container> /usr/local/bin/lame
$ podman run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdpocket

```bash
$ singularity exec <container> /usr/local/bin/mdpocket
$ podman run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_annotation

```bash
$ singularity exec <container> /usr/local/bin/opencv_annotation
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_interactive-calibration

```bash
$ singularity exec <container> /usr/local/bin/opencv_interactive-calibration
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_interactive-calibration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_interactive-calibration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_version

```bash
$ singularity exec <container> /usr/local/bin/opencv_version
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_visualisation

```bash
$ singularity exec <container> /usr/local/bin/opencv_visualisation
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_visualisation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_visualisation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opencv_waldboost_detector

```bash
$ singularity exec <container> /usr/local/bin/opencv_waldboost_detector
$ podman run --it --rm --entrypoint /usr/local/bin/opencv_waldboost_detector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opencv_waldboost_detector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup_vars_opencv4.sh

```bash
$ singularity exec <container> /usr/local/bin/setup_vars_opencv4.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup_vars_opencv4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### targetDB

```bash
$ singularity exec <container> /usr/local/bin/targetDB
$ podman run --it --rm --entrypoint /usr/local/bin/targetDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/targetDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### target_DB

```bash
$ singularity exec <container> /usr/local/bin/target_DB
$ podman run --it --rm --entrypoint /usr/local/bin/target_DB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/target_DB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tmrdemo

```bash
$ singularity exec <container> /usr/local/bin/tmrdemo
$ podman run --it --rm --entrypoint /usr/local/bin/tmrdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tmrdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpocket

```bash
$ singularity exec <container> /usr/local/bin/tpocket
$ podman run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x264

```bash
$ singularity exec <container> /usr/local/bin/x264
$ podman run --it --rm --entrypoint /usr/local/bin/x264   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x264   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### nettle-lfib-stream

```bash
$ singularity exec <container> /usr/local/bin/nettle-lfib-stream
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-lfib-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nettle-pbkdf2

```bash
$ singularity exec <container> /usr/local/bin/nettle-pbkdf2
$ podman run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nettle-pbkdf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocsptool

```bash
$ singularity exec <container> /usr/local/bin/ocsptool
$ podman run --it --rm --entrypoint /usr/local/bin/ocsptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocsptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkcs1-conv

```bash
$ singularity exec <container> /usr/local/bin/pkcs1-conv
$ podman run --it --rm --entrypoint /usr/local/bin/pkcs1-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkcs1-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psktool

```bash
$ singularity exec <container> /usr/local/bin/psktool
$ podman run --it --rm --entrypoint /usr/local/bin/psktool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psktool   -v ${PWD} -w ${PWD} <container> -c " $@"
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