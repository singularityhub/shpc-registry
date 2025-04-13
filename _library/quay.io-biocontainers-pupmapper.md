---
layout: container
name:  "quay.io/biocontainers/pupmapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pupmapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pupmapper/container.yaml"
updated_at: "2025-04-13 04:54:50.885291"
latest: "0.0.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pupmapper"
aliases:
 - "bedgraphtobigwig"
 - "bedtobigbed"
 - "bigbedinfo"
 - "bigbedtobed"
 - "bigtools"
 - "bigwigaverageoverbed"
 - "bigwiginfo"
 - "bigwigmerge"
 - "bigwigtobedgraph"
 - "bigwigvaluesoverbed"
 - "boostchr.pl"
 - "column_remover.pl.bak"
 - "create_randompairs.pl"
 - "duplicate_header_remover.pl.bak"
 - "fragment_4dnpairs.pl.bak"
 - "genmap"
 - "juicer_shortform2pairs.pl.bak"
 - "merged_nodup2pairs.pl.bak"
 - "old_merged_nodup2pairs.pl.bak"
 - "pupmapper"
 - "bam2pairs"
 - "column_remover.pl"
 - "duplicate_header_remover.pl"
 - "fragment_4dnpairs.pl"
 - "juicer_shortform2pairs.pl"
 - "merge-pairs.sh"
 - "merged_nodup2pairs.pl"
 - "old_merged_nodup2pairs.pl"
 - "pairix"
 - "pairs_merger"
 - "process_merged_nodup.sh"
 - "process_old_merged_nodup.sh"
 - "streamer_1d"
 - "annot-tsv"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "faidx"
 - "numpy-config"
versions:
 - "0.0.9--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pupmapper"
config: {"url": "https://biocontainers.pro/tools/pupmapper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pupmapper", "latest": {"0.0.9--pyhdfd78af_0": "sha256:3e81aaa19953bdf2ff725abc1cfeb9ce33f537d8d4ce5766e1bd3c73df6c71db"}, "tags": {"0.0.9--pyhdfd78af_0": "sha256:3e81aaa19953bdf2ff725abc1cfeb9ce33f537d8d4ce5766e1bd3c73df6c71db"}, "docker": "quay.io/biocontainers/pupmapper", "aliases": {"bedgraphtobigwig": "/usr/local/bin/bedgraphtobigwig", "bedtobigbed": "/usr/local/bin/bedtobigbed", "bigbedinfo": "/usr/local/bin/bigbedinfo", "bigbedtobed": "/usr/local/bin/bigbedtobed", "bigtools": "/usr/local/bin/bigtools", "bigwigaverageoverbed": "/usr/local/bin/bigwigaverageoverbed", "bigwiginfo": "/usr/local/bin/bigwiginfo", "bigwigmerge": "/usr/local/bin/bigwigmerge", "bigwigtobedgraph": "/usr/local/bin/bigwigtobedgraph", "bigwigvaluesoverbed": "/usr/local/bin/bigwigvaluesoverbed", "boostchr.pl": "/usr/local/bin/boostchr.pl", "column_remover.pl.bak": "/usr/local/bin/column_remover.pl.bak", "create_randompairs.pl": "/usr/local/bin/create_randompairs.pl", "duplicate_header_remover.pl.bak": "/usr/local/bin/duplicate_header_remover.pl.bak", "fragment_4dnpairs.pl.bak": "/usr/local/bin/fragment_4dnpairs.pl.bak", "genmap": "/usr/local/bin/genmap", "juicer_shortform2pairs.pl.bak": "/usr/local/bin/juicer_shortform2pairs.pl.bak", "merged_nodup2pairs.pl.bak": "/usr/local/bin/merged_nodup2pairs.pl.bak", "old_merged_nodup2pairs.pl.bak": "/usr/local/bin/old_merged_nodup2pairs.pl.bak", "pupmapper": "/usr/local/bin/pupmapper", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairix": "/usr/local/bin/pairix", "pairs_merger": "/usr/local/bin/pairs_merger", "process_merged_nodup.sh": "/usr/local/bin/process_merged_nodup.sh", "process_old_merged_nodup.sh": "/usr/local/bin/process_old_merged_nodup.sh", "streamer_1d": "/usr/local/bin/streamer_1d", "annot-tsv": "/usr/local/bin/annot-tsv", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "faidx": "/usr/local/bin/faidx", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pupmapper.
singularity registry hpc automated addition for pupmapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pupmapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pupmapper:0.0.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pupmapper/0.0.9--pyhdfd78af_0
$ module help quay.io/biocontainers/pupmapper/0.0.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pupmapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pupmapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pupmapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pupmapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pupmapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pupmapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedgraphtobigwig

```bash
$ singularity exec <container> /usr/local/bin/bedgraphtobigwig
$ podman run --it --rm --entrypoint /usr/local/bin/bedgraphtobigwig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedgraphtobigwig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtobigbed

```bash
$ singularity exec <container> /usr/local/bin/bedtobigbed
$ podman run --it --rm --entrypoint /usr/local/bin/bedtobigbed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtobigbed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigbedinfo

```bash
$ singularity exec <container> /usr/local/bin/bigbedinfo
$ podman run --it --rm --entrypoint /usr/local/bin/bigbedinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigbedinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigbedtobed

```bash
$ singularity exec <container> /usr/local/bin/bigbedtobed
$ podman run --it --rm --entrypoint /usr/local/bin/bigbedtobed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigbedtobed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigtools

```bash
$ singularity exec <container> /usr/local/bin/bigtools
$ podman run --it --rm --entrypoint /usr/local/bin/bigtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigaverageoverbed

```bash
$ singularity exec <container> /usr/local/bin/bigwigaverageoverbed
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigaverageoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigaverageoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwiginfo

```bash
$ singularity exec <container> /usr/local/bin/bigwiginfo
$ podman run --it --rm --entrypoint /usr/local/bin/bigwiginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwiginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigmerge

```bash
$ singularity exec <container> /usr/local/bin/bigwigmerge
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigtobedgraph

```bash
$ singularity exec <container> /usr/local/bin/bigwigtobedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigtobedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigtobedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigwigvaluesoverbed

```bash
$ singularity exec <container> /usr/local/bin/bigwigvaluesoverbed
$ podman run --it --rm --entrypoint /usr/local/bin/bigwigvaluesoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigwigvaluesoverbed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### boostchr.pl

```bash
$ singularity exec <container> /usr/local/bin/boostchr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_randompairs.pl

```bash
$ singularity exec <container> /usr/local/bin/create_randompairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/create_randompairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_randompairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genmap

```bash
$ singularity exec <container> /usr/local/bin/genmap
$ podman run --it --rm --entrypoint /usr/local/bin/genmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pupmapper

```bash
$ singularity exec <container> /usr/local/bin/pupmapper
$ podman run --it --rm --entrypoint /usr/local/bin/pupmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pupmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-pairs.sh

```bash
$ singularity exec <container> /usr/local/bin/merge-pairs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairix

```bash
$ singularity exec <container> /usr/local/bin/pairix
$ podman run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairs_merger

```bash
$ singularity exec <container> /usr/local/bin/pairs_merger
$ podman run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_merged_nodup.sh

```bash
$ singularity exec <container> /usr/local/bin/process_merged_nodup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_old_merged_nodup.sh

```bash
$ singularity exec <container> /usr/local/bin/process_old_merged_nodup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_old_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_old_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamer_1d

```bash
$ singularity exec <container> /usr/local/bin/streamer_1d
$ podman run --it --rm --entrypoint /usr/local/bin/streamer_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamer_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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