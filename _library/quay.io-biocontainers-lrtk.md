---
layout: container
name:  "quay.io/biocontainers/lrtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lrtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lrtk/container.yaml"
updated_at: "2023-07-13 03:21:31.417906"
latest: "1.5--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/lrtk"
aliases:
 - "Aquila_assembly_based_variants_call"
 - "Aquila_clean"
 - "Aquila_phasing_all_variants"
 - "Aquila_step0_sortbam"
 - "Aquila_step0_sortbam_multilibs"
 - "Aquila_step1"
 - "Aquila_step1_multilibs"
 - "Aquila_step2"
 - "GenomeAnalysisTK"
 - "HAPCUT2"
 - "LinkFragments.py"
 - "calculate_haplotype_statistics.py"
 - "extractHAIRS"
 - "gatk-register"
 - "hapcut2"
 - "lrtk"
 - "sam_add_rg.pl"
 - "split_ref_by_bai_datasize.py"
 - "update_version.sh"
 - "whatshap"
 - "gatk"
 - "fastp"
 - "picard"
 - "tabix++"
 - "bamleftalign"
 - "bc"
 - "coverage_to_regions.py"
 - "dc"
 - "fasta_generate_regions.py"
 - "freebayes-parallel"
 - "generate_freebayes_region_scripts.sh"
 - "abba-baba"
 - "bFst"
 - "bed2region"
 - "bgziptabix"
 - "dumpContigsFromHeader"
 - "freebayes"
 - "genotypeSummary"
 - "hapLrt"
 - "iHS"
 - "meltEHH"
 - "normalize-iHS"
 - "pFst"
 - "pVst"
 - "permuteGPAT++"
versions:
 - "1.5--pyh5e36f6f_0"
description: "singularity registry hpc automated addition for lrtk"
config: {"url": "https://biocontainers.pro/tools/lrtk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lrtk", "latest": {"1.5--pyh5e36f6f_0": "sha256:33b618c5f1b969f42637e2eedf64a43253ac21e1726f4d828bf234c5eb20e8e3"}, "tags": {"1.5--pyh5e36f6f_0": "sha256:33b618c5f1b969f42637e2eedf64a43253ac21e1726f4d828bf234c5eb20e8e3"}, "docker": "quay.io/biocontainers/lrtk", "aliases": {"Aquila_assembly_based_variants_call": "/usr/local/bin/Aquila_assembly_based_variants_call", "Aquila_clean": "/usr/local/bin/Aquila_clean", "Aquila_phasing_all_variants": "/usr/local/bin/Aquila_phasing_all_variants", "Aquila_step0_sortbam": "/usr/local/bin/Aquila_step0_sortbam", "Aquila_step0_sortbam_multilibs": "/usr/local/bin/Aquila_step0_sortbam_multilibs", "Aquila_step1": "/usr/local/bin/Aquila_step1", "Aquila_step1_multilibs": "/usr/local/bin/Aquila_step1_multilibs", "Aquila_step2": "/usr/local/bin/Aquila_step2", "GenomeAnalysisTK": "/usr/local/bin/GenomeAnalysisTK", "HAPCUT2": "/usr/local/bin/HAPCUT2", "LinkFragments.py": "/usr/local/bin/LinkFragments.py", "calculate_haplotype_statistics.py": "/usr/local/bin/calculate_haplotype_statistics.py", "extractHAIRS": "/usr/local/bin/extractHAIRS", "gatk-register": "/usr/local/bin/gatk-register", "hapcut2": "/usr/local/bin/hapcut2", "lrtk": "/usr/local/bin/lrtk", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py", "update_version.sh": "/usr/local/bin/update_version.sh", "whatshap": "/usr/local/bin/whatshap", "gatk": "/usr/local/bin/gatk", "fastp": "/usr/local/bin/fastp", "picard": "/usr/local/bin/picard", "tabix++": "/usr/local/bin/tabix++", "bamleftalign": "/usr/local/bin/bamleftalign", "bc": "/usr/local/bin/bc", "coverage_to_regions.py": "/usr/local/bin/coverage_to_regions.py", "dc": "/usr/local/bin/dc", "fasta_generate_regions.py": "/usr/local/bin/fasta_generate_regions.py", "freebayes-parallel": "/usr/local/bin/freebayes-parallel", "generate_freebayes_region_scripts.sh": "/usr/local/bin/generate_freebayes_region_scripts.sh", "abba-baba": "/usr/local/bin/abba-baba", "bFst": "/usr/local/bin/bFst", "bed2region": "/usr/local/bin/bed2region", "bgziptabix": "/usr/local/bin/bgziptabix", "dumpContigsFromHeader": "/usr/local/bin/dumpContigsFromHeader", "freebayes": "/usr/local/bin/freebayes", "genotypeSummary": "/usr/local/bin/genotypeSummary", "hapLrt": "/usr/local/bin/hapLrt", "iHS": "/usr/local/bin/iHS", "meltEHH": "/usr/local/bin/meltEHH", "normalize-iHS": "/usr/local/bin/normalize-iHS", "pFst": "/usr/local/bin/pFst", "pVst": "/usr/local/bin/pVst", "permuteGPAT++": "/usr/local/bin/permuteGPAT++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lrtk.
singularity registry hpc automated addition for lrtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lrtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lrtk:1.5--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lrtk/1.5--pyh5e36f6f_0
$ module help quay.io/biocontainers/lrtk/1.5--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lrtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lrtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lrtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lrtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lrtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lrtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Aquila_assembly_based_variants_call

```bash
$ singularity exec <container> /usr/local/bin/Aquila_assembly_based_variants_call
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_assembly_based_variants_call   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_assembly_based_variants_call   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_clean

```bash
$ singularity exec <container> /usr/local/bin/Aquila_clean
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_phasing_all_variants

```bash
$ singularity exec <container> /usr/local/bin/Aquila_phasing_all_variants
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_phasing_all_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_phasing_all_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step0_sortbam

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step0_sortbam
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step0_sortbam_multilibs

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step0_sortbam_multilibs
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step1

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step1
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step1_multilibs

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step1_multilibs
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step1_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step1_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step2

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step2
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenomeAnalysisTK

```bash
$ singularity exec <container> /usr/local/bin/GenomeAnalysisTK
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HAPCUT2

```bash
$ singularity exec <container> /usr/local/bin/HAPCUT2
$ podman run --it --rm --entrypoint /usr/local/bin/HAPCUT2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HAPCUT2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LinkFragments.py

```bash
$ singularity exec <container> /usr/local/bin/LinkFragments.py
$ podman run --it --rm --entrypoint /usr/local/bin/LinkFragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LinkFragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calculate_haplotype_statistics.py

```bash
$ singularity exec <container> /usr/local/bin/calculate_haplotype_statistics.py
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_haplotype_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_haplotype_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractHAIRS

```bash
$ singularity exec <container> /usr/local/bin/extractHAIRS
$ podman run --it --rm --entrypoint /usr/local/bin/extractHAIRS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractHAIRS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk-register

```bash
$ singularity exec <container> /usr/local/bin/gatk-register
$ podman run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapcut2

```bash
$ singularity exec <container> /usr/local/bin/hapcut2
$ podman run --it --rm --entrypoint /usr/local/bin/hapcut2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapcut2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrtk

```bash
$ singularity exec <container> /usr/local/bin/lrtk
$ podman run --it --rm --entrypoint /usr/local/bin/lrtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_add_rg.pl

```bash
$ singularity exec <container> /usr/local/bin/sam_add_rg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_ref_by_bai_datasize.py

```bash
$ singularity exec <container> /usr/local/bin/split_ref_by_bai_datasize.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_version.sh

```bash
$ singularity exec <container> /usr/local/bin/update_version.sh
$ podman run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whatshap

```bash
$ singularity exec <container> /usr/local/bin/whatshap
$ podman run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk

```bash
$ singularity exec <container> /usr/local/bin/gatk
$ podman run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamleftalign

```bash
$ singularity exec <container> /usr/local/bin/bamleftalign
$ podman run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_to_regions.py

```bash
$ singularity exec <container> /usr/local/bin/coverage_to_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_generate_regions.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_generate_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freebayes-parallel

```bash
$ singularity exec <container> /usr/local/bin/freebayes-parallel
$ podman run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_freebayes_region_scripts.sh

```bash
$ singularity exec <container> /usr/local/bin/generate_freebayes_region_scripts.sh
$ podman run --it --rm --entrypoint /usr/local/bin/generate_freebayes_region_scripts.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_freebayes_region_scripts.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abba-baba

```bash
$ singularity exec <container> /usr/local/bin/abba-baba
$ podman run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bFst

```bash
$ singularity exec <container> /usr/local/bin/bFst
$ podman run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2region

```bash
$ singularity exec <container> /usr/local/bin/bed2region
$ podman run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgziptabix

```bash
$ singularity exec <container> /usr/local/bin/bgziptabix
$ podman run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpContigsFromHeader

```bash
$ singularity exec <container> /usr/local/bin/dumpContigsFromHeader
$ podman run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freebayes

```bash
$ singularity exec <container> /usr/local/bin/freebayes
$ podman run --it --rm --entrypoint /usr/local/bin/freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotypeSummary

```bash
$ singularity exec <container> /usr/local/bin/genotypeSummary
$ podman run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapLrt

```bash
$ singularity exec <container> /usr/local/bin/hapLrt
$ podman run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iHS

```bash
$ singularity exec <container> /usr/local/bin/iHS
$ podman run --it --rm --entrypoint /usr/local/bin/iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meltEHH

```bash
$ singularity exec <container> /usr/local/bin/meltEHH
$ podman run --it --rm --entrypoint /usr/local/bin/meltEHH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meltEHH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize-iHS

```bash
$ singularity exec <container> /usr/local/bin/normalize-iHS
$ podman run --it --rm --entrypoint /usr/local/bin/normalize-iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize-iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pFst

```bash
$ singularity exec <container> /usr/local/bin/pFst
$ podman run --it --rm --entrypoint /usr/local/bin/pFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pVst

```bash
$ singularity exec <container> /usr/local/bin/pVst
$ podman run --it --rm --entrypoint /usr/local/bin/pVst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pVst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### permuteGPAT++

```bash
$ singularity exec <container> /usr/local/bin/permuteGPAT++
$ podman run --it --rm --entrypoint /usr/local/bin/permuteGPAT++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/permuteGPAT++   -v ${PWD} -w ${PWD} <container> -c " $@"
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