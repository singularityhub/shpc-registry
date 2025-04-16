---
layout: container
name:  "quay.io/biocontainers/bioconductor-bioga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bioga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bioga/container.yaml"
updated_at: "2025-04-16 05:35:25.616058"
latest: "1.0.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bioga"
aliases:
 - "cllayerinfo"
 - "dec265"
 - "protoc-28.2.0"
 - "wayland-scanner"
 - "vpxdec"
 - "vpxenc"
 - "x265"
 - "ffmpeg"
 - "ffprobe"
 - "h264dec"
 - "h264enc"
 - "x264"
 - "rav1e"
 - "pandoc-lua"
 - "SvtAv1EncApp"
 - "dav1d"
 - "aomdec"
 - "aomenc"
 - "x86_64-conda-linux-gnu.cfg"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "pandoc-server"
 - "lame"
 - "x86_64-conda-linux-gnu-pkg-config"
 - "Magick++-config"
 - "MagickCore-config"
 - "MagickWand-config"
versions:
 - "1.0.0--r44he5774e6_0"
description: "singularity registry hpc automated addition for bioconductor-bioga"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bioga", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-bioga", "latest": {"1.0.0--r44he5774e6_0": "sha256:bb721aebeca4c0f1b8f843ffd861ee337eaaed07bae1f234302aea18b30edc6d"}, "tags": {"1.0.0--r44he5774e6_0": "sha256:bb721aebeca4c0f1b8f843ffd861ee337eaaed07bae1f234302aea18b30edc6d"}, "docker": "quay.io/biocontainers/bioconductor-bioga", "aliases": {"cllayerinfo": "/usr/local/bin/cllayerinfo", "dec265": "/usr/local/bin/dec265", "protoc-28.2.0": "/usr/local/bin/protoc-28.2.0", "wayland-scanner": "/usr/local/bin/wayland-scanner", "vpxdec": "/usr/local/bin/vpxdec", "vpxenc": "/usr/local/bin/vpxenc", "x265": "/usr/local/bin/x265", "ffmpeg": "/usr/local/bin/ffmpeg", "ffprobe": "/usr/local/bin/ffprobe", "h264dec": "/usr/local/bin/h264dec", "h264enc": "/usr/local/bin/h264enc", "x264": "/usr/local/bin/x264", "rav1e": "/usr/local/bin/rav1e", "pandoc-lua": "/usr/local/bin/pandoc-lua", "SvtAv1EncApp": "/usr/local/bin/SvtAv1EncApp", "dav1d": "/usr/local/bin/dav1d", "aomdec": "/usr/local/bin/aomdec", "aomenc": "/usr/local/bin/aomenc", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "pandoc-server": "/usr/local/bin/pandoc-server", "lame": "/usr/local/bin/lame", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bioga.
singularity registry hpc automated addition for bioconductor-bioga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bioga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bioga:1.0.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bioga/1.0.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-bioga/1.0.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bioga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bioga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bioga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bioga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cllayerinfo

```bash
$ singularity exec <container> /usr/local/bin/cllayerinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dec265

```bash
$ singularity exec <container> /usr/local/bin/dec265
$ podman run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.2.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.2.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### x265

```bash
$ singularity exec <container> /usr/local/bin/x265
$ podman run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### rav1e

```bash
$ singularity exec <container> /usr/local/bin/rav1e
$ podman run --it --rm --entrypoint /usr/local/bin/rav1e   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rav1e   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lame

```bash
$ singularity exec <container> /usr/local/bin/lame
$ podman run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Magick++-config

```bash
$ singularity exec <container> /usr/local/bin/Magick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickCore-config

```bash
$ singularity exec <container> /usr/local/bin/MagickCore-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickWand-config

```bash
$ singularity exec <container> /usr/local/bin/MagickWand-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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