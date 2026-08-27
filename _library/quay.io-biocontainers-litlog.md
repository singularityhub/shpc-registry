---
layout: container
name:  "quay.io/biocontainers/litlog"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/litlog/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/litlog/container.yaml"
updated_at: "2026-08-27 23:39:46.050783"
latest: "0.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/litlog"
aliases:
 - "convertfilestopdf"
 - "convertfilestops"
 - "convertformat"
 - "convertsegfilestopdf"
 - "convertsegfilestops"
 - "converttopdf"
 - "converttops"
 - "fileinfo"
 - "imagetops"
 - "jbig2dec"
 - "litlog"
 - "mutool"
 - "pymupdf"
 - "tesseract"
 - "xtractprotos"
 - "spirv-diff"
 - "spirv-as"
 - "spirv-cfg"
 - "spirv-dis"
 - "spirv-lesspipe.sh"
 - "spirv-link"
 - "spirv-lint"
 - "spirv-objdump"
 - "spirv-opt"
 - "spirv-reduce"
 - "spirv-val"
 - "bsdunzip"
 - "fc-genconf"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "xslt-config"
 - "xsltproc"
 - "numpy-config"
 - "gif2rgb"
 - "gifbuild"
versions:
 - "0.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for litlog"
config: {"url": "https://biocontainers.pro/tools/litlog", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for litlog", "latest": {"0.1.1--pyhdfd78af_0": "sha256:9ae8b1dd1fe354ad5a0c7a337f3b729895958b74cf4e6a9022aab6702fe537c8"}, "tags": {"0.1.1--pyhdfd78af_0": "sha256:9ae8b1dd1fe354ad5a0c7a337f3b729895958b74cf4e6a9022aab6702fe537c8"}, "docker": "quay.io/biocontainers/litlog", "aliases": {"convertfilestopdf": "/usr/local/bin/convertfilestopdf", "convertfilestops": "/usr/local/bin/convertfilestops", "convertformat": "/usr/local/bin/convertformat", "convertsegfilestopdf": "/usr/local/bin/convertsegfilestopdf", "convertsegfilestops": "/usr/local/bin/convertsegfilestops", "converttopdf": "/usr/local/bin/converttopdf", "converttops": "/usr/local/bin/converttops", "fileinfo": "/usr/local/bin/fileinfo", "imagetops": "/usr/local/bin/imagetops", "jbig2dec": "/usr/local/bin/jbig2dec", "litlog": "/usr/local/bin/litlog", "mutool": "/usr/local/bin/mutool", "pymupdf": "/usr/local/bin/pymupdf", "tesseract": "/usr/local/bin/tesseract", "xtractprotos": "/usr/local/bin/xtractprotos", "spirv-diff": "/usr/local/bin/spirv-diff", "spirv-as": "/usr/local/bin/spirv-as", "spirv-cfg": "/usr/local/bin/spirv-cfg", "spirv-dis": "/usr/local/bin/spirv-dis", "spirv-lesspipe.sh": "/usr/local/bin/spirv-lesspipe.sh", "spirv-link": "/usr/local/bin/spirv-link", "spirv-lint": "/usr/local/bin/spirv-lint", "spirv-objdump": "/usr/local/bin/spirv-objdump", "spirv-opt": "/usr/local/bin/spirv-opt", "spirv-reduce": "/usr/local/bin/spirv-reduce", "spirv-val": "/usr/local/bin/spirv-val", "bsdunzip": "/usr/local/bin/bsdunzip", "fc-genconf": "/usr/local/bin/fc-genconf", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "numpy-config": "/usr/local/bin/numpy-config", "gif2rgb": "/usr/local/bin/gif2rgb", "gifbuild": "/usr/local/bin/gifbuild"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/litlog.
singularity registry hpc automated addition for litlog
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/litlog
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/litlog:0.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/litlog/0.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/litlog/0.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### litlog-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### litlog-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### litlog-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### litlog-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### litlog-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### litlog-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convertfilestopdf

```bash
$ singularity exec <container> /usr/local/bin/convertfilestopdf
$ podman run --it --rm --entrypoint /usr/local/bin/convertfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertfilestops

```bash
$ singularity exec <container> /usr/local/bin/convertfilestops
$ podman run --it --rm --entrypoint /usr/local/bin/convertfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertformat

```bash
$ singularity exec <container> /usr/local/bin/convertformat
$ podman run --it --rm --entrypoint /usr/local/bin/convertformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertsegfilestopdf

```bash
$ singularity exec <container> /usr/local/bin/convertsegfilestopdf
$ podman run --it --rm --entrypoint /usr/local/bin/convertsegfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertsegfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertsegfilestops

```bash
$ singularity exec <container> /usr/local/bin/convertsegfilestops
$ podman run --it --rm --entrypoint /usr/local/bin/convertsegfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertsegfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### converttopdf

```bash
$ singularity exec <container> /usr/local/bin/converttopdf
$ podman run --it --rm --entrypoint /usr/local/bin/converttopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converttopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### converttops

```bash
$ singularity exec <container> /usr/local/bin/converttops
$ podman run --it --rm --entrypoint /usr/local/bin/converttops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converttops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fileinfo

```bash
$ singularity exec <container> /usr/local/bin/fileinfo
$ podman run --it --rm --entrypoint /usr/local/bin/fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagetops

```bash
$ singularity exec <container> /usr/local/bin/imagetops
$ podman run --it --rm --entrypoint /usr/local/bin/imagetops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagetops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jbig2dec

```bash
$ singularity exec <container> /usr/local/bin/jbig2dec
$ podman run --it --rm --entrypoint /usr/local/bin/jbig2dec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jbig2dec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### litlog

```bash
$ singularity exec <container> /usr/local/bin/litlog
$ podman run --it --rm --entrypoint /usr/local/bin/litlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/litlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutool

```bash
$ singularity exec <container> /usr/local/bin/mutool
$ podman run --it --rm --entrypoint /usr/local/bin/mutool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pymupdf

```bash
$ singularity exec <container> /usr/local/bin/pymupdf
$ podman run --it --rm --entrypoint /usr/local/bin/pymupdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pymupdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tesseract

```bash
$ singularity exec <container> /usr/local/bin/tesseract
$ podman run --it --rm --entrypoint /usr/local/bin/tesseract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tesseract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtractprotos

```bash
$ singularity exec <container> /usr/local/bin/xtractprotos
$ podman run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-diff

```bash
$ singularity exec <container> /usr/local/bin/spirv-diff
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-as

```bash
$ singularity exec <container> /usr/local/bin/spirv-as
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-cfg

```bash
$ singularity exec <container> /usr/local/bin/spirv-cfg
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-dis

```bash
$ singularity exec <container> /usr/local/bin/spirv-dis
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-lesspipe.sh

```bash
$ singularity exec <container> /usr/local/bin/spirv-lesspipe.sh
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-lesspipe.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-lesspipe.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-link

```bash
$ singularity exec <container> /usr/local/bin/spirv-link
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-lint

```bash
$ singularity exec <container> /usr/local/bin/spirv-lint
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-objdump

```bash
$ singularity exec <container> /usr/local/bin/spirv-objdump
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-opt

```bash
$ singularity exec <container> /usr/local/bin/spirv-opt
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-reduce

```bash
$ singularity exec <container> /usr/local/bin/spirv-reduce
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-val

```bash
$ singularity exec <container> /usr/local/bin/spirv-val
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-val   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-val   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
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