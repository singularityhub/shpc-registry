---
layout: container
name:  "quay.io/biocontainers/metasmash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metasmash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metasmash/container.yaml"
updated_at: "2026-04-27 05:30:01.580196"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metasmash"
aliases:
 - "brawn"
 - "download-antismash-databases"
 - "hmmalign2"
 - "hmmbuild2"
 - "hmmcalibrate2"
 - "hmmconvert2"
 - "hmmemit2"
 - "hmmfetch2"
 - "hmmindex2"
 - "hmmpfam2"
 - "hmmsearch2"
 - "metasmash"
 - "moods-dna.py"
 - "pysassc"
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
 - "xsearch"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for metasmash"
config: {"url": "https://biocontainers.pro/tools/metasmash", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metasmash", "latest": {"0.1.0--pyhdfd78af_0": "sha256:7d4bafb9952292119fef53f58b09c7ef26cb7282c7c766793fc02b194012b918"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:7d4bafb9952292119fef53f58b09c7ef26cb7282c7c766793fc02b194012b918"}, "docker": "quay.io/biocontainers/metasmash", "aliases": {"brawn": "/usr/local/bin/brawn", "download-antismash-databases": "/usr/local/bin/download-antismash-databases", "hmmalign2": "/usr/local/bin/hmmalign2", "hmmbuild2": "/usr/local/bin/hmmbuild2", "hmmcalibrate2": "/usr/local/bin/hmmcalibrate2", "hmmconvert2": "/usr/local/bin/hmmconvert2", "hmmemit2": "/usr/local/bin/hmmemit2", "hmmfetch2": "/usr/local/bin/hmmfetch2", "hmmindex2": "/usr/local/bin/hmmindex2", "hmmpfam2": "/usr/local/bin/hmmpfam2", "hmmsearch2": "/usr/local/bin/hmmsearch2", "metasmash": "/usr/local/bin/metasmash", "moods-dna.py": "/usr/local/bin/moods-dna.py", "pysassc": "/usr/local/bin/pysassc", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo", "xlink": "/usr/local/bin/xlink", "xlink.ini": "/usr/local/bin/xlink.ini", "xsearch": "/usr/local/bin/xsearch", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metasmash.
singularity registry hpc automated addition for metasmash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metasmash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metasmash:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metasmash/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/metasmash/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metasmash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metasmash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metasmash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metasmash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metasmash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metasmash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### brawn

```bash
$ singularity exec <container> /usr/local/bin/brawn
$ podman run --it --rm --entrypoint /usr/local/bin/brawn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brawn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-antismash-databases

```bash
$ singularity exec <container> /usr/local/bin/download-antismash-databases
$ podman run --it --rm --entrypoint /usr/local/bin/download-antismash-databases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-antismash-databases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmalign2

```bash
$ singularity exec <container> /usr/local/bin/hmmalign2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmbuild2

```bash
$ singularity exec <container> /usr/local/bin/hmmbuild2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmcalibrate2

```bash
$ singularity exec <container> /usr/local/bin/hmmcalibrate2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert2

```bash
$ singularity exec <container> /usr/local/bin/hmmconvert2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit2

```bash
$ singularity exec <container> /usr/local/bin/hmmemit2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmfetch2

```bash
$ singularity exec <container> /usr/local/bin/hmmfetch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmindex2

```bash
$ singularity exec <container> /usr/local/bin/hmmindex2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpfam2

```bash
$ singularity exec <container> /usr/local/bin/hmmpfam2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsearch2

```bash
$ singularity exec <container> /usr/local/bin/hmmsearch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metasmash

```bash
$ singularity exec <container> /usr/local/bin/metasmash
$ podman run --it --rm --entrypoint /usr/local/bin/metasmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metasmash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moods-dna.py

```bash
$ singularity exec <container> /usr/local/bin/moods-dna.py
$ podman run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysassc

```bash
$ singularity exec <container> /usr/local/bin/pysassc
$ podman run --it --rm --entrypoint /usr/local/bin/pysassc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysassc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xsearch

```bash
$ singularity exec <container> /usr/local/bin/xsearch
$ podman run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_print_template.py

```bash
$ singularity exec <container> /usr/local/bin/align_print_template.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_extract_ranges.py

```bash
$ singularity exec <container> /usr/local/bin/axt_extract_ranges.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_lav.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_lav.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_maf.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_maf.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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