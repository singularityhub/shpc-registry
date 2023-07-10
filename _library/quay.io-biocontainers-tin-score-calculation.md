---
layout: container
name:  "quay.io/biocontainers/tin-score-calculation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tin-score-calculation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tin-score-calculation/container.yaml"
updated_at: "2023-07-10 03:29:49.547398"
latest: "0.6.3--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/tin-score-calculation"
aliases:
 - "FPKM-UQ.py"
 - "FPKM_count.py"
 - "RNA_fragment_size.py"
 - "RPKM_saturation.py"
 - "bam2fq.py"
 - "bam2wig.py"
 - "bam_stat.py"
 - "calculate-tin.py"
 - "clipping_profile.py"
 - "deletion_profile.py"
 - "divide_bam.py"
 - "geneBody_coverage.py"
 - "geneBody_coverage2.py"
 - "infer_experiment.py"
 - "inner_distance.py"
 - "insertion_profile.py"
 - "junction_annotation.py"
 - "junction_saturation.py"
 - "merge-tin.py"
 - "mismatch_profile.py"
 - "normalize_bigwig.py"
 - "overlay_bigwig.py"
 - "plot-tin.py"
 - "read_GC.py"
 - "read_NVC.py"
 - "read_distribution.py"
 - "read_duplication.py"
 - "read_hexamer.py"
 - "read_quality.py"
 - "split_bam.py"
 - "split_paired_bam.py"
 - "summarize-tin.py"
 - "tin.py"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
 - "bed_bigwig_profile.py"
 - "bed_build_windows.py"
 - "bed_complement.py"
 - "bed_count_by_interval.py"
versions:
 - "0.6.3--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for tin-score-calculation"
config: {"url": "https://biocontainers.pro/tools/tin-score-calculation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tin-score-calculation", "latest": {"0.6.3--pyh5e36f6f_0": "sha256:fd3473790607c10792b8ca45185a67a0fb1754260ae0dbfe0b8dd759b9f564f6"}, "tags": {"0.6.3--pyh5e36f6f_0": "sha256:fd3473790607c10792b8ca45185a67a0fb1754260ae0dbfe0b8dd759b9f564f6"}, "docker": "quay.io/biocontainers/tin-score-calculation", "aliases": {"FPKM-UQ.py": "/usr/local/bin/FPKM-UQ.py", "FPKM_count.py": "/usr/local/bin/FPKM_count.py", "RNA_fragment_size.py": "/usr/local/bin/RNA_fragment_size.py", "RPKM_saturation.py": "/usr/local/bin/RPKM_saturation.py", "bam2fq.py": "/usr/local/bin/bam2fq.py", "bam2wig.py": "/usr/local/bin/bam2wig.py", "bam_stat.py": "/usr/local/bin/bam_stat.py", "calculate-tin.py": "/usr/local/bin/calculate-tin.py", "clipping_profile.py": "/usr/local/bin/clipping_profile.py", "deletion_profile.py": "/usr/local/bin/deletion_profile.py", "divide_bam.py": "/usr/local/bin/divide_bam.py", "geneBody_coverage.py": "/usr/local/bin/geneBody_coverage.py", "geneBody_coverage2.py": "/usr/local/bin/geneBody_coverage2.py", "infer_experiment.py": "/usr/local/bin/infer_experiment.py", "inner_distance.py": "/usr/local/bin/inner_distance.py", "insertion_profile.py": "/usr/local/bin/insertion_profile.py", "junction_annotation.py": "/usr/local/bin/junction_annotation.py", "junction_saturation.py": "/usr/local/bin/junction_saturation.py", "merge-tin.py": "/usr/local/bin/merge-tin.py", "mismatch_profile.py": "/usr/local/bin/mismatch_profile.py", "normalize_bigwig.py": "/usr/local/bin/normalize_bigwig.py", "overlay_bigwig.py": "/usr/local/bin/overlay_bigwig.py", "plot-tin.py": "/usr/local/bin/plot-tin.py", "read_GC.py": "/usr/local/bin/read_GC.py", "read_NVC.py": "/usr/local/bin/read_NVC.py", "read_distribution.py": "/usr/local/bin/read_distribution.py", "read_duplication.py": "/usr/local/bin/read_duplication.py", "read_hexamer.py": "/usr/local/bin/read_hexamer.py", "read_quality.py": "/usr/local/bin/read_quality.py", "split_bam.py": "/usr/local/bin/split_bam.py", "split_paired_bam.py": "/usr/local/bin/split_paired_bam.py", "summarize-tin.py": "/usr/local/bin/summarize-tin.py", "tin.py": "/usr/local/bin/tin.py", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py", "bed_count_by_interval.py": "/usr/local/bin/bed_count_by_interval.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tin-score-calculation.
shpc-registry automated BioContainers addition for tin-score-calculation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tin-score-calculation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tin-score-calculation:0.6.3--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tin-score-calculation/0.6.3--pyh5e36f6f_0
$ module help quay.io/biocontainers/tin-score-calculation/0.6.3--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tin-score-calculation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tin-score-calculation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tin-score-calculation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tin-score-calculation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tin-score-calculation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tin-score-calculation-inspect-deffile:

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


#### calculate-tin.py

```bash
$ singularity exec <container> /usr/local/bin/calculate-tin.py
$ podman run --it --rm --entrypoint /usr/local/bin/calculate-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### merge-tin.py

```bash
$ singularity exec <container> /usr/local/bin/merge-tin.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### plot-tin.py

```bash
$ singularity exec <container> /usr/local/bin/plot-tin.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### summarize-tin.py

```bash
$ singularity exec <container> /usr/local/bin/summarize-tin.py
$ podman run --it --rm --entrypoint /usr/local/bin/summarize-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize-tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tin.py

```bash
$ singularity exec <container> /usr/local/bin/tin.py
$ podman run --it --rm --entrypoint /usr/local/bin/tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bed_count_by_interval.py

```bash
$ singularity exec <container> /usr/local/bin/bed_count_by_interval.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_count_by_interval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_count_by_interval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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