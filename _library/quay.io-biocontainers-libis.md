---
layout: container
name:  "quay.io/biocontainers/libis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libis/container.yaml"
updated_at: "2025-11-25 03:32:47.697507"
latest: "0.1.6--py_0"
container_url: "https://biocontainers.pro/tools/libis"
aliases:
 - "LiBis"
 - "bamsort.sh"
 - "bbf"
 - "bseqc2"
 - "bseqc2mbiasplot.R"
 - "bsmap"
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
 - "igzip"
 - "pigz"
 - "unpigz"
 - "idn2"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
versions:
 - "0.1.6--py_0"
description: "shpc-registry automated BioContainers addition for libis"
config: {"url": "https://biocontainers.pro/tools/libis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libis", "latest": {"0.1.6--py_0": "sha256:17cfd3c97160af78f846b652f0d6182b25f2cdfbc70ed1685749643f8d6e85b3"}, "tags": {"0.1.6--py_0": "sha256:17cfd3c97160af78f846b652f0d6182b25f2cdfbc70ed1685749643f8d6e85b3"}, "docker": "quay.io/biocontainers/libis", "aliases": {"LiBis": "/usr/local/bin/LiBis", "bamsort.sh": "/usr/local/bin/bamsort.sh", "bbf": "/usr/local/bin/bbf", "bseqc2": "/usr/local/bin/bseqc2", "bseqc2mbiasplot.R": "/usr/local/bin/bseqc2mbiasplot.R", "bsmap": "/usr/local/bin/bsmap", "mcall": "/usr/local/bin/mcall", "mcomp": "/usr/local/bin/mcomp", "moabs": "/usr/local/bin/moabs", "numCI": "/usr/local/bin/numCI", "pefilter": "/usr/local/bin/pefilter", "preprocess_novoalign.sh": "/usr/local/bin/preprocess_novoalign.sh", "redepth.pl": "/usr/local/bin/redepth.pl", "routines.pm": "/usr/local/bin/routines.pm", "template_for_cfg": "/usr/local/bin/template_for_cfg", "template_for_qsub": "/usr/local/bin/template_for_qsub", "trim_galore": "/usr/local/bin/trim_galore", "cutadapt": "/usr/local/bin/cutadapt", "fastqc": "/usr/local/bin/fastqc", "igzip": "/usr/local/bin/igzip", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "idn2": "/usr/local/bin/idn2", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/libis.
shpc-registry automated BioContainers addition for libis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libis:0.1.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libis/0.1.6--py_0
$ module help quay.io/biocontainers/libis/0.1.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libis-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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