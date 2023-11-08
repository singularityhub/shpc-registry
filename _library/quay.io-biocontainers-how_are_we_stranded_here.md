---
layout: container
name:  "quay.io/biocontainers/how_are_we_stranded_here"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/how_are_we_stranded_here/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/how_are_we_stranded_here/container.yaml"
updated_at: "2023-11-08 02:43:54.751799"
latest: "1.0.1--pyhfa5458b_0"
container_url: "https://biocontainers.pro/tools/how_are_we_stranded_here"
aliases:
 - "FPKM-UQ.py"
 - "FPKM_count.py"
 - "RNA_fragment_size.py"
 - "RPKM_saturation.py"
 - "bam2fq.py"
 - "bam2wig.py"
 - "bam_stat.py"
 - "check_strandedness"
 - "clipping_profile.py"
 - "deletion_profile.py"
 - "divide_bam.py"
 - "geneBody_coverage.py"
 - "geneBody_coverage2.py"
 - "gff32gtf"
 - "infer_experiment.py"
 - "inner_distance.py"
 - "insertion_profile.py"
 - "junction_annotation.py"
 - "junction_saturation.py"
 - "kallisto"
 - "mismatch_profile.py"
 - "normalize_bigwig.py"
 - "overlay_bigwig.py"
 - "read_GC.py"
 - "read_NVC.py"
 - "read_distribution.py"
 - "read_duplication.py"
 - "read_hexamer.py"
 - "read_quality.py"
 - "split_bam.py"
 - "split_paired_bam.py"
 - "tin.py"
 - "gtf2bed"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
 - "bed_bigwig_profile.py"
 - "bed_build_windows.py"
 - "bed_complement.py"
versions:
 - "1.0.1--pyhfa5458b_0"
description: "shpc-registry automated BioContainers addition for how_are_we_stranded_here"
config: {"url": "https://biocontainers.pro/tools/how_are_we_stranded_here", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for how_are_we_stranded_here", "latest": {"1.0.1--pyhfa5458b_0": "sha256:ad7581058ab8b39a888b527e23e69b74d23df3d95a91734646d3ee11b9af4f74"}, "tags": {"1.0.1--pyhfa5458b_0": "sha256:ad7581058ab8b39a888b527e23e69b74d23df3d95a91734646d3ee11b9af4f74"}, "docker": "quay.io/biocontainers/how_are_we_stranded_here", "aliases": {"FPKM-UQ.py": "/usr/local/bin/FPKM-UQ.py", "FPKM_count.py": "/usr/local/bin/FPKM_count.py", "RNA_fragment_size.py": "/usr/local/bin/RNA_fragment_size.py", "RPKM_saturation.py": "/usr/local/bin/RPKM_saturation.py", "bam2fq.py": "/usr/local/bin/bam2fq.py", "bam2wig.py": "/usr/local/bin/bam2wig.py", "bam_stat.py": "/usr/local/bin/bam_stat.py", "check_strandedness": "/usr/local/bin/check_strandedness", "clipping_profile.py": "/usr/local/bin/clipping_profile.py", "deletion_profile.py": "/usr/local/bin/deletion_profile.py", "divide_bam.py": "/usr/local/bin/divide_bam.py", "geneBody_coverage.py": "/usr/local/bin/geneBody_coverage.py", "geneBody_coverage2.py": "/usr/local/bin/geneBody_coverage2.py", "gff32gtf": "/usr/local/bin/gff32gtf", "infer_experiment.py": "/usr/local/bin/infer_experiment.py", "inner_distance.py": "/usr/local/bin/inner_distance.py", "insertion_profile.py": "/usr/local/bin/insertion_profile.py", "junction_annotation.py": "/usr/local/bin/junction_annotation.py", "junction_saturation.py": "/usr/local/bin/junction_saturation.py", "kallisto": "/usr/local/bin/kallisto", "mismatch_profile.py": "/usr/local/bin/mismatch_profile.py", "normalize_bigwig.py": "/usr/local/bin/normalize_bigwig.py", "overlay_bigwig.py": "/usr/local/bin/overlay_bigwig.py", "read_GC.py": "/usr/local/bin/read_GC.py", "read_NVC.py": "/usr/local/bin/read_NVC.py", "read_distribution.py": "/usr/local/bin/read_distribution.py", "read_duplication.py": "/usr/local/bin/read_duplication.py", "read_hexamer.py": "/usr/local/bin/read_hexamer.py", "read_quality.py": "/usr/local/bin/read_quality.py", "split_bam.py": "/usr/local/bin/split_bam.py", "split_paired_bam.py": "/usr/local/bin/split_paired_bam.py", "tin.py": "/usr/local/bin/tin.py", "gtf2bed": "/usr/local/bin/gtf2bed", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/how_are_we_stranded_here.
shpc-registry automated BioContainers addition for how_are_we_stranded_here
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/how_are_we_stranded_here
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/how_are_we_stranded_here:1.0.1--pyhfa5458b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/how_are_we_stranded_here/1.0.1--pyhfa5458b_0
$ module help quay.io/biocontainers/how_are_we_stranded_here/1.0.1--pyhfa5458b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### how_are_we_stranded_here-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### how_are_we_stranded_here-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### how_are_we_stranded_here-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### how_are_we_stranded_here-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### how_are_we_stranded_here-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### how_are_we_stranded_here-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FPKM-UQ.py

```bash
$ singularity exec <container> /usr/local/bin/FPKM-UQ.py
$ podman run --it --rm --entrypoint /usr/local/bin/FPKM-UQ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FPKM-UQ.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FPKM_count.py

```bash
$ singularity exec <container> /usr/local/bin/FPKM_count.py
$ podman run --it --rm --entrypoint /usr/local/bin/FPKM_count.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FPKM_count.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA_fragment_size.py

```bash
$ singularity exec <container> /usr/local/bin/RNA_fragment_size.py
$ podman run --it --rm --entrypoint /usr/local/bin/RNA_fragment_size.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA_fragment_size.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RPKM_saturation.py

```bash
$ singularity exec <container> /usr/local/bin/RPKM_saturation.py
$ podman run --it --rm --entrypoint /usr/local/bin/RPKM_saturation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RPKM_saturation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2fq.py

```bash
$ singularity exec <container> /usr/local/bin/bam2fq.py
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2wig.py

```bash
$ singularity exec <container> /usr/local/bin/bam2wig.py
$ podman run --it --rm --entrypoint /usr/local/bin/bam2wig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2wig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_stat.py

```bash
$ singularity exec <container> /usr/local/bin/bam_stat.py
$ podman run --it --rm --entrypoint /usr/local/bin/bam_stat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_stat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_strandedness

```bash
$ singularity exec <container> /usr/local/bin/check_strandedness
$ podman run --it --rm --entrypoint /usr/local/bin/check_strandedness   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_strandedness   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clipping_profile.py

```bash
$ singularity exec <container> /usr/local/bin/clipping_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/clipping_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clipping_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deletion_profile.py

```bash
$ singularity exec <container> /usr/local/bin/deletion_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/deletion_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deletion_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### divide_bam.py

```bash
$ singularity exec <container> /usr/local/bin/divide_bam.py
$ podman run --it --rm --entrypoint /usr/local/bin/divide_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/divide_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneBody_coverage.py

```bash
$ singularity exec <container> /usr/local/bin/geneBody_coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneBody_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneBody_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneBody_coverage2.py

```bash
$ singularity exec <container> /usr/local/bin/geneBody_coverage2.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneBody_coverage2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneBody_coverage2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff32gtf

```bash
$ singularity exec <container> /usr/local/bin/gff32gtf
$ podman run --it --rm --entrypoint /usr/local/bin/gff32gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff32gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infer_experiment.py

```bash
$ singularity exec <container> /usr/local/bin/infer_experiment.py
$ podman run --it --rm --entrypoint /usr/local/bin/infer_experiment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infer_experiment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inner_distance.py

```bash
$ singularity exec <container> /usr/local/bin/inner_distance.py
$ podman run --it --rm --entrypoint /usr/local/bin/inner_distance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inner_distance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### insertion_profile.py

```bash
$ singularity exec <container> /usr/local/bin/insertion_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/insertion_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/insertion_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### junction_annotation.py

```bash
$ singularity exec <container> /usr/local/bin/junction_annotation.py
$ podman run --it --rm --entrypoint /usr/local/bin/junction_annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/junction_annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### junction_saturation.py

```bash
$ singularity exec <container> /usr/local/bin/junction_saturation.py
$ podman run --it --rm --entrypoint /usr/local/bin/junction_saturation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/junction_saturation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mismatch_profile.py

```bash
$ singularity exec <container> /usr/local/bin/mismatch_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/mismatch_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mismatch_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize_bigwig.py

```bash
$ singularity exec <container> /usr/local/bin/normalize_bigwig.py
$ podman run --it --rm --entrypoint /usr/local/bin/normalize_bigwig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize_bigwig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### overlay_bigwig.py

```bash
$ singularity exec <container> /usr/local/bin/overlay_bigwig.py
$ podman run --it --rm --entrypoint /usr/local/bin/overlay_bigwig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/overlay_bigwig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_GC.py

```bash
$ singularity exec <container> /usr/local/bin/read_GC.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_GC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_GC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_NVC.py

```bash
$ singularity exec <container> /usr/local/bin/read_NVC.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_NVC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_NVC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_distribution.py

```bash
$ singularity exec <container> /usr/local/bin/read_distribution.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_duplication.py

```bash
$ singularity exec <container> /usr/local/bin/read_duplication.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_duplication.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_duplication.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_hexamer.py

```bash
$ singularity exec <container> /usr/local/bin/read_hexamer.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_hexamer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_hexamer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_quality.py

```bash
$ singularity exec <container> /usr/local/bin/read_quality.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_quality.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_quality.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_bam.py

```bash
$ singularity exec <container> /usr/local/bin/split_bam.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_paired_bam.py

```bash
$ singularity exec <container> /usr/local/bin/split_paired_bam.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_paired_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_paired_bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tin.py

```bash
$ singularity exec <container> /usr/local/bin/tin.py
$ podman run --it --rm --entrypoint /usr/local/bin/tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2bed

```bash
$ singularity exec <container> /usr/local/bin/gtf2bed
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_print_template.py

```bash
$ singularity exec <container> /usr/local/bin/align_print_template.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_extract_ranges.py

```bash
$ singularity exec <container> /usr/local/bin/axt_extract_ranges.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_lav.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_lav.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_maf.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_maf.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_bigwig_profile.py

```bash
$ singularity exec <container> /usr/local/bin/bed_bigwig_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_bigwig_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_bigwig_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_build_windows.py

```bash
$ singularity exec <container> /usr/local/bin/bed_build_windows.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_build_windows.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_build_windows.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_complement.py

```bash
$ singularity exec <container> /usr/local/bin/bed_complement.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_complement.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_complement.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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