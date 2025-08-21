---
layout: container
name:  "quay.io/biocontainers/gff3toddbj"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gff3toddbj/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gff3toddbj/container.yaml"
updated_at: "2025-08-21 06:44:29.124123"
latest: "0.4.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/gff3toddbj"
aliases:
 - "compare-ddbj"
 - "genbank-to-ddbj"
 - "gff3-to-ddbj"
 - "list-products"
 - "normalize-entry-names"
 - "split-fasta"
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
 - "0.4.0--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for gff3toddbj"
config: {"url": "https://biocontainers.pro/tools/gff3toddbj", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gff3toddbj", "latest": {"0.4.0--pyh5e36f6f_0": "sha256:d8b0ebd5392bfd00f5cf42f7ebfc56c56cba0fdff9a4e964769f3767228c42b8"}, "tags": {"0.4.0--pyh5e36f6f_0": "sha256:d8b0ebd5392bfd00f5cf42f7ebfc56c56cba0fdff9a4e964769f3767228c42b8"}, "docker": "quay.io/biocontainers/gff3toddbj", "aliases": {"compare-ddbj": "/usr/local/bin/compare-ddbj", "genbank-to-ddbj": "/usr/local/bin/genbank-to-ddbj", "gff3-to-ddbj": "/usr/local/bin/gff3-to-ddbj", "list-products": "/usr/local/bin/list-products", "normalize-entry-names": "/usr/local/bin/normalize-entry-names", "split-fasta": "/usr/local/bin/split-fasta", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py", "bed_count_by_interval.py": "/usr/local/bin/bed_count_by_interval.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gff3toddbj.
shpc-registry automated BioContainers addition for gff3toddbj
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gff3toddbj
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gff3toddbj:0.4.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gff3toddbj/0.4.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/gff3toddbj/0.4.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gff3toddbj-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gff3toddbj-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gff3toddbj-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gff3toddbj-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gff3toddbj-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gff3toddbj-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compare-ddbj

```bash
$ singularity exec <container> /usr/local/bin/compare-ddbj
$ podman run --it --rm --entrypoint /usr/local/bin/compare-ddbj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-ddbj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbank-to-ddbj

```bash
$ singularity exec <container> /usr/local/bin/genbank-to-ddbj
$ podman run --it --rm --entrypoint /usr/local/bin/genbank-to-ddbj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbank-to-ddbj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3-to-ddbj

```bash
$ singularity exec <container> /usr/local/bin/gff3-to-ddbj
$ podman run --it --rm --entrypoint /usr/local/bin/gff3-to-ddbj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3-to-ddbj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list-products

```bash
$ singularity exec <container> /usr/local/bin/list-products
$ podman run --it --rm --entrypoint /usr/local/bin/list-products   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list-products   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize-entry-names

```bash
$ singularity exec <container> /usr/local/bin/normalize-entry-names
$ podman run --it --rm --entrypoint /usr/local/bin/normalize-entry-names   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize-entry-names   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-fasta

```bash
$ singularity exec <container> /usr/local/bin/split-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/split-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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