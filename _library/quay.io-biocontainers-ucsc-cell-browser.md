---
layout: container
name:  "quay.io/biocontainers/ucsc-cell-browser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ucsc-cell-browser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ucsc-cell-browser/container.yaml"
updated_at: "2023-01-23 02:51:54.107979"
latest: "1.1.1--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/ucsc-cell-browser"
aliases:
 - "cbBuild"
 - "cbGenes"
 - "cbGuessGencode"
 - "cbHub"
 - "cbImportCellranger"
 - "cbImportScanpy"
 - "cbImportSeurat"
 - "cbMarkerAnnotate"
 - "cbScanpy"
 - "cbSeurat"
 - "cbTool"
 - "cbUpgrade"
 - "natsort"
 - "mirror_server"
 - "mirror_server_stop"
 - "f2py3.10"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "2to3-3.10"
 - "idle3.10"
versions:
 - "1.1.1--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for ucsc-cell-browser"
config: {"url": "https://biocontainers.pro/tools/ucsc-cell-browser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ucsc-cell-browser", "latest": {"1.1.1--pyhdfd78af_1": "sha256:f3a65e13b73dbdfa24b4183dd7b4a1ad49737d58fabb93efff9f4f3bdf665c11"}, "tags": {"1.1.1--pyhdfd78af_1": "sha256:f3a65e13b73dbdfa24b4183dd7b4a1ad49737d58fabb93efff9f4f3bdf665c11"}, "docker": "quay.io/biocontainers/ucsc-cell-browser", "aliases": {"cbBuild": "/usr/local/bin/cbBuild", "cbGenes": "/usr/local/bin/cbGenes", "cbGuessGencode": "/usr/local/bin/cbGuessGencode", "cbHub": "/usr/local/bin/cbHub", "cbImportCellranger": "/usr/local/bin/cbImportCellranger", "cbImportScanpy": "/usr/local/bin/cbImportScanpy", "cbImportSeurat": "/usr/local/bin/cbImportSeurat", "cbMarkerAnnotate": "/usr/local/bin/cbMarkerAnnotate", "cbScanpy": "/usr/local/bin/cbScanpy", "cbSeurat": "/usr/local/bin/cbSeurat", "cbTool": "/usr/local/bin/cbTool", "cbUpgrade": "/usr/local/bin/cbUpgrade", "natsort": "/usr/local/bin/natsort", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "f2py3.10": "/usr/local/bin/f2py3.10", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ucsc-cell-browser.
shpc-registry automated BioContainers addition for ucsc-cell-browser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ucsc-cell-browser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ucsc-cell-browser:1.1.1--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ucsc-cell-browser/1.1.1--pyhdfd78af_1
$ module help quay.io/biocontainers/ucsc-cell-browser/1.1.1--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ucsc-cell-browser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ucsc-cell-browser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ucsc-cell-browser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ucsc-cell-browser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ucsc-cell-browser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ucsc-cell-browser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cbBuild

```bash
$ singularity exec <container> /usr/local/bin/cbBuild
$ podman run --it --rm --entrypoint /usr/local/bin/cbBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbGenes

```bash
$ singularity exec <container> /usr/local/bin/cbGenes
$ podman run --it --rm --entrypoint /usr/local/bin/cbGenes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbGenes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbGuessGencode

```bash
$ singularity exec <container> /usr/local/bin/cbGuessGencode
$ podman run --it --rm --entrypoint /usr/local/bin/cbGuessGencode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbGuessGencode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbHub

```bash
$ singularity exec <container> /usr/local/bin/cbHub
$ podman run --it --rm --entrypoint /usr/local/bin/cbHub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbHub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbImportCellranger

```bash
$ singularity exec <container> /usr/local/bin/cbImportCellranger
$ podman run --it --rm --entrypoint /usr/local/bin/cbImportCellranger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbImportCellranger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbImportScanpy

```bash
$ singularity exec <container> /usr/local/bin/cbImportScanpy
$ podman run --it --rm --entrypoint /usr/local/bin/cbImportScanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbImportScanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbImportSeurat

```bash
$ singularity exec <container> /usr/local/bin/cbImportSeurat
$ podman run --it --rm --entrypoint /usr/local/bin/cbImportSeurat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbImportSeurat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbMarkerAnnotate

```bash
$ singularity exec <container> /usr/local/bin/cbMarkerAnnotate
$ podman run --it --rm --entrypoint /usr/local/bin/cbMarkerAnnotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbMarkerAnnotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbScanpy

```bash
$ singularity exec <container> /usr/local/bin/cbScanpy
$ podman run --it --rm --entrypoint /usr/local/bin/cbScanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbScanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbSeurat

```bash
$ singularity exec <container> /usr/local/bin/cbSeurat
$ podman run --it --rm --entrypoint /usr/local/bin/cbSeurat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbSeurat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbTool

```bash
$ singularity exec <container> /usr/local/bin/cbTool
$ podman run --it --rm --entrypoint /usr/local/bin/cbTool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbTool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbUpgrade

```bash
$ singularity exec <container> /usr/local/bin/cbUpgrade
$ podman run --it --rm --entrypoint /usr/local/bin/cbUpgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbUpgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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