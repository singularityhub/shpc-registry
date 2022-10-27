---
layout: container
name:  "quay.io/biocontainers/bohra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bohra/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bohra/container.yaml"
updated_at: "2022-10-27 01:13:03.889553"
latest: "1.2.9--py_0"
container_url: "https://biocontainers.pro/tools/bohra"
aliases:
 - "abritamr"
 - "amr_report"
 - "amrfinder"
 - "amrfinder_update"
 - "bohra"
 - "create_pan_genome"
 - "create_pan_genome_plots.R"
 - "croco-0.6-config"
 - "csslint-0.6"
 - "dna_mutation"
 - "extract_proteome_from_gff"
 - "fasta2parts"
 - "fasta_check"
 - "gff_check"
 - "iterative_cdhit"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "pan_genome_assembly_statistics"
 - "pan_genome_core_alignment"
 - "pan_genome_post_analysis"
 - "pan_genome_reorder_spreadsheet"
 - "parallel_all_against_all_blastp"
 - "protein_alignment_from_nucleotides"
 - "query_pan_genome"
 - "roary"
 - "roary-create_pan_genome_plots.R"
 - "roary-pan_genome_reorder_spreadsheet"
 - "roary-query_pan_genome"
 - "roary-unique_genes_per_sample"
 - "shovill"
 - "snp-dists"
 - "transfer_annotation_to_groups"
 - "x86_64-conda_cos6-linux-gnu-pkg-config"
versions:
 - "1.2.9--py_0"
description: "shpc-registry automated BioContainers addition for bohra"
config: {"url": "https://biocontainers.pro/tools/bohra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bohra", "latest": {"1.2.9--py_0": "sha256:1c7945448913cb47ccd34f3f8dde4aca6e9ba1fb46776daa4eb170c393ed5f62"}, "tags": {"1.2.9--py_0": "sha256:1c7945448913cb47ccd34f3f8dde4aca6e9ba1fb46776daa4eb170c393ed5f62"}, "docker": "quay.io/biocontainers/bohra", "aliases": {"abritamr": "/usr/local/bin/abritamr", "amr_report": "/usr/local/bin/amr_report", "amrfinder": "/usr/local/bin/amrfinder", "amrfinder_update": "/usr/local/bin/amrfinder_update", "bohra": "/usr/local/bin/bohra", "create_pan_genome": "/usr/local/bin/create_pan_genome", "create_pan_genome_plots.R": "/usr/local/bin/create_pan_genome_plots.R", "croco-0.6-config": "/usr/local/bin/croco-0.6-config", "csslint-0.6": "/usr/local/bin/csslint-0.6", "dna_mutation": "/usr/local/bin/dna_mutation", "extract_proteome_from_gff": "/usr/local/bin/extract_proteome_from_gff", "fasta2parts": "/usr/local/bin/fasta2parts", "fasta_check": "/usr/local/bin/fasta_check", "gff_check": "/usr/local/bin/gff_check", "iterative_cdhit": "/usr/local/bin/iterative_cdhit", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "pan_genome_assembly_statistics": "/usr/local/bin/pan_genome_assembly_statistics", "pan_genome_core_alignment": "/usr/local/bin/pan_genome_core_alignment", "pan_genome_post_analysis": "/usr/local/bin/pan_genome_post_analysis", "pan_genome_reorder_spreadsheet": "/usr/local/bin/pan_genome_reorder_spreadsheet", "parallel_all_against_all_blastp": "/usr/local/bin/parallel_all_against_all_blastp", "protein_alignment_from_nucleotides": "/usr/local/bin/protein_alignment_from_nucleotides", "query_pan_genome": "/usr/local/bin/query_pan_genome", "roary": "/usr/local/bin/roary", "roary-create_pan_genome_plots.R": "/usr/local/bin/roary-create_pan_genome_plots.R", "roary-pan_genome_reorder_spreadsheet": "/usr/local/bin/roary-pan_genome_reorder_spreadsheet", "roary-query_pan_genome": "/usr/local/bin/roary-query_pan_genome", "roary-unique_genes_per_sample": "/usr/local/bin/roary-unique_genes_per_sample", "shovill": "/usr/local/bin/shovill", "snp-dists": "/usr/local/bin/snp-dists", "transfer_annotation_to_groups": "/usr/local/bin/transfer_annotation_to_groups", "x86_64-conda_cos6-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bohra.
shpc-registry automated BioContainers addition for bohra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bohra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bohra:1.2.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bohra/1.2.9--py_0
$ module help quay.io/biocontainers/bohra/1.2.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bohra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bohra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bohra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bohra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bohra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bohra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abritamr

```bash
$ singularity exec <container> /usr/local/bin/abritamr
$ podman run --it --rm --entrypoint /usr/local/bin/abritamr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abritamr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amr_report

```bash
$ singularity exec <container> /usr/local/bin/amr_report
$ podman run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amr_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder

```bash
$ singularity exec <container> /usr/local/bin/amrfinder
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder_update

```bash
$ singularity exec <container> /usr/local/bin/amrfinder_update
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bohra

```bash
$ singularity exec <container> /usr/local/bin/bohra
$ podman run --it --rm --entrypoint /usr/local/bin/bohra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bohra   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### croco-0.6-config

```bash
$ singularity exec <container> /usr/local/bin/croco-0.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csslint-0.6

```bash
$ singularity exec <container> /usr/local/bin/csslint-0.6
$ podman run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dna_mutation

```bash
$ singularity exec <container> /usr/local/bin/dna_mutation
$ podman run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna_mutation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_proteome_from_gff

```bash
$ singularity exec <container> /usr/local/bin/extract_proteome_from_gff
$ podman run --it --rm --entrypoint /usr/local/bin/extract_proteome_from_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_proteome_from_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2parts

```bash
$ singularity exec <container> /usr/local/bin/fasta2parts
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2parts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_check

```bash
$ singularity exec <container> /usr/local/bin/fasta_check
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_check

```bash
$ singularity exec <container> /usr/local/bin/gff_check
$ podman run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iterative_cdhit

```bash
$ singularity exec <container> /usr/local/bin/iterative_cdhit
$ podman run --it --rm --entrypoint /usr/local/bin/iterative_cdhit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iterative_cdhit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2

```bash
$ singularity exec <container> /usr/local/bin/kraken2
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-build

```bash
$ singularity exec <container> /usr/local/bin/kraken2-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-inspect

```bash
$ singularity exec <container> /usr/local/bin/kraken2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### shovill

```bash
$ singularity exec <container> /usr/local/bin/shovill
$ podman run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp-dists

```bash
$ singularity exec <container> /usr/local/bin/snp-dists
$ podman run --it --rm --entrypoint /usr/local/bin/snp-dists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-dists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transfer_annotation_to_groups

```bash
$ singularity exec <container> /usr/local/bin/transfer_annotation_to_groups
$ podman run --it --rm --entrypoint /usr/local/bin/transfer_annotation_to_groups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transfer_annotation_to_groups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos6-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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