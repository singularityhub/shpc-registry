---
layout: container
name:  "quay.io/biocontainers/rpf-count-cds"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rpf-count-cds/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rpf-count-cds/container.yaml"
updated_at: "2024-06-30 02:39:22.323843"
latest: "0.0.1--py_1"
container_url: "https://biocontainers.pro/tools/rpf-count-cds"
aliases:
 - "RPF_count_CDS.py"
 - "RPF_count_CDS_nonStranded.py"
 - "htseq-count"
 - "htseq-qa"
 - "conv-template"
 - "from-template"
 - "qhelpconverter"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
versions:
 - "0.0.1--py_1"
description: "shpc-registry automated BioContainers addition for rpf-count-cds"
config: {"url": "https://biocontainers.pro/tools/rpf-count-cds", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rpf-count-cds", "latest": {"0.0.1--py_1": "sha256:3b397775181005e0ec2784811d9437efd68a72c805d6d861983b0294a61b76fd"}, "tags": {"0.0.1--py_1": "sha256:3b397775181005e0ec2784811d9437efd68a72c805d6d861983b0294a61b76fd"}, "docker": "quay.io/biocontainers/rpf-count-cds", "aliases": {"RPF_count_CDS.py": "/usr/local/bin/RPF_count_CDS.py", "RPF_count_CDS_nonStranded.py": "/usr/local/bin/RPF_count_CDS_nonStranded.py", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "qhelpconverter": "/usr/local/bin/qhelpconverter", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rpf-count-cds.
shpc-registry automated BioContainers addition for rpf-count-cds
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rpf-count-cds
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rpf-count-cds:0.0.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rpf-count-cds/0.0.1--py_1
$ module help quay.io/biocontainers/rpf-count-cds/0.0.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rpf-count-cds-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rpf-count-cds-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rpf-count-cds-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rpf-count-cds-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rpf-count-cds-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rpf-count-cds-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RPF_count_CDS.py

```bash
$ singularity exec <container> /usr/local/bin/RPF_count_CDS.py
$ podman run --it --rm --entrypoint /usr/local/bin/RPF_count_CDS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RPF_count_CDS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RPF_count_CDS_nonStranded.py

```bash
$ singularity exec <container> /usr/local/bin/RPF_count_CDS_nonStranded.py
$ podman run --it --rm --entrypoint /usr/local/bin/RPF_count_CDS_nonStranded.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RPF_count_CDS_nonStranded.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
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