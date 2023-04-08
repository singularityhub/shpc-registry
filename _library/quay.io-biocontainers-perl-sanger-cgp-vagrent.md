---
layout: container
name:  "quay.io/biocontainers/perl-sanger-cgp-vagrent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-sanger-cgp-vagrent/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-sanger-cgp-vagrent/container.yaml"
updated_at: "2023-04-08 02:45:49.504387"
latest: "3.7.0--pl5321hec16e2b_1"
container_url: "https://biocontainers.pro/tools/perl-sanger-cgp-vagrent"
aliases:
 - "Admin_CacheFileBuilder.pl"
 - "Admin_EnsemblReferenceFileGenerator.pl"
 - "Admin_EnsemblTranscriptFilter.pl"
 - "Admin_GeneRegionBedDumper.pl"
 - "AnnotateVcf.pl"
 - "addVagrentContext.pl"
 - "l4p-tmpl"
 - "bp_aacomp"
 - "bp_bioflat_index"
 - "bp_biogetseq"
 - "bp_dbsplit"
 - "bp_extract_feature_seq"
 - "bp_fastam9_to_table"
 - "bp_fetch"
 - "bp_filter_search"
 - "bp_find-blast-matches"
versions:
 - "3.7.0--pl5321hec16e2b_1"
description: "shpc-registry automated BioContainers addition for perl-sanger-cgp-vagrent"
config: {"url": "https://biocontainers.pro/tools/perl-sanger-cgp-vagrent", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-sanger-cgp-vagrent", "latest": {"3.7.0--pl5321hec16e2b_1": "sha256:21b665ffd2368e55f31813e904c17d6f23490bdb1524424d79f1c89e719bc207"}, "tags": {"3.7.0--pl5321hec16e2b_1": "sha256:21b665ffd2368e55f31813e904c17d6f23490bdb1524424d79f1c89e719bc207"}, "docker": "quay.io/biocontainers/perl-sanger-cgp-vagrent", "aliases": {"Admin_CacheFileBuilder.pl": "/usr/local/bin/Admin_CacheFileBuilder.pl", "Admin_EnsemblReferenceFileGenerator.pl": "/usr/local/bin/Admin_EnsemblReferenceFileGenerator.pl", "Admin_EnsemblTranscriptFilter.pl": "/usr/local/bin/Admin_EnsemblTranscriptFilter.pl", "Admin_GeneRegionBedDumper.pl": "/usr/local/bin/Admin_GeneRegionBedDumper.pl", "AnnotateVcf.pl": "/usr/local/bin/AnnotateVcf.pl", "addVagrentContext.pl": "/usr/local/bin/addVagrentContext.pl", "l4p-tmpl": "/usr/local/bin/l4p-tmpl", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index", "bp_biogetseq": "/usr/local/bin/bp_biogetseq", "bp_dbsplit": "/usr/local/bin/bp_dbsplit", "bp_extract_feature_seq": "/usr/local/bin/bp_extract_feature_seq", "bp_fastam9_to_table": "/usr/local/bin/bp_fastam9_to_table", "bp_fetch": "/usr/local/bin/bp_fetch", "bp_filter_search": "/usr/local/bin/bp_filter_search", "bp_find-blast-matches": "/usr/local/bin/bp_find-blast-matches"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-sanger-cgp-vagrent.
shpc-registry automated BioContainers addition for perl-sanger-cgp-vagrent
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-vagrent
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-vagrent:3.7.0--pl5321hec16e2b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-sanger-cgp-vagrent/3.7.0--pl5321hec16e2b_1
$ module help quay.io/biocontainers/perl-sanger-cgp-vagrent/3.7.0--pl5321hec16e2b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-sanger-cgp-vagrent-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-vagrent-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-vagrent-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-sanger-cgp-vagrent-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-sanger-cgp-vagrent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-sanger-cgp-vagrent-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Admin_CacheFileBuilder.pl

```bash
$ singularity exec <container> /usr/local/bin/Admin_CacheFileBuilder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Admin_CacheFileBuilder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Admin_CacheFileBuilder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Admin_EnsemblReferenceFileGenerator.pl

```bash
$ singularity exec <container> /usr/local/bin/Admin_EnsemblReferenceFileGenerator.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Admin_EnsemblReferenceFileGenerator.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Admin_EnsemblReferenceFileGenerator.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Admin_EnsemblTranscriptFilter.pl

```bash
$ singularity exec <container> /usr/local/bin/Admin_EnsemblTranscriptFilter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Admin_EnsemblTranscriptFilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Admin_EnsemblTranscriptFilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Admin_GeneRegionBedDumper.pl

```bash
$ singularity exec <container> /usr/local/bin/Admin_GeneRegionBedDumper.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Admin_GeneRegionBedDumper.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Admin_GeneRegionBedDumper.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnnotateVcf.pl

```bash
$ singularity exec <container> /usr/local/bin/AnnotateVcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/AnnotateVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnnotateVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addVagrentContext.pl

```bash
$ singularity exec <container> /usr/local/bin/addVagrentContext.pl
$ podman run --it --rm --entrypoint /usr/local/bin/addVagrentContext.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addVagrentContext.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### l4p-tmpl

```bash
$ singularity exec <container> /usr/local/bin/l4p-tmpl
$ podman run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
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