---
layout: container
name:  "quay.io/biocontainers/fasten"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fasten/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fasten/container.yaml"
updated_at: "2023-01-13 03:02:12.580724"
latest: "0.4.4--hec16e2b_1"
container_url: "https://biocontainers.pro/tools/fasten"
aliases:
 - "fasten_clean"
 - "fasten_combine"
 - "fasten_convert"
 - "fasten_kmer"
 - "fasten_metrics"
 - "fasten_mutate"
 - "fasten_pe"
 - "fasten_progress"
 - "fasten_quality_filter"
 - "fasten_randomize"
 - "fasten_regex"
 - "fasten_replace"
 - "fasten_sample"
 - "fasten_shuffle"
 - "fasten_sort"
 - "fasten_straighten"
 - "fasten_trim"
 - "fasten_validate"
versions:
 - "0.4.4--hec16e2b_1"
description: "shpc-registry automated BioContainers addition for fasten"
config: {"url": "https://biocontainers.pro/tools/fasten", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fasten", "latest": {"0.4.4--hec16e2b_1": "sha256:f820c7e2b4920d186e69eab5b2a2bb79c7b5e2b1d8383cfd9cef81fc22baf4b8"}, "tags": {"0.4.4--hec16e2b_1": "sha256:f820c7e2b4920d186e69eab5b2a2bb79c7b5e2b1d8383cfd9cef81fc22baf4b8"}, "docker": "quay.io/biocontainers/fasten", "aliases": {"fasten_clean": "/usr/local/bin/fasten_clean", "fasten_combine": "/usr/local/bin/fasten_combine", "fasten_convert": "/usr/local/bin/fasten_convert", "fasten_kmer": "/usr/local/bin/fasten_kmer", "fasten_metrics": "/usr/local/bin/fasten_metrics", "fasten_mutate": "/usr/local/bin/fasten_mutate", "fasten_pe": "/usr/local/bin/fasten_pe", "fasten_progress": "/usr/local/bin/fasten_progress", "fasten_quality_filter": "/usr/local/bin/fasten_quality_filter", "fasten_randomize": "/usr/local/bin/fasten_randomize", "fasten_regex": "/usr/local/bin/fasten_regex", "fasten_replace": "/usr/local/bin/fasten_replace", "fasten_sample": "/usr/local/bin/fasten_sample", "fasten_shuffle": "/usr/local/bin/fasten_shuffle", "fasten_sort": "/usr/local/bin/fasten_sort", "fasten_straighten": "/usr/local/bin/fasten_straighten", "fasten_trim": "/usr/local/bin/fasten_trim", "fasten_validate": "/usr/local/bin/fasten_validate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fasten.
shpc-registry automated BioContainers addition for fasten
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fasten
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fasten:0.4.4--hec16e2b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fasten/0.4.4--hec16e2b_1
$ module help quay.io/biocontainers/fasten/0.4.4--hec16e2b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fasten-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fasten-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fasten-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fasten-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fasten-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fasten-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasten_clean

```bash
$ singularity exec <container> /usr/local/bin/fasten_clean
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_combine

```bash
$ singularity exec <container> /usr/local/bin/fasten_combine
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_convert

```bash
$ singularity exec <container> /usr/local/bin/fasten_convert
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_kmer

```bash
$ singularity exec <container> /usr/local/bin/fasten_kmer
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_kmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_kmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_metrics

```bash
$ singularity exec <container> /usr/local/bin/fasten_metrics
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_metrics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_metrics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_mutate

```bash
$ singularity exec <container> /usr/local/bin/fasten_mutate
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_pe

```bash
$ singularity exec <container> /usr/local/bin/fasten_pe
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_pe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_pe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_progress

```bash
$ singularity exec <container> /usr/local/bin/fasten_progress
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_progress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_progress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_quality_filter

```bash
$ singularity exec <container> /usr/local/bin/fasten_quality_filter
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_quality_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_quality_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_randomize

```bash
$ singularity exec <container> /usr/local/bin/fasten_randomize
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_randomize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_randomize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_regex

```bash
$ singularity exec <container> /usr/local/bin/fasten_regex
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_regex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_regex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_replace

```bash
$ singularity exec <container> /usr/local/bin/fasten_replace
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_replace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_replace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_sample

```bash
$ singularity exec <container> /usr/local/bin/fasten_sample
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_shuffle

```bash
$ singularity exec <container> /usr/local/bin/fasten_shuffle
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_sort

```bash
$ singularity exec <container> /usr/local/bin/fasten_sort
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_straighten

```bash
$ singularity exec <container> /usr/local/bin/fasten_straighten
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_straighten   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_straighten   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_trim

```bash
$ singularity exec <container> /usr/local/bin/fasten_trim
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasten_validate

```bash
$ singularity exec <container> /usr/local/bin/fasten_validate
$ podman run --it --rm --entrypoint /usr/local/bin/fasten_validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasten_validate   -v ${PWD} -w ${PWD} <container> -c " $@"
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