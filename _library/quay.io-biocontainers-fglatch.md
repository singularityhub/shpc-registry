---
layout: container
name:  "quay.io/biocontainers/fglatch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fglatch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fglatch/container.yaml"
updated_at: "2026-06-14 07:04:38.930283"
latest: "0.6.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/fglatch"
aliases:
 - "apython"
 - "binaryornot"
 - "cover"
 - "fglatch"
 - "flyte-cli"
 - "gql-cli"
 - "inv"
 - "invoke"
 - "latch"
 - "lint"
 - "mprof"
 - "publish.py"
 - "pyflyte"
 - "pyflyte-execute"
 - "pyflyte-fast-execute"
 - "pyflyte-map-execute"
 - "watchfiles"
 - "xattr"
 - "cookiecutter"
 - "protoc-29.3.0"
 - "protoc-gen-upb-29.3.0"
 - "protoc-gen-upb_minitable-29.3.0"
 - "protoc-gen-upbdefs-29.3.0"
 - "slugify"
 - "keyring"
 - "wsdump"
 - "get_gprof"
 - "protoc-gen-upb_minitable"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
 - "rst2pseudoxml"
 - "rst2s5"
 - "rst2xetex"
 - "rst2xml"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "get_objgraph"
 - "undill"
 - "jp.py"
versions:
 - "0.6.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for fglatch"
config: {"url": "https://biocontainers.pro/tools/fglatch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fglatch", "latest": {"0.6.0--pyhdfd78af_0": "sha256:2e25916e603a24bb6e8c67480662086d5569ee0308147380a028a77e42106f71"}, "tags": {"0.6.0--pyhdfd78af_0": "sha256:2e25916e603a24bb6e8c67480662086d5569ee0308147380a028a77e42106f71"}, "docker": "quay.io/biocontainers/fglatch", "aliases": {"apython": "/usr/local/bin/apython", "binaryornot": "/usr/local/bin/binaryornot", "cover": "/usr/local/bin/cover", "fglatch": "/usr/local/bin/fglatch", "flyte-cli": "/usr/local/bin/flyte-cli", "gql-cli": "/usr/local/bin/gql-cli", "inv": "/usr/local/bin/inv", "invoke": "/usr/local/bin/invoke", "latch": "/usr/local/bin/latch", "lint": "/usr/local/bin/lint", "mprof": "/usr/local/bin/mprof", "publish.py": "/usr/local/bin/publish.py", "pyflyte": "/usr/local/bin/pyflyte", "pyflyte-execute": "/usr/local/bin/pyflyte-execute", "pyflyte-fast-execute": "/usr/local/bin/pyflyte-fast-execute", "pyflyte-map-execute": "/usr/local/bin/pyflyte-map-execute", "watchfiles": "/usr/local/bin/watchfiles", "xattr": "/usr/local/bin/xattr", "cookiecutter": "/usr/local/bin/cookiecutter", "protoc-29.3.0": "/usr/local/bin/protoc-29.3.0", "protoc-gen-upb-29.3.0": "/usr/local/bin/protoc-gen-upb-29.3.0", "protoc-gen-upb_minitable-29.3.0": "/usr/local/bin/protoc-gen-upb_minitable-29.3.0", "protoc-gen-upbdefs-29.3.0": "/usr/local/bin/protoc-gen-upbdefs-29.3.0", "slugify": "/usr/local/bin/slugify", "keyring": "/usr/local/bin/keyring", "wsdump": "/usr/local/bin/wsdump", "get_gprof": "/usr/local/bin/get_gprof", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt", "rst2pseudoxml": "/usr/local/bin/rst2pseudoxml", "rst2s5": "/usr/local/bin/rst2s5", "rst2xetex": "/usr/local/bin/rst2xetex", "rst2xml": "/usr/local/bin/rst2xml", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "jp.py": "/usr/local/bin/jp.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fglatch.
singularity registry hpc automated addition for fglatch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fglatch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fglatch:0.6.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fglatch/0.6.0--pyhdfd78af_0
$ module help quay.io/biocontainers/fglatch/0.6.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fglatch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fglatch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fglatch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fglatch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fglatch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fglatch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### apython

```bash
$ singularity exec <container> /usr/local/bin/apython
$ podman run --it --rm --entrypoint /usr/local/bin/apython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/apython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binaryornot

```bash
$ singularity exec <container> /usr/local/bin/binaryornot
$ podman run --it --rm --entrypoint /usr/local/bin/binaryornot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binaryornot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cover

```bash
$ singularity exec <container> /usr/local/bin/cover
$ podman run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fglatch

```bash
$ singularity exec <container> /usr/local/bin/fglatch
$ podman run --it --rm --entrypoint /usr/local/bin/fglatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fglatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flyte-cli

```bash
$ singularity exec <container> /usr/local/bin/flyte-cli
$ podman run --it --rm --entrypoint /usr/local/bin/flyte-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flyte-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gql-cli

```bash
$ singularity exec <container> /usr/local/bin/gql-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inv

```bash
$ singularity exec <container> /usr/local/bin/inv
$ podman run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invoke

```bash
$ singularity exec <container> /usr/local/bin/invoke
$ podman run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### latch

```bash
$ singularity exec <container> /usr/local/bin/latch
$ podman run --it --rm --entrypoint /usr/local/bin/latch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/latch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lint

```bash
$ singularity exec <container> /usr/local/bin/lint
$ podman run --it --rm --entrypoint /usr/local/bin/lint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mprof

```bash
$ singularity exec <container> /usr/local/bin/mprof
$ podman run --it --rm --entrypoint /usr/local/bin/mprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### publish.py

```bash
$ singularity exec <container> /usr/local/bin/publish.py
$ podman run --it --rm --entrypoint /usr/local/bin/publish.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/publish.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte

```bash
$ singularity exec <container> /usr/local/bin/pyflyte
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte-execute

```bash
$ singularity exec <container> /usr/local/bin/pyflyte-execute
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte-fast-execute

```bash
$ singularity exec <container> /usr/local/bin/pyflyte-fast-execute
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte-fast-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte-fast-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte-map-execute

```bash
$ singularity exec <container> /usr/local/bin/pyflyte-map-execute
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte-map-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte-map-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchfiles

```bash
$ singularity exec <container> /usr/local/bin/watchfiles
$ podman run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xattr

```bash
$ singularity exec <container> /usr/local/bin/xattr
$ podman run --it --rm --entrypoint /usr/local/bin/xattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cookiecutter

```bash
$ singularity exec <container> /usr/local/bin/cookiecutter
$ podman run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex

```bash
$ singularity exec <container> /usr/local/bin/rst2latex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man

```bash
$ singularity exec <container> /usr/local/bin/rst2man
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt

```bash
$ singularity exec <container> /usr/local/bin/rst2odt
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5

```bash
$ singularity exec <container> /usr/local/bin/rst2s5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml

```bash
$ singularity exec <container> /usr/local/bin/rst2xml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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