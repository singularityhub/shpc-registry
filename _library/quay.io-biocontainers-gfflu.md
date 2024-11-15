---
layout: container
name:  "quay.io/biocontainers/gfflu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfflu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfflu/container.yaml"
updated_at: "2024-11-15 03:19:29.036537"
latest: "0.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gfflu"
aliases:
 - "blastn_vdb"
 - "gfflu"
 - "miniprot"
 - "tblastn_vdb"
 - "markdown-it"
 - "uuid"
 - "uuid-config"
 - "test_pcre"
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
versions:
 - "0.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for gfflu"
config: {"url": "https://biocontainers.pro/tools/gfflu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gfflu", "latest": {"0.0.2--pyhdfd78af_0": "sha256:61e7841ec57bbf2f0106410a5cd9a99efc504f52692593791f44f755fddc07b2"}, "tags": {"0.0.2--pyhdfd78af_0": "sha256:61e7841ec57bbf2f0106410a5cd9a99efc504f52692593791f44f755fddc07b2"}, "docker": "quay.io/biocontainers/gfflu", "aliases": {"blastn_vdb": "/usr/local/bin/blastn_vdb", "gfflu": "/usr/local/bin/gfflu", "miniprot": "/usr/local/bin/miniprot", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "markdown-it": "/usr/local/bin/markdown-it", "uuid": "/usr/local/bin/uuid", "uuid-config": "/usr/local/bin/uuid-config", "test_pcre": "/usr/local/bin/test_pcre", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py", "bed_count_by_interval.py": "/usr/local/bin/bed_count_by_interval.py", "bed_count_overlapping.py": "/usr/local/bin/bed_count_overlapping.py", "bed_coverage.py": "/usr/local/bin/bed_coverage.py", "bed_coverage_by_interval.py": "/usr/local/bin/bed_coverage_by_interval.py", "bed_diff_basewise_summary.py": "/usr/local/bin/bed_diff_basewise_summary.py", "bed_extend_to.py": "/usr/local/bin/bed_extend_to.py", "bed_intersect.py": "/usr/local/bin/bed_intersect.py", "bed_intersect_basewise.py": "/usr/local/bin/bed_intersect_basewise.py", "bed_merge_overlapping.py": "/usr/local/bin/bed_merge_overlapping.py", "bed_rand_intersect.py": "/usr/local/bin/bed_rand_intersect.py", "bed_subtract_basewise.py": "/usr/local/bin/bed_subtract_basewise.py", "bnMapper.py": "/usr/local/bin/bnMapper.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfflu.
singularity registry hpc automated addition for gfflu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfflu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfflu:0.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfflu/0.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/gfflu/0.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfflu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfflu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfflu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfflu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfflu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfflu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfflu

```bash
$ singularity exec <container> /usr/local/bin/gfflu
$ podman run --it --rm --entrypoint /usr/local/bin/gfflu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfflu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniprot

```bash
$ singularity exec <container> /usr/local/bin/miniprot
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid

```bash
$ singularity exec <container> /usr/local/bin/uuid
$ podman run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid-config

```bash
$ singularity exec <container> /usr/local/bin/uuid-config
$ podman run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
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