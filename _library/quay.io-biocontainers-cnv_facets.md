---
layout: container
name:  "quay.io/biocontainers/cnv_facets"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cnv_facets/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cnv_facets/container.yaml"
updated_at: "2024-04-21 03:04:11.140458"
latest: "0.16.0--py38r36h4b26f60_1"
container_url: "https://biocontainers.pro/tools/cnv_facets"
aliases:
 - "cnv_facets.R"
 - "snp-pileup"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "wget"
 - "ace2sam"
 - "blast2sam.pl"
versions:
 - "v0.11.3--r351_2"
 - "0.16.0--py38r36h4b26f60_1"
 - "0.15.0--r36h4b26f60_1"
 - "0.14.0--r351h14c3975_1"
 - "0.13.0--r351h14c3975_1"
 - "0.12.1--r351h14c3975_1"
description: "shpc-registry automated BioContainers addition for cnv_facets"
config: {"url": "https://biocontainers.pro/tools/cnv_facets", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cnv_facets", "latest": {"0.16.0--py38r36h4b26f60_1": "sha256:11a4bce7d58ef48538fe478d73991b65193024225b90fe4936c4bc88325b507a"}, "tags": {"v0.11.3--r351_2": "sha256:c6fb22e0ee176146131e9dfe8411b0e3e2128ec6a65c96441ca59c6fc1427068", "0.16.0--py38r36h4b26f60_1": "sha256:11a4bce7d58ef48538fe478d73991b65193024225b90fe4936c4bc88325b507a", "0.15.0--r36h4b26f60_1": "sha256:129a23cde5a82afa6258739692f9e1d41e3c6ceea2cbade77ec85e1755ff7359", "0.14.0--r351h14c3975_1": "sha256:e2c567ece38c9aa0cfad6ac7b5b5c4b98fcbbee261e4ceefbc3fac66879439d6", "0.13.0--r351h14c3975_1": "sha256:651054e8dab1d2554638644ca44fee2bc8e6bf11fb9a9fc0bb6e163f37cfcda8", "0.12.1--r351h14c3975_1": "sha256:b9bc31d2fe8729a166891219d3723301351670b0d83d3692891953c006de87d7"}, "docker": "quay.io/biocontainers/cnv_facets", "aliases": {"cnv_facets.R": "/usr/local/bin/cnv_facets.R", "snp-pileup": "/usr/local/bin/snp-pileup", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "wget": "/usr/local/bin/wget", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cnv_facets.
shpc-registry automated BioContainers addition for cnv_facets
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cnv_facets
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cnv_facets:0.16.0--py38r36h4b26f60_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cnv_facets/0.16.0--py38r36h4b26f60_1
$ module help quay.io/biocontainers/cnv_facets/0.16.0--py38r36h4b26f60_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cnv_facets-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cnv_facets-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cnv_facets-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cnv_facets-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cnv_facets-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cnv_facets-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cnv_facets.R

```bash
$ singularity exec <container> /usr/local/bin/cnv_facets.R
$ podman run --it --rm --entrypoint /usr/local/bin/cnv_facets.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnv_facets.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp-pileup

```bash
$ singularity exec <container> /usr/local/bin/snp-pileup
$ podman run --it --rm --entrypoint /usr/local/bin/snp-pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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