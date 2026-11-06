---
layout: container
name:  "quay.io/biocontainers/hashbrown"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hashbrown/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hashbrown/container.yaml"
updated_at: "2026-11-06 18:07:53.085322"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hashbrown"
aliases:
 - "Bandage"
 - "fastahack"
 - "filtlong"
 - "gfa_connector"
 - "hashbrown"
 - "kmercounter"
 - "medaka_consensus_joint"
 - "medaka_variant"
 - "mosdepth"
 - "pl2bat.pl"
 - "polypolish"
 - "pypolca"
 - "saute"
 - "saute_prot"
 - "shasta"
 - "syntax_suggest"
 - "vcfnullgenofields"
 - "vcfwave"
 - "weasyprint"
 - "yaggo"
 - "medaka"
 - "medaka_consensus"
 - "medaka_counts"
 - "medaka_data_path"
 - "medaka_version_report"
 - "skesa"
 - "binspreader"
 - "demux_fast5"
 - "mini_align"
 - "pathracer-seq-fs"
 - "spades-hpc"
 - "icarus.py"
 - "metaquast"
 - "metaquast.py"
 - "pathracer"
 - "porechop"
 - "quast"
 - "quast-download-busco"
 - "quast-download-gridss"
 - "quast-download-silva"
 - "quast-lg.py"
 - "quast.py"
 - "check_compression"
 - "compress_fast5"
 - "spades-gfa-split"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for hashbrown"
config: {"url": "https://biocontainers.pro/tools/hashbrown", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hashbrown", "latest": {"1.1.0--pyhdfd78af_0": "sha256:78748a063b7fba76b6ff4a0ad036a8f0a53fdb2a6976bc9e4c0c5eaeda4303af"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:78748a063b7fba76b6ff4a0ad036a8f0a53fdb2a6976bc9e4c0c5eaeda4303af"}, "docker": "quay.io/biocontainers/hashbrown", "aliases": {"Bandage": "/usr/local/bin/Bandage", "fastahack": "/usr/local/bin/fastahack", "filtlong": "/usr/local/bin/filtlong", "gfa_connector": "/usr/local/bin/gfa_connector", "hashbrown": "/usr/local/bin/hashbrown", "kmercounter": "/usr/local/bin/kmercounter", "medaka_consensus_joint": "/usr/local/bin/medaka_consensus_joint", "medaka_variant": "/usr/local/bin/medaka_variant", "mosdepth": "/usr/local/bin/mosdepth", "pl2bat.pl": "/usr/local/bin/pl2bat.pl", "polypolish": "/usr/local/bin/polypolish", "pypolca": "/usr/local/bin/pypolca", "saute": "/usr/local/bin/saute", "saute_prot": "/usr/local/bin/saute_prot", "shasta": "/usr/local/bin/shasta", "syntax_suggest": "/usr/local/bin/syntax_suggest", "vcfnullgenofields": "/usr/local/bin/vcfnullgenofields", "vcfwave": "/usr/local/bin/vcfwave", "weasyprint": "/usr/local/bin/weasyprint", "yaggo": "/usr/local/bin/yaggo", "medaka": "/usr/local/bin/medaka", "medaka_consensus": "/usr/local/bin/medaka_consensus", "medaka_counts": "/usr/local/bin/medaka_counts", "medaka_data_path": "/usr/local/bin/medaka_data_path", "medaka_version_report": "/usr/local/bin/medaka_version_report", "skesa": "/usr/local/bin/skesa", "binspreader": "/usr/local/bin/binspreader", "demux_fast5": "/usr/local/bin/demux_fast5", "mini_align": "/usr/local/bin/mini_align", "pathracer-seq-fs": "/usr/local/bin/pathracer-seq-fs", "spades-hpc": "/usr/local/bin/spades-hpc", "icarus.py": "/usr/local/bin/icarus.py", "metaquast": "/usr/local/bin/metaquast", "metaquast.py": "/usr/local/bin/metaquast.py", "pathracer": "/usr/local/bin/pathracer", "porechop": "/usr/local/bin/porechop", "quast": "/usr/local/bin/quast", "quast-download-busco": "/usr/local/bin/quast-download-busco", "quast-download-gridss": "/usr/local/bin/quast-download-gridss", "quast-download-silva": "/usr/local/bin/quast-download-silva", "quast-lg.py": "/usr/local/bin/quast-lg.py", "quast.py": "/usr/local/bin/quast.py", "check_compression": "/usr/local/bin/check_compression", "compress_fast5": "/usr/local/bin/compress_fast5", "spades-gfa-split": "/usr/local/bin/spades-gfa-split"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hashbrown.
singularity registry hpc automated addition for hashbrown
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hashbrown
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hashbrown:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hashbrown/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/hashbrown/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hashbrown-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hashbrown-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hashbrown-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hashbrown-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hashbrown-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hashbrown-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bandage

```bash
$ singularity exec <container> /usr/local/bin/Bandage
$ podman run --it --rm --entrypoint /usr/local/bin/Bandage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bandage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastahack

```bash
$ singularity exec <container> /usr/local/bin/fastahack
$ podman run --it --rm --entrypoint /usr/local/bin/fastahack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastahack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filtlong

```bash
$ singularity exec <container> /usr/local/bin/filtlong
$ podman run --it --rm --entrypoint /usr/local/bin/filtlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filtlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa_connector

```bash
$ singularity exec <container> /usr/local/bin/gfa_connector
$ podman run --it --rm --entrypoint /usr/local/bin/gfa_connector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa_connector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hashbrown

```bash
$ singularity exec <container> /usr/local/bin/hashbrown
$ podman run --it --rm --entrypoint /usr/local/bin/hashbrown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hashbrown   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmercounter

```bash
$ singularity exec <container> /usr/local/bin/kmercounter
$ podman run --it --rm --entrypoint /usr/local/bin/kmercounter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmercounter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_consensus_joint

```bash
$ singularity exec <container> /usr/local/bin/medaka_consensus_joint
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_consensus_joint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_consensus_joint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_variant

```bash
$ singularity exec <container> /usr/local/bin/medaka_variant
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pl2bat.pl

```bash
$ singularity exec <container> /usr/local/bin/pl2bat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pl2bat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pl2bat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### polypolish

```bash
$ singularity exec <container> /usr/local/bin/polypolish
$ podman run --it --rm --entrypoint /usr/local/bin/polypolish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polypolish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypolca

```bash
$ singularity exec <container> /usr/local/bin/pypolca
$ podman run --it --rm --entrypoint /usr/local/bin/pypolca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypolca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saute

```bash
$ singularity exec <container> /usr/local/bin/saute
$ podman run --it --rm --entrypoint /usr/local/bin/saute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saute_prot

```bash
$ singularity exec <container> /usr/local/bin/saute_prot
$ podman run --it --rm --entrypoint /usr/local/bin/saute_prot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saute_prot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shasta

```bash
$ singularity exec <container> /usr/local/bin/shasta
$ podman run --it --rm --entrypoint /usr/local/bin/shasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### syntax_suggest

```bash
$ singularity exec <container> /usr/local/bin/syntax_suggest
$ podman run --it --rm --entrypoint /usr/local/bin/syntax_suggest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/syntax_suggest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnullgenofields

```bash
$ singularity exec <container> /usr/local/bin/vcfnullgenofields
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnullgenofields   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnullgenofields   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfwave

```bash
$ singularity exec <container> /usr/local/bin/vcfwave
$ podman run --it --rm --entrypoint /usr/local/bin/vcfwave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfwave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weasyprint

```bash
$ singularity exec <container> /usr/local/bin/weasyprint
$ podman run --it --rm --entrypoint /usr/local/bin/weasyprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weasyprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yaggo

```bash
$ singularity exec <container> /usr/local/bin/yaggo
$ podman run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka

```bash
$ singularity exec <container> /usr/local/bin/medaka
$ podman run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_consensus

```bash
$ singularity exec <container> /usr/local/bin/medaka_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_counts

```bash
$ singularity exec <container> /usr/local/bin/medaka_counts
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_data_path

```bash
$ singularity exec <container> /usr/local/bin/medaka_data_path
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_version_report

```bash
$ singularity exec <container> /usr/local/bin/medaka_version_report
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skesa

```bash
$ singularity exec <container> /usr/local/bin/skesa
$ podman run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binspreader

```bash
$ singularity exec <container> /usr/local/bin/binspreader
$ podman run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demux_fast5

```bash
$ singularity exec <container> /usr/local/bin/demux_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mini_align

```bash
$ singularity exec <container> /usr/local/bin/mini_align
$ podman run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer-seq-fs

```bash
$ singularity exec <container> /usr/local/bin/pathracer-seq-fs
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hpc

```bash
$ singularity exec <container> /usr/local/bin/spades-hpc
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pathracer

```bash
$ singularity exec <container> /usr/local/bin/pathracer
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### porechop

```bash
$ singularity exec <container> /usr/local/bin/porechop
$ podman run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### check_compression

```bash
$ singularity exec <container> /usr/local/bin/check_compression
$ podman run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress_fast5

```bash
$ singularity exec <container> /usr/local/bin/compress_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gfa-split

```bash
$ singularity exec <container> /usr/local/bin/spades-gfa-split
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
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