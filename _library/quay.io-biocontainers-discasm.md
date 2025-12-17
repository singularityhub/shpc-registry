---
layout: container
name:  "quay.io/biocontainers/discasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/discasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/discasm/container.yaml"
updated_at: "2025-12-17 03:41:36.381862"
latest: "0.1.3--1"
container_url: "https://biocontainers.pro/tools/discasm"
aliases:
 - "DISCASM"
 - "PtR"
 - "Trinity"
 - "TrinityStats.pl"
 - "Trinity_gene_splice_modeler.py"
 - "abundance_estimates_to_matrix.pl"
 - "align_and_estimate_abundance.pl"
 - "analyze_blastPlus_topHit_coverage.pl"
 - "analyze_diff_expr.pl"
 - "contig_ExN50_statistic.pl"
 - "define_clusters_by_cutting_tree.pl"
 - "extract_supertranscript_from_reference.py"
 - "filter_low_expr_transcripts.pl"
 - "get_Trinity_gene_to_trans_map.pl"
 - "insilico_read_normalization.pl"
 - "oases"
 - "oases_pipeline.py"
 - "retrieve_sequences_from_fasta.pl"
 - "run_DE_analysis.pl"
 - "run_DE_analysis_from_samples_file.pl"
 - "seqtk-trinity"
 - "sift_bam_max_cov.pl"
 - "salmon"
 - "STAR"
 - "STARlong"
 - "velvetg"
 - "velveth"
 - "giffilter"
 - "gifsponge"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
versions:
 - "0.1.3--1"
description: "shpc-registry automated BioContainers addition for discasm"
config: {"url": "https://biocontainers.pro/tools/discasm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for discasm", "latest": {"0.1.3--1": "sha256:84390168a720688448aba016ae87f070692045f8f4dcb13b7a7e4af0561e1a77"}, "tags": {"0.1.3--1": "sha256:84390168a720688448aba016ae87f070692045f8f4dcb13b7a7e4af0561e1a77"}, "docker": "quay.io/biocontainers/discasm", "aliases": {"DISCASM": "/usr/local/bin/DISCASM", "PtR": "/usr/local/bin/PtR", "Trinity": "/usr/local/bin/Trinity", "TrinityStats.pl": "/usr/local/bin/TrinityStats.pl", "Trinity_gene_splice_modeler.py": "/usr/local/bin/Trinity_gene_splice_modeler.py", "abundance_estimates_to_matrix.pl": "/usr/local/bin/abundance_estimates_to_matrix.pl", "align_and_estimate_abundance.pl": "/usr/local/bin/align_and_estimate_abundance.pl", "analyze_blastPlus_topHit_coverage.pl": "/usr/local/bin/analyze_blastPlus_topHit_coverage.pl", "analyze_diff_expr.pl": "/usr/local/bin/analyze_diff_expr.pl", "contig_ExN50_statistic.pl": "/usr/local/bin/contig_ExN50_statistic.pl", "define_clusters_by_cutting_tree.pl": "/usr/local/bin/define_clusters_by_cutting_tree.pl", "extract_supertranscript_from_reference.py": "/usr/local/bin/extract_supertranscript_from_reference.py", "filter_low_expr_transcripts.pl": "/usr/local/bin/filter_low_expr_transcripts.pl", "get_Trinity_gene_to_trans_map.pl": "/usr/local/bin/get_Trinity_gene_to_trans_map.pl", "insilico_read_normalization.pl": "/usr/local/bin/insilico_read_normalization.pl", "oases": "/usr/local/bin/oases", "oases_pipeline.py": "/usr/local/bin/oases_pipeline.py", "retrieve_sequences_from_fasta.pl": "/usr/local/bin/retrieve_sequences_from_fasta.pl", "run_DE_analysis.pl": "/usr/local/bin/run_DE_analysis.pl", "run_DE_analysis_from_samples_file.pl": "/usr/local/bin/run_DE_analysis_from_samples_file.pl", "seqtk-trinity": "/usr/local/bin/seqtk-trinity", "sift_bam_max_cov.pl": "/usr/local/bin/sift_bam_max_cov.pl", "salmon": "/usr/local/bin/salmon", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth", "giffilter": "/usr/local/bin/giffilter", "gifsponge": "/usr/local/bin/gifsponge", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/discasm.
shpc-registry automated BioContainers addition for discasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/discasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/discasm:0.1.3--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/discasm/0.1.3--1
$ module help quay.io/biocontainers/discasm/0.1.3--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### discasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### discasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### discasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### discasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### discasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### discasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DISCASM

```bash
$ singularity exec <container> /usr/local/bin/DISCASM
$ podman run --it --rm --entrypoint /usr/local/bin/DISCASM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DISCASM   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### extract_supertranscript_from_reference.py

```bash
$ singularity exec <container> /usr/local/bin/extract_supertranscript_from_reference.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_supertranscript_from_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_supertranscript_from_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_low_expr_transcripts.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_low_expr_transcripts.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_low_expr_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_low_expr_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_Trinity_gene_to_trans_map.pl

```bash
$ singularity exec <container> /usr/local/bin/get_Trinity_gene_to_trans_map.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_Trinity_gene_to_trans_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_Trinity_gene_to_trans_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### insilico_read_normalization.pl

```bash
$ singularity exec <container> /usr/local/bin/insilico_read_normalization.pl
$ podman run --it --rm --entrypoint /usr/local/bin/insilico_read_normalization.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/insilico_read_normalization.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oases

```bash
$ singularity exec <container> /usr/local/bin/oases
$ podman run --it --rm --entrypoint /usr/local/bin/oases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oases_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/oases_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/oases_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oases_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retrieve_sequences_from_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/retrieve_sequences_from_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/retrieve_sequences_from_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retrieve_sequences_from_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### seqtk-trinity

```bash
$ singularity exec <container> /usr/local/bin/seqtk-trinity
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk-trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk-trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sift_bam_max_cov.pl

```bash
$ singularity exec <container> /usr/local/bin/sift_bam_max_cov.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sift_bam_max_cov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sift_bam_max_cov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### salmon

```bash
$ singularity exec <container> /usr/local/bin/salmon
$ podman run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffilter

```bash
$ singularity exec <container> /usr/local/bin/giffilter
$ podman run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifsponge

```bash
$ singularity exec <container> /usr/local/bin/gifsponge
$ podman run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
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