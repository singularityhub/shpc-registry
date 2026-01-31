---
layout: container
name:  "quay.io/biocontainers/metawrap-assembly"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metawrap-assembly/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metawrap-assembly/container.yaml"
updated_at: "2026-01-31 04:35:52.053978"
latest: "1.3.0--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/metawrap-assembly"
aliases:
 - "bdf2gdfont.PLS"
 - "config-metawrap"
 - "cvtbdf.pl"
 - "megahit_asm_core"
 - "megahit_sdbg_build"
 - "metaWRAP"
 - "metawrap"
 - "pl2bat.pl"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
 - "icarus.py"
 - "metaquast"
 - "metaquast.py"
 - "pair-at-a-time"
 - "print-missing-subranges"
 - "quast"
 - "quast-download-busco"
 - "quast-download-gridss"
 - "quast-download-silva"
 - "quast-lg.py"
 - "quast.py"
 - "sort-by-length"
 - "xcommon.sh"
 - "xfetch"
 - "xfetch.ini"
 - "xfilter"
 - "xinfo"
versions:
 - "1.3.0--hdfd78af_3"
description: "singularity registry hpc automated addition for metawrap-assembly"
config: {"url": "https://biocontainers.pro/tools/metawrap-assembly", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metawrap-assembly", "latest": {"1.3.0--hdfd78af_3": "sha256:07270c50213e8f892faa135637312e0955d4bec2251370df051074d3e9d81521"}, "tags": {"1.3.0--hdfd78af_3": "sha256:07270c50213e8f892faa135637312e0955d4bec2251370df051074d3e9d81521"}, "docker": "quay.io/biocontainers/metawrap-assembly", "aliases": {"bdf2gdfont.PLS": "/usr/local/bin/bdf2gdfont.PLS", "config-metawrap": "/usr/local/bin/config-metawrap", "cvtbdf.pl": "/usr/local/bin/cvtbdf.pl", "megahit_asm_core": "/usr/local/bin/megahit_asm_core", "megahit_sdbg_build": "/usr/local/bin/megahit_sdbg_build", "metaWRAP": "/usr/local/bin/metaWRAP", "metawrap": "/usr/local/bin/metawrap", "pl2bat.pl": "/usr/local/bin/pl2bat.pl", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "icarus.py": "/usr/local/bin/icarus.py", "metaquast": "/usr/local/bin/metaquast", "metaquast.py": "/usr/local/bin/metaquast.py", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "quast": "/usr/local/bin/quast", "quast-download-busco": "/usr/local/bin/quast-download-busco", "quast-download-gridss": "/usr/local/bin/quast-download-gridss", "quast-download-silva": "/usr/local/bin/quast-download-silva", "quast-lg.py": "/usr/local/bin/quast-lg.py", "quast.py": "/usr/local/bin/quast.py", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metawrap-assembly.
singularity registry hpc automated addition for metawrap-assembly
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metawrap-assembly
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metawrap-assembly:1.3.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metawrap-assembly/1.3.0--hdfd78af_3
$ module help quay.io/biocontainers/metawrap-assembly/1.3.0--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metawrap-assembly-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-assembly-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-assembly-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metawrap-assembly-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metawrap-assembly-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metawrap-assembly-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bdf2gdfont.PLS

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.PLS
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config-metawrap

```bash
$ singularity exec <container> /usr/local/bin/config-metawrap
$ podman run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cvtbdf.pl

```bash
$ singularity exec <container> /usr/local/bin/cvtbdf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_asm_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_asm_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_asm_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_asm_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_sdbg_build

```bash
$ singularity exec <container> /usr/local/bin/megahit_sdbg_build
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_sdbg_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_sdbg_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaWRAP

```bash
$ singularity exec <container> /usr/local/bin/metaWRAP
$ podman run --it --rm --entrypoint /usr/local/bin/metaWRAP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaWRAP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metawrap

```bash
$ singularity exec <container> /usr/local/bin/metawrap
$ podman run --it --rm --entrypoint /usr/local/bin/metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pl2bat.pl

```bash
$ singularity exec <container> /usr/local/bin/pl2bat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pl2bat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pl2bat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icarus.py

```bash
$ singularity exec <container> /usr/local/bin/icarus.py
$ podman run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icarus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaquast

```bash
$ singularity exec <container> /usr/local/bin/metaquast
$ podman run --it --rm --entrypoint /usr/local/bin/metaquast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaquast.py

```bash
$ singularity exec <container> /usr/local/bin/metaquast.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaquast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/pair-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-missing-subranges

```bash
$ singularity exec <container> /usr/local/bin/print-missing-subranges
$ podman run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast

```bash
$ singularity exec <container> /usr/local/bin/quast
$ podman run --it --rm --entrypoint /usr/local/bin/quast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-busco

```bash
$ singularity exec <container> /usr/local/bin/quast-download-busco
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-busco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-busco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-gridss

```bash
$ singularity exec <container> /usr/local/bin/quast-download-gridss
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-gridss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-gridss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-download-silva

```bash
$ singularity exec <container> /usr/local/bin/quast-download-silva
$ podman run --it --rm --entrypoint /usr/local/bin/quast-download-silva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-download-silva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast-lg.py

```bash
$ singularity exec <container> /usr/local/bin/quast-lg.py
$ podman run --it --rm --entrypoint /usr/local/bin/quast-lg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast-lg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quast.py

```bash
$ singularity exec <container> /usr/local/bin/quast.py
$ podman run --it --rm --entrypoint /usr/local/bin/quast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-by-length

```bash
$ singularity exec <container> /usr/local/bin/sort-by-length
$ podman run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/xcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch

```bash
$ singularity exec <container> /usr/local/bin/xfetch
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch.ini

```bash
$ singularity exec <container> /usr/local/bin/xfetch.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfilter

```bash
$ singularity exec <container> /usr/local/bin/xfilter
$ podman run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xinfo

```bash
$ singularity exec <container> /usr/local/bin/xinfo
$ podman run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
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