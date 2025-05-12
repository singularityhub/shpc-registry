---
layout: container
name:  "quay.io/biocontainers/emblmygff3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/emblmygff3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/emblmygff3/container.yaml"
updated_at: "2025-05-12 03:31:32.935743"
latest: "2.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/emblmygff3"
aliases:
 - "EMBLmyGFF3"
 - "EMBLmyGFF3-augustus-example"
 - "EMBLmyGFF3-maker-example"
 - "EMBLmyGFF3-prokka-example"
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
 - "2.1--py_0"
 - "2--py_1"
 - "2.2--pyhdfd78af_1"
 - "2.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for emblmygff3"
config: {"url": "https://biocontainers.pro/tools/emblmygff3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for emblmygff3", "latest": {"2.3--pyhdfd78af_0": "sha256:aa44953a8b546bcbc8a5cb9c34750a74f386a75f4c5de5bde47f4855afac312d"}, "tags": {"2.1--py_0": "sha256:f464ed6a5a58d5ac4ed4904b72be10da0e1d1b3c79050e7da37769a1736e7020", "2--py_1": "sha256:e7af473b044cdb424a4df52d9eb1ffa90e95dd9a63b3af51f904617fa0827b87", "2.2--pyhdfd78af_1": "sha256:1944dc1f926281cd2368e406c3c8a46a34ebaddcaf3ea2e58b921a4af5481fc0", "2.3--pyhdfd78af_0": "sha256:aa44953a8b546bcbc8a5cb9c34750a74f386a75f4c5de5bde47f4855afac312d"}, "docker": "quay.io/biocontainers/emblmygff3", "aliases": {"EMBLmyGFF3": "/usr/local/bin/EMBLmyGFF3", "EMBLmyGFF3-augustus-example": "/usr/local/bin/EMBLmyGFF3-augustus-example", "EMBLmyGFF3-maker-example": "/usr/local/bin/EMBLmyGFF3-maker-example", "EMBLmyGFF3-prokka-example": "/usr/local/bin/EMBLmyGFF3-prokka-example", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py", "bed_count_by_interval.py": "/usr/local/bin/bed_count_by_interval.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/emblmygff3.
shpc-registry automated BioContainers addition for emblmygff3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/emblmygff3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/emblmygff3:2.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/emblmygff3/2.3--pyhdfd78af_0
$ module help quay.io/biocontainers/emblmygff3/2.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### emblmygff3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### emblmygff3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### emblmygff3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### emblmygff3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### emblmygff3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### emblmygff3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EMBLmyGFF3

```bash
$ singularity exec <container> /usr/local/bin/EMBLmyGFF3
$ podman run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EMBLmyGFF3-augustus-example

```bash
$ singularity exec <container> /usr/local/bin/EMBLmyGFF3-augustus-example
$ podman run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3-augustus-example   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3-augustus-example   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EMBLmyGFF3-maker-example

```bash
$ singularity exec <container> /usr/local/bin/EMBLmyGFF3-maker-example
$ podman run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3-maker-example   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3-maker-example   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EMBLmyGFF3-prokka-example

```bash
$ singularity exec <container> /usr/local/bin/EMBLmyGFF3-prokka-example
$ podman run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3-prokka-example   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EMBLmyGFF3-prokka-example   -v ${PWD} -w ${PWD} <container> -c " $@"
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