---
layout: container
name:  "quay.io/biocontainers/metamlst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metamlst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metamlst/container.yaml"
updated_at: "2025-10-20 03:37:22.138723"
latest: "1.2.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metamlst"
aliases:
 - "breadth_depth.py"
 - "consensus.py"
 - "consensus_aDNA.py"
 - "metaMLST-DBtools.py"
 - "metaMLST_functions.py"
 - "metamlst-index.py"
 - "metamlst-merge.py"
 - "metamlst.py"
 - "mlst.py"
 - "poly.py"
 - "polymut.py"
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
 - "bed_count_overlapping.py"
 - "bed_coverage.py"
 - "bed_coverage_by_interval.py"
 - "bed_diff_basewise_summary.py"
 - "bed_extend_to.py"
 - "bed_intersect.py"
 - "bed_intersect_basewise.py"
 - "bed_merge_overlapping.py"
 - "bed_rand_intersect.py"
 - "bed_subtract_basewise.py"
 - "bnMapper.py"
 - "div_snp_table_chr.py"
 - "find_in_sorted_file.py"
 - "gene_fourfold_sites.py"
 - "get_scores_in_intervals.py"
versions:
 - "1.2.3--hdfd78af_0"
description: "singularity registry hpc automated addition for metamlst"
config: {"url": "https://biocontainers.pro/tools/metamlst", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metamlst", "latest": {"1.2.3--hdfd78af_0": "sha256:53374077c743ef3b89824e2ab3be1cb4c97a56b94e002981cc5af540bb681c32"}, "tags": {"1.2.3--hdfd78af_0": "sha256:53374077c743ef3b89824e2ab3be1cb4c97a56b94e002981cc5af540bb681c32"}, "docker": "quay.io/biocontainers/metamlst", "aliases": {"breadth_depth.py": "/usr/local/bin/breadth_depth.py", "consensus.py": "/usr/local/bin/consensus.py", "consensus_aDNA.py": "/usr/local/bin/consensus_aDNA.py", "metaMLST-DBtools.py": "/usr/local/bin/metaMLST-DBtools.py", "metaMLST_functions.py": "/usr/local/bin/metaMLST_functions.py", "metamlst-index.py": "/usr/local/bin/metamlst-index.py", "metamlst-merge.py": "/usr/local/bin/metamlst-merge.py", "metamlst.py": "/usr/local/bin/metamlst.py", "mlst.py": "/usr/local/bin/mlst.py", "poly.py": "/usr/local/bin/poly.py", "polymut.py": "/usr/local/bin/polymut.py", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py", "bed_count_by_interval.py": "/usr/local/bin/bed_count_by_interval.py", "bed_count_overlapping.py": "/usr/local/bin/bed_count_overlapping.py", "bed_coverage.py": "/usr/local/bin/bed_coverage.py", "bed_coverage_by_interval.py": "/usr/local/bin/bed_coverage_by_interval.py", "bed_diff_basewise_summary.py": "/usr/local/bin/bed_diff_basewise_summary.py", "bed_extend_to.py": "/usr/local/bin/bed_extend_to.py", "bed_intersect.py": "/usr/local/bin/bed_intersect.py", "bed_intersect_basewise.py": "/usr/local/bin/bed_intersect_basewise.py", "bed_merge_overlapping.py": "/usr/local/bin/bed_merge_overlapping.py", "bed_rand_intersect.py": "/usr/local/bin/bed_rand_intersect.py", "bed_subtract_basewise.py": "/usr/local/bin/bed_subtract_basewise.py", "bnMapper.py": "/usr/local/bin/bnMapper.py", "div_snp_table_chr.py": "/usr/local/bin/div_snp_table_chr.py", "find_in_sorted_file.py": "/usr/local/bin/find_in_sorted_file.py", "gene_fourfold_sites.py": "/usr/local/bin/gene_fourfold_sites.py", "get_scores_in_intervals.py": "/usr/local/bin/get_scores_in_intervals.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metamlst.
singularity registry hpc automated addition for metamlst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metamlst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metamlst:1.2.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metamlst/1.2.3--hdfd78af_0
$ module help quay.io/biocontainers/metamlst/1.2.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metamlst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metamlst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metamlst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metamlst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metamlst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metamlst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### breadth_depth.py

```bash
$ singularity exec <container> /usr/local/bin/breadth_depth.py
$ podman run --it --rm --entrypoint /usr/local/bin/breadth_depth.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/breadth_depth.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus.py

```bash
$ singularity exec <container> /usr/local/bin/consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus_aDNA.py

```bash
$ singularity exec <container> /usr/local/bin/consensus_aDNA.py
$ podman run --it --rm --entrypoint /usr/local/bin/consensus_aDNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus_aDNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaMLST-DBtools.py

```bash
$ singularity exec <container> /usr/local/bin/metaMLST-DBtools.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaMLST-DBtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaMLST-DBtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaMLST_functions.py

```bash
$ singularity exec <container> /usr/local/bin/metaMLST_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaMLST_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaMLST_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metamlst-index.py

```bash
$ singularity exec <container> /usr/local/bin/metamlst-index.py
$ podman run --it --rm --entrypoint /usr/local/bin/metamlst-index.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metamlst-index.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metamlst-merge.py

```bash
$ singularity exec <container> /usr/local/bin/metamlst-merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/metamlst-merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metamlst-merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metamlst.py

```bash
$ singularity exec <container> /usr/local/bin/metamlst.py
$ podman run --it --rm --entrypoint /usr/local/bin/metamlst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metamlst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst.py

```bash
$ singularity exec <container> /usr/local/bin/mlst.py
$ podman run --it --rm --entrypoint /usr/local/bin/mlst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poly.py

```bash
$ singularity exec <container> /usr/local/bin/poly.py
$ podman run --it --rm --entrypoint /usr/local/bin/poly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### polymut.py

```bash
$ singularity exec <container> /usr/local/bin/polymut.py
$ podman run --it --rm --entrypoint /usr/local/bin/polymut.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polymut.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bed_count_overlapping.py

```bash
$ singularity exec <container> /usr/local/bin/bed_count_overlapping.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_count_overlapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_count_overlapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_coverage.py

```bash
$ singularity exec <container> /usr/local/bin/bed_coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_coverage_by_interval.py

```bash
$ singularity exec <container> /usr/local/bin/bed_coverage_by_interval.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_coverage_by_interval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_coverage_by_interval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_diff_basewise_summary.py

```bash
$ singularity exec <container> /usr/local/bin/bed_diff_basewise_summary.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_diff_basewise_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_diff_basewise_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_extend_to.py

```bash
$ singularity exec <container> /usr/local/bin/bed_extend_to.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_extend_to.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_extend_to.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_intersect.py

```bash
$ singularity exec <container> /usr/local/bin/bed_intersect.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_intersect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_intersect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_intersect_basewise.py

```bash
$ singularity exec <container> /usr/local/bin/bed_intersect_basewise.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_intersect_basewise.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_intersect_basewise.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_merge_overlapping.py

```bash
$ singularity exec <container> /usr/local/bin/bed_merge_overlapping.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_merge_overlapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_merge_overlapping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_rand_intersect.py

```bash
$ singularity exec <container> /usr/local/bin/bed_rand_intersect.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_rand_intersect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_rand_intersect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_subtract_basewise.py

```bash
$ singularity exec <container> /usr/local/bin/bed_subtract_basewise.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed_subtract_basewise.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_subtract_basewise.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bnMapper.py

```bash
$ singularity exec <container> /usr/local/bin/bnMapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/bnMapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bnMapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### div_snp_table_chr.py

```bash
$ singularity exec <container> /usr/local/bin/div_snp_table_chr.py
$ podman run --it --rm --entrypoint /usr/local/bin/div_snp_table_chr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/div_snp_table_chr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_in_sorted_file.py

```bash
$ singularity exec <container> /usr/local/bin/find_in_sorted_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_in_sorted_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_in_sorted_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_fourfold_sites.py

```bash
$ singularity exec <container> /usr/local/bin/gene_fourfold_sites.py
$ podman run --it --rm --entrypoint /usr/local/bin/gene_fourfold_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_fourfold_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/get_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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