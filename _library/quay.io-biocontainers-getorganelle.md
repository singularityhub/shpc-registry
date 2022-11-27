---
layout: container
name:  "quay.io/biocontainers/getorganelle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/getorganelle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/getorganelle/container.yaml"
updated_at: "2022-11-27 13:06:59.817663"
latest: "1.7.6.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/getorganelle"
aliases:
 - "check_annotations.py"
 - "cook_coding_for_blast.py"
 - "disentangle_organelle_assembly.py"
 - "evaluate_assembly_using_mapping.py"
 - "fastg_to_gfa.py"
 - "get_organelle_config.py"
 - "get_organelle_from_assembly.py"
 - "get_organelle_from_reads.py"
 - "get_pair_reads.py"
 - "gfa_to_fasta.py"
 - "gfa_to_fastg.py"
 - "isympy"
 - "join_spades_fastg_by_blast.py"
 - "make_batch_for_get_organelle.py"
 - "make_batch_for_iteratively_mapping_assembling.py"
 - "plastome_arch_info.py"
 - "reconstruct_graph_from_fasta.py"
 - "rm_low_coverage_duplicated_contigs.py"
 - "round_statistics.py"
 - "slim_graph.py"
 - "summary_get_organelle_output.py"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "mag-improve"
 - "spades-convert-bin-to-fasta"
 - "spades-gsimplifier"
 - "spades-kmer-estimating"
 - "spades-read-filter"
 - "spaligner"
 - "spades-bwa"
 - "spades-core"
versions:
 - "1.7.6.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for getorganelle"
config: {"url": "https://biocontainers.pro/tools/getorganelle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for getorganelle", "latest": {"1.7.6.1--pyh5e36f6f_0": "sha256:675d6c87fa16e483c1ced595e9ba032b57179032e940ba500099094340a6c226"}, "tags": {"1.7.6.1--pyh5e36f6f_0": "sha256:675d6c87fa16e483c1ced595e9ba032b57179032e940ba500099094340a6c226"}, "docker": "quay.io/biocontainers/getorganelle", "aliases": {"check_annotations.py": "/usr/local/bin/check_annotations.py", "cook_coding_for_blast.py": "/usr/local/bin/cook_coding_for_blast.py", "disentangle_organelle_assembly.py": "/usr/local/bin/disentangle_organelle_assembly.py", "evaluate_assembly_using_mapping.py": "/usr/local/bin/evaluate_assembly_using_mapping.py", "fastg_to_gfa.py": "/usr/local/bin/fastg_to_gfa.py", "get_organelle_config.py": "/usr/local/bin/get_organelle_config.py", "get_organelle_from_assembly.py": "/usr/local/bin/get_organelle_from_assembly.py", "get_organelle_from_reads.py": "/usr/local/bin/get_organelle_from_reads.py", "get_pair_reads.py": "/usr/local/bin/get_pair_reads.py", "gfa_to_fasta.py": "/usr/local/bin/gfa_to_fasta.py", "gfa_to_fastg.py": "/usr/local/bin/gfa_to_fastg.py", "isympy": "/usr/local/bin/isympy", "join_spades_fastg_by_blast.py": "/usr/local/bin/join_spades_fastg_by_blast.py", "make_batch_for_get_organelle.py": "/usr/local/bin/make_batch_for_get_organelle.py", "make_batch_for_iteratively_mapping_assembling.py": "/usr/local/bin/make_batch_for_iteratively_mapping_assembling.py", "plastome_arch_info.py": "/usr/local/bin/plastome_arch_info.py", "reconstruct_graph_from_fasta.py": "/usr/local/bin/reconstruct_graph_from_fasta.py", "rm_low_coverage_duplicated_contigs.py": "/usr/local/bin/rm_low_coverage_duplicated_contigs.py", "round_statistics.py": "/usr/local/bin/round_statistics.py", "slim_graph.py": "/usr/local/bin/slim_graph.py", "summary_get_organelle_output.py": "/usr/local/bin/summary_get_organelle_output.py", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "mag-improve": "/usr/local/bin/mag-improve", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-read-filter": "/usr/local/bin/spades-read-filter", "spaligner": "/usr/local/bin/spaligner", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-core": "/usr/local/bin/spades-core"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/getorganelle.
shpc-registry automated BioContainers addition for getorganelle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/getorganelle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/getorganelle:1.7.6.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/getorganelle/1.7.6.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/getorganelle/1.7.6.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### getorganelle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### getorganelle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### getorganelle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### getorganelle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### getorganelle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### getorganelle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check_annotations.py

```bash
$ singularity exec <container> /usr/local/bin/check_annotations.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_annotations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_annotations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cook_coding_for_blast.py

```bash
$ singularity exec <container> /usr/local/bin/cook_coding_for_blast.py
$ podman run --it --rm --entrypoint /usr/local/bin/cook_coding_for_blast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cook_coding_for_blast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disentangle_organelle_assembly.py

```bash
$ singularity exec <container> /usr/local/bin/disentangle_organelle_assembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/disentangle_organelle_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disentangle_organelle_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evaluate_assembly_using_mapping.py

```bash
$ singularity exec <container> /usr/local/bin/evaluate_assembly_using_mapping.py
$ podman run --it --rm --entrypoint /usr/local/bin/evaluate_assembly_using_mapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluate_assembly_using_mapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastg_to_gfa.py

```bash
$ singularity exec <container> /usr/local/bin/fastg_to_gfa.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastg_to_gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastg_to_gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_organelle_config.py

```bash
$ singularity exec <container> /usr/local/bin/get_organelle_config.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_organelle_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_organelle_config.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_organelle_from_assembly.py

```bash
$ singularity exec <container> /usr/local/bin/get_organelle_from_assembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_organelle_from_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_organelle_from_assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_organelle_from_reads.py

```bash
$ singularity exec <container> /usr/local/bin/get_organelle_from_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_organelle_from_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_organelle_from_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_pair_reads.py

```bash
$ singularity exec <container> /usr/local/bin/get_pair_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_pair_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_pair_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/gfa_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/gfa_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa_to_fastg.py

```bash
$ singularity exec <container> /usr/local/bin/gfa_to_fastg.py
$ podman run --it --rm --entrypoint /usr/local/bin/gfa_to_fastg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa_to_fastg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### join_spades_fastg_by_blast.py

```bash
$ singularity exec <container> /usr/local/bin/join_spades_fastg_by_blast.py
$ podman run --it --rm --entrypoint /usr/local/bin/join_spades_fastg_by_blast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/join_spades_fastg_by_blast.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_batch_for_get_organelle.py

```bash
$ singularity exec <container> /usr/local/bin/make_batch_for_get_organelle.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_batch_for_get_organelle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_batch_for_get_organelle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_batch_for_iteratively_mapping_assembling.py

```bash
$ singularity exec <container> /usr/local/bin/make_batch_for_iteratively_mapping_assembling.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_batch_for_iteratively_mapping_assembling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_batch_for_iteratively_mapping_assembling.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plastome_arch_info.py

```bash
$ singularity exec <container> /usr/local/bin/plastome_arch_info.py
$ podman run --it --rm --entrypoint /usr/local/bin/plastome_arch_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plastome_arch_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reconstruct_graph_from_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/reconstruct_graph_from_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/reconstruct_graph_from_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reconstruct_graph_from_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rm_low_coverage_duplicated_contigs.py

```bash
$ singularity exec <container> /usr/local/bin/rm_low_coverage_duplicated_contigs.py
$ podman run --it --rm --entrypoint /usr/local/bin/rm_low_coverage_duplicated_contigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rm_low_coverage_duplicated_contigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### round_statistics.py

```bash
$ singularity exec <container> /usr/local/bin/round_statistics.py
$ podman run --it --rm --entrypoint /usr/local/bin/round_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/round_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slim_graph.py

```bash
$ singularity exec <container> /usr/local/bin/slim_graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/slim_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slim_graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summary_get_organelle_output.py

```bash
$ singularity exec <container> /usr/local/bin/summary_get_organelle_output.py
$ podman run --it --rm --entrypoint /usr/local/bin/summary_get_organelle_output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summary_get_organelle_output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-mapping-stats

```bash
$ singularity exec <container> /usr/local/bin/cds-mapping-stats
$ podman run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-subgraphs

```bash
$ singularity exec <container> /usr/local/bin/cds-subgraphs
$ podman run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mag-improve

```bash
$ singularity exec <container> /usr/local/bin/mag-improve
$ podman run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gsimplifier

```bash
$ singularity exec <container> /usr/local/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmer-estimating

```bash
$ singularity exec <container> /usr/local/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter

```bash
$ singularity exec <container> /usr/local/bin/spades-read-filter
$ podman run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner

```bash
$ singularity exec <container> /usr/local/bin/spaligner
$ podman run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-bwa

```bash
$ singularity exec <container> /usr/local/bin/spades-bwa
$ podman run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-core

```bash
$ singularity exec <container> /usr/local/bin/spades-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
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