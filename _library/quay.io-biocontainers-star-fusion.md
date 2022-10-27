---
layout: container
name:  "quay.io/biocontainers/star-fusion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/star-fusion/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/star-fusion/container.yaml"
updated_at: "2022-10-27 01:01:42.186364"
latest: "1.9.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/star-fusion"
aliases:
 - "PtR"
 - "STAR-Fusion"
 - "TrinityStats.pl"
 - "Trinity_gene_splice_modeler.py"
 - "abundance_estimates_to_matrix.pl"
 - "align_and_estimate_abundance.pl"
 - "analyze_blastPlus_topHit_coverage.pl"
 - "analyze_diff_expr.pl"
 - "blast_and_promiscuity_filter.pl"
 - "contig_ExN50_statistic.pl"
 - "create_datauri"
 - "create_report"
 - "define_clusters_by_cutting_tree.pl"
 - "extract_supertranscript_from_reference.py"
 - "filter_low_expr_transcripts.pl"
 - "get_Trinity_gene_to_trans_map.pl"
 - "gmap.nosimd"
 - "gmap_cat"
 - "gmapl.nosimd"
 - "gsnap.nosimd"
 - "gsnapl.nosimd"
 - "indexdb_cat"
 - "insilico_read_normalization.pl"
 - "prep_genome_lib.pl"
 - "retrieve_sequences_from_fasta.pl"
 - "run_DE_analysis.pl"
 - "run_DE_analysis_from_samples_file.pl"
 - "seqtk-trinity"
 - "sift_bam_max_cov.pl"
versions:
 - "1.9.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for star-fusion"
config: {"url": "https://biocontainers.pro/tools/star-fusion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for star-fusion", "latest": {"1.9.1--hdfd78af_1": "sha256:5384117b0b85919e8c91b526509d797a5561290a1deaab8e60745db25c99f2c0"}, "tags": {"1.9.1--hdfd78af_1": "sha256:5384117b0b85919e8c91b526509d797a5561290a1deaab8e60745db25c99f2c0"}, "docker": "quay.io/biocontainers/star-fusion", "aliases": {"PtR": "/usr/local/bin/PtR", "STAR-Fusion": "/usr/local/bin/STAR-Fusion", "TrinityStats.pl": "/usr/local/bin/TrinityStats.pl", "Trinity_gene_splice_modeler.py": "/usr/local/bin/Trinity_gene_splice_modeler.py", "abundance_estimates_to_matrix.pl": "/usr/local/bin/abundance_estimates_to_matrix.pl", "align_and_estimate_abundance.pl": "/usr/local/bin/align_and_estimate_abundance.pl", "analyze_blastPlus_topHit_coverage.pl": "/usr/local/bin/analyze_blastPlus_topHit_coverage.pl", "analyze_diff_expr.pl": "/usr/local/bin/analyze_diff_expr.pl", "blast_and_promiscuity_filter.pl": "/usr/local/bin/blast_and_promiscuity_filter.pl", "contig_ExN50_statistic.pl": "/usr/local/bin/contig_ExN50_statistic.pl", "create_datauri": "/usr/local/bin/create_datauri", "create_report": "/usr/local/bin/create_report", "define_clusters_by_cutting_tree.pl": "/usr/local/bin/define_clusters_by_cutting_tree.pl", "extract_supertranscript_from_reference.py": "/usr/local/bin/extract_supertranscript_from_reference.py", "filter_low_expr_transcripts.pl": "/usr/local/bin/filter_low_expr_transcripts.pl", "get_Trinity_gene_to_trans_map.pl": "/usr/local/bin/get_Trinity_gene_to_trans_map.pl", "gmap.nosimd": "/usr/local/bin/gmap.nosimd", "gmap_cat": "/usr/local/bin/gmap_cat", "gmapl.nosimd": "/usr/local/bin/gmapl.nosimd", "gsnap.nosimd": "/usr/local/bin/gsnap.nosimd", "gsnapl.nosimd": "/usr/local/bin/gsnapl.nosimd", "indexdb_cat": "/usr/local/bin/indexdb_cat", "insilico_read_normalization.pl": "/usr/local/bin/insilico_read_normalization.pl", "prep_genome_lib.pl": "/usr/local/bin/prep_genome_lib.pl", "retrieve_sequences_from_fasta.pl": "/usr/local/bin/retrieve_sequences_from_fasta.pl", "run_DE_analysis.pl": "/usr/local/bin/run_DE_analysis.pl", "run_DE_analysis_from_samples_file.pl": "/usr/local/bin/run_DE_analysis_from_samples_file.pl", "seqtk-trinity": "/usr/local/bin/seqtk-trinity", "sift_bam_max_cov.pl": "/usr/local/bin/sift_bam_max_cov.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/star-fusion.
shpc-registry automated BioContainers addition for star-fusion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/star-fusion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/star-fusion:1.9.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/star-fusion/1.9.1--hdfd78af_1
$ module help quay.io/biocontainers/star-fusion/1.9.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### star-fusion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### star-fusion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### star-fusion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### star-fusion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### star-fusion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### star-fusion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PtR

```bash
$ singularity exec <container> /usr/local/bin/PtR
$ podman run --it --rm --entrypoint /usr/local/bin/PtR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PtR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-Fusion

```bash
$ singularity exec <container> /usr/local/bin/STAR-Fusion
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-Fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-Fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### blast_and_promiscuity_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_and_promiscuity_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_and_promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_and_promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contig_ExN50_statistic.pl

```bash
$ singularity exec <container> /usr/local/bin/contig_ExN50_statistic.pl
$ podman run --it --rm --entrypoint /usr/local/bin/contig_ExN50_statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contig_ExN50_statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_datauri

```bash
$ singularity exec <container> /usr/local/bin/create_datauri
$ podman run --it --rm --entrypoint /usr/local/bin/create_datauri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_datauri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_report

```bash
$ singularity exec <container> /usr/local/bin/create_report
$ podman run --it --rm --entrypoint /usr/local/bin/create_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_report   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gmap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_cat

```bash
$ singularity exec <container> /usr/local/bin/gmap_cat
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_cat

```bash
$ singularity exec <container> /usr/local/bin/indexdb_cat
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### insilico_read_normalization.pl

```bash
$ singularity exec <container> /usr/local/bin/insilico_read_normalization.pl
$ podman run --it --rm --entrypoint /usr/local/bin/insilico_read_normalization.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/insilico_read_normalization.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prep_genome_lib.pl

```bash
$ singularity exec <container> /usr/local/bin/prep_genome_lib.pl
$ podman run --it --rm --entrypoint /usr/local/bin/prep_genome_lib.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prep_genome_lib.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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