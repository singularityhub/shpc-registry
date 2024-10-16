---
layout: container
name:  "quay.io/biocontainers/metabat2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabat2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metabat2/container.yaml"
updated_at: "2024-10-16 03:56:55.226395"
latest: "2.17--hd498684_0"
container_url: "https://biocontainers.pro/tools/metabat2"
aliases:
 - "aggregateBinDepths.pl"
 - "aggregateContigOverlapsByBin.pl"
 - "contigOverlaps"
 - "jgi_summarize_bam_contig_depths"
 - "merge_depths.pl"
 - "metabat"
 - "metabat1"
 - "metabat2"
 - "runMetaBat.sh"
 - "perl5.26.2"
 - "podselect"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.15--h986a166_1"
 - "2.15--h4da6f23_2"
 - "2.17--hd498684_0"
description: "shpc-registry automated BioContainers addition for metabat2"
config: {"url": "https://biocontainers.pro/tools/metabat2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metabat2", "latest": {"2.17--hd498684_0": "sha256:3c47312a75c7e7d44ce7716cb30339bf41f13cd0e3ea0eb398f7cd6d6031ecc7"}, "tags": {"2.15--h986a166_1": "sha256:a2feaebcef454d3053e56545da9d81fc4e25a42ec58c8d801b0a2ce57bc76051", "2.15--h4da6f23_2": "sha256:b35adaca1250056035bdd3e44b2503f877b2f1ab61841ef0e2675c8cdc75eed3", "2.17--hd498684_0": "sha256:3c47312a75c7e7d44ce7716cb30339bf41f13cd0e3ea0eb398f7cd6d6031ecc7"}, "docker": "quay.io/biocontainers/metabat2", "aliases": {"aggregateBinDepths.pl": "/usr/local/bin/aggregateBinDepths.pl", "aggregateContigOverlapsByBin.pl": "/usr/local/bin/aggregateContigOverlapsByBin.pl", "contigOverlaps": "/usr/local/bin/contigOverlaps", "jgi_summarize_bam_contig_depths": "/usr/local/bin/jgi_summarize_bam_contig_depths", "merge_depths.pl": "/usr/local/bin/merge_depths.pl", "metabat": "/usr/local/bin/metabat", "metabat1": "/usr/local/bin/metabat1", "metabat2": "/usr/local/bin/metabat2", "runMetaBat.sh": "/usr/local/bin/runMetaBat.sh", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabat2.
shpc-registry automated BioContainers addition for metabat2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabat2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabat2:2.17--hd498684_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabat2/2.17--hd498684_0
$ module help quay.io/biocontainers/metabat2/2.17--hd498684_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabat2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabat2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabat2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabat2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabat2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabat2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aggregateBinDepths.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateBinDepths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregateContigOverlapsByBin.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateContigOverlapsByBin.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contigOverlaps

```bash
$ singularity exec <container> /usr/local/bin/contigOverlaps
$ podman run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jgi_summarize_bam_contig_depths

```bash
$ singularity exec <container> /usr/local/bin/jgi_summarize_bam_contig_depths
$ podman run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_depths.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_depths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_depths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_depths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat

```bash
$ singularity exec <container> /usr/local/bin/metabat
$ podman run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat1

```bash
$ singularity exec <container> /usr/local/bin/metabat1
$ podman run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat2

```bash
$ singularity exec <container> /usr/local/bin/metabat2
$ podman run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMetaBat.sh

```bash
$ singularity exec <container> /usr/local/bin/runMetaBat.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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