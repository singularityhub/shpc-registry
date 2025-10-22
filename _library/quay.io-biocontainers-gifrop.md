---
layout: container
name:  "quay.io/biocontainers/gifrop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gifrop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gifrop/container.yaml"
updated_at: "2025-10-22 03:53:41.168331"
latest: "0.0.9--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/gifrop"
aliases:
 - "abricate"
 - "abricate-get_db"
 - "cluster_graphs.R"
 - "create_pan_genome"
 - "create_pan_genome_plots.R"
 - "extract_proteome_from_gff"
 - "gifrop"
 - "gifrop_R_reqs.R"
 - "gifrop_classify.R"
 - "gifrop_cluster.R"
 - "gifrop_id.R"
 - "gifrop_pannotate.R"
 - "gifrop_plots.R"
 - "iterative_cdhit"
 - "pan_genome_assembly_statistics"
 - "pan_genome_core_alignment"
 - "pan_genome_post_analysis"
 - "pan_genome_reorder_spreadsheet"
 - "pan_pipe"
 - "parallel_all_against_all_blastp"
 - "protein_alignment_from_nucleotides"
 - "query_pan_genome"
 - "roary"
 - "roary-create_pan_genome_plots.R"
 - "roary-pan_genome_reorder_spreadsheet"
 - "roary-query_pan_genome"
 - "roary-unique_genes_per_sample"
 - "submodule_test.R"
 - "tbl2asn-test"
 - "transfer_annotation_to_groups"
 - "yapp"
 - "fix-sqn-date"
 - "prank"
 - "faketime"
 - "real-tbl2asn"
 - "prokka-abricate_to_fasta_db"
 - "any2fasta"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
versions:
 - "0.0.9--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for gifrop"
config: {"url": "https://biocontainers.pro/tools/gifrop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gifrop", "latest": {"0.0.9--hdfd78af_0": "sha256:c23feca560501c93d3fc4f246644011a4d2445c507c1105bbaa275f9c83fd36f"}, "tags": {"0.0.9--hdfd78af_0": "sha256:c23feca560501c93d3fc4f246644011a4d2445c507c1105bbaa275f9c83fd36f"}, "docker": "quay.io/biocontainers/gifrop", "aliases": {"abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "cluster_graphs.R": "/usr/local/bin/cluster_graphs.R", "create_pan_genome": "/usr/local/bin/create_pan_genome", "create_pan_genome_plots.R": "/usr/local/bin/create_pan_genome_plots.R", "extract_proteome_from_gff": "/usr/local/bin/extract_proteome_from_gff", "gifrop": "/usr/local/bin/gifrop", "gifrop_R_reqs.R": "/usr/local/bin/gifrop_R_reqs.R", "gifrop_classify.R": "/usr/local/bin/gifrop_classify.R", "gifrop_cluster.R": "/usr/local/bin/gifrop_cluster.R", "gifrop_id.R": "/usr/local/bin/gifrop_id.R", "gifrop_pannotate.R": "/usr/local/bin/gifrop_pannotate.R", "gifrop_plots.R": "/usr/local/bin/gifrop_plots.R", "iterative_cdhit": "/usr/local/bin/iterative_cdhit", "pan_genome_assembly_statistics": "/usr/local/bin/pan_genome_assembly_statistics", "pan_genome_core_alignment": "/usr/local/bin/pan_genome_core_alignment", "pan_genome_post_analysis": "/usr/local/bin/pan_genome_post_analysis", "pan_genome_reorder_spreadsheet": "/usr/local/bin/pan_genome_reorder_spreadsheet", "pan_pipe": "/usr/local/bin/pan_pipe", "parallel_all_against_all_blastp": "/usr/local/bin/parallel_all_against_all_blastp", "protein_alignment_from_nucleotides": "/usr/local/bin/protein_alignment_from_nucleotides", "query_pan_genome": "/usr/local/bin/query_pan_genome", "roary": "/usr/local/bin/roary", "roary-create_pan_genome_plots.R": "/usr/local/bin/roary-create_pan_genome_plots.R", "roary-pan_genome_reorder_spreadsheet": "/usr/local/bin/roary-pan_genome_reorder_spreadsheet", "roary-query_pan_genome": "/usr/local/bin/roary-query_pan_genome", "roary-unique_genes_per_sample": "/usr/local/bin/roary-unique_genes_per_sample", "submodule_test.R": "/usr/local/bin/submodule_test.R", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "transfer_annotation_to_groups": "/usr/local/bin/transfer_annotation_to_groups", "yapp": "/usr/local/bin/yapp", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "prank": "/usr/local/bin/prank", "faketime": "/usr/local/bin/faketime", "real-tbl2asn": "/usr/local/bin/real-tbl2asn", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "any2fasta": "/usr/local/bin/any2fasta", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gifrop.
shpc-registry automated BioContainers addition for gifrop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gifrop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gifrop:0.0.9--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gifrop/0.0.9--hdfd78af_0
$ module help quay.io/biocontainers/gifrop/0.0.9--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gifrop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gifrop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gifrop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gifrop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gifrop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gifrop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster_graphs.R

```bash
$ singularity exec <container> /usr/local/bin/cluster_graphs.R
$ podman run --it --rm --entrypoint /usr/local/bin/cluster_graphs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster_graphs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_pan_genome

```bash
$ singularity exec <container> /usr/local/bin/create_pan_genome
$ podman run --it --rm --entrypoint /usr/local/bin/create_pan_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_pan_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_pan_genome_plots.R

```bash
$ singularity exec <container> /usr/local/bin/create_pan_genome_plots.R
$ podman run --it --rm --entrypoint /usr/local/bin/create_pan_genome_plots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_pan_genome_plots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_proteome_from_gff

```bash
$ singularity exec <container> /usr/local/bin/extract_proteome_from_gff
$ podman run --it --rm --entrypoint /usr/local/bin/extract_proteome_from_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_proteome_from_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifrop

```bash
$ singularity exec <container> /usr/local/bin/gifrop
$ podman run --it --rm --entrypoint /usr/local/bin/gifrop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifrop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifrop_R_reqs.R

```bash
$ singularity exec <container> /usr/local/bin/gifrop_R_reqs.R
$ podman run --it --rm --entrypoint /usr/local/bin/gifrop_R_reqs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifrop_R_reqs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifrop_classify.R

```bash
$ singularity exec <container> /usr/local/bin/gifrop_classify.R
$ podman run --it --rm --entrypoint /usr/local/bin/gifrop_classify.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifrop_classify.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifrop_cluster.R

```bash
$ singularity exec <container> /usr/local/bin/gifrop_cluster.R
$ podman run --it --rm --entrypoint /usr/local/bin/gifrop_cluster.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifrop_cluster.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifrop_id.R

```bash
$ singularity exec <container> /usr/local/bin/gifrop_id.R
$ podman run --it --rm --entrypoint /usr/local/bin/gifrop_id.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifrop_id.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifrop_pannotate.R

```bash
$ singularity exec <container> /usr/local/bin/gifrop_pannotate.R
$ podman run --it --rm --entrypoint /usr/local/bin/gifrop_pannotate.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifrop_pannotate.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifrop_plots.R

```bash
$ singularity exec <container> /usr/local/bin/gifrop_plots.R
$ podman run --it --rm --entrypoint /usr/local/bin/gifrop_plots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifrop_plots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iterative_cdhit

```bash
$ singularity exec <container> /usr/local/bin/iterative_cdhit
$ podman run --it --rm --entrypoint /usr/local/bin/iterative_cdhit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iterative_cdhit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pan_genome_assembly_statistics

```bash
$ singularity exec <container> /usr/local/bin/pan_genome_assembly_statistics
$ podman run --it --rm --entrypoint /usr/local/bin/pan_genome_assembly_statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pan_genome_assembly_statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pan_genome_core_alignment

```bash
$ singularity exec <container> /usr/local/bin/pan_genome_core_alignment
$ podman run --it --rm --entrypoint /usr/local/bin/pan_genome_core_alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pan_genome_core_alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pan_genome_post_analysis

```bash
$ singularity exec <container> /usr/local/bin/pan_genome_post_analysis
$ podman run --it --rm --entrypoint /usr/local/bin/pan_genome_post_analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pan_genome_post_analysis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pan_genome_reorder_spreadsheet

```bash
$ singularity exec <container> /usr/local/bin/pan_genome_reorder_spreadsheet
$ podman run --it --rm --entrypoint /usr/local/bin/pan_genome_reorder_spreadsheet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pan_genome_reorder_spreadsheet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pan_pipe

```bash
$ singularity exec <container> /usr/local/bin/pan_pipe
$ podman run --it --rm --entrypoint /usr/local/bin/pan_pipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pan_pipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel_all_against_all_blastp

```bash
$ singularity exec <container> /usr/local/bin/parallel_all_against_all_blastp
$ podman run --it --rm --entrypoint /usr/local/bin/parallel_all_against_all_blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel_all_against_all_blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protein_alignment_from_nucleotides

```bash
$ singularity exec <container> /usr/local/bin/protein_alignment_from_nucleotides
$ podman run --it --rm --entrypoint /usr/local/bin/protein_alignment_from_nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protein_alignment_from_nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### query_pan_genome

```bash
$ singularity exec <container> /usr/local/bin/query_pan_genome
$ podman run --it --rm --entrypoint /usr/local/bin/query_pan_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/query_pan_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roary

```bash
$ singularity exec <container> /usr/local/bin/roary
$ podman run --it --rm --entrypoint /usr/local/bin/roary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roary-create_pan_genome_plots.R

```bash
$ singularity exec <container> /usr/local/bin/roary-create_pan_genome_plots.R
$ podman run --it --rm --entrypoint /usr/local/bin/roary-create_pan_genome_plots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roary-create_pan_genome_plots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roary-pan_genome_reorder_spreadsheet

```bash
$ singularity exec <container> /usr/local/bin/roary-pan_genome_reorder_spreadsheet
$ podman run --it --rm --entrypoint /usr/local/bin/roary-pan_genome_reorder_spreadsheet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roary-pan_genome_reorder_spreadsheet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roary-query_pan_genome

```bash
$ singularity exec <container> /usr/local/bin/roary-query_pan_genome
$ podman run --it --rm --entrypoint /usr/local/bin/roary-query_pan_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roary-query_pan_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roary-unique_genes_per_sample

```bash
$ singularity exec <container> /usr/local/bin/roary-unique_genes_per_sample
$ podman run --it --rm --entrypoint /usr/local/bin/roary-unique_genes_per_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roary-unique_genes_per_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### submodule_test.R

```bash
$ singularity exec <container> /usr/local/bin/submodule_test.R
$ podman run --it --rm --entrypoint /usr/local/bin/submodule_test.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/submodule_test.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transfer_annotation_to_groups

```bash
$ singularity exec <container> /usr/local/bin/transfer_annotation_to_groups
$ podman run --it --rm --entrypoint /usr/local/bin/transfer_annotation_to_groups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transfer_annotation_to_groups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yapp

```bash
$ singularity exec <container> /usr/local/bin/yapp
$ podman run --it --rm --entrypoint /usr/local/bin/yapp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yapp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix-sqn-date

```bash
$ singularity exec <container> /usr/local/bin/fix-sqn-date
$ podman run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prank

```bash
$ singularity exec <container> /usr/local/bin/prank
$ podman run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faketime

```bash
$ singularity exec <container> /usr/local/bin/faketime
$ podman run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### real-tbl2asn

```bash
$ singularity exec <container> /usr/local/bin/real-tbl2asn
$ podman run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-abricate_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-abricate_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
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