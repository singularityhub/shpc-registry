---
layout: container
name:  "quay.io/biocontainers/cmfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cmfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cmfinder/container.yaml"
updated_at: "2023-07-11 03:16:27.128152"
latest: "0.4.1.9--h470a237_2"
container_url: "https://biocontainers.pro/tools/cmfinder"
aliases:
 - "COPYRIGHT"
 - "RNAPhylo"
 - "ScoreMotif.pl"
 - "Stockholm.pm"
 - "_cmfinder.pl"
 - "align"
 - "canda"
 - "candf"
 - "cands"
 - "cmfinder"
 - "cmfinder.pl"
 - "cmfinder04"
 - "cmfinder04.pl"
 - "comb_motif.pl"
 - "compare_motif.pl"
 - "count_seq"
 - "diff_motif"
 - "fasta2col"
 - "filter.pl"
 - "findphyl"
 - "hmmpair"
 - "io.pl"
 - "merge_motif.pl"
 - "mltree"
 - "perl5.22.2"
 - "rank_cmfinder.pl"
 - "rm_dup.pl"
 - "select_cmfinder.pl"
 - "sreformat"
 - "summarize"
 - "summary_rank.pl"
 - "test_pcre"
 - "blastdbcp"
 - "gene_info_reader"
 - "seqdb_demo"
 - "seqdb_perf"
 - "clustalw"
 - "c2ph"
 - "pstruct"
 - "seedtop"
 - "cluster"
versions:
 - "0.4.1.9--h470a237_2"
description: "shpc-registry automated BioContainers addition for cmfinder"
config: {"url": "https://biocontainers.pro/tools/cmfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cmfinder", "latest": {"0.4.1.9--h470a237_2": "sha256:ada3bd095628a1dfe42895e0e3f67218947d97cd4d6ed60bec40802236b956c9"}, "tags": {"0.4.1.9--h470a237_2": "sha256:ada3bd095628a1dfe42895e0e3f67218947d97cd4d6ed60bec40802236b956c9"}, "docker": "quay.io/biocontainers/cmfinder", "aliases": {"COPYRIGHT": "/usr/local/bin/COPYRIGHT", "RNAPhylo": "/usr/local/bin/RNAPhylo", "ScoreMotif.pl": "/usr/local/bin/ScoreMotif.pl", "Stockholm.pm": "/usr/local/bin/Stockholm.pm", "_cmfinder.pl": "/usr/local/bin/_cmfinder.pl", "align": "/usr/local/bin/align", "canda": "/usr/local/bin/canda", "candf": "/usr/local/bin/candf", "cands": "/usr/local/bin/cands", "cmfinder": "/usr/local/bin/cmfinder", "cmfinder.pl": "/usr/local/bin/cmfinder.pl", "cmfinder04": "/usr/local/bin/cmfinder04", "cmfinder04.pl": "/usr/local/bin/cmfinder04.pl", "comb_motif.pl": "/usr/local/bin/comb_motif.pl", "compare_motif.pl": "/usr/local/bin/compare_motif.pl", "count_seq": "/usr/local/bin/count_seq", "diff_motif": "/usr/local/bin/diff_motif", "fasta2col": "/usr/local/bin/fasta2col", "filter.pl": "/usr/local/bin/filter.pl", "findphyl": "/usr/local/bin/findphyl", "hmmpair": "/usr/local/bin/hmmpair", "io.pl": "/usr/local/bin/io.pl", "merge_motif.pl": "/usr/local/bin/merge_motif.pl", "mltree": "/usr/local/bin/mltree", "perl5.22.2": "/usr/local/bin/perl5.22.2", "rank_cmfinder.pl": "/usr/local/bin/rank_cmfinder.pl", "rm_dup.pl": "/usr/local/bin/rm_dup.pl", "select_cmfinder.pl": "/usr/local/bin/select_cmfinder.pl", "sreformat": "/usr/local/bin/sreformat", "summarize": "/usr/local/bin/summarize", "summary_rank.pl": "/usr/local/bin/summary_rank.pl", "test_pcre": "/usr/local/bin/test_pcre", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf", "clustalw": "/usr/local/bin/clustalw", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "seedtop": "/usr/local/bin/seedtop", "cluster": "/usr/local/bin/cluster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cmfinder.
shpc-registry automated BioContainers addition for cmfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cmfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cmfinder:0.4.1.9--h470a237_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cmfinder/0.4.1.9--h470a237_2
$ module help quay.io/biocontainers/cmfinder/0.4.1.9--h470a237_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cmfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cmfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cmfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cmfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cmfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cmfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### COPYRIGHT

```bash
$ singularity exec <container> /usr/local/bin/COPYRIGHT
$ podman run --it --rm --entrypoint /usr/local/bin/COPYRIGHT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COPYRIGHT   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAPhylo

```bash
$ singularity exec <container> /usr/local/bin/RNAPhylo
$ podman run --it --rm --entrypoint /usr/local/bin/RNAPhylo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAPhylo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ScoreMotif.pl

```bash
$ singularity exec <container> /usr/local/bin/ScoreMotif.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ScoreMotif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ScoreMotif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Stockholm.pm

```bash
$ singularity exec <container> /usr/local/bin/Stockholm.pm
$ podman run --it --rm --entrypoint /usr/local/bin/Stockholm.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Stockholm.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _cmfinder.pl

```bash
$ singularity exec <container> /usr/local/bin/_cmfinder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/_cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align

```bash
$ singularity exec <container> /usr/local/bin/align
$ podman run --it --rm --entrypoint /usr/local/bin/align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canda

```bash
$ singularity exec <container> /usr/local/bin/canda
$ podman run --it --rm --entrypoint /usr/local/bin/canda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### candf

```bash
$ singularity exec <container> /usr/local/bin/candf
$ podman run --it --rm --entrypoint /usr/local/bin/candf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/candf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cands

```bash
$ singularity exec <container> /usr/local/bin/cands
$ podman run --it --rm --entrypoint /usr/local/bin/cands   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cands   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfinder

```bash
$ singularity exec <container> /usr/local/bin/cmfinder
$ podman run --it --rm --entrypoint /usr/local/bin/cmfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfinder.pl

```bash
$ singularity exec <container> /usr/local/bin/cmfinder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfinder04

```bash
$ singularity exec <container> /usr/local/bin/cmfinder04
$ podman run --it --rm --entrypoint /usr/local/bin/cmfinder04   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfinder04   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfinder04.pl

```bash
$ singularity exec <container> /usr/local/bin/cmfinder04.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cmfinder04.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfinder04.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comb_motif.pl

```bash
$ singularity exec <container> /usr/local/bin/comb_motif.pl
$ podman run --it --rm --entrypoint /usr/local/bin/comb_motif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comb_motif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_motif.pl

```bash
$ singularity exec <container> /usr/local/bin/compare_motif.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compare_motif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_motif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count_seq

```bash
$ singularity exec <container> /usr/local/bin/count_seq
$ podman run --it --rm --entrypoint /usr/local/bin/count_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diff_motif

```bash
$ singularity exec <container> /usr/local/bin/diff_motif
$ podman run --it --rm --entrypoint /usr/local/bin/diff_motif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diff_motif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2col

```bash
$ singularity exec <container> /usr/local/bin/fasta2col
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2col   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2col   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter.pl

```bash
$ singularity exec <container> /usr/local/bin/filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findphyl

```bash
$ singularity exec <container> /usr/local/bin/findphyl
$ podman run --it --rm --entrypoint /usr/local/bin/findphyl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findphyl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpair

```bash
$ singularity exec <container> /usr/local/bin/hmmpair
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### io.pl

```bash
$ singularity exec <container> /usr/local/bin/io.pl
$ podman run --it --rm --entrypoint /usr/local/bin/io.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_motif.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_motif.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_motif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_motif.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mltree

```bash
$ singularity exec <container> /usr/local/bin/mltree
$ podman run --it --rm --entrypoint /usr/local/bin/mltree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mltree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rank_cmfinder.pl

```bash
$ singularity exec <container> /usr/local/bin/rank_cmfinder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rank_cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rank_cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rm_dup.pl

```bash
$ singularity exec <container> /usr/local/bin/rm_dup.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rm_dup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rm_dup.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_cmfinder.pl

```bash
$ singularity exec <container> /usr/local/bin/select_cmfinder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_cmfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sreformat

```bash
$ singularity exec <container> /usr/local/bin/sreformat
$ podman run --it --rm --entrypoint /usr/local/bin/sreformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sreformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarize

```bash
$ singularity exec <container> /usr/local/bin/summarize
$ podman run --it --rm --entrypoint /usr/local/bin/summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summary_rank.pl

```bash
$ singularity exec <container> /usr/local/bin/summary_rank.pl
$ podman run --it --rm --entrypoint /usr/local/bin/summary_rank.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summary_rank.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcp

```bash
$ singularity exec <container> /usr/local/bin/blastdbcp
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_info_reader

```bash
$ singularity exec <container> /usr/local/bin/gene_info_reader
$ podman run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_demo

```bash
$ singularity exec <container> /usr/local/bin/seqdb_demo
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_perf

```bash
$ singularity exec <container> /usr/local/bin/seqdb_perf
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw

```bash
$ singularity exec <container> /usr/local/bin/clustalw
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seedtop

```bash
$ singularity exec <container> /usr/local/bin/seedtop
$ podman run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster

```bash
$ singularity exec <container> /usr/local/bin/cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
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