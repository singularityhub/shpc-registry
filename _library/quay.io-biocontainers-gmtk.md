---
layout: container
name:  "quay.io/biocontainers/gmtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gmtk/container.yaml"
updated_at: "2026-01-05 06:01:36.770436"
latest: "1.4.4--h4c2f4bb_16"
container_url: "https://biocontainers.pro/tools/gmtk"
aliases:
 - "discrete-mi"
 - "fixTri.sh"
 - "generate_random_graph.pl"
 - "gmtkDMLPtrain"
 - "gmtkDTindex"
 - "gmtkEMtrain"
 - "gmtkJT"
 - "gmtkKernel"
 - "gmtkMMItrain"
 - "gmtkModelInfo"
 - "gmtkNGramIndex"
 - "gmtkOnline"
 - "gmtkParmConvert"
 - "gmtkPrint"
 - "gmtkTFmerge"
 - "gmtkTie"
 - "gmtkTime"
 - "gmtkTriangulate"
 - "gmtkViterbi"
 - "obs-cat"
 - "obs-concat"
 - "obs-diff"
 - "obs-info"
 - "obs-print"
 - "obs-skmeans"
 - "obs-stats"
 - "obs-window"
 - "triangulateGA"
 - "triangulateParallel"
 - "triangulateTimings"
 - "mirror_server"
 - "mirror_server_stop"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
versions:
 - "1.4.4--h0326b38_9"
 - "1.4.4--h0326b38_12"
 - "1.4.4--hd959fe9_13"
 - "1.4.4--hd959fe9_14"
 - "1.4.4--h1b96c6b_15"
 - "1.4.4--h4c2f4bb_16"
description: "shpc-registry automated BioContainers addition for gmtk"
config: {"url": "https://biocontainers.pro/tools/gmtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gmtk", "latest": {"1.4.4--h4c2f4bb_16": "sha256:0e0a59e714b5a1bc81b5273299e58241247b6b0ee95ac53c4e7853b7c9e07c3d"}, "tags": {"1.4.4--h0326b38_9": "sha256:c0e74d5fe9113bb4d6cd7ad25d09b8d1829932683064f3435a6e99a9659c0efb", "1.4.4--h0326b38_12": "sha256:7f7538fc809b32ed5fea1b570cfd163e2016bb0753b84a8995c5df62572aa705", "1.4.4--hd959fe9_13": "sha256:6ab5ccd320fc5885e35958fb432b3ab087524f5ccb2d8e2e1db2c5fd07e57039", "1.4.4--hd959fe9_14": "sha256:c6dc561e6b0b5b6b5a12ecea2cfce06bc1fad6c22f07056755f9a93e599f907f", "1.4.4--h1b96c6b_15": "sha256:608e62dddd5914940364bf8c94236e16a133b948d7a815a35fa8332ca0743876", "1.4.4--h4c2f4bb_16": "sha256:0e0a59e714b5a1bc81b5273299e58241247b6b0ee95ac53c4e7853b7c9e07c3d"}, "docker": "quay.io/biocontainers/gmtk", "aliases": {"discrete-mi": "/usr/local/bin/discrete-mi", "fixTri.sh": "/usr/local/bin/fixTri.sh", "generate_random_graph.pl": "/usr/local/bin/generate_random_graph.pl", "gmtkDMLPtrain": "/usr/local/bin/gmtkDMLPtrain", "gmtkDTindex": "/usr/local/bin/gmtkDTindex", "gmtkEMtrain": "/usr/local/bin/gmtkEMtrain", "gmtkJT": "/usr/local/bin/gmtkJT", "gmtkKernel": "/usr/local/bin/gmtkKernel", "gmtkMMItrain": "/usr/local/bin/gmtkMMItrain", "gmtkModelInfo": "/usr/local/bin/gmtkModelInfo", "gmtkNGramIndex": "/usr/local/bin/gmtkNGramIndex", "gmtkOnline": "/usr/local/bin/gmtkOnline", "gmtkParmConvert": "/usr/local/bin/gmtkParmConvert", "gmtkPrint": "/usr/local/bin/gmtkPrint", "gmtkTFmerge": "/usr/local/bin/gmtkTFmerge", "gmtkTie": "/usr/local/bin/gmtkTie", "gmtkTime": "/usr/local/bin/gmtkTime", "gmtkTriangulate": "/usr/local/bin/gmtkTriangulate", "gmtkViterbi": "/usr/local/bin/gmtkViterbi", "obs-cat": "/usr/local/bin/obs-cat", "obs-concat": "/usr/local/bin/obs-concat", "obs-diff": "/usr/local/bin/obs-diff", "obs-info": "/usr/local/bin/obs-info", "obs-print": "/usr/local/bin/obs-print", "obs-skmeans": "/usr/local/bin/obs-skmeans", "obs-stats": "/usr/local/bin/obs-stats", "obs-window": "/usr/local/bin/obs-window", "triangulateGA": "/usr/local/bin/triangulateGA", "triangulateParallel": "/usr/local/bin/triangulateParallel", "triangulateTimings": "/usr/local/bin/triangulateTimings", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmtk.
shpc-registry automated BioContainers addition for gmtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmtk:1.4.4--h4c2f4bb_16
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmtk/1.4.4--h4c2f4bb_16
$ module help quay.io/biocontainers/gmtk/1.4.4--h4c2f4bb_16
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### discrete-mi

```bash
$ singularity exec <container> /usr/local/bin/discrete-mi
$ podman run --it --rm --entrypoint /usr/local/bin/discrete-mi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/discrete-mi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fixTri.sh

```bash
$ singularity exec <container> /usr/local/bin/fixTri.sh
$ podman run --it --rm --entrypoint /usr/local/bin/fixTri.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fixTri.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_random_graph.pl

```bash
$ singularity exec <container> /usr/local/bin/generate_random_graph.pl
$ podman run --it --rm --entrypoint /usr/local/bin/generate_random_graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_random_graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkDMLPtrain

```bash
$ singularity exec <container> /usr/local/bin/gmtkDMLPtrain
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkDMLPtrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkDMLPtrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkDTindex

```bash
$ singularity exec <container> /usr/local/bin/gmtkDTindex
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkDTindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkDTindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkEMtrain

```bash
$ singularity exec <container> /usr/local/bin/gmtkEMtrain
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkEMtrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkEMtrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkJT

```bash
$ singularity exec <container> /usr/local/bin/gmtkJT
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkJT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkJT   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkKernel

```bash
$ singularity exec <container> /usr/local/bin/gmtkKernel
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkKernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkKernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkMMItrain

```bash
$ singularity exec <container> /usr/local/bin/gmtkMMItrain
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkMMItrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkMMItrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkModelInfo

```bash
$ singularity exec <container> /usr/local/bin/gmtkModelInfo
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkModelInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkModelInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkNGramIndex

```bash
$ singularity exec <container> /usr/local/bin/gmtkNGramIndex
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkNGramIndex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkNGramIndex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkOnline

```bash
$ singularity exec <container> /usr/local/bin/gmtkOnline
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkOnline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkOnline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkParmConvert

```bash
$ singularity exec <container> /usr/local/bin/gmtkParmConvert
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkParmConvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkParmConvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkPrint

```bash
$ singularity exec <container> /usr/local/bin/gmtkPrint
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkTFmerge

```bash
$ singularity exec <container> /usr/local/bin/gmtkTFmerge
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkTFmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkTFmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkTie

```bash
$ singularity exec <container> /usr/local/bin/gmtkTie
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkTie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkTie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkTime

```bash
$ singularity exec <container> /usr/local/bin/gmtkTime
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkTime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkTime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkTriangulate

```bash
$ singularity exec <container> /usr/local/bin/gmtkTriangulate
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkTriangulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkTriangulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtkViterbi

```bash
$ singularity exec <container> /usr/local/bin/gmtkViterbi
$ podman run --it --rm --entrypoint /usr/local/bin/gmtkViterbi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtkViterbi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-cat

```bash
$ singularity exec <container> /usr/local/bin/obs-cat
$ podman run --it --rm --entrypoint /usr/local/bin/obs-cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-concat

```bash
$ singularity exec <container> /usr/local/bin/obs-concat
$ podman run --it --rm --entrypoint /usr/local/bin/obs-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-diff

```bash
$ singularity exec <container> /usr/local/bin/obs-diff
$ podman run --it --rm --entrypoint /usr/local/bin/obs-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-info

```bash
$ singularity exec <container> /usr/local/bin/obs-info
$ podman run --it --rm --entrypoint /usr/local/bin/obs-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-print

```bash
$ singularity exec <container> /usr/local/bin/obs-print
$ podman run --it --rm --entrypoint /usr/local/bin/obs-print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-skmeans

```bash
$ singularity exec <container> /usr/local/bin/obs-skmeans
$ podman run --it --rm --entrypoint /usr/local/bin/obs-skmeans   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-skmeans   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-stats

```bash
$ singularity exec <container> /usr/local/bin/obs-stats
$ podman run --it --rm --entrypoint /usr/local/bin/obs-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obs-window

```bash
$ singularity exec <container> /usr/local/bin/obs-window
$ podman run --it --rm --entrypoint /usr/local/bin/obs-window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obs-window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### triangulateGA

```bash
$ singularity exec <container> /usr/local/bin/triangulateGA
$ podman run --it --rm --entrypoint /usr/local/bin/triangulateGA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/triangulateGA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### triangulateParallel

```bash
$ singularity exec <container> /usr/local/bin/triangulateParallel
$ podman run --it --rm --entrypoint /usr/local/bin/triangulateParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/triangulateParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### triangulateTimings

```bash
$ singularity exec <container> /usr/local/bin/triangulateTimings
$ podman run --it --rm --entrypoint /usr/local/bin/triangulateTimings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/triangulateTimings   -v ${PWD} -w ${PWD} <container> -c " $@"
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