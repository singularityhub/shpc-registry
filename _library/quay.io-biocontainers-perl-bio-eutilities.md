---
layout: container
name:  "quay.io/biocontainers/perl-bio-eutilities"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-eutilities/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-eutilities/container.yaml"
updated_at: "2025-11-22 03:44:14.053768"
latest: "1.77--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-bio-eutilities"
aliases:
 - "bp_einfo"
 - "bp_genbank_ref_extractor"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "bp_aacomp"
 - "bp_bioflat_index"
 - "bp_biogetseq"
 - "bp_dbsplit"
 - "bp_extract_feature_seq"
 - "bp_fastam9_to_table"
 - "bp_fetch"
 - "bp_filter_search"
versions:
 - "1.77--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-bio-eutilities"
config: {"url": "https://biocontainers.pro/tools/perl-bio-eutilities", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-eutilities", "latest": {"1.77--pl5321hdfd78af_0": "sha256:4b53f846adff2da3234a8e4764a441fe6d64d8be0e79f1f0886e1be86157517a"}, "tags": {"1.77--pl5321hdfd78af_0": "sha256:4b53f846adff2da3234a8e4764a441fe6d64d8be0e79f1f0886e1be86157517a"}, "docker": "quay.io/biocontainers/perl-bio-eutilities", "aliases": {"bp_einfo": "/usr/local/bin/bp_einfo", "bp_genbank_ref_extractor": "/usr/local/bin/bp_genbank_ref_extractor", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-eutilities.
shpc-registry automated BioContainers addition for perl-bio-eutilities
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-eutilities
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-eutilities:1.77--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-eutilities/1.77--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-bio-eutilities/1.77--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-eutilities-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-eutilities-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-eutilities-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-eutilities-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-eutilities-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-eutilities-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bp_einfo

```bash
$ singularity exec <container> /usr/local/bin/bp_einfo
$ podman run --it --rm --entrypoint /usr/local/bin/bp_einfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_einfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_genbank_ref_extractor

```bash
$ singularity exec <container> /usr/local/bin/bp_genbank_ref_extractor
$ podman run --it --rm --entrypoint /usr/local/bin/bp_genbank_ref_extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_genbank_ref_extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2BSML.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_search2BSML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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