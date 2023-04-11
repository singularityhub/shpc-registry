---
layout: container
name:  "quay.io/biocontainers/hamip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hamip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hamip/container.yaml"
updated_at: "2023-04-11 02:59:17.565865"
latest: "0.0.3.2--py_0"
container_url: "https://biocontainers.pro/tools/hamip"
aliases:
 - "HaMiP"
 - "LiBis"
 - "bamsort.sh"
 - "bbf"
 - "bseqc2"
 - "bseqc2mbiasplot.R"
 - "bsmap"
 - "fetchChromSizes"
 - "mcall"
 - "mcomp"
 - "moabs"
 - "numCI"
 - "pefilter"
 - "preprocess_novoalign.sh"
 - "redepth.pl"
 - "routines.pm"
 - "template_for_cfg"
 - "template_for_qsub"
 - "trim_galore"
 - "cutadapt"
 - "fastqc"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "pigz"
 - "unpigz"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
versions:
 - "0.0.3.2--py_0"
description: "shpc-registry automated BioContainers addition for hamip"
config: {"url": "https://biocontainers.pro/tools/hamip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hamip", "latest": {"0.0.3.2--py_0": "sha256:1af48747c1ad4c2cfe9e212772329b33cfc79400c7de8b7a4506afe4b75d6097"}, "tags": {"0.0.3.2--py_0": "sha256:1af48747c1ad4c2cfe9e212772329b33cfc79400c7de8b7a4506afe4b75d6097"}, "docker": "quay.io/biocontainers/hamip", "aliases": {"HaMiP": "/usr/local/bin/HaMiP", "LiBis": "/usr/local/bin/LiBis", "bamsort.sh": "/usr/local/bin/bamsort.sh", "bbf": "/usr/local/bin/bbf", "bseqc2": "/usr/local/bin/bseqc2", "bseqc2mbiasplot.R": "/usr/local/bin/bseqc2mbiasplot.R", "bsmap": "/usr/local/bin/bsmap", "fetchChromSizes": "/usr/local/bin/fetchChromSizes", "mcall": "/usr/local/bin/mcall", "mcomp": "/usr/local/bin/mcomp", "moabs": "/usr/local/bin/moabs", "numCI": "/usr/local/bin/numCI", "pefilter": "/usr/local/bin/pefilter", "preprocess_novoalign.sh": "/usr/local/bin/preprocess_novoalign.sh", "redepth.pl": "/usr/local/bin/redepth.pl", "routines.pm": "/usr/local/bin/routines.pm", "template_for_cfg": "/usr/local/bin/template_for_cfg", "template_for_qsub": "/usr/local/bin/template_for_qsub", "trim_galore": "/usr/local/bin/trim_galore", "cutadapt": "/usr/local/bin/cutadapt", "fastqc": "/usr/local/bin/fastqc", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hamip.
shpc-registry automated BioContainers addition for hamip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hamip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hamip:0.0.3.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hamip/0.0.3.2--py_0
$ module help quay.io/biocontainers/hamip/0.0.3.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hamip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hamip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hamip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hamip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hamip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hamip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HaMiP

```bash
$ singularity exec <container> /usr/local/bin/HaMiP
$ podman run --it --rm --entrypoint /usr/local/bin/HaMiP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HaMiP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LiBis

```bash
$ singularity exec <container> /usr/local/bin/LiBis
$ podman run --it --rm --entrypoint /usr/local/bin/LiBis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LiBis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamsort.sh

```bash
$ singularity exec <container> /usr/local/bin/bamsort.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bamsort.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamsort.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbf

```bash
$ singularity exec <container> /usr/local/bin/bbf
$ podman run --it --rm --entrypoint /usr/local/bin/bbf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bseqc2

```bash
$ singularity exec <container> /usr/local/bin/bseqc2
$ podman run --it --rm --entrypoint /usr/local/bin/bseqc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bseqc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bseqc2mbiasplot.R

```bash
$ singularity exec <container> /usr/local/bin/bseqc2mbiasplot.R
$ podman run --it --rm --entrypoint /usr/local/bin/bseqc2mbiasplot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bseqc2mbiasplot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsmap

```bash
$ singularity exec <container> /usr/local/bin/bsmap
$ podman run --it --rm --entrypoint /usr/local/bin/bsmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchChromSizes

```bash
$ singularity exec <container> /usr/local/bin/fetchChromSizes
$ podman run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcall

```bash
$ singularity exec <container> /usr/local/bin/mcall
$ podman run --it --rm --entrypoint /usr/local/bin/mcall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcomp

```bash
$ singularity exec <container> /usr/local/bin/mcomp
$ podman run --it --rm --entrypoint /usr/local/bin/mcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moabs

```bash
$ singularity exec <container> /usr/local/bin/moabs
$ podman run --it --rm --entrypoint /usr/local/bin/moabs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moabs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numCI

```bash
$ singularity exec <container> /usr/local/bin/numCI
$ podman run --it --rm --entrypoint /usr/local/bin/numCI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numCI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pefilter

```bash
$ singularity exec <container> /usr/local/bin/pefilter
$ podman run --it --rm --entrypoint /usr/local/bin/pefilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pefilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocess_novoalign.sh

```bash
$ singularity exec <container> /usr/local/bin/preprocess_novoalign.sh
$ podman run --it --rm --entrypoint /usr/local/bin/preprocess_novoalign.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocess_novoalign.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### redepth.pl

```bash
$ singularity exec <container> /usr/local/bin/redepth.pl
$ podman run --it --rm --entrypoint /usr/local/bin/redepth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redepth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### routines.pm

```bash
$ singularity exec <container> /usr/local/bin/routines.pm
$ podman run --it --rm --entrypoint /usr/local/bin/routines.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/routines.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### template_for_cfg

```bash
$ singularity exec <container> /usr/local/bin/template_for_cfg
$ podman run --it --rm --entrypoint /usr/local/bin/template_for_cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/template_for_cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### template_for_qsub

```bash
$ singularity exec <container> /usr/local/bin/template_for_qsub
$ podman run --it --rm --entrypoint /usr/local/bin/template_for_qsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/template_for_qsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_galore

```bash
$ singularity exec <container> /usr/local/bin/trim_galore
$ podman run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
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