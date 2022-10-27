---
layout: container
name:  "quay.io/biocontainers/guessmylt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/guessmylt/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/guessmylt/container.yaml"
updated_at: "2022-10-27 01:15:34.906706"
latest: "0.2.5--py_0"
container_url: "https://biocontainers.pro/tools/guessmylt"
aliases:
 - ".busco-post-link.sh"
 - "GUESSmyLT"
 - "GUESSmyLT-example"
 - "PtR"
 - "Trinity"
 - "TrinityStats.pl"
 - "Trinity_gene_splice_modeler.py"
 - "abundance_estimates_to_matrix.pl"
 - "align_and_estimate_abundance.pl"
 - "analyze_blastPlus_topHit_coverage.pl"
 - "analyze_diff_expr.pl"
 - "autoRun.pathInfo"
 - "b2"
 - "bamtools-2.4.1"
 - "bjam"
 - "contig_ExN50_statistic.pl"
 - "define_clusters_by_cutting_tree.pl"
 - "espoca"
 - "extract_supertranscript_from_reference.py"
 - "filterGenesIn_mRNAname.pl.patch"
 - "filter_low_expr_transcripts.pl"
 - "generate_plot"
 - "generate_plot.py"
 - "get_Trinity_gene_to_trans_map.pl"
 - "gtf2gff.pl.origexit"
 - "insilico_read_normalization.pl"
 - "intron2exex.pl"
 - "ratewig.pl"
 - "retrieve_sequences_from_fasta.pl"
 - "run_BUSCO.py"
 - "run_DE_analysis.pl"
 - "run_DE_analysis_from_samples_file.pl"
 - "run_Trinity_from_samples_file.pl"
 - "run_busco"
 - "run_expr_quantification_from_samples_file.pl"
 - "seqtk-trinity"
 - "webserver-results.body"
versions:
 - "0.2.5--py_0"
description: "shpc-registry automated BioContainers addition for guessmylt"
config: {"url": "https://biocontainers.pro/tools/guessmylt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for guessmylt", "latest": {"0.2.5--py_0": "sha256:aa7fceb1b8c605680f47115d5a56785367ffe1dbafdafa599eec6b067cafe719"}, "tags": {"0.2.5--py_0": "sha256:aa7fceb1b8c605680f47115d5a56785367ffe1dbafdafa599eec6b067cafe719"}, "docker": "quay.io/biocontainers/guessmylt", "aliases": {".busco-post-link.sh": "/usr/local/bin/.busco-post-link.sh", "GUESSmyLT": "/usr/local/bin/GUESSmyLT", "GUESSmyLT-example": "/usr/local/bin/GUESSmyLT-example", "PtR": "/usr/local/bin/PtR", "Trinity": "/usr/local/bin/Trinity", "TrinityStats.pl": "/usr/local/bin/TrinityStats.pl", "Trinity_gene_splice_modeler.py": "/usr/local/bin/Trinity_gene_splice_modeler.py", "abundance_estimates_to_matrix.pl": "/usr/local/bin/abundance_estimates_to_matrix.pl", "align_and_estimate_abundance.pl": "/usr/local/bin/align_and_estimate_abundance.pl", "analyze_blastPlus_topHit_coverage.pl": "/usr/local/bin/analyze_blastPlus_topHit_coverage.pl", "analyze_diff_expr.pl": "/usr/local/bin/analyze_diff_expr.pl", "autoRun.pathInfo": "/usr/local/bin/autoRun.pathInfo", "b2": "/usr/local/bin/b2", "bamtools-2.4.1": "/usr/local/bin/bamtools-2.4.1", "bjam": "/usr/local/bin/bjam", "contig_ExN50_statistic.pl": "/usr/local/bin/contig_ExN50_statistic.pl", "define_clusters_by_cutting_tree.pl": "/usr/local/bin/define_clusters_by_cutting_tree.pl", "espoca": "/usr/local/bin/espoca", "extract_supertranscript_from_reference.py": "/usr/local/bin/extract_supertranscript_from_reference.py", "filterGenesIn_mRNAname.pl.patch": "/usr/local/bin/filterGenesIn_mRNAname.pl.patch", "filter_low_expr_transcripts.pl": "/usr/local/bin/filter_low_expr_transcripts.pl", "generate_plot": "/usr/local/bin/generate_plot", "generate_plot.py": "/usr/local/bin/generate_plot.py", "get_Trinity_gene_to_trans_map.pl": "/usr/local/bin/get_Trinity_gene_to_trans_map.pl", "gtf2gff.pl.origexit": "/usr/local/bin/gtf2gff.pl.origexit", "insilico_read_normalization.pl": "/usr/local/bin/insilico_read_normalization.pl", "intron2exex.pl": "/usr/local/bin/intron2exex.pl", "ratewig.pl": "/usr/local/bin/ratewig.pl", "retrieve_sequences_from_fasta.pl": "/usr/local/bin/retrieve_sequences_from_fasta.pl", "run_BUSCO.py": "/usr/local/bin/run_BUSCO.py", "run_DE_analysis.pl": "/usr/local/bin/run_DE_analysis.pl", "run_DE_analysis_from_samples_file.pl": "/usr/local/bin/run_DE_analysis_from_samples_file.pl", "run_Trinity_from_samples_file.pl": "/usr/local/bin/run_Trinity_from_samples_file.pl", "run_busco": "/usr/local/bin/run_busco", "run_expr_quantification_from_samples_file.pl": "/usr/local/bin/run_expr_quantification_from_samples_file.pl", "seqtk-trinity": "/usr/local/bin/seqtk-trinity", "webserver-results.body": "/usr/local/bin/webserver-results.body"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/guessmylt.
shpc-registry automated BioContainers addition for guessmylt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/guessmylt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/guessmylt:0.2.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/guessmylt/0.2.5--py_0
$ module help quay.io/biocontainers/guessmylt/0.2.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### guessmylt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### guessmylt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### guessmylt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### guessmylt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### guessmylt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### guessmylt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .busco-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.busco-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.busco-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.busco-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GUESSmyLT

```bash
$ singularity exec <container> /usr/local/bin/GUESSmyLT
$ podman run --it --rm --entrypoint /usr/local/bin/GUESSmyLT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GUESSmyLT   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GUESSmyLT-example

```bash
$ singularity exec <container> /usr/local/bin/GUESSmyLT-example
$ podman run --it --rm --entrypoint /usr/local/bin/GUESSmyLT-example   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GUESSmyLT-example   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PtR

```bash
$ singularity exec <container> /usr/local/bin/PtR
$ podman run --it --rm --entrypoint /usr/local/bin/PtR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PtR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Trinity

```bash
$ singularity exec <container> /usr/local/bin/Trinity
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TrinityStats.pl

```bash
$ singularity exec <container> /usr/local/bin/TrinityStats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TrinityStats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TrinityStats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Trinity_gene_splice_modeler.py

```bash
$ singularity exec <container> /usr/local/bin/Trinity_gene_splice_modeler.py
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity_gene_splice_modeler.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity_gene_splice_modeler.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abundance_estimates_to_matrix.pl

```bash
$ singularity exec <container> /usr/local/bin/abundance_estimates_to_matrix.pl
$ podman run --it --rm --entrypoint /usr/local/bin/abundance_estimates_to_matrix.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abundance_estimates_to_matrix.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_and_estimate_abundance.pl

```bash
$ singularity exec <container> /usr/local/bin/align_and_estimate_abundance.pl
$ podman run --it --rm --entrypoint /usr/local/bin/align_and_estimate_abundance.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_and_estimate_abundance.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyze_blastPlus_topHit_coverage.pl

```bash
$ singularity exec <container> /usr/local/bin/analyze_blastPlus_topHit_coverage.pl
$ podman run --it --rm --entrypoint /usr/local/bin/analyze_blastPlus_topHit_coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze_blastPlus_topHit_coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyze_diff_expr.pl

```bash
$ singularity exec <container> /usr/local/bin/analyze_diff_expr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/analyze_diff_expr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze_diff_expr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoRun.pathInfo

```bash
$ singularity exec <container> /usr/local/bin/autoRun.pathInfo
$ podman run --it --rm --entrypoint /usr/local/bin/autoRun.pathInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoRun.pathInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2

```bash
$ singularity exec <container> /usr/local/bin/b2
$ podman run --it --rm --entrypoint /usr/local/bin/b2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools-2.4.1

```bash
$ singularity exec <container> /usr/local/bin/bamtools-2.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bjam

```bash
$ singularity exec <container> /usr/local/bin/bjam
$ podman run --it --rm --entrypoint /usr/local/bin/bjam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bjam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contig_ExN50_statistic.pl

```bash
$ singularity exec <container> /usr/local/bin/contig_ExN50_statistic.pl
$ podman run --it --rm --entrypoint /usr/local/bin/contig_ExN50_statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contig_ExN50_statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### define_clusters_by_cutting_tree.pl

```bash
$ singularity exec <container> /usr/local/bin/define_clusters_by_cutting_tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/define_clusters_by_cutting_tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/define_clusters_by_cutting_tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### espoca

```bash
$ singularity exec <container> /usr/local/bin/espoca
$ podman run --it --rm --entrypoint /usr/local/bin/espoca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/espoca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_supertranscript_from_reference.py

```bash
$ singularity exec <container> /usr/local/bin/extract_supertranscript_from_reference.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_supertranscript_from_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_supertranscript_from_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterGenesIn_mRNAname.pl.patch

```bash
$ singularity exec <container> /usr/local/bin/filterGenesIn_mRNAname.pl.patch
$ podman run --it --rm --entrypoint /usr/local/bin/filterGenesIn_mRNAname.pl.patch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterGenesIn_mRNAname.pl.patch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_low_expr_transcripts.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_low_expr_transcripts.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_low_expr_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_low_expr_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_plot

```bash
$ singularity exec <container> /usr/local/bin/generate_plot
$ podman run --it --rm --entrypoint /usr/local/bin/generate_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_plot.py

```bash
$ singularity exec <container> /usr/local/bin/generate_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_Trinity_gene_to_trans_map.pl

```bash
$ singularity exec <container> /usr/local/bin/get_Trinity_gene_to_trans_map.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_Trinity_gene_to_trans_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_Trinity_gene_to_trans_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2gff.pl.origexit

```bash
$ singularity exec <container> /usr/local/bin/gtf2gff.pl.origexit
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2gff.pl.origexit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2gff.pl.origexit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### insilico_read_normalization.pl

```bash
$ singularity exec <container> /usr/local/bin/insilico_read_normalization.pl
$ podman run --it --rm --entrypoint /usr/local/bin/insilico_read_normalization.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/insilico_read_normalization.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron2exex.pl

```bash
$ singularity exec <container> /usr/local/bin/intron2exex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/intron2exex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron2exex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ratewig.pl

```bash
$ singularity exec <container> /usr/local/bin/ratewig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ratewig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ratewig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retrieve_sequences_from_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/retrieve_sequences_from_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/retrieve_sequences_from_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retrieve_sequences_from_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_BUSCO.py

```bash
$ singularity exec <container> /usr/local/bin/run_BUSCO.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_BUSCO.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_BUSCO.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_DE_analysis.pl

```bash
$ singularity exec <container> /usr/local/bin/run_DE_analysis.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_DE_analysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_DE_analysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_DE_analysis_from_samples_file.pl

```bash
$ singularity exec <container> /usr/local/bin/run_DE_analysis_from_samples_file.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_DE_analysis_from_samples_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_DE_analysis_from_samples_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_Trinity_from_samples_file.pl

```bash
$ singularity exec <container> /usr/local/bin/run_Trinity_from_samples_file.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_Trinity_from_samples_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_Trinity_from_samples_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_busco

```bash
$ singularity exec <container> /usr/local/bin/run_busco
$ podman run --it --rm --entrypoint /usr/local/bin/run_busco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_busco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_expr_quantification_from_samples_file.pl

```bash
$ singularity exec <container> /usr/local/bin/run_expr_quantification_from_samples_file.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_expr_quantification_from_samples_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_expr_quantification_from_samples_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk-trinity

```bash
$ singularity exec <container> /usr/local/bin/seqtk-trinity
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk-trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk-trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webserver-results.body

```bash
$ singularity exec <container> /usr/local/bin/webserver-results.body
$ podman run --it --rm --entrypoint /usr/local/bin/webserver-results.body   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webserver-results.body   -v ${PWD} -w ${PWD} <container> -c " $@"
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