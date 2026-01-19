---
layout: container
name:  "quay.io/biocontainers/metawrap-binning"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metawrap-binning/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metawrap-binning/container.yaml"
updated_at: "2026-01-19 04:40:32.860361"
latest: "1.3.0"
container_url: "https://biocontainers.pro/tools/metawrap-binning"
aliases:
 - "aggregateBinDepths.pl"
 - "aggregateContigOverlapsByBin.pl"
 - "concoct"
 - "concoct_coverage_table.py"
 - "concoct_refine"
 - "contigOverlaps"
 - "cut_up_fasta.py"
 - "extract_fasta_bins.py"
 - "jgi_summarize_bam_contig_depths"
 - "merge_cutup_clustering.py"
 - "metabat"
 - "metabat1"
 - "metabat2"
 - "runMetaBat.sh"
 - "run_MaxBin.pl"
 - "bazel-scan.py"
 - "config-metawrap"
 - "fa2fq"
 - "filter_blat"
 - "filter_contigs"
 - "filterfa"
 - "idba"
 - "idba_hybrid"
 - "idba_tran"
 - "idba_tran_test"
 - "idba_ud"
 - "metaWRAP"
 - "metawrap"
 - "parallel_blat"
 - "parallel_rna_blat"
 - "print_graph"
 - "raw_n50"
 - "run-unittest.py"
 - "sample_reads"
 - "scaffold"
 - "scan.py"
 - "shuffle_reads"
 - "sim_reads"
 - "sim_reads_tran"
 - "sort_psl"
versions:
 - "1.3.0"
description: "singularity registry hpc automated addition for metawrap-binning"
config: {"url": "https://biocontainers.pro/tools/metawrap-binning", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metawrap-binning", "latest": {"1.3.0": "sha256:c0bc5e9af1036a75b22342f32846df7724898ad8a878f1886c96e3a743b13400"}, "tags": {"1.3.0": "sha256:c0bc5e9af1036a75b22342f32846df7724898ad8a878f1886c96e3a743b13400"}, "docker": "quay.io/biocontainers/metawrap-binning", "aliases": {"aggregateBinDepths.pl": "/usr/local/bin/aggregateBinDepths.pl", "aggregateContigOverlapsByBin.pl": "/usr/local/bin/aggregateContigOverlapsByBin.pl", "concoct": "/usr/local/bin/concoct", "concoct_coverage_table.py": "/usr/local/bin/concoct_coverage_table.py", "concoct_refine": "/usr/local/bin/concoct_refine", "contigOverlaps": "/usr/local/bin/contigOverlaps", "cut_up_fasta.py": "/usr/local/bin/cut_up_fasta.py", "extract_fasta_bins.py": "/usr/local/bin/extract_fasta_bins.py", "jgi_summarize_bam_contig_depths": "/usr/local/bin/jgi_summarize_bam_contig_depths", "merge_cutup_clustering.py": "/usr/local/bin/merge_cutup_clustering.py", "metabat": "/usr/local/bin/metabat", "metabat1": "/usr/local/bin/metabat1", "metabat2": "/usr/local/bin/metabat2", "runMetaBat.sh": "/usr/local/bin/runMetaBat.sh", "run_MaxBin.pl": "/usr/local/bin/run_MaxBin.pl", "bazel-scan.py": "/usr/local/bin/bazel-scan.py", "config-metawrap": "/usr/local/bin/config-metawrap", "fa2fq": "/usr/local/bin/fa2fq", "filter_blat": "/usr/local/bin/filter_blat", "filter_contigs": "/usr/local/bin/filter_contigs", "filterfa": "/usr/local/bin/filterfa", "idba": "/usr/local/bin/idba", "idba_hybrid": "/usr/local/bin/idba_hybrid", "idba_tran": "/usr/local/bin/idba_tran", "idba_tran_test": "/usr/local/bin/idba_tran_test", "idba_ud": "/usr/local/bin/idba_ud", "metaWRAP": "/usr/local/bin/metaWRAP", "metawrap": "/usr/local/bin/metawrap", "parallel_blat": "/usr/local/bin/parallel_blat", "parallel_rna_blat": "/usr/local/bin/parallel_rna_blat", "print_graph": "/usr/local/bin/print_graph", "raw_n50": "/usr/local/bin/raw_n50", "run-unittest.py": "/usr/local/bin/run-unittest.py", "sample_reads": "/usr/local/bin/sample_reads", "scaffold": "/usr/local/bin/scaffold", "scan.py": "/usr/local/bin/scan.py", "shuffle_reads": "/usr/local/bin/shuffle_reads", "sim_reads": "/usr/local/bin/sim_reads", "sim_reads_tran": "/usr/local/bin/sim_reads_tran", "sort_psl": "/usr/local/bin/sort_psl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metawrap-binning.
singularity registry hpc automated addition for metawrap-binning
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metawrap-binning
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metawrap-binning:1.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metawrap-binning/1.3.0
$ module help quay.io/biocontainers/metawrap-binning/1.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metawrap-binning-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-binning-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metawrap-binning-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metawrap-binning-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metawrap-binning-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metawrap-binning-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aggregateBinDepths.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateBinDepths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregateContigOverlapsByBin.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateContigOverlapsByBin.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoct

```bash
$ singularity exec <container> /usr/local/bin/concoct
$ podman run --it --rm --entrypoint /usr/local/bin/concoct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoct_coverage_table.py

```bash
$ singularity exec <container> /usr/local/bin/concoct_coverage_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/concoct_coverage_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct_coverage_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoct_refine

```bash
$ singularity exec <container> /usr/local/bin/concoct_refine
$ podman run --it --rm --entrypoint /usr/local/bin/concoct_refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct_refine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contigOverlaps

```bash
$ singularity exec <container> /usr/local/bin/contigOverlaps
$ podman run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut_up_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/cut_up_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/cut_up_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut_up_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_fasta_bins.py

```bash
$ singularity exec <container> /usr/local/bin/extract_fasta_bins.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_fasta_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_fasta_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jgi_summarize_bam_contig_depths

```bash
$ singularity exec <container> /usr/local/bin/jgi_summarize_bam_contig_depths
$ podman run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_cutup_clustering.py

```bash
$ singularity exec <container> /usr/local/bin/merge_cutup_clustering.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_cutup_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_cutup_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat

```bash
$ singularity exec <container> /usr/local/bin/metabat
$ podman run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat1

```bash
$ singularity exec <container> /usr/local/bin/metabat1
$ podman run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat2

```bash
$ singularity exec <container> /usr/local/bin/metabat2
$ podman run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMetaBat.sh

```bash
$ singularity exec <container> /usr/local/bin/runMetaBat.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_MaxBin.pl

```bash
$ singularity exec <container> /usr/local/bin/run_MaxBin.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_MaxBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_MaxBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bazel-scan.py

```bash
$ singularity exec <container> /usr/local/bin/bazel-scan.py
$ podman run --it --rm --entrypoint /usr/local/bin/bazel-scan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bazel-scan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config-metawrap

```bash
$ singularity exec <container> /usr/local/bin/config-metawrap
$ podman run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config-metawrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fa2fq

```bash
$ singularity exec <container> /usr/local/bin/fa2fq
$ podman run --it --rm --entrypoint /usr/local/bin/fa2fq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fa2fq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_blat

```bash
$ singularity exec <container> /usr/local/bin/filter_blat
$ podman run --it --rm --entrypoint /usr/local/bin/filter_blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_contigs

```bash
$ singularity exec <container> /usr/local/bin/filter_contigs
$ podman run --it --rm --entrypoint /usr/local/bin/filter_contigs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_contigs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterfa

```bash
$ singularity exec <container> /usr/local/bin/filterfa
$ podman run --it --rm --entrypoint /usr/local/bin/filterfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idba

```bash
$ singularity exec <container> /usr/local/bin/idba
$ podman run --it --rm --entrypoint /usr/local/bin/idba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idba_hybrid

```bash
$ singularity exec <container> /usr/local/bin/idba_hybrid
$ podman run --it --rm --entrypoint /usr/local/bin/idba_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idba_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idba_tran

```bash
$ singularity exec <container> /usr/local/bin/idba_tran
$ podman run --it --rm --entrypoint /usr/local/bin/idba_tran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idba_tran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idba_tran_test

```bash
$ singularity exec <container> /usr/local/bin/idba_tran_test
$ podman run --it --rm --entrypoint /usr/local/bin/idba_tran_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idba_tran_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idba_ud

```bash
$ singularity exec <container> /usr/local/bin/idba_ud
$ podman run --it --rm --entrypoint /usr/local/bin/idba_ud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idba_ud   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### parallel_blat

```bash
$ singularity exec <container> /usr/local/bin/parallel_blat
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_rna_blat

```bash
$ singularity exec <container> /usr/local/bin/parallel_rna_blat
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_rna_blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_rna_blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print_graph

```bash
$ singularity exec <container> /usr/local/bin/print_graph
$ podman run --it --rm --entrypoint /usr/local/bin/print_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raw_n50

```bash
$ singularity exec <container> /usr/local/bin/raw_n50
$ podman run --it --rm --entrypoint /usr/local/bin/raw_n50   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raw_n50   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-unittest.py

```bash
$ singularity exec <container> /usr/local/bin/run-unittest.py
$ podman run --it --rm --entrypoint /usr/local/bin/run-unittest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-unittest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample_reads

```bash
$ singularity exec <container> /usr/local/bin/sample_reads
$ podman run --it --rm --entrypoint /usr/local/bin/sample_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scaffold

```bash
$ singularity exec <container> /usr/local/bin/scaffold
$ podman run --it --rm --entrypoint /usr/local/bin/scaffold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scaffold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scan.py

```bash
$ singularity exec <container> /usr/local/bin/scan.py
$ podman run --it --rm --entrypoint /usr/local/bin/scan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffle_reads

```bash
$ singularity exec <container> /usr/local/bin/shuffle_reads
$ podman run --it --rm --entrypoint /usr/local/bin/shuffle_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffle_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sim_reads

```bash
$ singularity exec <container> /usr/local/bin/sim_reads
$ podman run --it --rm --entrypoint /usr/local/bin/sim_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sim_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sim_reads_tran

```bash
$ singularity exec <container> /usr/local/bin/sim_reads_tran
$ podman run --it --rm --entrypoint /usr/local/bin/sim_reads_tran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sim_reads_tran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort_psl

```bash
$ singularity exec <container> /usr/local/bin/sort_psl
$ podman run --it --rm --entrypoint /usr/local/bin/sort_psl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort_psl   -v ${PWD} -w ${PWD} <container> -c " $@"
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