---
layout: container
name:  "quay.io/biocontainers/smallgenomeutilities"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smallgenomeutilities/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smallgenomeutilities/container.yaml"
updated_at: "2023-10-24 02:26:32.716706"
latest: "0.3.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/smallgenomeutilities"
aliases:
 - "aln2basecnt"
 - "compute_mds"
 - "convert_qr"
 - "convert_reference"
 - "coverage_stats"
 - "extract_consensus"
 - "extract_coverage_intervals"
 - "extract_sam"
 - "extract_seq"
 - "frameshift_deletions_checks"
 - "gather_coverage"
 - "mapper"
 - "min_coverage"
 - "minority_freq"
 - "pair_sequences"
 - "predict_num_reads"
 - "pysamstats"
 - "remove_gaps_msa"
 - "coverage"
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
 - "0.3.8--pyhdfd78af_0"
 - "0.3.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for smallgenomeutilities"
config: {"url": "https://biocontainers.pro/tools/smallgenomeutilities", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smallgenomeutilities", "latest": {"0.3.9--pyhdfd78af_0": "sha256:d20d6a293a56894a83d467d55e0f8c319bae2013d89a98c24dce18b439915238"}, "tags": {"0.3.8--pyhdfd78af_0": "sha256:7b8704ad07a1c8115ceb8601485aac729a0db24b7e6d746e46823c46950b4e0e", "0.3.9--pyhdfd78af_0": "sha256:d20d6a293a56894a83d467d55e0f8c319bae2013d89a98c24dce18b439915238"}, "docker": "quay.io/biocontainers/smallgenomeutilities", "aliases": {"aln2basecnt": "/usr/local/bin/aln2basecnt", "compute_mds": "/usr/local/bin/compute_mds", "convert_qr": "/usr/local/bin/convert_qr", "convert_reference": "/usr/local/bin/convert_reference", "coverage_stats": "/usr/local/bin/coverage_stats", "extract_consensus": "/usr/local/bin/extract_consensus", "extract_coverage_intervals": "/usr/local/bin/extract_coverage_intervals", "extract_sam": "/usr/local/bin/extract_sam", "extract_seq": "/usr/local/bin/extract_seq", "frameshift_deletions_checks": "/usr/local/bin/frameshift_deletions_checks", "gather_coverage": "/usr/local/bin/gather_coverage", "mapper": "/usr/local/bin/mapper", "min_coverage": "/usr/local/bin/min_coverage", "minority_freq": "/usr/local/bin/minority_freq", "pair_sequences": "/usr/local/bin/pair_sequences", "predict_num_reads": "/usr/local/bin/predict_num_reads", "pysamstats": "/usr/local/bin/pysamstats", "remove_gaps_msa": "/usr/local/bin/remove_gaps_msa", "coverage": "/usr/local/bin/coverage", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smallgenomeutilities.
shpc-registry automated BioContainers addition for smallgenomeutilities
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smallgenomeutilities
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smallgenomeutilities:0.3.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smallgenomeutilities/0.3.9--pyhdfd78af_0
$ module help quay.io/biocontainers/smallgenomeutilities/0.3.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smallgenomeutilities-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smallgenomeutilities-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smallgenomeutilities-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smallgenomeutilities-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smallgenomeutilities-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smallgenomeutilities-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aln2basecnt

```bash
$ singularity exec <container> /usr/local/bin/aln2basecnt
$ podman run --it --rm --entrypoint /usr/local/bin/aln2basecnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aln2basecnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute_mds

```bash
$ singularity exec <container> /usr/local/bin/compute_mds
$ podman run --it --rm --entrypoint /usr/local/bin/compute_mds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute_mds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_qr

```bash
$ singularity exec <container> /usr/local/bin/convert_qr
$ podman run --it --rm --entrypoint /usr/local/bin/convert_qr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_qr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert_reference

```bash
$ singularity exec <container> /usr/local/bin/convert_reference
$ podman run --it --rm --entrypoint /usr/local/bin/convert_reference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_reference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_stats

```bash
$ singularity exec <container> /usr/local/bin/coverage_stats
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_consensus

```bash
$ singularity exec <container> /usr/local/bin/extract_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/extract_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_coverage_intervals

```bash
$ singularity exec <container> /usr/local/bin/extract_coverage_intervals
$ podman run --it --rm --entrypoint /usr/local/bin/extract_coverage_intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_coverage_intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_sam

```bash
$ singularity exec <container> /usr/local/bin/extract_sam
$ podman run --it --rm --entrypoint /usr/local/bin/extract_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_seq

```bash
$ singularity exec <container> /usr/local/bin/extract_seq
$ podman run --it --rm --entrypoint /usr/local/bin/extract_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### frameshift_deletions_checks

```bash
$ singularity exec <container> /usr/local/bin/frameshift_deletions_checks
$ podman run --it --rm --entrypoint /usr/local/bin/frameshift_deletions_checks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/frameshift_deletions_checks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gather_coverage

```bash
$ singularity exec <container> /usr/local/bin/gather_coverage
$ podman run --it --rm --entrypoint /usr/local/bin/gather_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gather_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapper

```bash
$ singularity exec <container> /usr/local/bin/mapper
$ podman run --it --rm --entrypoint /usr/local/bin/mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### min_coverage

```bash
$ singularity exec <container> /usr/local/bin/min_coverage
$ podman run --it --rm --entrypoint /usr/local/bin/min_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/min_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minority_freq

```bash
$ singularity exec <container> /usr/local/bin/minority_freq
$ podman run --it --rm --entrypoint /usr/local/bin/minority_freq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minority_freq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair_sequences

```bash
$ singularity exec <container> /usr/local/bin/pair_sequences
$ podman run --it --rm --entrypoint /usr/local/bin/pair_sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair_sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### predict_num_reads

```bash
$ singularity exec <container> /usr/local/bin/predict_num_reads
$ podman run --it --rm --entrypoint /usr/local/bin/predict_num_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predict_num_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysamstats

```bash
$ singularity exec <container> /usr/local/bin/pysamstats
$ podman run --it --rm --entrypoint /usr/local/bin/pysamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_gaps_msa

```bash
$ singularity exec <container> /usr/local/bin/remove_gaps_msa
$ podman run --it --rm --entrypoint /usr/local/bin/remove_gaps_msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_gaps_msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
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