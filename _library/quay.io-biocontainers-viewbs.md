---
layout: container
name:  "quay.io/biocontainers/viewbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/viewbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/viewbs/container.yaml"
updated_at: "2023-10-16 02:26:34.653013"
latest: "0.1.11--pl5321h031d066_3"
container_url: "https://biocontainers.pro/tools/viewbs"
aliases:
 - "ViewBS"
 - "brat2bismark.pl"
 - "bsseeker2bismark.pl"
 - "demo-getopt-long-subcommand"
 - "gff2tab.pl"
 - "mer_fig.R"
 - "bam2bedgraph"
 - "bp_pairwise_kaks"
 - "bp_find-blast-matches.pl"
 - "t_coffee"
 - "baseml"
 - "basemlg"
 - "chi2"
 - "codeml"
 - "evolver"
 - "infinitesites"
versions:
 - "0.1.9--pl5262h779adbc_0"
 - "0.1.11--pl5321hec16e2b_2"
 - "0.1.11--pl5321h031d066_3"
description: "shpc-registry automated BioContainers addition for viewbs"
config: {"url": "https://biocontainers.pro/tools/viewbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for viewbs", "latest": {"0.1.11--pl5321h031d066_3": "sha256:969898388e80363c71823c29493ade49119894fbc54c248cae0d7ca7701060d0"}, "tags": {"0.1.9--pl5262h779adbc_0": "sha256:e6c2ad6c0ad34f6d913df526279f77179af4bb9b38813647558b45dce7105558", "0.1.11--pl5321hec16e2b_2": "sha256:0ef331248994e60823bdc026589577eddd0b76a4504e2c2bb85f8d41319dda76", "0.1.11--pl5321h031d066_3": "sha256:969898388e80363c71823c29493ade49119894fbc54c248cae0d7ca7701060d0"}, "docker": "quay.io/biocontainers/viewbs", "aliases": {"ViewBS": "/usr/local/bin/ViewBS", "brat2bismark.pl": "/usr/local/bin/brat2bismark.pl", "bsseeker2bismark.pl": "/usr/local/bin/bsseeker2bismark.pl", "demo-getopt-long-subcommand": "/usr/local/bin/demo-getopt-long-subcommand", "gff2tab.pl": "/usr/local/bin/gff2tab.pl", "mer_fig.R": "/usr/local/bin/mer_fig.R", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_pairwise_kaks": "/usr/local/bin/bp_pairwise_kaks", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "t_coffee": "/usr/local/bin/t_coffee", "baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg", "chi2": "/usr/local/bin/chi2", "codeml": "/usr/local/bin/codeml", "evolver": "/usr/local/bin/evolver", "infinitesites": "/usr/local/bin/infinitesites"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/viewbs.
shpc-registry automated BioContainers addition for viewbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/viewbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/viewbs:0.1.11--pl5321h031d066_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/viewbs/0.1.11--pl5321h031d066_3
$ module help quay.io/biocontainers/viewbs/0.1.11--pl5321h031d066_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### viewbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### viewbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### viewbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### viewbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### viewbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### viewbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ViewBS

```bash
$ singularity exec <container> /usr/local/bin/ViewBS
$ podman run --it --rm --entrypoint /usr/local/bin/ViewBS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ViewBS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brat2bismark.pl

```bash
$ singularity exec <container> /usr/local/bin/brat2bismark.pl
$ podman run --it --rm --entrypoint /usr/local/bin/brat2bismark.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brat2bismark.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsseeker2bismark.pl

```bash
$ singularity exec <container> /usr/local/bin/bsseeker2bismark.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bsseeker2bismark.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsseeker2bismark.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demo-getopt-long-subcommand

```bash
$ singularity exec <container> /usr/local/bin/demo-getopt-long-subcommand
$ podman run --it --rm --entrypoint /usr/local/bin/demo-getopt-long-subcommand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demo-getopt-long-subcommand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2tab.pl

```bash
$ singularity exec <container> /usr/local/bin/gff2tab.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff2tab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2tab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mer_fig.R

```bash
$ singularity exec <container> /usr/local/bin/mer_fig.R
$ podman run --it --rm --entrypoint /usr/local/bin/mer_fig.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mer_fig.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t_coffee

```bash
$ singularity exec <container> /usr/local/bin/t_coffee
$ podman run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basemlg

```bash
$ singularity exec <container> /usr/local/bin/basemlg
$ podman run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chi2

```bash
$ singularity exec <container> /usr/local/bin/chi2
$ podman run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codeml

```bash
$ singularity exec <container> /usr/local/bin/codeml
$ podman run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evolver

```bash
$ singularity exec <container> /usr/local/bin/evolver
$ podman run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infinitesites

```bash
$ singularity exec <container> /usr/local/bin/infinitesites
$ podman run --it --rm --entrypoint /usr/local/bin/infinitesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infinitesites   -v ${PWD} -w ${PWD} <container> -c " $@"
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