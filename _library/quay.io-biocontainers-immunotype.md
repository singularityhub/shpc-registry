---
layout: container
name:  "quay.io/biocontainers/immunotype"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/immunotype/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/immunotype/container.yaml"
updated_at: "2026-05-02 06:03:58.323020"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/immunotype"
aliases:
 - "email_validator"
 - "fastapi"
 - "glslang"
 - "glslangValidator"
 - "glslc"
 - "gradio"
 - "hf"
 - "hf-gradio"
 - "immunotype"
 - "immunotype-app"
 - "ruff"
 - "spirv-diff"
 - "upload_theme"
 - "uvicorn"
 - "watchfiles"
 - "websockets"
 - "tiny-agents"
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
 - "xxh3sum"
 - "protoc-33.5.0"
 - "protoc-gen-upb-33.5.0"
 - "protoc-gen-upb_minitable-33.5.0"
 - "protoc-gen-upbdefs-33.5.0"
 - "cllayerinfo"
 - "vpxdec"
 - "vpxenc"
 - "ffmpeg"
 - "ffprobe"
 - "h264dec"
 - "h264enc"
versions:
 - "1.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for immunotype"
config: {"url": "https://biocontainers.pro/tools/immunotype", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for immunotype", "latest": {"1.0.2--pyhdfd78af_0": "sha256:07bb3b4ec03ae3728ba2b71401390c21b907899851c9cd3456e4aa0316f315d0"}, "tags": {"1.0.2--pyhdfd78af_0": "sha256:07bb3b4ec03ae3728ba2b71401390c21b907899851c9cd3456e4aa0316f315d0"}, "docker": "quay.io/biocontainers/immunotype", "aliases": {"email_validator": "/usr/local/bin/email_validator", "fastapi": "/usr/local/bin/fastapi", "glslang": "/usr/local/bin/glslang", "glslangValidator": "/usr/local/bin/glslangValidator", "glslc": "/usr/local/bin/glslc", "gradio": "/usr/local/bin/gradio", "hf": "/usr/local/bin/hf", "hf-gradio": "/usr/local/bin/hf-gradio", "immunotype": "/usr/local/bin/immunotype", "immunotype-app": "/usr/local/bin/immunotype-app", "ruff": "/usr/local/bin/ruff", "spirv-diff": "/usr/local/bin/spirv-diff", "upload_theme": "/usr/local/bin/upload_theme", "uvicorn": "/usr/local/bin/uvicorn", "watchfiles": "/usr/local/bin/watchfiles", "websockets": "/usr/local/bin/websockets", "tiny-agents": "/usr/local/bin/tiny-agents", "ffplay": "/usr/local/bin/ffplay", "sdl2-config": "/usr/local/bin/sdl2-config", "spirv-as": "/usr/local/bin/spirv-as", "spirv-cfg": "/usr/local/bin/spirv-cfg", "spirv-dis": "/usr/local/bin/spirv-dis", "spirv-lesspipe.sh": "/usr/local/bin/spirv-lesspipe.sh", "spirv-link": "/usr/local/bin/spirv-link", "spirv-lint": "/usr/local/bin/spirv-lint", "spirv-objdump": "/usr/local/bin/spirv-objdump", "spirv-opt": "/usr/local/bin/spirv-opt", "spirv-reduce": "/usr/local/bin/spirv-reduce", "spirv-val": "/usr/local/bin/spirv-val", "xxh3sum": "/usr/local/bin/xxh3sum", "protoc-33.5.0": "/usr/local/bin/protoc-33.5.0", "protoc-gen-upb-33.5.0": "/usr/local/bin/protoc-gen-upb-33.5.0", "protoc-gen-upb_minitable-33.5.0": "/usr/local/bin/protoc-gen-upb_minitable-33.5.0", "protoc-gen-upbdefs-33.5.0": "/usr/local/bin/protoc-gen-upbdefs-33.5.0", "cllayerinfo": "/usr/local/bin/cllayerinfo", "vpxdec": "/usr/local/bin/vpxdec", "vpxenc": "/usr/local/bin/vpxenc", "ffmpeg": "/usr/local/bin/ffmpeg", "ffprobe": "/usr/local/bin/ffprobe", "h264dec": "/usr/local/bin/h264dec", "h264enc": "/usr/local/bin/h264enc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/immunotype.
singularity registry hpc automated addition for immunotype
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/immunotype
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/immunotype:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/immunotype/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/immunotype/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### immunotype-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### immunotype-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### immunotype-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### immunotype-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### immunotype-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### immunotype-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### email_validator

```bash
$ singularity exec <container> /usr/local/bin/email_validator
$ podman run --it --rm --entrypoint /usr/local/bin/email_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/email_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastapi

```bash
$ singularity exec <container> /usr/local/bin/fastapi
$ podman run --it --rm --entrypoint /usr/local/bin/fastapi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastapi   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gradio

```bash
$ singularity exec <container> /usr/local/bin/gradio
$ podman run --it --rm --entrypoint /usr/local/bin/gradio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gradio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hf

```bash
$ singularity exec <container> /usr/local/bin/hf
$ podman run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hf-gradio

```bash
$ singularity exec <container> /usr/local/bin/hf-gradio
$ podman run --it --rm --entrypoint /usr/local/bin/hf-gradio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hf-gradio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### immunotype

```bash
$ singularity exec <container> /usr/local/bin/immunotype
$ podman run --it --rm --entrypoint /usr/local/bin/immunotype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/immunotype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### immunotype-app

```bash
$ singularity exec <container> /usr/local/bin/immunotype-app
$ podman run --it --rm --entrypoint /usr/local/bin/immunotype-app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/immunotype-app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruff

```bash
$ singularity exec <container> /usr/local/bin/ruff
$ podman run --it --rm --entrypoint /usr/local/bin/ruff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-diff

```bash
$ singularity exec <container> /usr/local/bin/spirv-diff
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upload_theme

```bash
$ singularity exec <container> /usr/local/bin/upload_theme
$ podman run --it --rm --entrypoint /usr/local/bin/upload_theme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upload_theme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvicorn

```bash
$ singularity exec <container> /usr/local/bin/uvicorn
$ podman run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchfiles

```bash
$ singularity exec <container> /usr/local/bin/watchfiles
$ podman run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### websockets

```bash
$ singularity exec <container> /usr/local/bin/websockets
$ podman run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiny-agents

```bash
$ singularity exec <container> /usr/local/bin/tiny-agents
$ podman run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cllayerinfo

```bash
$ singularity exec <container> /usr/local/bin/cllayerinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
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