---
layout: container
name:  "quay.io/biocontainers/mashtree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mashtree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mashtree/container.yaml"
updated_at: "2023-11-27 03:04:16.187633"
latest: "1.4.6--pl5321h031d066_0"
container_url: "https://biocontainers.pro/tools/mashtree"
aliases:
 - "mashtree"
 - "mashtree_bootstrap.pl"
 - "mashtree_cluster.pl"
 - "mashtree_init.pl"
 - "mashtree_jackknife.pl"
 - "mashtree_wrapper_deprecated.pl"
 - "min_abundance_finder.pl"
 - "quicktree"
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
 - "1.2.0--pl5321hec16e2b_1"
 - "1.2.0--pl5321h031d066_2"
 - "1.4.5--pl5321h031d066_0"
 - "1.4.6--pl5321h031d066_0"
description: "shpc-registry automated BioContainers addition for mashtree"
config: {"url": "https://biocontainers.pro/tools/mashtree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mashtree", "latest": {"1.4.6--pl5321h031d066_0": "sha256:590a0e41bb56cba0205391ff4c1c9747921dcc5754309f754c4e1e7ed2ec5316"}, "tags": {"1.2.0--pl5321hec16e2b_1": "sha256:7c2a10ebdf36ae6c1b97fd320b64ab27b11415499d2737e83cc21b4061f448ab", "1.2.0--pl5321h031d066_2": "sha256:955826c1f60bff0f26361a5e91947bdab3689e017f77978bc023c7dc690d46c5", "1.4.5--pl5321h031d066_0": "sha256:aac6b53551782aca24a19792c923b0445e860b344e9a8d294c6754825e3d8664", "1.4.6--pl5321h031d066_0": "sha256:590a0e41bb56cba0205391ff4c1c9747921dcc5754309f754c4e1e7ed2ec5316"}, "docker": "quay.io/biocontainers/mashtree", "aliases": {"mashtree": "/usr/local/bin/mashtree", "mashtree_bootstrap.pl": "/usr/local/bin/mashtree_bootstrap.pl", "mashtree_cluster.pl": "/usr/local/bin/mashtree_cluster.pl", "mashtree_init.pl": "/usr/local/bin/mashtree_init.pl", "mashtree_jackknife.pl": "/usr/local/bin/mashtree_jackknife.pl", "mashtree_wrapper_deprecated.pl": "/usr/local/bin/mashtree_wrapper_deprecated.pl", "min_abundance_finder.pl": "/usr/local/bin/min_abundance_finder.pl", "quicktree": "/usr/local/bin/quicktree", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search", "bp_find-blast-matches": "/usr/local/bin/bp_find-blast-matches", "bp_gccalc": "/usr/local/bin/bp_gccalc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mashtree.
shpc-registry automated BioContainers addition for mashtree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mashtree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mashtree:1.4.6--pl5321h031d066_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mashtree/1.4.6--pl5321h031d066_0
$ module help quay.io/biocontainers/mashtree/1.4.6--pl5321h031d066_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mashtree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mashtree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mashtree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mashtree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mashtree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mashtree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mashtree

```bash
$ singularity exec <container> /usr/local/bin/mashtree
$ podman run --it --rm --entrypoint /usr/local/bin/mashtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mashtree_bootstrap.pl

```bash
$ singularity exec <container> /usr/local/bin/mashtree_bootstrap.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mashtree_bootstrap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashtree_bootstrap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mashtree_cluster.pl

```bash
$ singularity exec <container> /usr/local/bin/mashtree_cluster.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mashtree_cluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashtree_cluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mashtree_init.pl

```bash
$ singularity exec <container> /usr/local/bin/mashtree_init.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mashtree_init.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashtree_init.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mashtree_jackknife.pl

```bash
$ singularity exec <container> /usr/local/bin/mashtree_jackknife.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mashtree_jackknife.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashtree_jackknife.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mashtree_wrapper_deprecated.pl

```bash
$ singularity exec <container> /usr/local/bin/mashtree_wrapper_deprecated.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mashtree_wrapper_deprecated.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mashtree_wrapper_deprecated.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### min_abundance_finder.pl

```bash
$ singularity exec <container> /usr/local/bin/min_abundance_finder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/min_abundance_finder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/min_abundance_finder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quicktree

```bash
$ singularity exec <container> /usr/local/bin/quicktree
$ podman run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
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