---
layout: container
name:  "quay.io/biocontainers/perl-bioperl-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bioperl-core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bioperl-core/container.yaml"
updated_at: "2024-08-02 02:44:50.635718"
latest: "1.007002--pl5321hdfd78af_4"
container_url: "https://biocontainers.pro/tools/perl-bioperl-core"
aliases:
 - "bp_aacomp"
 - "bp_bioflat_index"
 - "bp_biogetseq"
 - "bp_dbsplit"
 - "bp_extract_feature_seq"
 - "bp_fastam9_to_table"
 - "bp_fetch"
 - "bp_filter_search"
 - "bp_find-blast-matches"
 - "bp_gccalc"
versions:
 - "1.7.8--pl5321hdfd78af_1"
 - "1.007002--pl5321hdfd78af_4"
description: "shpc-registry automated BioContainers addition for perl-bioperl-core"
config: {"url": "https://biocontainers.pro/tools/perl-bioperl-core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bioperl-core", "latest": {"1.007002--pl5321hdfd78af_4": "sha256:f61797093debaceca5a8f356ae0fd3065f247d943d7c154ac5db829615d8267f"}, "tags": {"1.7.8--pl5321hdfd78af_1": "sha256:44b47ade77cae2b11f555d921483841143880d0cb03f8d3714e666ee859082b9", "1.007002--pl5321hdfd78af_4": "sha256:f61797093debaceca5a8f356ae0fd3065f247d943d7c154ac5db829615d8267f"}, "docker": "quay.io/biocontainers/perl-bioperl-core", "aliases": {"bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search", "bp_find-blast-matches": "/usr/local/bin/bp_find-blast-matches", "bp_gccalc": "/usr/local/bin/bp_gccalc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bioperl-core.
shpc-registry automated BioContainers addition for perl-bioperl-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bioperl-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bioperl-core:1.007002--pl5321hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bioperl-core/1.007002--pl5321hdfd78af_4
$ module help quay.io/biocontainers/perl-bioperl-core/1.007002--pl5321hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bioperl-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bioperl-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bioperl-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bioperl-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bioperl-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bioperl-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bp_aacomp

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_dbsplit

```bash
$ singularity exec <container> /usr/local/bin/bp_dbsplit
$ podman run --it --rm --entrypoint /usr/local/bin/bp_dbsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_dbsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_extract_feature_seq

```bash
$ singularity exec <container> /usr/local/bin/bp_extract_feature_seq
$ podman run --it --rm --entrypoint /usr/local/bin/bp_extract_feature_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_extract_feature_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_fastam9_to_table

```bash
$ singularity exec <container> /usr/local/bin/bp_fastam9_to_table
$ podman run --it --rm --entrypoint /usr/local/bin/bp_fastam9_to_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_fastam9_to_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_fetch

```bash
$ singularity exec <container> /usr/local/bin/bp_fetch
$ podman run --it --rm --entrypoint /usr/local/bin/bp_fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_filter_search

```bash
$ singularity exec <container> /usr/local/bin/bp_filter_search
$ podman run --it --rm --entrypoint /usr/local/bin/bp_filter_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_filter_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_gccalc

```bash
$ singularity exec <container> /usr/local/bin/bp_gccalc
$ podman run --it --rm --entrypoint /usr/local/bin/bp_gccalc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_gccalc   -v ${PWD} -w ${PWD} <container> -c " $@"
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