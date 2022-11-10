---
layout: container
name:  "quay.io/biocontainers/cistrome-ceas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cistrome-ceas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cistrome-ceas/container.yaml"
updated_at: "2022-11-10 00:22:20.081890"
latest: "1.0.2b1--py_2"
container_url: "https://biocontainers.pro/tools/cistrome-ceas"
aliases:
 - "ChIPAssoc"
 - "build_genomeBG"
 - "ceas"
 - "ceasBW"
 - "gca"
 - "sitepro"
 - "siteproBW"
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
 - "1.0.2b1--py_2"
description: "shpc-registry automated BioContainers addition for cistrome-ceas"
config: {"url": "https://biocontainers.pro/tools/cistrome-ceas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cistrome-ceas", "latest": {"1.0.2b1--py_2": "sha256:896e86d8944f61f0bc90a356bf0efda21ea08625a9de1bec7fa0d42e39e4a17e"}, "tags": {"1.0.2b1--py_2": "sha256:896e86d8944f61f0bc90a356bf0efda21ea08625a9de1bec7fa0d42e39e4a17e"}, "docker": "quay.io/biocontainers/cistrome-ceas", "aliases": {"ChIPAssoc": "/usr/local/bin/ChIPAssoc", "build_genomeBG": "/usr/local/bin/build_genomeBG", "ceas": "/usr/local/bin/ceas", "ceasBW": "/usr/local/bin/ceasBW", "gca": "/usr/local/bin/gca", "sitepro": "/usr/local/bin/sitepro", "siteproBW": "/usr/local/bin/siteproBW", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bed_bigwig_profile.py": "/usr/local/bin/bed_bigwig_profile.py", "bed_build_windows.py": "/usr/local/bin/bed_build_windows.py", "bed_complement.py": "/usr/local/bin/bed_complement.py", "bed_count_by_interval.py": "/usr/local/bin/bed_count_by_interval.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cistrome-ceas.
shpc-registry automated BioContainers addition for cistrome-ceas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cistrome-ceas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cistrome-ceas:1.0.2b1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cistrome-ceas/1.0.2b1--py_2
$ module help quay.io/biocontainers/cistrome-ceas/1.0.2b1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cistrome-ceas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cistrome-ceas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cistrome-ceas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cistrome-ceas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cistrome-ceas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cistrome-ceas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ChIPAssoc

```bash
$ singularity exec <container> /usr/local/bin/ChIPAssoc
$ podman run --it --rm --entrypoint /usr/local/bin/ChIPAssoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChIPAssoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_genomeBG

```bash
$ singularity exec <container> /usr/local/bin/build_genomeBG
$ podman run --it --rm --entrypoint /usr/local/bin/build_genomeBG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_genomeBG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ceas

```bash
$ singularity exec <container> /usr/local/bin/ceas
$ podman run --it --rm --entrypoint /usr/local/bin/ceas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ceas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ceasBW

```bash
$ singularity exec <container> /usr/local/bin/ceasBW
$ podman run --it --rm --entrypoint /usr/local/bin/ceasBW   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ceasBW   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gca

```bash
$ singularity exec <container> /usr/local/bin/gca
$ podman run --it --rm --entrypoint /usr/local/bin/gca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sitepro

```bash
$ singularity exec <container> /usr/local/bin/sitepro
$ podman run --it --rm --entrypoint /usr/local/bin/sitepro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sitepro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### siteproBW

```bash
$ singularity exec <container> /usr/local/bin/siteproBW
$ podman run --it --rm --entrypoint /usr/local/bin/siteproBW   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/siteproBW   -v ${PWD} -w ${PWD} <container> -c " $@"
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