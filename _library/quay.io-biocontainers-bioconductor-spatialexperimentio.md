---
layout: container
name:  "quay.io/biocontainers/bioconductor-spatialexperimentio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spatialexperimentio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spatialexperimentio/container.yaml"
updated_at: "2026-03-22 05:03:54.523211"
latest: "1.2.0--r45hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spatialexperimentio"
aliases:
 - "protoc-33.5.0"
 - "protoc-gen-upb-33.5.0"
 - "protoc-gen-upb_minitable-33.5.0"
 - "protoc-gen-upbdefs-33.5.0"
 - "protoc-gen-upb_minitable"
 - "h2benchmark"
 - "dot_sandbox"
 - "dec265"
 - "gtk-builder-tool"
 - "gtk-encode-symbolic-svg"
 - "gtk-launch"
 - "gtk-query-immodules-3.0"
 - "gtk-query-settings"
 - "checksum-profile"
 - "elastishadow"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "x265"
 - "wayland-scanner"
 - "SvtAv1EncApp"
 - "dav1d"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "aomdec"
versions:
 - "1.2.0--r45hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-spatialexperimentio"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spatialexperimentio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-spatialexperimentio", "latest": {"1.2.0--r45hdfd78af_0": "sha256:581d52e7762557d46890d3559b36f898652bd5e64b337fbc9619eacd8393a145"}, "tags": {"1.2.0--r45hdfd78af_0": "sha256:581d52e7762557d46890d3559b36f898652bd5e64b337fbc9619eacd8393a145"}, "docker": "quay.io/biocontainers/bioconductor-spatialexperimentio", "aliases": {"protoc-33.5.0": "/usr/local/bin/protoc-33.5.0", "protoc-gen-upb-33.5.0": "/usr/local/bin/protoc-gen-upb-33.5.0", "protoc-gen-upb_minitable-33.5.0": "/usr/local/bin/protoc-gen-upb_minitable-33.5.0", "protoc-gen-upbdefs-33.5.0": "/usr/local/bin/protoc-gen-upbdefs-33.5.0", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "h2benchmark": "/usr/local/bin/h2benchmark", "dot_sandbox": "/usr/local/bin/dot_sandbox", "dec265": "/usr/local/bin/dec265", "gtk-builder-tool": "/usr/local/bin/gtk-builder-tool", "gtk-encode-symbolic-svg": "/usr/local/bin/gtk-encode-symbolic-svg", "gtk-launch": "/usr/local/bin/gtk-launch", "gtk-query-immodules-3.0": "/usr/local/bin/gtk-query-immodules-3.0", "gtk-query-settings": "/usr/local/bin/gtk-query-settings", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "x265": "/usr/local/bin/x265", "wayland-scanner": "/usr/local/bin/wayland-scanner", "SvtAv1EncApp": "/usr/local/bin/SvtAv1EncApp", "dav1d": "/usr/local/bin/dav1d", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "aomdec": "/usr/local/bin/aomdec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spatialexperimentio.
singularity registry hpc automated addition for bioconductor-spatialexperimentio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialexperimentio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialexperimentio:1.2.0--r45hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spatialexperimentio/1.2.0--r45hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spatialexperimentio/1.2.0--r45hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spatialexperimentio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialexperimentio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialexperimentio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spatialexperimentio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spatialexperimentio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spatialexperimentio-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dot_sandbox

```bash
$ singularity exec <container> /usr/local/bin/dot_sandbox
$ podman run --it --rm --entrypoint /usr/local/bin/dot_sandbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dot_sandbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dec265

```bash
$ singularity exec <container> /usr/local/bin/dec265
$ podman run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-encode-symbolic-svg

```bash
$ singularity exec <container> /usr/local/bin/gtk-encode-symbolic-svg
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-launch

```bash
$ singularity exec <container> /usr/local/bin/gtk-launch
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-3.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-settings

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-settings
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### x265

```bash
$ singularity exec <container> /usr/local/bin/x265
$ podman run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### aomdec

```bash
$ singularity exec <container> /usr/local/bin/aomdec
$ podman run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
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