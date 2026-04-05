---
layout: container
name:  "quay.io/biocontainers/genomesyn2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomesyn2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genomesyn2/container.yaml"
updated_at: "2026-04-05 04:48:20.270008"
latest: "1.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/genomesyn2"
aliases:
 - "GenomeSyn2"
 - "GenomeSyn2.pl"
 - "cairosvg"
 - "extract_mRNA_protein.info.pl"
 - "merge_synteny_info.pl"
 - "minimap2_paf2tsv.pl"
 - "mummer_coords2tsv.pl"
 - "run_blastp.sh"
 - "run_diamond.sh"
 - "run_minimap2.sh"
 - "run_mmseqs.sh"
 - "run_mummer.sh"
 - "syntax_suggest"
 - "yaggo"
 - "gffread"
 - "rbs"
 - "rdbg"
 - "typeprof"
 - "racc"
 - "bundle"
 - "bundler"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
 - "pair-at-a-time"
 - "print-missing-subranges"
 - "sort-by-length"
 - "xcommon.sh"
 - "xfetch"
 - "xfetch.ini"
 - "xfilter"
 - "xinfo"
 - "xlink"
 - "xlink.ini"
versions:
 - "1.1.0--hdfd78af_0"
description: "singularity registry hpc automated addition for genomesyn2"
config: {"url": "https://biocontainers.pro/tools/genomesyn2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for genomesyn2", "latest": {"1.1.0--hdfd78af_0": "sha256:fbc575403a7c188c7496fcc0a0ac8ee38e0d0f31c2920fc03f77988448e39ef4"}, "tags": {"1.1.0--hdfd78af_0": "sha256:fbc575403a7c188c7496fcc0a0ac8ee38e0d0f31c2920fc03f77988448e39ef4"}, "docker": "quay.io/biocontainers/genomesyn2", "aliases": {"GenomeSyn2": "/usr/local/bin/GenomeSyn2", "GenomeSyn2.pl": "/usr/local/bin/GenomeSyn2.pl", "cairosvg": "/usr/local/bin/cairosvg", "extract_mRNA_protein.info.pl": "/usr/local/bin/extract_mRNA_protein.info.pl", "merge_synteny_info.pl": "/usr/local/bin/merge_synteny_info.pl", "minimap2_paf2tsv.pl": "/usr/local/bin/minimap2_paf2tsv.pl", "mummer_coords2tsv.pl": "/usr/local/bin/mummer_coords2tsv.pl", "run_blastp.sh": "/usr/local/bin/run_blastp.sh", "run_diamond.sh": "/usr/local/bin/run_diamond.sh", "run_minimap2.sh": "/usr/local/bin/run_minimap2.sh", "run_mmseqs.sh": "/usr/local/bin/run_mmseqs.sh", "run_mummer.sh": "/usr/local/bin/run_mummer.sh", "syntax_suggest": "/usr/local/bin/syntax_suggest", "yaggo": "/usr/local/bin/yaggo", "gffread": "/usr/local/bin/gffread", "rbs": "/usr/local/bin/rbs", "rdbg": "/usr/local/bin/rdbg", "typeprof": "/usr/local/bin/typeprof", "racc": "/usr/local/bin/racc", "bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo", "xlink": "/usr/local/bin/xlink", "xlink.ini": "/usr/local/bin/xlink.ini"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomesyn2.
singularity registry hpc automated addition for genomesyn2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomesyn2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomesyn2:1.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomesyn2/1.1.0--hdfd78af_0
$ module help quay.io/biocontainers/genomesyn2/1.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomesyn2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomesyn2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomesyn2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomesyn2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomesyn2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomesyn2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GenomeSyn2

```bash
$ singularity exec <container> /usr/local/bin/GenomeSyn2
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeSyn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeSyn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenomeSyn2.pl

```bash
$ singularity exec <container> /usr/local/bin/GenomeSyn2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeSyn2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeSyn2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_mRNA_protein.info.pl

```bash
$ singularity exec <container> /usr/local/bin/extract_mRNA_protein.info.pl
$ podman run --it --rm --entrypoint /usr/local/bin/extract_mRNA_protein.info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_mRNA_protein.info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_synteny_info.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_synteny_info.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_synteny_info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_synteny_info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2_paf2tsv.pl

```bash
$ singularity exec <container> /usr/local/bin/minimap2_paf2tsv.pl
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2_paf2tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2_paf2tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer_coords2tsv.pl

```bash
$ singularity exec <container> /usr/local/bin/mummer_coords2tsv.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mummer_coords2tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer_coords2tsv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_blastp.sh

```bash
$ singularity exec <container> /usr/local/bin/run_blastp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_blastp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_blastp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_diamond.sh

```bash
$ singularity exec <container> /usr/local/bin/run_diamond.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_diamond.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_diamond.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_minimap2.sh

```bash
$ singularity exec <container> /usr/local/bin/run_minimap2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_minimap2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_minimap2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_mmseqs.sh

```bash
$ singularity exec <container> /usr/local/bin/run_mmseqs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_mmseqs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_mmseqs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_mummer.sh

```bash
$ singularity exec <container> /usr/local/bin/run_mummer.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_mummer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_mummer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### syntax_suggest

```bash
$ singularity exec <container> /usr/local/bin/syntax_suggest
$ podman run --it --rm --entrypoint /usr/local/bin/syntax_suggest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/syntax_suggest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yaggo

```bash
$ singularity exec <container> /usr/local/bin/yaggo
$ podman run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbs

```bash
$ singularity exec <container> /usr/local/bin/rbs
$ podman run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdbg

```bash
$ singularity exec <container> /usr/local/bin/rdbg
$ podman run --it --rm --entrypoint /usr/local/bin/rdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typeprof

```bash
$ singularity exec <container> /usr/local/bin/typeprof
$ podman run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc

```bash
$ singularity exec <container> /usr/local/bin/racc
$ podman run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle

```bash
$ singularity exec <container> /usr/local/bin/bundle
$ podman run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundler

```bash
$ singularity exec <container> /usr/local/bin/bundler
$ podman run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xlink

```bash
$ singularity exec <container> /usr/local/bin/xlink
$ podman run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink.ini

```bash
$ singularity exec <container> /usr/local/bin/xlink.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
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