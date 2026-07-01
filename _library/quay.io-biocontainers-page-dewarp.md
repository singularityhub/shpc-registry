---
layout: container
name:  "quay.io/biocontainers/page-dewarp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/page-dewarp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/page-dewarp/container.yaml"
updated_at: "2026-07-01 15:24:56.512323"
latest: "0.2.7"
container_url: "https://biocontainers.pro/tools/page-dewarp"
aliases:
 - "glslang"
 - "glslangValidator"
 - "glslc"
 - "kmap2qmap6"
 - "lcheck6"
 - "lconvert6"
 - "lrelease-pro6"
 - "lrelease6"
 - "ltext2id6"
 - "lupdate-pro6"
 - "lupdate6"
 - "page-dewarp"
 - "spirv-diff"
 - "wasmdeployqt6"
 - "exrmanifest"
 - "exrmetrics"
 - "exr2aces"
 - "exrenvmap"
 - "exrheader"
 - "exrinfo"
 - "exrmakepreview"
 - "exrmaketiled"
 - "exrmultipart"
 - "exrmultiview"
 - "exrstdattr"
 - "ojph_compress"
 - "ojph_expand"
 - "ffplay"
 - "sdl2-config"
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
versions:
 - "0.2.7"
description: "singularity registry hpc automated addition for page-dewarp"
config: {"url": "https://biocontainers.pro/tools/page-dewarp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for page-dewarp", "latest": {"0.2.7": "sha256:fa900602ecf828eb4f07b031c015c95101e7fc00f00f73ec35c44d4cafae7ace"}, "tags": {"0.2.7": "sha256:fa900602ecf828eb4f07b031c015c95101e7fc00f00f73ec35c44d4cafae7ace"}, "docker": "quay.io/biocontainers/page-dewarp", "aliases": {"glslang": "/usr/local/bin/glslang", "glslangValidator": "/usr/local/bin/glslangValidator", "glslc": "/usr/local/bin/glslc", "kmap2qmap6": "/usr/local/bin/kmap2qmap6", "lcheck6": "/usr/local/bin/lcheck6", "lconvert6": "/usr/local/bin/lconvert6", "lrelease-pro6": "/usr/local/bin/lrelease-pro6", "lrelease6": "/usr/local/bin/lrelease6", "ltext2id6": "/usr/local/bin/ltext2id6", "lupdate-pro6": "/usr/local/bin/lupdate-pro6", "lupdate6": "/usr/local/bin/lupdate6", "page-dewarp": "/usr/local/bin/page-dewarp", "spirv-diff": "/usr/local/bin/spirv-diff", "wasmdeployqt6": "/usr/local/bin/wasmdeployqt6", "exrmanifest": "/usr/local/bin/exrmanifest", "exrmetrics": "/usr/local/bin/exrmetrics", "exr2aces": "/usr/local/bin/exr2aces", "exrenvmap": "/usr/local/bin/exrenvmap", "exrheader": "/usr/local/bin/exrheader", "exrinfo": "/usr/local/bin/exrinfo", "exrmakepreview": "/usr/local/bin/exrmakepreview", "exrmaketiled": "/usr/local/bin/exrmaketiled", "exrmultipart": "/usr/local/bin/exrmultipart", "exrmultiview": "/usr/local/bin/exrmultiview", "exrstdattr": "/usr/local/bin/exrstdattr", "ojph_compress": "/usr/local/bin/ojph_compress", "ojph_expand": "/usr/local/bin/ojph_expand", "ffplay": "/usr/local/bin/ffplay", "sdl2-config": "/usr/local/bin/sdl2-config", "spirv-as": "/usr/local/bin/spirv-as", "spirv-cfg": "/usr/local/bin/spirv-cfg", "spirv-dis": "/usr/local/bin/spirv-dis", "spirv-lesspipe.sh": "/usr/local/bin/spirv-lesspipe.sh", "spirv-link": "/usr/local/bin/spirv-link", "spirv-lint": "/usr/local/bin/spirv-lint", "spirv-objdump": "/usr/local/bin/spirv-objdump", "spirv-opt": "/usr/local/bin/spirv-opt", "spirv-reduce": "/usr/local/bin/spirv-reduce", "spirv-val": "/usr/local/bin/spirv-val"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/page-dewarp.
singularity registry hpc automated addition for page-dewarp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/page-dewarp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/page-dewarp:0.2.7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/page-dewarp/0.2.7
$ module help quay.io/biocontainers/page-dewarp/0.2.7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### page-dewarp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### page-dewarp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### page-dewarp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### page-dewarp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### page-dewarp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### page-dewarp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glslang

```bash
$ singularity exec <container> /usr/local/bin/glslang
$ podman run --it --rm --entrypoint /usr/local/bin/glslang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glslang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glslangValidator

```bash
$ singularity exec <container> /usr/local/bin/glslangValidator
$ podman run --it --rm --entrypoint /usr/local/bin/glslangValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glslangValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glslc

```bash
$ singularity exec <container> /usr/local/bin/glslc
$ podman run --it --rm --entrypoint /usr/local/bin/glslc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glslc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmap2qmap6

```bash
$ singularity exec <container> /usr/local/bin/kmap2qmap6
$ podman run --it --rm --entrypoint /usr/local/bin/kmap2qmap6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmap2qmap6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lcheck6

```bash
$ singularity exec <container> /usr/local/bin/lcheck6
$ podman run --it --rm --entrypoint /usr/local/bin/lcheck6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lcheck6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lconvert6

```bash
$ singularity exec <container> /usr/local/bin/lconvert6
$ podman run --it --rm --entrypoint /usr/local/bin/lconvert6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lconvert6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease-pro6

```bash
$ singularity exec <container> /usr/local/bin/lrelease-pro6
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease6

```bash
$ singularity exec <container> /usr/local/bin/lrelease6
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ltext2id6

```bash
$ singularity exec <container> /usr/local/bin/ltext2id6
$ podman run --it --rm --entrypoint /usr/local/bin/ltext2id6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ltext2id6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate-pro6

```bash
$ singularity exec <container> /usr/local/bin/lupdate-pro6
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate6

```bash
$ singularity exec <container> /usr/local/bin/lupdate6
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### page-dewarp

```bash
$ singularity exec <container> /usr/local/bin/page-dewarp
$ podman run --it --rm --entrypoint /usr/local/bin/page-dewarp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/page-dewarp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-diff

```bash
$ singularity exec <container> /usr/local/bin/spirv-diff
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wasmdeployqt6

```bash
$ singularity exec <container> /usr/local/bin/wasmdeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/wasmdeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wasmdeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmanifest

```bash
$ singularity exec <container> /usr/local/bin/exrmanifest
$ podman run --it --rm --entrypoint /usr/local/bin/exrmanifest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmanifest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmetrics

```bash
$ singularity exec <container> /usr/local/bin/exrmetrics
$ podman run --it --rm --entrypoint /usr/local/bin/exrmetrics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmetrics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exr2aces

```bash
$ singularity exec <container> /usr/local/bin/exr2aces
$ podman run --it --rm --entrypoint /usr/local/bin/exr2aces   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exr2aces   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrenvmap

```bash
$ singularity exec <container> /usr/local/bin/exrenvmap
$ podman run --it --rm --entrypoint /usr/local/bin/exrenvmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrenvmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrheader

```bash
$ singularity exec <container> /usr/local/bin/exrheader
$ podman run --it --rm --entrypoint /usr/local/bin/exrheader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrheader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrinfo

```bash
$ singularity exec <container> /usr/local/bin/exrinfo
$ podman run --it --rm --entrypoint /usr/local/bin/exrinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmakepreview

```bash
$ singularity exec <container> /usr/local/bin/exrmakepreview
$ podman run --it --rm --entrypoint /usr/local/bin/exrmakepreview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmakepreview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmaketiled

```bash
$ singularity exec <container> /usr/local/bin/exrmaketiled
$ podman run --it --rm --entrypoint /usr/local/bin/exrmaketiled   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmaketiled   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmultipart

```bash
$ singularity exec <container> /usr/local/bin/exrmultipart
$ podman run --it --rm --entrypoint /usr/local/bin/exrmultipart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmultipart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrmultiview

```bash
$ singularity exec <container> /usr/local/bin/exrmultiview
$ podman run --it --rm --entrypoint /usr/local/bin/exrmultiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrmultiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exrstdattr

```bash
$ singularity exec <container> /usr/local/bin/exrstdattr
$ podman run --it --rm --entrypoint /usr/local/bin/exrstdattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exrstdattr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ffplay

```bash
$ singularity exec <container> /usr/local/bin/ffplay
$ podman run --it --rm --entrypoint /usr/local/bin/ffplay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffplay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdl2-config

```bash
$ singularity exec <container> /usr/local/bin/sdl2-config
$ podman run --it --rm --entrypoint /usr/local/bin/sdl2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdl2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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