---
layout: container
name:  "quay.io/biocontainers/perl-grass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-grass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-grass/container.yaml"
updated_at: "2024-04-06 03:03:10.959901"
latest: "1.1.6--2"
container_url: "https://biocontainers.pro/tools/perl-grass"
aliases:
 - "bdf2gdfont.PLS"
 - "brass_bedpe2vcf.pl"
 - "cgpAppendIdsToVcf.pl"
 - "cgpVCFSplit.pl"
 - "cover"
 - "cpancover"
 - "cvtbdf.pl"
 - "dotty"
 - "gcov2perl"
 - "grass.pl"
 - "lneato"
 - "pod_cover"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "gdlib-config"
 - "bam2bedgraph"
 - "perl5.22.0"
 - "ace.pl"
 - "ccconfig"
 - "SOAPsh.pl"
 - "map"
versions:
 - "1.1.6--2"
description: "shpc-registry automated BioContainers addition for perl-grass"
config: {"url": "https://biocontainers.pro/tools/perl-grass", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-grass", "latest": {"1.1.6--2": "sha256:98ea23c1ab595cf5ebcb52da21ee76328a288b1b048dca31878eb75458104603"}, "tags": {"1.1.6--2": "sha256:98ea23c1ab595cf5ebcb52da21ee76328a288b1b048dca31878eb75458104603"}, "docker": "quay.io/biocontainers/perl-grass", "aliases": {"bdf2gdfont.PLS": "/usr/local/bin/bdf2gdfont.PLS", "brass_bedpe2vcf.pl": "/usr/local/bin/brass_bedpe2vcf.pl", "cgpAppendIdsToVcf.pl": "/usr/local/bin/cgpAppendIdsToVcf.pl", "cgpVCFSplit.pl": "/usr/local/bin/cgpVCFSplit.pl", "cover": "/usr/local/bin/cover", "cpancover": "/usr/local/bin/cpancover", "cvtbdf.pl": "/usr/local/bin/cvtbdf.pl", "dotty": "/usr/local/bin/dotty", "gcov2perl": "/usr/local/bin/gcov2perl", "grass.pl": "/usr/local/bin/grass.pl", "lneato": "/usr/local/bin/lneato", "pod_cover": "/usr/local/bin/pod_cover", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "gdlib-config": "/usr/local/bin/gdlib-config", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "perl5.22.0": "/usr/local/bin/perl5.22.0", "ace.pl": "/usr/local/bin/ace.pl", "ccconfig": "/usr/local/bin/ccconfig", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "map": "/usr/local/bin/map"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-grass.
shpc-registry automated BioContainers addition for perl-grass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-grass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-grass:1.1.6--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-grass/1.1.6--2
$ module help quay.io/biocontainers/perl-grass/1.1.6--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-grass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-grass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-grass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-grass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-grass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-grass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bdf2gdfont.PLS

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.PLS
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brass_bedpe2vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/brass_bedpe2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/brass_bedpe2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brass_bedpe2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpAppendIdsToVcf.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpAppendIdsToVcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpVCFSplit.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpVCFSplit.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cover

```bash
$ singularity exec <container> /usr/local/bin/cover
$ podman run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpancover

```bash
$ singularity exec <container> /usr/local/bin/cpancover
$ podman run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cvtbdf.pl

```bash
$ singularity exec <container> /usr/local/bin/cvtbdf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotty

```bash
$ singularity exec <container> /usr/local/bin/dotty
$ podman run --it --rm --entrypoint /usr/local/bin/dotty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov2perl

```bash
$ singularity exec <container> /usr/local/bin/gcov2perl
$ podman run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grass.pl

```bash
$ singularity exec <container> /usr/local/bin/grass.pl
$ podman run --it --rm --entrypoint /usr/local/bin/grass.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grass.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lneato

```bash
$ singularity exec <container> /usr/local/bin/lneato
$ podman run --it --rm --entrypoint /usr/local/bin/lneato   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lneato   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod_cover

```bash
$ singularity exec <container> /usr/local/bin/pod_cover
$ podman run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccconfig

```bash
$ singularity exec <container> /usr/local/bin/ccconfig
$ podman run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map

```bash
$ singularity exec <container> /usr/local/bin/map
$ podman run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
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