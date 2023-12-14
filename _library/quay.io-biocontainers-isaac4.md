---
layout: container
name:  "quay.io/biocontainers/isaac4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isaac4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isaac4/container.yaml"
updated_at: "2023-12-14 02:43:17.834228"
latest: "04.18.11.09--h07bff40_0"
container_url: "https://biocontainers.pro/tools/isaac4"
aliases:
 - "isaac-align"
 - "isaac-merge-references"
 - "isaac-pack-reference"
 - "isaac-reorder-reference"
 - "isaac-sort-reference"
 - "isaac-unpack-reference"
 - "chrpath"
 - "gnuplot"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "compile-et.pl"
 - "gdlib-config"
 - "prerr.properties"
versions:
 - "04.18.11.09--h07bff40_0"
description: "shpc-registry automated BioContainers addition for isaac4"
config: {"url": "https://biocontainers.pro/tools/isaac4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isaac4", "latest": {"04.18.11.09--h07bff40_0": "sha256:2ceb7f80eaa0068b5390a5802e1f261c27575a84251b94b65d8722ceef5f3844"}, "tags": {"04.18.11.09--h07bff40_0": "sha256:2ceb7f80eaa0068b5390a5802e1f261c27575a84251b94b65d8722ceef5f3844"}, "docker": "quay.io/biocontainers/isaac4", "aliases": {"isaac-align": "/usr/local/bin/isaac-align", "isaac-merge-references": "/usr/local/bin/isaac-merge-references", "isaac-pack-reference": "/usr/local/bin/isaac-pack-reference", "isaac-reorder-reference": "/usr/local/bin/isaac-reorder-reference", "isaac-sort-reference": "/usr/local/bin/isaac-sort-reference", "isaac-unpack-reference": "/usr/local/bin/isaac-unpack-reference", "chrpath": "/usr/local/bin/chrpath", "gnuplot": "/usr/local/bin/gnuplot", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "compile-et.pl": "/usr/local/bin/compile-et.pl", "gdlib-config": "/usr/local/bin/gdlib-config", "prerr.properties": "/usr/local/bin/prerr.properties"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isaac4.
shpc-registry automated BioContainers addition for isaac4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isaac4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isaac4:04.18.11.09--h07bff40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isaac4/04.18.11.09--h07bff40_0
$ module help quay.io/biocontainers/isaac4/04.18.11.09--h07bff40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isaac4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isaac4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isaac4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isaac4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isaac4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isaac4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isaac-align

```bash
$ singularity exec <container> /usr/local/bin/isaac-align
$ podman run --it --rm --entrypoint /usr/local/bin/isaac-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isaac-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isaac-merge-references

```bash
$ singularity exec <container> /usr/local/bin/isaac-merge-references
$ podman run --it --rm --entrypoint /usr/local/bin/isaac-merge-references   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isaac-merge-references   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isaac-pack-reference

```bash
$ singularity exec <container> /usr/local/bin/isaac-pack-reference
$ podman run --it --rm --entrypoint /usr/local/bin/isaac-pack-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isaac-pack-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isaac-reorder-reference

```bash
$ singularity exec <container> /usr/local/bin/isaac-reorder-reference
$ podman run --it --rm --entrypoint /usr/local/bin/isaac-reorder-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isaac-reorder-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isaac-sort-reference

```bash
$ singularity exec <container> /usr/local/bin/isaac-sort-reference
$ podman run --it --rm --entrypoint /usr/local/bin/isaac-sort-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isaac-sort-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isaac-unpack-reference

```bash
$ singularity exec <container> /usr/local/bin/isaac-unpack-reference
$ podman run --it --rm --entrypoint /usr/local/bin/isaac-unpack-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isaac-unpack-reference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrpath

```bash
$ singularity exec <container> /usr/local/bin/chrpath
$ podman run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerr.properties

```bash
$ singularity exec <container> /usr/local/bin/prerr.properties
$ podman run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
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