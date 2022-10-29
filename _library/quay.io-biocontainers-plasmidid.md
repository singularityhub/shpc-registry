---
layout: container
name:  "quay.io/biocontainers/plasmidid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plasmidid/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/plasmidid/container.yaml"
updated_at: "2022-10-29 05:30:52.454041"
latest: "1.6.5--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/plasmidid"
aliases:
 - "adapt_filter_coverage.sh"
 - "blast_align.sh"
 - "blast_to_bed.sh"
 - "blast_to_complete.sh"
 - "blast_to_link.sh"
 - "bowtie_mapper.sh"
 - "build_karyotype.sh"
 - "calculate_seqlen.sh"
 - "cdhit_cluster.sh"
 - "check_dependencies.sh"
 - "check_mandatory_files.sh"
 - "coordinate_adapter.sh"
 - "download_plasmid_database.py"
 - "draw_circos_images.sh"
 - "filter_fasta.sh"
 - "get_coverage.sh"
 - "gff_to_bed.sh"
 - "mash_screener.sh"
 - "mashclust.py"
 - "ncbi_database_fetcher.sh"
 - "plasmidID"
 - "process_cluster_output.sh"
 - "prokka_annotation.sh"
 - "quality_trim.sh"
 - "rename_from_fasta.sh"
 - "sam_to_bam.sh"
 - "spades_assembly.sh"
 - "summary_report_pid.py"
 - "summary_table.sh"
 - "tbl2asn-test"
 - "2to3-3.7"
 - "CA.pm"
 - "SOAPsh.pl"
 - "accn-at-a-time"
 - "ace.pl"
 - "ace2sam"
 - "acyclic"
 - "alimask"
 - "amino-acid-composition"
 - "annotate"
versions:
 - "1.6.5--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for plasmidid"
config: {"url": "https://biocontainers.pro/tools/plasmidid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plasmidid", "latest": {"1.6.5--hdfd78af_0": "sha256:b8e8a9c07ff3144644d55cdcff0c6c4fd4b8fdf8f4f3d503c47e0d9ed84a315f"}, "tags": {"1.6.5--hdfd78af_0": "sha256:b8e8a9c07ff3144644d55cdcff0c6c4fd4b8fdf8f4f3d503c47e0d9ed84a315f"}, "docker": "quay.io/biocontainers/plasmidid", "aliases": {"adapt_filter_coverage.sh": "/usr/local/bin/adapt_filter_coverage.sh", "blast_align.sh": "/usr/local/bin/blast_align.sh", "blast_to_bed.sh": "/usr/local/bin/blast_to_bed.sh", "blast_to_complete.sh": "/usr/local/bin/blast_to_complete.sh", "blast_to_link.sh": "/usr/local/bin/blast_to_link.sh", "bowtie_mapper.sh": "/usr/local/bin/bowtie_mapper.sh", "build_karyotype.sh": "/usr/local/bin/build_karyotype.sh", "calculate_seqlen.sh": "/usr/local/bin/calculate_seqlen.sh", "cdhit_cluster.sh": "/usr/local/bin/cdhit_cluster.sh", "check_dependencies.sh": "/usr/local/bin/check_dependencies.sh", "check_mandatory_files.sh": "/usr/local/bin/check_mandatory_files.sh", "coordinate_adapter.sh": "/usr/local/bin/coordinate_adapter.sh", "download_plasmid_database.py": "/usr/local/bin/download_plasmid_database.py", "draw_circos_images.sh": "/usr/local/bin/draw_circos_images.sh", "filter_fasta.sh": "/usr/local/bin/filter_fasta.sh", "get_coverage.sh": "/usr/local/bin/get_coverage.sh", "gff_to_bed.sh": "/usr/local/bin/gff_to_bed.sh", "mash_screener.sh": "/usr/local/bin/mash_screener.sh", "mashclust.py": "/usr/local/bin/mashclust.py", "ncbi_database_fetcher.sh": "/usr/local/bin/ncbi_database_fetcher.sh", "plasmidID": "/usr/local/bin/plasmidID", "process_cluster_output.sh": "/usr/local/bin/process_cluster_output.sh", "prokka_annotation.sh": "/usr/local/bin/prokka_annotation.sh", "quality_trim.sh": "/usr/local/bin/quality_trim.sh", "rename_from_fasta.sh": "/usr/local/bin/rename_from_fasta.sh", "sam_to_bam.sh": "/usr/local/bin/sam_to_bam.sh", "spades_assembly.sh": "/usr/local/bin/spades_assembly.sh", "summary_report_pid.py": "/usr/local/bin/summary_report_pid.py", "summary_table.sh": "/usr/local/bin/summary_table.sh", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "2to3-3.7": "/usr/local/bin/2to3-3.7", "CA.pm": "/usr/local/bin/CA.pm", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "ace.pl": "/usr/local/bin/ace.pl", "ace2sam": "/usr/local/bin/ace2sam", "acyclic": "/usr/local/bin/acyclic", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "annotate": "/usr/local/bin/annotate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plasmidid.
shpc-registry automated BioContainers addition for plasmidid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plasmidid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plasmidid:1.6.5--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plasmidid/1.6.5--hdfd78af_0
$ module help quay.io/biocontainers/plasmidid/1.6.5--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plasmidid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plasmidid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plasmidid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plasmidid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plasmidid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plasmidid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adapt_filter_coverage.sh

```bash
$ singularity exec <container> /usr/local/bin/adapt_filter_coverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adapt_filter_coverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adapt_filter_coverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_align.sh

```bash
$ singularity exec <container> /usr/local/bin/blast_align.sh
$ podman run --it --rm --entrypoint /usr/local/bin/blast_align.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_align.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_to_bed.sh

```bash
$ singularity exec <container> /usr/local/bin/blast_to_bed.sh
$ podman run --it --rm --entrypoint /usr/local/bin/blast_to_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_to_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_to_complete.sh

```bash
$ singularity exec <container> /usr/local/bin/blast_to_complete.sh
$ podman run --it --rm --entrypoint /usr/local/bin/blast_to_complete.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_to_complete.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_to_link.sh

```bash
$ singularity exec <container> /usr/local/bin/blast_to_link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/blast_to_link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_to_link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie_mapper.sh

```bash
$ singularity exec <container> /usr/local/bin/bowtie_mapper.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie_mapper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie_mapper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_karyotype.sh

```bash
$ singularity exec <container> /usr/local/bin/build_karyotype.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_karyotype.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_karyotype.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calculate_seqlen.sh

```bash
$ singularity exec <container> /usr/local/bin/calculate_seqlen.sh
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_seqlen.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_seqlen.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdhit_cluster.sh

```bash
$ singularity exec <container> /usr/local/bin/cdhit_cluster.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cdhit_cluster.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdhit_cluster.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_dependencies.sh

```bash
$ singularity exec <container> /usr/local/bin/check_dependencies.sh
$ podman run --it --rm --entrypoint /usr/local/bin/check_dependencies.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_dependencies.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_mandatory_files.sh

```bash
$ singularity exec <container> /usr/local/bin/check_mandatory_files.sh
$ podman run --it --rm --entrypoint /usr/local/bin/check_mandatory_files.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_mandatory_files.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coordinate_adapter.sh

```bash
$ singularity exec <container> /usr/local/bin/coordinate_adapter.sh
$ podman run --it --rm --entrypoint /usr/local/bin/coordinate_adapter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coordinate_adapter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_plasmid_database.py

```bash
$ singularity exec <container> /usr/local/bin/download_plasmid_database.py
$ podman run --it --rm --entrypoint /usr/local/bin/download_plasmid_database.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_plasmid_database.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_circos_images.sh

```bash
$ singularity exec <container> /usr/local/bin/draw_circos_images.sh
$ podman run --it --rm --entrypoint /usr/local/bin/draw_circos_images.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_circos_images.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_fasta.sh

```bash
$ singularity exec <container> /usr/local/bin/filter_fasta.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filter_fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_coverage.sh

```bash
$ singularity exec <container> /usr/local/bin/get_coverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/get_coverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_coverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_to_bed.sh

```bash
$ singularity exec <container> /usr/local/bin/gff_to_bed.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gff_to_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_to_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mash_screener.sh

```bash
$ singularity exec <container> /usr/local/bin/mash_screener.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mash_screener.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash_screener.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mashclust.py

```bash
$ singularity exec <container> /usr/local/bin/mashclust.py
$ podman run --it --rm --entrypoint /usr/local/bin/mashclust.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashclust.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi_database_fetcher.sh

```bash
$ singularity exec <container> /usr/local/bin/ncbi_database_fetcher.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi_database_fetcher.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi_database_fetcher.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidID

```bash
$ singularity exec <container> /usr/local/bin/plasmidID
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidID   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidID   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_cluster_output.sh

```bash
$ singularity exec <container> /usr/local/bin/process_cluster_output.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_cluster_output.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_cluster_output.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka_annotation.sh

```bash
$ singularity exec <container> /usr/local/bin/prokka_annotation.sh
$ podman run --it --rm --entrypoint /usr/local/bin/prokka_annotation.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka_annotation.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quality_trim.sh

```bash
$ singularity exec <container> /usr/local/bin/quality_trim.sh
$ podman run --it --rm --entrypoint /usr/local/bin/quality_trim.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quality_trim.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_from_fasta.sh

```bash
$ singularity exec <container> /usr/local/bin/rename_from_fasta.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rename_from_fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_from_fasta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_to_bam.sh

```bash
$ singularity exec <container> /usr/local/bin/sam_to_bam.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sam_to_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_to_bam.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades_assembly.sh

```bash
$ singularity exec <container> /usr/local/bin/spades_assembly.sh
$ podman run --it --rm --entrypoint /usr/local/bin/spades_assembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades_assembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summary_report_pid.py

```bash
$ singularity exec <container> /usr/local/bin/summary_report_pid.py
$ podman run --it --rm --entrypoint /usr/local/bin/summary_report_pid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summary_report_pid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summary_table.sh

```bash
$ singularity exec <container> /usr/local/bin/summary_table.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summary_table.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summary_table.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
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