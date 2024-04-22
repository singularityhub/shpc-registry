---
layout: container
name:  "quay.io/biocontainers/mitgard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mitgard/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mitgard/container.yaml"
updated_at: "2024-04-22 03:03:41.089692"
latest: "1.0--py39hdfd78af_1"
container_url: "https://biocontainers.pro/tools/mitgard"
aliases:
 - "MITGARD.py"
 - "PtR"
 - "RearrangementCheck.py"
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
 - "msa2consensus.py"
 - "retrieve_sequences_from_fasta.pl"
 - "run_DE_analysis.pl"
 - "run_DE_analysis_from_samples_file.pl"
 - "sam2msa.py"
 - "seqtk-trinity"
 - "sift_bam_max_cov.pl"
 - "salmon"
 - "jemalloc-config"
 - "jeprof"
 - "jemalloc.sh"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
versions:
 - "1.0--py39hdfd78af_1"
description: "shpc-registry automated BioContainers addition for mitgard"
config: {"url": "https://biocontainers.pro/tools/mitgard", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mitgard", "latest": {"1.0--py39hdfd78af_1": "sha256:d61ff0e17a0e8444e6207a36beb04d70e7ab6d42b5aea280a6a7c8f809447895"}, "tags": {"1.0--py39hdfd78af_1": "sha256:d61ff0e17a0e8444e6207a36beb04d70e7ab6d42b5aea280a6a7c8f809447895"}, "docker": "quay.io/biocontainers/mitgard", "aliases": {"MITGARD.py": "/usr/local/bin/MITGARD.py", "PtR": "/usr/local/bin/PtR", "RearrangementCheck.py": "/usr/local/bin/RearrangementCheck.py", "Trinity": "/usr/local/bin/Trinity", "TrinityStats.pl": "/usr/local/bin/TrinityStats.pl", "Trinity_gene_splice_modeler.py": "/usr/local/bin/Trinity_gene_splice_modeler.py", "abundance_estimates_to_matrix.pl": "/usr/local/bin/abundance_estimates_to_matrix.pl", "align_and_estimate_abundance.pl": "/usr/local/bin/align_and_estimate_abundance.pl", "analyze_blastPlus_topHit_coverage.pl": "/usr/local/bin/analyze_blastPlus_topHit_coverage.pl", "analyze_diff_expr.pl": "/usr/local/bin/analyze_diff_expr.pl", "contig_ExN50_statistic.pl": "/usr/local/bin/contig_ExN50_statistic.pl", "define_clusters_by_cutting_tree.pl": "/usr/local/bin/define_clusters_by_cutting_tree.pl", "extract_supertranscript_from_reference.py": "/usr/local/bin/extract_supertranscript_from_reference.py", "filter_low_expr_transcripts.pl": "/usr/local/bin/filter_low_expr_transcripts.pl", "get_Trinity_gene_to_trans_map.pl": "/usr/local/bin/get_Trinity_gene_to_trans_map.pl", "insilico_read_normalization.pl": "/usr/local/bin/insilico_read_normalization.pl", "msa2consensus.py": "/usr/local/bin/msa2consensus.py", "retrieve_sequences_from_fasta.pl": "/usr/local/bin/retrieve_sequences_from_fasta.pl", "run_DE_analysis.pl": "/usr/local/bin/run_DE_analysis.pl", "run_DE_analysis_from_samples_file.pl": "/usr/local/bin/run_DE_analysis_from_samples_file.pl", "sam2msa.py": "/usr/local/bin/sam2msa.py", "seqtk-trinity": "/usr/local/bin/seqtk-trinity", "sift_bam_max_cov.pl": "/usr/local/bin/sift_bam_max_cov.pl", "salmon": "/usr/local/bin/salmon", "jemalloc-config": "/usr/local/bin/jemalloc-config", "jeprof": "/usr/local/bin/jeprof", "jemalloc.sh": "/usr/local/bin/jemalloc.sh", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mitgard.
shpc-registry automated BioContainers addition for mitgard
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mitgard
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mitgard:1.0--py39hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mitgard/1.0--py39hdfd78af_1
$ module help quay.io/biocontainers/mitgard/1.0--py39hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mitgard-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mitgard-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mitgard-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mitgard-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mitgard-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mitgard-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MITGARD.py

```bash
$ singularity exec <container> /usr/local/bin/MITGARD.py
$ podman run --it --rm --entrypoint /usr/local/bin/MITGARD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MITGARD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PtR

```bash
$ singularity exec <container> /usr/local/bin/PtR
$ podman run --it --rm --entrypoint /usr/local/bin/PtR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PtR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RearrangementCheck.py

```bash
$ singularity exec <container> /usr/local/bin/RearrangementCheck.py
$ podman run --it --rm --entrypoint /usr/local/bin/RearrangementCheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RearrangementCheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### msa2consensus.py

```bash
$ singularity exec <container> /usr/local/bin/msa2consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/msa2consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa2consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sam2msa.py

```bash
$ singularity exec <container> /usr/local/bin/sam2msa.py
$ podman run --it --rm --entrypoint /usr/local/bin/sam2msa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2msa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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