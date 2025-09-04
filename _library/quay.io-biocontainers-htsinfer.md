---
layout: container
name:  "quay.io/biocontainers/htsinfer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/htsinfer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/htsinfer/container.yaml"
updated_at: "2025-09-04 03:23:06.531183"
latest: "1.0.0_rc.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/htsinfer"
aliases:
 - "STAR-avx"
 - "STAR-avx2"
 - "STAR-plain"
 - "STAR-sse3"
 - "STAR-sse4.1"
 - "STAR-ssse3"
 - "STARlong-avx"
 - "STARlong-avx2"
 - "STARlong-plain"
 - "STARlong-sse3"
 - "STARlong-sse4.1"
 - "STARlong-ssse3"
 - "annot-tsv"
 - "htsinfer"
 - "kallisto"
 - "STAR"
 - "STARlong"
 - "cutadapt"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "igzip"
 - "pigz"
 - "unpigz"
 - "mirror_server"
 - "mirror_server_stop"
 - "f2py3.10"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5import"
 - "h5jam"
 - "h5ls"
versions:
 - "0.9.0--pyhdfd78af_0"
 - "0.10.0--pyhdfd78af_0"
 - "0.11.0--pyhdfd78af_1"
 - "1.0.0_rc.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for htsinfer"
config: {"url": "https://biocontainers.pro/tools/htsinfer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for htsinfer", "latest": {"1.0.0_rc.1--pyhdfd78af_0": "sha256:5371b0445963a5912a0e359a076ed02673d82e780d7b3104ee43f46be17fd1ca"}, "tags": {"0.9.0--pyhdfd78af_0": "sha256:6148ab06a46990c7bf746ce7d1bb5d2e314da0a3fe5dd5221c1a028a60dd87ae", "0.10.0--pyhdfd78af_0": "sha256:17e728bbb8d66f06b233d2f2cd74be9882d3f8f368a3b618be990be01f40332c", "0.11.0--pyhdfd78af_1": "sha256:c2e2f62b8b91947cbe6d382fa6a22ed73b3a446f5747882cea82d2b0e3911927", "1.0.0_rc.1--pyhdfd78af_0": "sha256:5371b0445963a5912a0e359a076ed02673d82e780d7b3104ee43f46be17fd1ca"}, "docker": "quay.io/biocontainers/htsinfer", "aliases": {"STAR-avx": "/usr/local/bin/STAR-avx", "STAR-avx2": "/usr/local/bin/STAR-avx2", "STAR-plain": "/usr/local/bin/STAR-plain", "STAR-sse3": "/usr/local/bin/STAR-sse3", "STAR-sse4.1": "/usr/local/bin/STAR-sse4.1", "STAR-ssse3": "/usr/local/bin/STAR-ssse3", "STARlong-avx": "/usr/local/bin/STARlong-avx", "STARlong-avx2": "/usr/local/bin/STARlong-avx2", "STARlong-plain": "/usr/local/bin/STARlong-plain", "STARlong-sse3": "/usr/local/bin/STARlong-sse3", "STARlong-sse4.1": "/usr/local/bin/STARlong-sse4.1", "STARlong-ssse3": "/usr/local/bin/STARlong-ssse3", "annot-tsv": "/usr/local/bin/annot-tsv", "htsinfer": "/usr/local/bin/htsinfer", "kallisto": "/usr/local/bin/kallisto", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "cutadapt": "/usr/local/bin/cutadapt", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "igzip": "/usr/local/bin/igzip", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "f2py3.10": "/usr/local/bin/f2py3.10", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug", "h5diff": "/usr/local/bin/h5diff", "h5import": "/usr/local/bin/h5import", "h5jam": "/usr/local/bin/h5jam", "h5ls": "/usr/local/bin/h5ls"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/htsinfer.
singularity registry hpc automated addition for htsinfer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/htsinfer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/htsinfer:1.0.0_rc.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/htsinfer/1.0.0_rc.1--pyhdfd78af_0
$ module help quay.io/biocontainers/htsinfer/1.0.0_rc.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htsinfer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htsinfer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htsinfer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htsinfer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htsinfer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htsinfer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### STAR-avx

```bash
$ singularity exec <container> /usr/local/bin/STAR-avx
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-avx2

```bash
$ singularity exec <container> /usr/local/bin/STAR-avx2
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-plain

```bash
$ singularity exec <container> /usr/local/bin/STAR-plain
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-sse3

```bash
$ singularity exec <container> /usr/local/bin/STAR-sse3
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-sse4.1

```bash
$ singularity exec <container> /usr/local/bin/STAR-sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-ssse3

```bash
$ singularity exec <container> /usr/local/bin/STAR-ssse3
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-avx

```bash
$ singularity exec <container> /usr/local/bin/STARlong-avx
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-avx2

```bash
$ singularity exec <container> /usr/local/bin/STARlong-avx2
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-plain

```bash
$ singularity exec <container> /usr/local/bin/STARlong-plain
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-sse3

```bash
$ singularity exec <container> /usr/local/bin/STARlong-sse3
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-sse4.1

```bash
$ singularity exec <container> /usr/local/bin/STARlong-sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-ssse3

```bash
$ singularity exec <container> /usr/local/bin/STARlong-ssse3
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsinfer

```bash
$ singularity exec <container> /usr/local/bin/htsinfer
$ podman run --it --rm --entrypoint /usr/local/bin/htsinfer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsinfer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5diff

```bash
$ singularity exec <container> /usr/local/bin/h5diff
$ podman run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5import

```bash
$ singularity exec <container> /usr/local/bin/h5import
$ podman run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5jam

```bash
$ singularity exec <container> /usr/local/bin/h5jam
$ podman run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5ls

```bash
$ singularity exec <container> /usr/local/bin/h5ls
$ podman run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
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