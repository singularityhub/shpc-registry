---
layout: container
name:  "quay.io/biocontainers/mitogeneextractor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mitogeneextractor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mitogeneextractor/container.yaml"
updated_at: "2026-08-12 04:52:05.650317"
latest: "1.9.6--hc52dbad_0"
container_url: "https://biocontainers.pro/tools/mitogeneextractor"
aliases:
 - "MitoGeneExtractor"
 - "MitoGeneExtractor-v1.9.6"
 - "esd2esi"
 - "exonerate-server"
 - "fasta2esd"
 - "fastaannotatecdna"
 - "fastachecksum"
 - "fastaclip"
 - "fastacomposition"
 - "fastadiff"
 - "fastaexplode"
 - "fastafetch"
 - "fastahardmask"
 - "fastaindex"
 - "fastalength"
 - "fastanrdb"
 - "fastaoverlap"
 - "fastareformat"
 - "fastaremove"
 - "fastarevcomp"
 - "fastasoftmask"
 - "fastasubseq"
 - "fastatranslate"
 - "fastavalidcds"
 - "ipcress"
 - "exonerate"
 - "fastaclean"
versions:
 - "1.9.6--hc52dbad_0"
description: "singularity registry hpc automated addition for mitogeneextractor"
config: {"url": "https://biocontainers.pro/tools/mitogeneextractor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mitogeneextractor", "latest": {"1.9.6--hc52dbad_0": "sha256:8f4facc2907fe982ccc962b8726cacc7d2611068c3b32358613e9a2bc34ad1dd"}, "tags": {"1.9.6--hc52dbad_0": "sha256:8f4facc2907fe982ccc962b8726cacc7d2611068c3b32358613e9a2bc34ad1dd"}, "docker": "quay.io/biocontainers/mitogeneextractor", "aliases": {"MitoGeneExtractor": "/usr/local/bin/MitoGeneExtractor", "MitoGeneExtractor-v1.9.6": "/usr/local/bin/MitoGeneExtractor-v1.9.6", "esd2esi": "/usr/local/bin/esd2esi", "exonerate-server": "/usr/local/bin/exonerate-server", "fasta2esd": "/usr/local/bin/fasta2esd", "fastaannotatecdna": "/usr/local/bin/fastaannotatecdna", "fastachecksum": "/usr/local/bin/fastachecksum", "fastaclip": "/usr/local/bin/fastaclip", "fastacomposition": "/usr/local/bin/fastacomposition", "fastadiff": "/usr/local/bin/fastadiff", "fastaexplode": "/usr/local/bin/fastaexplode", "fastafetch": "/usr/local/bin/fastafetch", "fastahardmask": "/usr/local/bin/fastahardmask", "fastaindex": "/usr/local/bin/fastaindex", "fastalength": "/usr/local/bin/fastalength", "fastanrdb": "/usr/local/bin/fastanrdb", "fastaoverlap": "/usr/local/bin/fastaoverlap", "fastareformat": "/usr/local/bin/fastareformat", "fastaremove": "/usr/local/bin/fastaremove", "fastarevcomp": "/usr/local/bin/fastarevcomp", "fastasoftmask": "/usr/local/bin/fastasoftmask", "fastasubseq": "/usr/local/bin/fastasubseq", "fastatranslate": "/usr/local/bin/fastatranslate", "fastavalidcds": "/usr/local/bin/fastavalidcds", "ipcress": "/usr/local/bin/ipcress", "exonerate": "/usr/local/bin/exonerate", "fastaclean": "/usr/local/bin/fastaclean"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mitogeneextractor.
singularity registry hpc automated addition for mitogeneextractor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mitogeneextractor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mitogeneextractor:1.9.6--hc52dbad_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mitogeneextractor/1.9.6--hc52dbad_0
$ module help quay.io/biocontainers/mitogeneextractor/1.9.6--hc52dbad_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mitogeneextractor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mitogeneextractor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mitogeneextractor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mitogeneextractor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mitogeneextractor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mitogeneextractor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MitoGeneExtractor

```bash
$ singularity exec <container> /usr/local/bin/MitoGeneExtractor
$ podman run --it --rm --entrypoint /usr/local/bin/MitoGeneExtractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MitoGeneExtractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MitoGeneExtractor-v1.9.6

```bash
$ singularity exec <container> /usr/local/bin/MitoGeneExtractor-v1.9.6
$ podman run --it --rm --entrypoint /usr/local/bin/MitoGeneExtractor-v1.9.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MitoGeneExtractor-v1.9.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esd2esi

```bash
$ singularity exec <container> /usr/local/bin/esd2esi
$ podman run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate-server

```bash
$ singularity exec <container> /usr/local/bin/exonerate-server
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2esd

```bash
$ singularity exec <container> /usr/local/bin/fasta2esd
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaannotatecdna

```bash
$ singularity exec <container> /usr/local/bin/fastaannotatecdna
$ podman run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastachecksum

```bash
$ singularity exec <container> /usr/local/bin/fastachecksum
$ podman run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaclip

```bash
$ singularity exec <container> /usr/local/bin/fastaclip
$ podman run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacomposition

```bash
$ singularity exec <container> /usr/local/bin/fastacomposition
$ podman run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastadiff

```bash
$ singularity exec <container> /usr/local/bin/fastadiff
$ podman run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaexplode

```bash
$ singularity exec <container> /usr/local/bin/fastaexplode
$ podman run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastafetch

```bash
$ singularity exec <container> /usr/local/bin/fastafetch
$ podman run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastahardmask

```bash
$ singularity exec <container> /usr/local/bin/fastahardmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaindex

```bash
$ singularity exec <container> /usr/local/bin/fastaindex
$ podman run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastalength

```bash
$ singularity exec <container> /usr/local/bin/fastalength
$ podman run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastanrdb

```bash
$ singularity exec <container> /usr/local/bin/fastanrdb
$ podman run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaoverlap

```bash
$ singularity exec <container> /usr/local/bin/fastaoverlap
$ podman run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastareformat

```bash
$ singularity exec <container> /usr/local/bin/fastareformat
$ podman run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaremove

```bash
$ singularity exec <container> /usr/local/bin/fastaremove
$ podman run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastarevcomp

```bash
$ singularity exec <container> /usr/local/bin/fastarevcomp
$ podman run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasoftmask

```bash
$ singularity exec <container> /usr/local/bin/fastasoftmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasubseq

```bash
$ singularity exec <container> /usr/local/bin/fastasubseq
$ podman run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastatranslate

```bash
$ singularity exec <container> /usr/local/bin/fastatranslate
$ podman run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastavalidcds

```bash
$ singularity exec <container> /usr/local/bin/fastavalidcds
$ podman run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcress

```bash
$ singularity exec <container> /usr/local/bin/ipcress
$ podman run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate

```bash
$ singularity exec <container> /usr/local/bin/exonerate
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaclean

```bash
$ singularity exec <container> /usr/local/bin/fastaclean
$ podman run --it --rm --entrypoint /usr/local/bin/fastaclean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaclean   -v ${PWD} -w ${PWD} <container> -c " $@"
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