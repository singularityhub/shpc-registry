---
layout: container
name:  "quay.io/biocontainers/nasp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nasp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nasp/container.yaml"
updated_at: "2022-11-02 00:24:15.966164"
latest: "1.2.1--py36hf8e0771_1"
container_url: "https://biocontainers.pro/tools/nasp"
aliases:
 - "convert_external_genome"
 - "filter_matrix_by_coord.py"
 - "filter_matrix_by_distance.py"
 - "filter_matrix_by_genome.py"
 - "find_duplicates"
 - "format_fasta"
 - "matrix_to_fasta.py"
 - "merge_matrices.py"
 - "nasp"
 - "report_single_snps_single_isolate.py"
 - "varfilter.py"
 - "vcf_to_matrix"
 - "trimmomatic"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
versions:
 - "1.2.1--py36hf8e0771_1"
description: "shpc-registry automated BioContainers addition for nasp"
config: {"url": "https://biocontainers.pro/tools/nasp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nasp", "latest": {"1.2.1--py36hf8e0771_1": "sha256:cf8efe7ed51afd7fbdb14e1a250f5afa59a020c68aa0a6e4716c66f199440871"}, "tags": {"1.2.1--py36hf8e0771_1": "sha256:cf8efe7ed51afd7fbdb14e1a250f5afa59a020c68aa0a6e4716c66f199440871"}, "docker": "quay.io/biocontainers/nasp", "aliases": {"convert_external_genome": "/usr/local/bin/convert_external_genome", "filter_matrix_by_coord.py": "/usr/local/bin/filter_matrix_by_coord.py", "filter_matrix_by_distance.py": "/usr/local/bin/filter_matrix_by_distance.py", "filter_matrix_by_genome.py": "/usr/local/bin/filter_matrix_by_genome.py", "find_duplicates": "/usr/local/bin/find_duplicates", "format_fasta": "/usr/local/bin/format_fasta", "matrix_to_fasta.py": "/usr/local/bin/matrix_to_fasta.py", "merge_matrices.py": "/usr/local/bin/merge_matrices.py", "nasp": "/usr/local/bin/nasp", "report_single_snps_single_isolate.py": "/usr/local/bin/report_single_snps_single_isolate.py", "varfilter.py": "/usr/local/bin/varfilter.py", "vcf_to_matrix": "/usr/local/bin/vcf_to_matrix", "trimmomatic": "/usr/local/bin/trimmomatic", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nasp.
shpc-registry automated BioContainers addition for nasp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nasp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nasp:1.2.1--py36hf8e0771_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nasp/1.2.1--py36hf8e0771_1
$ module help quay.io/biocontainers/nasp/1.2.1--py36hf8e0771_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nasp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nasp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nasp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nasp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nasp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nasp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convert_external_genome

```bash
$ singularity exec <container> /usr/local/bin/convert_external_genome
$ podman run --it --rm --entrypoint /usr/local/bin/convert_external_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_external_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_matrix_by_coord.py

```bash
$ singularity exec <container> /usr/local/bin/filter_matrix_by_coord.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_matrix_by_coord.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_matrix_by_coord.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_matrix_by_distance.py

```bash
$ singularity exec <container> /usr/local/bin/filter_matrix_by_distance.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_matrix_by_distance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_matrix_by_distance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_matrix_by_genome.py

```bash
$ singularity exec <container> /usr/local/bin/filter_matrix_by_genome.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_matrix_by_genome.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_matrix_by_genome.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_duplicates

```bash
$ singularity exec <container> /usr/local/bin/find_duplicates
$ podman run --it --rm --entrypoint /usr/local/bin/find_duplicates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_duplicates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### format_fasta

```bash
$ singularity exec <container> /usr/local/bin/format_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/format_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/format_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matrix_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/matrix_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/matrix_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matrix_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_matrices.py

```bash
$ singularity exec <container> /usr/local/bin/merge_matrices.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_matrices.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_matrices.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nasp

```bash
$ singularity exec <container> /usr/local/bin/nasp
$ podman run --it --rm --entrypoint /usr/local/bin/nasp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nasp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### report_single_snps_single_isolate.py

```bash
$ singularity exec <container> /usr/local/bin/report_single_snps_single_isolate.py
$ podman run --it --rm --entrypoint /usr/local/bin/report_single_snps_single_isolate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/report_single_snps_single_isolate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varfilter.py

```bash
$ singularity exec <container> /usr/local/bin/varfilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_to_matrix

```bash
$ singularity exec <container> /usr/local/bin/vcf_to_matrix
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_to_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_to_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
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