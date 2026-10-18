---
layout: container
name:  "quay.io/biocontainers/ms-pred"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ms-pred/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ms-pred/container.yaml"
updated_at: "2026-10-18 07:07:42.970413"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ms-pred"
aliases:
 - "debuginfod-find"
 - "eu-addr2line"
 - "eu-ar"
 - "eu-elfclassify"
 - "eu-elfcmp"
 - "eu-elfcompress"
 - "eu-elflint"
 - "eu-findtextrel"
 - "eu-make-debug-archive"
 - "eu-nm"
 - "eu-objdump"
 - "eu-ranlib"
 - "eu-readelf"
 - "eu-size"
 - "eu-srcfiles"
 - "eu-stack"
 - "eu-strings"
 - "eu-strip"
 - "eu-unstrip"
 - "gdown"
 - "ipdb"
 - "ipdb3"
 - "main_cmd.py"
 - "memray"
 - "memray3.12"
 - "msbuddy"
 - "py-spy"
 - "pygrun"
 - "ray"
 - "tune"
 - "cairosvg"
 - "pathos_connect"
 - "portpicker"
 - "pox"
 - "ppserver"
 - "debugpy-adapter"
 - "virtualenv"
 - "coverage"
 - "debugpy"
 - "cffi-gen-src"
 - "p11-kit"
 - "p11tool"
 - "trust"
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "xxh3sum"
 - "flatc"
 - "protoc-25.3.0"
 - "cllayerinfo"
 - "bsdunzip"
 - "import_pb_to_tensorboard"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for ms-pred"
config: {"url": "https://biocontainers.pro/tools/ms-pred", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ms-pred", "latest": {"1.1.0--pyhdfd78af_0": "sha256:a678e16135b0f6f24bd83bcf7e8ddfa3daea2fdd6708128391e77af7947629ba"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:a678e16135b0f6f24bd83bcf7e8ddfa3daea2fdd6708128391e77af7947629ba"}, "docker": "quay.io/biocontainers/ms-pred", "aliases": {"debuginfod-find": "/usr/local/bin/debuginfod-find", "eu-addr2line": "/usr/local/bin/eu-addr2line", "eu-ar": "/usr/local/bin/eu-ar", "eu-elfclassify": "/usr/local/bin/eu-elfclassify", "eu-elfcmp": "/usr/local/bin/eu-elfcmp", "eu-elfcompress": "/usr/local/bin/eu-elfcompress", "eu-elflint": "/usr/local/bin/eu-elflint", "eu-findtextrel": "/usr/local/bin/eu-findtextrel", "eu-make-debug-archive": "/usr/local/bin/eu-make-debug-archive", "eu-nm": "/usr/local/bin/eu-nm", "eu-objdump": "/usr/local/bin/eu-objdump", "eu-ranlib": "/usr/local/bin/eu-ranlib", "eu-readelf": "/usr/local/bin/eu-readelf", "eu-size": "/usr/local/bin/eu-size", "eu-srcfiles": "/usr/local/bin/eu-srcfiles", "eu-stack": "/usr/local/bin/eu-stack", "eu-strings": "/usr/local/bin/eu-strings", "eu-strip": "/usr/local/bin/eu-strip", "eu-unstrip": "/usr/local/bin/eu-unstrip", "gdown": "/usr/local/bin/gdown", "ipdb": "/usr/local/bin/ipdb", "ipdb3": "/usr/local/bin/ipdb3", "main_cmd.py": "/usr/local/bin/main_cmd.py", "memray": "/usr/local/bin/memray", "memray3.12": "/usr/local/bin/memray3.12", "msbuddy": "/usr/local/bin/msbuddy", "py-spy": "/usr/local/bin/py-spy", "pygrun": "/usr/local/bin/pygrun", "ray": "/usr/local/bin/ray", "tune": "/usr/local/bin/tune", "cairosvg": "/usr/local/bin/cairosvg", "pathos_connect": "/usr/local/bin/pathos_connect", "portpicker": "/usr/local/bin/portpicker", "pox": "/usr/local/bin/pox", "ppserver": "/usr/local/bin/ppserver", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "virtualenv": "/usr/local/bin/virtualenv", "coverage": "/usr/local/bin/coverage", "debugpy": "/usr/local/bin/debugpy", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "trust": "/usr/local/bin/trust", "asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "xxh3sum": "/usr/local/bin/xxh3sum", "flatc": "/usr/local/bin/flatc", "protoc-25.3.0": "/usr/local/bin/protoc-25.3.0", "cllayerinfo": "/usr/local/bin/cllayerinfo", "bsdunzip": "/usr/local/bin/bsdunzip", "import_pb_to_tensorboard": "/usr/local/bin/import_pb_to_tensorboard", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ms-pred.
singularity registry hpc automated addition for ms-pred
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ms-pred
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ms-pred:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ms-pred/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/ms-pred/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ms-pred-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ms-pred-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ms-pred-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ms-pred-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ms-pred-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ms-pred-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### debuginfod-find

```bash
$ singularity exec <container> /usr/local/bin/debuginfod-find
$ podman run --it --rm --entrypoint /usr/local/bin/debuginfod-find   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debuginfod-find   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-addr2line

```bash
$ singularity exec <container> /usr/local/bin/eu-addr2line
$ podman run --it --rm --entrypoint /usr/local/bin/eu-addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-ar

```bash
$ singularity exec <container> /usr/local/bin/eu-ar
$ podman run --it --rm --entrypoint /usr/local/bin/eu-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elfclassify

```bash
$ singularity exec <container> /usr/local/bin/eu-elfclassify
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elfclassify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elfclassify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elfcmp

```bash
$ singularity exec <container> /usr/local/bin/eu-elfcmp
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elfcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elfcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elfcompress

```bash
$ singularity exec <container> /usr/local/bin/eu-elfcompress
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elfcompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elfcompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-elflint

```bash
$ singularity exec <container> /usr/local/bin/eu-elflint
$ podman run --it --rm --entrypoint /usr/local/bin/eu-elflint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-elflint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-findtextrel

```bash
$ singularity exec <container> /usr/local/bin/eu-findtextrel
$ podman run --it --rm --entrypoint /usr/local/bin/eu-findtextrel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-findtextrel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-make-debug-archive

```bash
$ singularity exec <container> /usr/local/bin/eu-make-debug-archive
$ podman run --it --rm --entrypoint /usr/local/bin/eu-make-debug-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-make-debug-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-nm

```bash
$ singularity exec <container> /usr/local/bin/eu-nm
$ podman run --it --rm --entrypoint /usr/local/bin/eu-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-objdump

```bash
$ singularity exec <container> /usr/local/bin/eu-objdump
$ podman run --it --rm --entrypoint /usr/local/bin/eu-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-ranlib

```bash
$ singularity exec <container> /usr/local/bin/eu-ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/eu-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-readelf

```bash
$ singularity exec <container> /usr/local/bin/eu-readelf
$ podman run --it --rm --entrypoint /usr/local/bin/eu-readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-size

```bash
$ singularity exec <container> /usr/local/bin/eu-size
$ podman run --it --rm --entrypoint /usr/local/bin/eu-size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-srcfiles

```bash
$ singularity exec <container> /usr/local/bin/eu-srcfiles
$ podman run --it --rm --entrypoint /usr/local/bin/eu-srcfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-srcfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-stack

```bash
$ singularity exec <container> /usr/local/bin/eu-stack
$ podman run --it --rm --entrypoint /usr/local/bin/eu-stack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-stack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-strings

```bash
$ singularity exec <container> /usr/local/bin/eu-strings
$ podman run --it --rm --entrypoint /usr/local/bin/eu-strings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-strings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-strip

```bash
$ singularity exec <container> /usr/local/bin/eu-strip
$ podman run --it --rm --entrypoint /usr/local/bin/eu-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eu-unstrip

```bash
$ singularity exec <container> /usr/local/bin/eu-unstrip
$ podman run --it --rm --entrypoint /usr/local/bin/eu-unstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eu-unstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdown

```bash
$ singularity exec <container> /usr/local/bin/gdown
$ podman run --it --rm --entrypoint /usr/local/bin/gdown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdown   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipdb

```bash
$ singularity exec <container> /usr/local/bin/ipdb
$ podman run --it --rm --entrypoint /usr/local/bin/ipdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipdb3

```bash
$ singularity exec <container> /usr/local/bin/ipdb3
$ podman run --it --rm --entrypoint /usr/local/bin/ipdb3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipdb3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### main_cmd.py

```bash
$ singularity exec <container> /usr/local/bin/main_cmd.py
$ podman run --it --rm --entrypoint /usr/local/bin/main_cmd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/main_cmd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memray

```bash
$ singularity exec <container> /usr/local/bin/memray
$ podman run --it --rm --entrypoint /usr/local/bin/memray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/memray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memray3.12

```bash
$ singularity exec <container> /usr/local/bin/memray3.12
$ podman run --it --rm --entrypoint /usr/local/bin/memray3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/memray3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msbuddy

```bash
$ singularity exec <container> /usr/local/bin/msbuddy
$ podman run --it --rm --entrypoint /usr/local/bin/msbuddy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msbuddy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py-spy

```bash
$ singularity exec <container> /usr/local/bin/py-spy
$ podman run --it --rm --entrypoint /usr/local/bin/py-spy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py-spy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygrun

```bash
$ singularity exec <container> /usr/local/bin/pygrun
$ podman run --it --rm --entrypoint /usr/local/bin/pygrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ray

```bash
$ singularity exec <container> /usr/local/bin/ray
$ podman run --it --rm --entrypoint /usr/local/bin/ray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tune

```bash
$ singularity exec <container> /usr/local/bin/tune
$ podman run --it --rm --entrypoint /usr/local/bin/tune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathos_connect

```bash
$ singularity exec <container> /usr/local/bin/pathos_connect
$ podman run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathos_connect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### portpicker

```bash
$ singularity exec <container> /usr/local/bin/portpicker
$ podman run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/portpicker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pox

```bash
$ singularity exec <container> /usr/local/bin/pox
$ podman run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppserver

```bash
$ singularity exec <container> /usr/local/bin/ppserver
$ podman run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv

```bash
$ singularity exec <container> /usr/local/bin/virtualenv
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11-kit

```bash
$ singularity exec <container> /usr/local/bin/p11-kit
$ podman run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11tool

```bash
$ singularity exec <container> /usr/local/bin/p11tool
$ podman run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust

```bash
$ singularity exec <container> /usr/local/bin/trust
$ podman run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flatc

```bash
$ singularity exec <container> /usr/local/bin/flatc
$ podman run --it --rm --entrypoint /usr/local/bin/flatc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flatc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-25.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-25.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cllayerinfo

```bash
$ singularity exec <container> /usr/local/bin/cllayerinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### import_pb_to_tensorboard

```bash
$ singularity exec <container> /usr/local/bin/import_pb_to_tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
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