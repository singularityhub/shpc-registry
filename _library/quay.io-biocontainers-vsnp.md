---
layout: container
name:  "quay.io/biocontainers/vsnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vsnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vsnp/container.yaml"
updated_at: "2024-11-13 03:35:27.291897"
latest: "2.03--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/vsnp"
aliases:
 - "abyss-rresolver-short"
 - "abyss-stack-size"
 - "cpuinfo"
 - "irqtop"
 - "lsirq"
 - "nsenter"
 - "prlimit"
 - "sam_add_rg.pl"
 - "scriptlive"
 - "update_version.sh"
 - "vSNP_step1.py"
 - "vSNP_step2.py"
 - "vsnp_alignment_vcf.py"
 - "vsnp_best_reference.py"
 - "vsnp_bruc_mlst.py"
 - "vsnp_chromosome_reference.py"
 - "vsnp_excel_merge_files.py"
 - "vsnp_fasta_gbk_gff_by_acc.py"
 - "vsnp_fasta_to_snps_table.py"
 - "vsnp_fastq_quality.py"
 - "vsnp_file_management.py"
 - "vsnp_filter_finder.py"
 - "vsnp_group_reporter.py"
 - "vsnp_html_step2_summary.py"
 - "vsnp_merge_vcf_into_fasta.py"
 - "vsnp_path_adder.py"
 - "vsnp_reference_options.py"
 - "vsnp_remove_from_analysis.py"
 - "vsnp_spoligotype.py"
 - "cal"
 - "chmem"
 - "choom"
 - "chrt"
 - "col"
 - "colcrt"
 - "colrm"
 - "column"
 - "dmesg"
 - "eject"
versions:
 - "2.03--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for vsnp"
config: {"url": "https://biocontainers.pro/tools/vsnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vsnp", "latest": {"2.03--hdfd78af_2": "sha256:05bb4ee3676e88481698f939591c2e582d9bc1df3dbea476081befe65089bd86"}, "tags": {"2.03--hdfd78af_2": "sha256:05bb4ee3676e88481698f939591c2e582d9bc1df3dbea476081befe65089bd86"}, "docker": "quay.io/biocontainers/vsnp", "aliases": {"abyss-rresolver-short": "/usr/local/bin/abyss-rresolver-short", "abyss-stack-size": "/usr/local/bin/abyss-stack-size", "cpuinfo": "/usr/local/bin/cpuinfo", "irqtop": "/usr/local/bin/irqtop", "lsirq": "/usr/local/bin/lsirq", "nsenter": "/usr/local/bin/nsenter", "prlimit": "/usr/local/bin/prlimit", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "scriptlive": "/usr/local/bin/scriptlive", "update_version.sh": "/usr/local/bin/update_version.sh", "vSNP_step1.py": "/usr/local/bin/vSNP_step1.py", "vSNP_step2.py": "/usr/local/bin/vSNP_step2.py", "vsnp_alignment_vcf.py": "/usr/local/bin/vsnp_alignment_vcf.py", "vsnp_best_reference.py": "/usr/local/bin/vsnp_best_reference.py", "vsnp_bruc_mlst.py": "/usr/local/bin/vsnp_bruc_mlst.py", "vsnp_chromosome_reference.py": "/usr/local/bin/vsnp_chromosome_reference.py", "vsnp_excel_merge_files.py": "/usr/local/bin/vsnp_excel_merge_files.py", "vsnp_fasta_gbk_gff_by_acc.py": "/usr/local/bin/vsnp_fasta_gbk_gff_by_acc.py", "vsnp_fasta_to_snps_table.py": "/usr/local/bin/vsnp_fasta_to_snps_table.py", "vsnp_fastq_quality.py": "/usr/local/bin/vsnp_fastq_quality.py", "vsnp_file_management.py": "/usr/local/bin/vsnp_file_management.py", "vsnp_filter_finder.py": "/usr/local/bin/vsnp_filter_finder.py", "vsnp_group_reporter.py": "/usr/local/bin/vsnp_group_reporter.py", "vsnp_html_step2_summary.py": "/usr/local/bin/vsnp_html_step2_summary.py", "vsnp_merge_vcf_into_fasta.py": "/usr/local/bin/vsnp_merge_vcf_into_fasta.py", "vsnp_path_adder.py": "/usr/local/bin/vsnp_path_adder.py", "vsnp_reference_options.py": "/usr/local/bin/vsnp_reference_options.py", "vsnp_remove_from_analysis.py": "/usr/local/bin/vsnp_remove_from_analysis.py", "vsnp_spoligotype.py": "/usr/local/bin/vsnp_spoligotype.py", "cal": "/usr/local/bin/cal", "chmem": "/usr/local/bin/chmem", "choom": "/usr/local/bin/choom", "chrt": "/usr/local/bin/chrt", "col": "/usr/local/bin/col", "colcrt": "/usr/local/bin/colcrt", "colrm": "/usr/local/bin/colrm", "column": "/usr/local/bin/column", "dmesg": "/usr/local/bin/dmesg", "eject": "/usr/local/bin/eject"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vsnp.
shpc-registry automated BioContainers addition for vsnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vsnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vsnp:2.03--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vsnp/2.03--hdfd78af_2
$ module help quay.io/biocontainers/vsnp/2.03--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vsnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vsnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vsnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vsnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vsnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vsnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-rresolver-short

```bash
$ singularity exec <container> /usr/local/bin/abyss-rresolver-short
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-stack-size

```bash
$ singularity exec <container> /usr/local/bin/abyss-stack-size
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irqtop

```bash
$ singularity exec <container> /usr/local/bin/irqtop
$ podman run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irqtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsirq

```bash
$ singularity exec <container> /usr/local/bin/lsirq
$ podman run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsirq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nsenter

```bash
$ singularity exec <container> /usr/local/bin/nsenter
$ podman run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nsenter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prlimit

```bash
$ singularity exec <container> /usr/local/bin/prlimit
$ podman run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prlimit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_add_rg.pl

```bash
$ singularity exec <container> /usr/local/bin/sam_add_rg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scriptlive

```bash
$ singularity exec <container> /usr/local/bin/scriptlive
$ podman run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_version.sh

```bash
$ singularity exec <container> /usr/local/bin/update_version.sh
$ podman run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vSNP_step1.py

```bash
$ singularity exec <container> /usr/local/bin/vSNP_step1.py
$ podman run --it --rm --entrypoint /usr/local/bin/vSNP_step1.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vSNP_step1.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vSNP_step2.py

```bash
$ singularity exec <container> /usr/local/bin/vSNP_step2.py
$ podman run --it --rm --entrypoint /usr/local/bin/vSNP_step2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vSNP_step2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_alignment_vcf.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_alignment_vcf.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_alignment_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_alignment_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_best_reference.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_best_reference.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_best_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_best_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_bruc_mlst.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_bruc_mlst.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_bruc_mlst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_bruc_mlst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_chromosome_reference.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_chromosome_reference.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_chromosome_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_chromosome_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_excel_merge_files.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_excel_merge_files.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_excel_merge_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_excel_merge_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_fasta_gbk_gff_by_acc.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_fasta_gbk_gff_by_acc.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_fasta_gbk_gff_by_acc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_fasta_gbk_gff_by_acc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_fasta_to_snps_table.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_fasta_to_snps_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_fasta_to_snps_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_fasta_to_snps_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_fastq_quality.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_fastq_quality.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_fastq_quality.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_fastq_quality.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_file_management.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_file_management.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_file_management.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_file_management.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_filter_finder.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_filter_finder.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_filter_finder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_filter_finder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_group_reporter.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_group_reporter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_group_reporter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_group_reporter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_html_step2_summary.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_html_step2_summary.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_html_step2_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_html_step2_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_merge_vcf_into_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_merge_vcf_into_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_merge_vcf_into_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_merge_vcf_into_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_path_adder.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_path_adder.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_path_adder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_path_adder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_reference_options.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_reference_options.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_reference_options.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_reference_options.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_remove_from_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_remove_from_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_remove_from_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_remove_from_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsnp_spoligotype.py

```bash
$ singularity exec <container> /usr/local/bin/vsnp_spoligotype.py
$ podman run --it --rm --entrypoint /usr/local/bin/vsnp_spoligotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsnp_spoligotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal

```bash
$ singularity exec <container> /usr/local/bin/cal
$ podman run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmem

```bash
$ singularity exec <container> /usr/local/bin/chmem
$ podman run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### choom

```bash
$ singularity exec <container> /usr/local/bin/choom
$ podman run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrt

```bash
$ singularity exec <container> /usr/local/bin/chrt
$ podman run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### col

```bash
$ singularity exec <container> /usr/local/bin/col
$ podman run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colcrt

```bash
$ singularity exec <container> /usr/local/bin/colcrt
$ podman run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colrm

```bash
$ singularity exec <container> /usr/local/bin/colrm
$ podman run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column

```bash
$ singularity exec <container> /usr/local/bin/column
$ podman run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmesg

```bash
$ singularity exec <container> /usr/local/bin/dmesg
$ podman run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eject

```bash
$ singularity exec <container> /usr/local/bin/eject
$ podman run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
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