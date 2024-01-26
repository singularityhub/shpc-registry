---
layout: container
name:  "quay.io/biocontainers/eval"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eval/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eval/container.yaml"
updated_at: "2024-01-26 03:06:41.936984"
latest: "2.2.8--pl526_1"
container_url: "https://biocontainers.pro/tools/eval"
aliases:
 - "RangeFinder.py"
 - "combine_eval_reports.pl"
 - "eval.pl"
 - "evaluate_gtf.pl"
 - "filter_badlist.pl"
 - "filter_gtfs.pl"
 - "get_distribution.pl"
 - "get_general_stats.pl"
 - "get_overlap_stats.pl"
 - "gff3_to_gtf.pl"
 - "graph_gtfs.pl"
 - "make_intron_lenght_vs_performance_graph.pl"
 - "merge_gtf_transcripts.py"
 - "validate_gtf.pl"
 - "validate_splice_sites.pl"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "bp_aacomp.pl"
 - "bp_biofetch_genbank_proxy.pl"
 - "bp_bioflat_index.pl"
 - "bp_biogetseq.pl"
 - "bp_blast2tree.pl"
 - "bp_bulk_load_gff.pl"
 - "bp_chaos_plot.pl"
 - "bp_classify_hits_kingdom.pl"
versions:
 - "2.2.8--pl526_1"
description: "shpc-registry automated BioContainers addition for eval"
config: {"url": "https://biocontainers.pro/tools/eval", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eval", "latest": {"2.2.8--pl526_1": "sha256:8fc80165439a7328b8332e38f4063047bf60204244a6dcac9e499abff5bec2d9"}, "tags": {"2.2.8--pl526_1": "sha256:8fc80165439a7328b8332e38f4063047bf60204244a6dcac9e499abff5bec2d9"}, "docker": "quay.io/biocontainers/eval", "aliases": {"RangeFinder.py": "/usr/local/bin/RangeFinder.py", "combine_eval_reports.pl": "/usr/local/bin/combine_eval_reports.pl", "eval.pl": "/usr/local/bin/eval.pl", "evaluate_gtf.pl": "/usr/local/bin/evaluate_gtf.pl", "filter_badlist.pl": "/usr/local/bin/filter_badlist.pl", "filter_gtfs.pl": "/usr/local/bin/filter_gtfs.pl", "get_distribution.pl": "/usr/local/bin/get_distribution.pl", "get_general_stats.pl": "/usr/local/bin/get_general_stats.pl", "get_overlap_stats.pl": "/usr/local/bin/get_overlap_stats.pl", "gff3_to_gtf.pl": "/usr/local/bin/gff3_to_gtf.pl", "graph_gtfs.pl": "/usr/local/bin/graph_gtfs.pl", "make_intron_lenght_vs_performance_graph.pl": "/usr/local/bin/make_intron_lenght_vs_performance_graph.pl", "merge_gtf_transcripts.py": "/usr/local/bin/merge_gtf_transcripts.py", "validate_gtf.pl": "/usr/local/bin/validate_gtf.pl", "validate_splice_sites.pl": "/usr/local/bin/validate_splice_sites.pl", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "bp_aacomp.pl": "/usr/local/bin/bp_aacomp.pl", "bp_biofetch_genbank_proxy.pl": "/usr/local/bin/bp_biofetch_genbank_proxy.pl", "bp_bioflat_index.pl": "/usr/local/bin/bp_bioflat_index.pl", "bp_biogetseq.pl": "/usr/local/bin/bp_biogetseq.pl", "bp_blast2tree.pl": "/usr/local/bin/bp_blast2tree.pl", "bp_bulk_load_gff.pl": "/usr/local/bin/bp_bulk_load_gff.pl", "bp_chaos_plot.pl": "/usr/local/bin/bp_chaos_plot.pl", "bp_classify_hits_kingdom.pl": "/usr/local/bin/bp_classify_hits_kingdom.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eval.
shpc-registry automated BioContainers addition for eval
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eval
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eval:2.2.8--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eval/2.2.8--pl526_1
$ module help quay.io/biocontainers/eval/2.2.8--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eval-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eval-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eval-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eval-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eval-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eval-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RangeFinder.py

```bash
$ singularity exec <container> /usr/local/bin/RangeFinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/RangeFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RangeFinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_eval_reports.pl

```bash
$ singularity exec <container> /usr/local/bin/combine_eval_reports.pl
$ podman run --it --rm --entrypoint /usr/local/bin/combine_eval_reports.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_eval_reports.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval.pl

```bash
$ singularity exec <container> /usr/local/bin/eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evaluate_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/evaluate_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/evaluate_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluate_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_badlist.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_badlist.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_badlist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_badlist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_gtfs.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_gtfs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_gtfs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_gtfs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_distribution.pl

```bash
$ singularity exec <container> /usr/local/bin/get_distribution.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_distribution.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_distribution.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_general_stats.pl

```bash
$ singularity exec <container> /usr/local/bin/get_general_stats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_general_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_general_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_overlap_stats.pl

```bash
$ singularity exec <container> /usr/local/bin/get_overlap_stats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_overlap_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_overlap_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_to_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/gff3_to_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_to_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_to_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph_gtfs.pl

```bash
$ singularity exec <container> /usr/local/bin/graph_gtfs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/graph_gtfs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph_gtfs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_intron_lenght_vs_performance_graph.pl

```bash
$ singularity exec <container> /usr/local/bin/make_intron_lenght_vs_performance_graph.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_intron_lenght_vs_performance_graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_intron_lenght_vs_performance_graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_gtf_transcripts.py

```bash
$ singularity exec <container> /usr/local/bin/merge_gtf_transcripts.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_gtf_transcripts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_gtf_transcripts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/validate_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/validate_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate_splice_sites.pl

```bash
$ singularity exec <container> /usr/local/bin/validate_splice_sites.pl
$ podman run --it --rm --entrypoint /usr/local/bin/validate_splice_sites.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate_splice_sites.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2BSML.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_search2BSML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biofetch_genbank_proxy.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biofetch_genbank_proxy.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_blast2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_blast2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bulk_load_gff.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bulk_load_gff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_chaos_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_chaos_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_classify_hits_kingdom.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_classify_hits_kingdom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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