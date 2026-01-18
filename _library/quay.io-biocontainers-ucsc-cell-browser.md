---
layout: container
name:  "quay.io/biocontainers/ucsc-cell-browser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ucsc-cell-browser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ucsc-cell-browser/container.yaml"
updated_at: "2026-01-18 04:02:46.783011"
latest: "1.2.16--pyhdfd78af_0"
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
 - "1.2.2--pyhdfd78af_0"
 - "1.2.3--pyhdfd78af_0"
 - "1.2.4--pyhdfd78af_0"
 - "1.2.5--pyhdfd78af_0"
 - "1.2.6--pyhdfd78af_0"
 - "1.2.8--pyhdfd78af_0"
 - "1.2.12--pyhdfd78af_0"
 - "1.2.14--pyhdfd78af_0"
 - "1.2.15--pyhdfd78af_0"
 - "1.2.16--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ucsc-cell-browser"
config: {"url": "https://biocontainers.pro/tools/ucsc-cell-browser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ucsc-cell-browser", "latest": {"1.2.16--pyhdfd78af_0": "sha256:5aa1ddda7d3e8d3f17dc665c55b71d9849e58aea2639a97d3c48a0b7b88214b3"}, "tags": {"1.1.1--pyhdfd78af_1": "sha256:f3a65e13b73dbdfa24b4183dd7b4a1ad49737d58fabb93efff9f4f3bdf665c11", "1.2.2--pyhdfd78af_0": "sha256:ab35da61d3b259400d174751d9780ac4d2fe6279b54258ac4af7868bb9ccc18b", "1.2.3--pyhdfd78af_0": "sha256:32654d460a6d6580c82dbace0986fa83cbe711f22f1ba5e5302f689fe570dded", "1.2.4--pyhdfd78af_0": "sha256:ea4773ece14cc4f27e6456f11b7b66d390f02d67230a2255d9e2b37a575f3b6b", "1.2.5--pyhdfd78af_0": "sha256:c67f295a2487a29c97a8e58be0fe9a785ed76112ec4268b02345e0e6655e0c4d", "1.2.6--pyhdfd78af_0": "sha256:4e2a2b0b4eecf9f4a8a9a97cacbc56907a9ff4872f121827f0a677396cb069a1", "1.2.8--pyhdfd78af_0": "sha256:78c65e2c193a14f0bd9361497e301b086ae8cb5757b39d04f91dc3ed52d1cc51", "1.2.12--pyhdfd78af_0": "sha256:3e9be7ab9fea715df3a966de8cecde7e30c40d548a6b2fe51e7b1c57143a3bc5", "1.2.14--pyhdfd78af_0": "sha256:c0cd17324b3b5ed0e3074fcd16097bce7d41f5a2825f66993012c5760c6db2ef", "1.2.15--pyhdfd78af_0": "sha256:0d8ac44584dc1079efe031a997a7836b2a1f592fe38af0ec259153ce59fe6027", "1.2.16--pyhdfd78af_0": "sha256:5aa1ddda7d3e8d3f17dc665c55b71d9849e58aea2639a97d3c48a0b7b88214b3"}, "docker": "quay.io/biocontainers/ucsc-cell-browser", "aliases": {"cbBuild": "/usr/local/bin/cbBuild", "cbGenes": "/usr/local/bin/cbGenes", "cbGuessGencode": "/usr/local/bin/cbGuessGencode", "cbHub": "/usr/local/bin/cbHub", "cbImportCellranger": "/usr/local/bin/cbImportCellranger", "cbImportScanpy": "/usr/local/bin/cbImportScanpy", "cbImportSeurat": "/usr/local/bin/cbImportSeurat", "cbMarkerAnnotate": "/usr/local/bin/cbMarkerAnnotate", "cbScanpy": "/usr/local/bin/cbScanpy", "cbSeurat": "/usr/local/bin/cbSeurat", "cbTool": "/usr/local/bin/cbTool", "cbUpgrade": "/usr/local/bin/cbUpgrade", "natsort": "/usr/local/bin/natsort", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "f2py3.10": "/usr/local/bin/f2py3.10", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ucsc-cell-browser.
shpc-registry automated BioContainers addition for ucsc-cell-browser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ucsc-cell-browser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ucsc-cell-browser:1.2.16--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ucsc-cell-browser/1.2.16--pyhdfd78af_0
$ module help quay.io/biocontainers/ucsc-cell-browser/1.2.16--pyhdfd78af_0
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