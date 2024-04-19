---
layout: container
name:  "ghcr.io/autamus/libtiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/libtiff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/libtiff/container.yaml"
updated_at: "2024-04-19 03:11:27.364499"
latest: "4.4.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/libtiff"
aliases:
 - "fax2tiff"
 - "ppm2tiff"
 - "raw2tiff"
 - "tiff2bw"
 - "tiff2pdf"
 - "tiff2ps"
 - "tiff2rgba"
 - "tiffcmp"
 - "tiffcp"
 - "tiffcrop"
 - "tiffdither"
 - "tiffdump"
 - "tiffinfo"
 - "tiffmedian"
 - "tiffset"
 - "tiffsplit"
versions:
 - "4.1.0"
 - "4.3.0"
 - "latest"
 - "4.2.0"
 - "4.4.0"
description: "Libtiff is a library for reading and writing Tagged Image File Format (abbreviated TIFF) files."
config: {"docker": "ghcr.io/autamus/libtiff", "url": "https://github.com/orgs/autamus/packages/container/package/libtiff", "maintainer": "@vsoch", "description": "Libtiff is a library for reading and writing Tagged Image File Format (abbreviated TIFF) files.", "latest": {"4.4.0": "sha256:2775f8fea7aa5f16cf5a9b16ec4e79918c0418e8dcacc8ccac177c5d0c9ff073"}, "tags": {"4.1.0": "sha256:9b7046a7f1aeda65bbdd29587e89dc56c0831ee82e377591030ee340de2245fb", "4.3.0": "sha256:3502e639d185e196d1cb79fb751d290b9a5c69ca596f8635a8b976567b8ee29d", "latest": "sha256:2775f8fea7aa5f16cf5a9b16ec4e79918c0418e8dcacc8ccac177c5d0c9ff073", "4.2.0": "sha256:5e31be7f2575232321b0237b5adaf809bf5a6df2e2c87ff3b55a48dd87f6d145", "4.4.0": "sha256:2775f8fea7aa5f16cf5a9b16ec4e79918c0418e8dcacc8ccac177c5d0c9ff073"}, "aliases": {"fax2tiff": "/opt/view/bin/fax2tiff", "ppm2tiff": "/opt/view/bin/ppm2tiff", "raw2tiff": "/opt/view/bin/raw2tiff", "tiff2bw": "/opt/view/bin/tiff2bw", "tiff2pdf": "/opt/view/bin/tiff2pdf", "tiff2ps": "/opt/view/bin/tiff2ps", "tiff2rgba": "/opt/view/bin/tiff2rgba", "tiffcmp": "/opt/view/bin/tiffcmp", "tiffcp": "/opt/view/bin/tiffcp", "tiffcrop": "/opt/view/bin/tiffcrop", "tiffdither": "/opt/view/bin/tiffdither", "tiffdump": "/opt/view/bin/tiffdump", "tiffinfo": "/opt/view/bin/tiffinfo", "tiffmedian": "/opt/view/bin/tiffmedian", "tiffset": "/opt/view/bin/tiffset", "tiffsplit": "/opt/view/bin/tiffsplit"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/libtiff.
Libtiff is a library for reading and writing Tagged Image File Format (abbreviated TIFF) files.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/libtiff
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libtiff:4.4.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libtiff/4.4.0
$ module help ghcr.io/autamus/libtiff/4.4.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libtiff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libtiff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libtiff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libtiff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libtiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libtiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fax2tiff

```bash
$ singularity exec <container> /opt/view/bin/fax2tiff
$ podman run --it --rm --entrypoint /opt/view/bin/fax2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/fax2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppm2tiff

```bash
$ singularity exec <container> /opt/view/bin/ppm2tiff
$ podman run --it --rm --entrypoint /opt/view/bin/ppm2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ppm2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raw2tiff

```bash
$ singularity exec <container> /opt/view/bin/raw2tiff
$ podman run --it --rm --entrypoint /opt/view/bin/raw2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/raw2tiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2bw

```bash
$ singularity exec <container> /opt/view/bin/tiff2bw
$ podman run --it --rm --entrypoint /opt/view/bin/tiff2bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiff2bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2pdf

```bash
$ singularity exec <container> /opt/view/bin/tiff2pdf
$ podman run --it --rm --entrypoint /opt/view/bin/tiff2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiff2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2ps

```bash
$ singularity exec <container> /opt/view/bin/tiff2ps
$ podman run --it --rm --entrypoint /opt/view/bin/tiff2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiff2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2rgba

```bash
$ singularity exec <container> /opt/view/bin/tiff2rgba
$ podman run --it --rm --entrypoint /opt/view/bin/tiff2rgba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiff2rgba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcmp

```bash
$ singularity exec <container> /opt/view/bin/tiffcmp
$ podman run --it --rm --entrypoint /opt/view/bin/tiffcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcp

```bash
$ singularity exec <container> /opt/view/bin/tiffcp
$ podman run --it --rm --entrypoint /opt/view/bin/tiffcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcrop

```bash
$ singularity exec <container> /opt/view/bin/tiffcrop
$ podman run --it --rm --entrypoint /opt/view/bin/tiffcrop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffcrop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffdither

```bash
$ singularity exec <container> /opt/view/bin/tiffdither
$ podman run --it --rm --entrypoint /opt/view/bin/tiffdither   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffdither   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffdump

```bash
$ singularity exec <container> /opt/view/bin/tiffdump
$ podman run --it --rm --entrypoint /opt/view/bin/tiffdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffinfo

```bash
$ singularity exec <container> /opt/view/bin/tiffinfo
$ podman run --it --rm --entrypoint /opt/view/bin/tiffinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffmedian

```bash
$ singularity exec <container> /opt/view/bin/tiffmedian
$ podman run --it --rm --entrypoint /opt/view/bin/tiffmedian   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffmedian   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffset

```bash
$ singularity exec <container> /opt/view/bin/tiffset
$ podman run --it --rm --entrypoint /opt/view/bin/tiffset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffsplit

```bash
$ singularity exec <container> /opt/view/bin/tiffsplit
$ podman run --it --rm --entrypoint /opt/view/bin/tiffsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/tiffsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
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