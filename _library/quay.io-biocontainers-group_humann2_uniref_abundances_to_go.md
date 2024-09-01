---
layout: container
name:  "quay.io/biocontainers/group_humann2_uniref_abundances_to_go"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/group_humann2_uniref_abundances_to_go/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/group_humann2_uniref_abundances_to_go/container.yaml"
updated_at: "2024-09-01 03:17:44.723202"
latest: "1.3.0--0"
container_url: "https://biocontainers.pro/tools/group_humann2_uniref_abundances_to_go"
aliases:
 - "compare_gos.py"
 - "download_metaphlan2_db.py"
 - "fetch_associations.py"
 - "find_enrichment.py"
 - "go_plot.py"
 - "group_humann2_uniref_abundances_to_GO.sh"
 - "humann2"
 - "humann2_blastx_coverage"
 - "humann2_config"
 - "humann2_databases"
 - "humann2_humann1_kegg"
 - "humann2_join_tables"
 - "humann2_merge_abundance_tables"
 - "humann2_reduce_table"
 - "humann2_regroup_table"
 - "humann2_rename_table"
 - "humann2_renorm_table"
 - "humann2_rna_dna_norm"
 - "humann2_split_table"
 - "humann2_strain_profiler"
 - "humann2_test"
 - "map_to_slim.py"
 - "metaphlan2.py"
 - "metaphlan2krona.py"
 - "ncbi_gene_results_to_python.py"
 - "plot_go_term.py"
 - "prt_terms.py"
 - "pyqi"
 - "wr_hier.py"
 - "wr_sections.py"
 - "biom"
 - "vba_extract.py"
 - "diamond"
 - "cxpm"
 - "sxpm"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
versions:
 - "1.3.0--0"
description: "shpc-registry automated BioContainers addition for group_humann2_uniref_abundances_to_go"
config: {"url": "https://biocontainers.pro/tools/group_humann2_uniref_abundances_to_go", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for group_humann2_uniref_abundances_to_go", "latest": {"1.3.0--0": "sha256:7e882835baa57d01b4c883ab2e247e19589f8ae1706c509c717447d5ef89fc8c"}, "tags": {"1.3.0--0": "sha256:7e882835baa57d01b4c883ab2e247e19589f8ae1706c509c717447d5ef89fc8c"}, "docker": "quay.io/biocontainers/group_humann2_uniref_abundances_to_go", "aliases": {"compare_gos.py": "/usr/local/bin/compare_gos.py", "download_metaphlan2_db.py": "/usr/local/bin/download_metaphlan2_db.py", "fetch_associations.py": "/usr/local/bin/fetch_associations.py", "find_enrichment.py": "/usr/local/bin/find_enrichment.py", "go_plot.py": "/usr/local/bin/go_plot.py", "group_humann2_uniref_abundances_to_GO.sh": "/usr/local/bin/group_humann2_uniref_abundances_to_GO.sh", "humann2": "/usr/local/bin/humann2", "humann2_blastx_coverage": "/usr/local/bin/humann2_blastx_coverage", "humann2_config": "/usr/local/bin/humann2_config", "humann2_databases": "/usr/local/bin/humann2_databases", "humann2_humann1_kegg": "/usr/local/bin/humann2_humann1_kegg", "humann2_join_tables": "/usr/local/bin/humann2_join_tables", "humann2_merge_abundance_tables": "/usr/local/bin/humann2_merge_abundance_tables", "humann2_reduce_table": "/usr/local/bin/humann2_reduce_table", "humann2_regroup_table": "/usr/local/bin/humann2_regroup_table", "humann2_rename_table": "/usr/local/bin/humann2_rename_table", "humann2_renorm_table": "/usr/local/bin/humann2_renorm_table", "humann2_rna_dna_norm": "/usr/local/bin/humann2_rna_dna_norm", "humann2_split_table": "/usr/local/bin/humann2_split_table", "humann2_strain_profiler": "/usr/local/bin/humann2_strain_profiler", "humann2_test": "/usr/local/bin/humann2_test", "map_to_slim.py": "/usr/local/bin/map_to_slim.py", "metaphlan2.py": "/usr/local/bin/metaphlan2.py", "metaphlan2krona.py": "/usr/local/bin/metaphlan2krona.py", "ncbi_gene_results_to_python.py": "/usr/local/bin/ncbi_gene_results_to_python.py", "plot_go_term.py": "/usr/local/bin/plot_go_term.py", "prt_terms.py": "/usr/local/bin/prt_terms.py", "pyqi": "/usr/local/bin/pyqi", "wr_hier.py": "/usr/local/bin/wr_hier.py", "wr_sections.py": "/usr/local/bin/wr_sections.py", "biom": "/usr/local/bin/biom", "vba_extract.py": "/usr/local/bin/vba_extract.py", "diamond": "/usr/local/bin/diamond", "cxpm": "/usr/local/bin/cxpm", "sxpm": "/usr/local/bin/sxpm", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/group_humann2_uniref_abundances_to_go.
shpc-registry automated BioContainers addition for group_humann2_uniref_abundances_to_go
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/group_humann2_uniref_abundances_to_go
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/group_humann2_uniref_abundances_to_go:1.3.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/group_humann2_uniref_abundances_to_go/1.3.0--0
$ module help quay.io/biocontainers/group_humann2_uniref_abundances_to_go/1.3.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### group_humann2_uniref_abundances_to_go-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### group_humann2_uniref_abundances_to_go-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### group_humann2_uniref_abundances_to_go-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### group_humann2_uniref_abundances_to_go-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### group_humann2_uniref_abundances_to_go-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### group_humann2_uniref_abundances_to_go-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compare_gos.py

```bash
$ singularity exec <container> /usr/local/bin/compare_gos.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_metaphlan2_db.py

```bash
$ singularity exec <container> /usr/local/bin/download_metaphlan2_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/download_metaphlan2_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_metaphlan2_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_associations.py

```bash
$ singularity exec <container> /usr/local/bin/fetch_associations.py
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_enrichment.py

```bash
$ singularity exec <container> /usr/local/bin/find_enrichment.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go_plot.py

```bash
$ singularity exec <container> /usr/local/bin/go_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### group_humann2_uniref_abundances_to_GO.sh

```bash
$ singularity exec <container> /usr/local/bin/group_humann2_uniref_abundances_to_GO.sh
$ podman run --it --rm --entrypoint /usr/local/bin/group_humann2_uniref_abundances_to_GO.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/group_humann2_uniref_abundances_to_GO.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2

```bash
$ singularity exec <container> /usr/local/bin/humann2
$ podman run --it --rm --entrypoint /usr/local/bin/humann2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_blastx_coverage

```bash
$ singularity exec <container> /usr/local/bin/humann2_blastx_coverage
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_blastx_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_blastx_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_config

```bash
$ singularity exec <container> /usr/local/bin/humann2_config
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_databases

```bash
$ singularity exec <container> /usr/local/bin/humann2_databases
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_databases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_databases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_humann1_kegg

```bash
$ singularity exec <container> /usr/local/bin/humann2_humann1_kegg
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_humann1_kegg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_humann1_kegg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_join_tables

```bash
$ singularity exec <container> /usr/local/bin/humann2_join_tables
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_join_tables   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_join_tables   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_merge_abundance_tables

```bash
$ singularity exec <container> /usr/local/bin/humann2_merge_abundance_tables
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_merge_abundance_tables   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_merge_abundance_tables   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_reduce_table

```bash
$ singularity exec <container> /usr/local/bin/humann2_reduce_table
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_reduce_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_reduce_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_regroup_table

```bash
$ singularity exec <container> /usr/local/bin/humann2_regroup_table
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_regroup_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_regroup_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_rename_table

```bash
$ singularity exec <container> /usr/local/bin/humann2_rename_table
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_rename_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_rename_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_renorm_table

```bash
$ singularity exec <container> /usr/local/bin/humann2_renorm_table
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_renorm_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_renorm_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_rna_dna_norm

```bash
$ singularity exec <container> /usr/local/bin/humann2_rna_dna_norm
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_rna_dna_norm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_rna_dna_norm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_split_table

```bash
$ singularity exec <container> /usr/local/bin/humann2_split_table
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_split_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_split_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_strain_profiler

```bash
$ singularity exec <container> /usr/local/bin/humann2_strain_profiler
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_strain_profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_strain_profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humann2_test

```bash
$ singularity exec <container> /usr/local/bin/humann2_test
$ podman run --it --rm --entrypoint /usr/local/bin/humann2_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humann2_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_to_slim.py

```bash
$ singularity exec <container> /usr/local/bin/map_to_slim.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphlan2.py

```bash
$ singularity exec <container> /usr/local/bin/metaphlan2.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaphlan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphlan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphlan2krona.py

```bash
$ singularity exec <container> /usr/local/bin/metaphlan2krona.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaphlan2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphlan2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi_gene_results_to_python.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi_gene_results_to_python.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_go_term.py

```bash
$ singularity exec <container> /usr/local/bin/plot_go_term.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prt_terms.py

```bash
$ singularity exec <container> /usr/local/bin/prt_terms.py
$ podman run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyqi

```bash
$ singularity exec <container> /usr/local/bin/pyqi
$ podman run --it --rm --entrypoint /usr/local/bin/pyqi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyqi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_hier.py

```bash
$ singularity exec <container> /usr/local/bin/wr_hier.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_sections.py

```bash
$ singularity exec <container> /usr/local/bin/wr_sections.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxpm

```bash
$ singularity exec <container> /usr/local/bin/cxpm
$ podman run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sxpm

```bash
$ singularity exec <container> /usr/local/bin/sxpm
$ podman run --it --rm --entrypoint /usr/local/bin/sxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
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