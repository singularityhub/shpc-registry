---
layout: container
name:  "quay.io/biocontainers/oxbreaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oxbreaker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oxbreaker/container.yaml"
updated_at: "2026-06-01 07:13:53.602961"
latest: "1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/oxbreaker"
aliases:
 - "gtk4-builder-tool"
 - "gtk4-demo"
 - "gtk4-demo-application"
 - "gtk4-encode-symbolic-svg"
 - "gtk4-icon-editor"
 - "gtk4-image-tool"
 - "gtk4-launch"
 - "gtk4-node-editor"
 - "gtk4-path-tool"
 - "gtk4-print-editor"
 - "gtk4-query-settings"
 - "gtk4-rendernode-tool"
 - "gtk4-update-icon-cache"
 - "gtk4-widget-factory"
 - "oxbreaker"
 - "nextflow"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "hb-raster"
 - "hb-vector"
 - "wayland-scanner"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "basenc"
 - "b2sum"
 - "ls"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
 - "chown"
 - "chroot"
 - "cksum"
versions:
 - "1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for oxbreaker"
config: {"url": "https://biocontainers.pro/tools/oxbreaker", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for oxbreaker", "latest": {"1.0--pyhdfd78af_0": "sha256:d0e18369f7408d15084baa04aaf86a565ab09ffde970438df8789d9a05e387c9"}, "tags": {"1.0--pyhdfd78af_0": "sha256:d0e18369f7408d15084baa04aaf86a565ab09ffde970438df8789d9a05e387c9"}, "docker": "quay.io/biocontainers/oxbreaker", "aliases": {"gtk4-builder-tool": "/usr/local/bin/gtk4-builder-tool", "gtk4-demo": "/usr/local/bin/gtk4-demo", "gtk4-demo-application": "/usr/local/bin/gtk4-demo-application", "gtk4-encode-symbolic-svg": "/usr/local/bin/gtk4-encode-symbolic-svg", "gtk4-icon-editor": "/usr/local/bin/gtk4-icon-editor", "gtk4-image-tool": "/usr/local/bin/gtk4-image-tool", "gtk4-launch": "/usr/local/bin/gtk4-launch", "gtk4-node-editor": "/usr/local/bin/gtk4-node-editor", "gtk4-path-tool": "/usr/local/bin/gtk4-path-tool", "gtk4-print-editor": "/usr/local/bin/gtk4-print-editor", "gtk4-query-settings": "/usr/local/bin/gtk4-query-settings", "gtk4-rendernode-tool": "/usr/local/bin/gtk4-rendernode-tool", "gtk4-update-icon-cache": "/usr/local/bin/gtk4-update-icon-cache", "gtk4-widget-factory": "/usr/local/bin/gtk4-widget-factory", "oxbreaker": "/usr/local/bin/oxbreaker", "nextflow": "/usr/local/bin/nextflow", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "wayland-scanner": "/usr/local/bin/wayland-scanner", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot", "cksum": "/usr/local/bin/cksum"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oxbreaker.
singularity registry hpc automated addition for oxbreaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oxbreaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oxbreaker:1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oxbreaker/1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/oxbreaker/1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oxbreaker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oxbreaker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oxbreaker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oxbreaker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oxbreaker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oxbreaker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gtk4-builder-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk4-builder-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-demo

```bash
$ singularity exec <container> /usr/local/bin/gtk4-demo
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-demo-application

```bash
$ singularity exec <container> /usr/local/bin/gtk4-demo-application
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-demo-application   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-demo-application   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-encode-symbolic-svg

```bash
$ singularity exec <container> /usr/local/bin/gtk4-encode-symbolic-svg
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-icon-editor

```bash
$ singularity exec <container> /usr/local/bin/gtk4-icon-editor
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-icon-editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-icon-editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-image-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk4-image-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-image-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-image-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-launch

```bash
$ singularity exec <container> /usr/local/bin/gtk4-launch
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-node-editor

```bash
$ singularity exec <container> /usr/local/bin/gtk4-node-editor
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-node-editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-node-editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-path-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk4-path-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-path-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-path-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-print-editor

```bash
$ singularity exec <container> /usr/local/bin/gtk4-print-editor
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-print-editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-print-editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-query-settings

```bash
$ singularity exec <container> /usr/local/bin/gtk4-query-settings
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-rendernode-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk4-rendernode-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-rendernode-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-rendernode-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-update-icon-cache

```bash
$ singularity exec <container> /usr/local/bin/gtk4-update-icon-cache
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk4-widget-factory

```bash
$ singularity exec <container> /usr/local/bin/gtk4-widget-factory
$ podman run --it --rm --entrypoint /usr/local/bin/gtk4-widget-factory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk4-widget-factory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oxbreaker

```bash
$ singularity exec <container> /usr/local/bin/oxbreaker
$ podman run --it --rm --entrypoint /usr/local/bin/oxbreaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oxbreaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow

```bash
$ singularity exec <container> /usr/local/bin/nextflow
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-compile-repository

```bash
$ singularity exec <container> /usr/local/bin/gi-compile-repository
$ podman run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-decompile-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-decompile-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-inspect-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-inspect-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ls

```bash
$ singularity exec <container> /usr/local/bin/ls
$ podman run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat

```bash
$ singularity exec <container> /usr/local/bin/cat
$ podman run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chcon

```bash
$ singularity exec <container> /usr/local/bin/chcon
$ podman run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chgrp

```bash
$ singularity exec <container> /usr/local/bin/chgrp
$ podman run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmod

```bash
$ singularity exec <container> /usr/local/bin/chmod
$ podman run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chown

```bash
$ singularity exec <container> /usr/local/bin/chown
$ podman run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chroot

```bash
$ singularity exec <container> /usr/local/bin/chroot
$ podman run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cksum

```bash
$ singularity exec <container> /usr/local/bin/cksum
$ podman run --it --rm --entrypoint /usr/local/bin/cksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cksum   -v ${PWD} -w ${PWD} <container> -c " $@"
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