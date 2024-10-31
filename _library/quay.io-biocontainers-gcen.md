---
layout: container
name:  "quay.io/biocontainers/gcen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gcen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gcen/container.yaml"
updated_at: "2024-10-31 03:51:38.809859"
latest: "0.6.3--h9f5acd7_2"
container_url: "https://biocontainers.pro/tools/gcen"
aliases:
 - "calculate_accuracy"
 - "csv_to_tsv"
 - "data_filter"
 - "data_norm"
 - "data_stat"
 - "enrich"
 - "generate_expr_matrix_from_rsem"
 - "generate_expr_matrix_from_stringtie"
 - "module_identify"
 - "network_build"
 - "network_extract"
 - "network_merge"
 - "network_shuffle"
 - "network_stat"
 - "rwr"
 - "tsv_to_csv"
 - "annotate"
versions:
 - "0.6.3--h9f5acd7_0"
 - "0.6.3--h9f5acd7_2"
description: "shpc-registry automated BioContainers addition for gcen"
config: {"url": "https://biocontainers.pro/tools/gcen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gcen", "latest": {"0.6.3--h9f5acd7_2": "sha256:4b66c90b6d6e32c76fe78910a12022920783e4b096afc1434511f91f28c5cf17"}, "tags": {"0.6.3--h9f5acd7_0": "sha256:d8e0e085dbb0f2570b06a487f583fe402d603db541f22651e7915e1a6a5bae95", "0.6.3--h9f5acd7_2": "sha256:4b66c90b6d6e32c76fe78910a12022920783e4b096afc1434511f91f28c5cf17"}, "docker": "quay.io/biocontainers/gcen", "aliases": {"calculate_accuracy": "/usr/local/bin/calculate_accuracy", "csv_to_tsv": "/usr/local/bin/csv_to_tsv", "data_filter": "/usr/local/bin/data_filter", "data_norm": "/usr/local/bin/data_norm", "data_stat": "/usr/local/bin/data_stat", "enrich": "/usr/local/bin/enrich", "generate_expr_matrix_from_rsem": "/usr/local/bin/generate_expr_matrix_from_rsem", "generate_expr_matrix_from_stringtie": "/usr/local/bin/generate_expr_matrix_from_stringtie", "module_identify": "/usr/local/bin/module_identify", "network_build": "/usr/local/bin/network_build", "network_extract": "/usr/local/bin/network_extract", "network_merge": "/usr/local/bin/network_merge", "network_shuffle": "/usr/local/bin/network_shuffle", "network_stat": "/usr/local/bin/network_stat", "rwr": "/usr/local/bin/rwr", "tsv_to_csv": "/usr/local/bin/tsv_to_csv", "annotate": "/usr/local/bin/annotate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gcen.
shpc-registry automated BioContainers addition for gcen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gcen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gcen:0.6.3--h9f5acd7_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gcen/0.6.3--h9f5acd7_2
$ module help quay.io/biocontainers/gcen/0.6.3--h9f5acd7_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gcen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gcen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gcen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gcen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gcen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gcen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### calculate_accuracy

```bash
$ singularity exec <container> /usr/local/bin/calculate_accuracy
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_accuracy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_accuracy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv_to_tsv

```bash
$ singularity exec <container> /usr/local/bin/csv_to_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/csv_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### data_filter

```bash
$ singularity exec <container> /usr/local/bin/data_filter
$ podman run --it --rm --entrypoint /usr/local/bin/data_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/data_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### data_norm

```bash
$ singularity exec <container> /usr/local/bin/data_norm
$ podman run --it --rm --entrypoint /usr/local/bin/data_norm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/data_norm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### data_stat

```bash
$ singularity exec <container> /usr/local/bin/data_stat
$ podman run --it --rm --entrypoint /usr/local/bin/data_stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/data_stat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enrich

```bash
$ singularity exec <container> /usr/local/bin/enrich
$ podman run --it --rm --entrypoint /usr/local/bin/enrich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enrich   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_expr_matrix_from_rsem

```bash
$ singularity exec <container> /usr/local/bin/generate_expr_matrix_from_rsem
$ podman run --it --rm --entrypoint /usr/local/bin/generate_expr_matrix_from_rsem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_expr_matrix_from_rsem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_expr_matrix_from_stringtie

```bash
$ singularity exec <container> /usr/local/bin/generate_expr_matrix_from_stringtie
$ podman run --it --rm --entrypoint /usr/local/bin/generate_expr_matrix_from_stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_expr_matrix_from_stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### module_identify

```bash
$ singularity exec <container> /usr/local/bin/module_identify
$ podman run --it --rm --entrypoint /usr/local/bin/module_identify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/module_identify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### network_build

```bash
$ singularity exec <container> /usr/local/bin/network_build
$ podman run --it --rm --entrypoint /usr/local/bin/network_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/network_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### network_extract

```bash
$ singularity exec <container> /usr/local/bin/network_extract
$ podman run --it --rm --entrypoint /usr/local/bin/network_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/network_extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### network_merge

```bash
$ singularity exec <container> /usr/local/bin/network_merge
$ podman run --it --rm --entrypoint /usr/local/bin/network_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/network_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### network_shuffle

```bash
$ singularity exec <container> /usr/local/bin/network_shuffle
$ podman run --it --rm --entrypoint /usr/local/bin/network_shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/network_shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### network_stat

```bash
$ singularity exec <container> /usr/local/bin/network_stat
$ podman run --it --rm --entrypoint /usr/local/bin/network_stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/network_stat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rwr

```bash
$ singularity exec <container> /usr/local/bin/rwr
$ podman run --it --rm --entrypoint /usr/local/bin/rwr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rwr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv_to_csv

```bash
$ singularity exec <container> /usr/local/bin/tsv_to_csv
$ podman run --it --rm --entrypoint /usr/local/bin/tsv_to_csv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv_to_csv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
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