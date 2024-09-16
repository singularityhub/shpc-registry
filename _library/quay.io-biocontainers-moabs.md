---
layout: container
name:  "quay.io/biocontainers/moabs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moabs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/moabs/container.yaml"
updated_at: "2024-09-16 03:11:28.100514"
latest: "1.3.9.6--pl5321r42ha503a2d_6"
container_url: "https://biocontainers.pro/tools/moabs"
aliases:
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
 - "idn2"
 - "wget"
 - "samtools"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.3.9.6--pl5321r41h87262cc_3"
 - "1.3.9.6--pl5321r42h87262cc_4"
 - "1.3.9.6--pl5321r42h87262cc_5"
 - "1.3.9.6--pl5321r42ha503a2d_6"
description: "shpc-registry automated BioContainers addition for moabs"
config: {"url": "https://biocontainers.pro/tools/moabs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for moabs", "latest": {"1.3.9.6--pl5321r42ha503a2d_6": "sha256:528621d908bbbad93eed0ba8d6194644eb062e8786127d4730ae0f88f537f292"}, "tags": {"1.3.9.6--pl5321r41h87262cc_3": "sha256:656f4b98a7b42f3023c2c2b4bcbdfac065f72d16e89cee10389f82925fb8769c", "1.3.9.6--pl5321r42h87262cc_4": "sha256:c67001022771a3eb45d4f4a836220afd2f11d01f3818be8b4cd8387bdf8799d9", "1.3.9.6--pl5321r42h87262cc_5": "sha256:f1b860c9f72eabdbffef763c9680cd44049bc085c28ca452e1c406dd6bd382b7", "1.3.9.6--pl5321r42ha503a2d_6": "sha256:528621d908bbbad93eed0ba8d6194644eb062e8786127d4730ae0f88f537f292"}, "docker": "quay.io/biocontainers/moabs", "aliases": {"bamsort.sh": "/usr/local/bin/bamsort.sh", "bbf": "/usr/local/bin/bbf", "bseqc2": "/usr/local/bin/bseqc2", "bseqc2mbiasplot.R": "/usr/local/bin/bseqc2mbiasplot.R", "bsmap": "/usr/local/bin/bsmap", "mcall": "/usr/local/bin/mcall", "mcomp": "/usr/local/bin/mcomp", "moabs": "/usr/local/bin/moabs", "numCI": "/usr/local/bin/numCI", "pefilter": "/usr/local/bin/pefilter", "preprocess_novoalign.sh": "/usr/local/bin/preprocess_novoalign.sh", "redepth.pl": "/usr/local/bin/redepth.pl", "routines.pm": "/usr/local/bin/routines.pm", "template_for_cfg": "/usr/local/bin/template_for_cfg", "template_for_qsub": "/usr/local/bin/template_for_qsub", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "samtools": "/usr/local/bin/samtools", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moabs.
shpc-registry automated BioContainers addition for moabs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moabs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moabs:1.3.9.6--pl5321r42ha503a2d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moabs/1.3.9.6--pl5321r42ha503a2d_6
$ module help quay.io/biocontainers/moabs/1.3.9.6--pl5321r42ha503a2d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moabs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moabs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moabs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moabs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moabs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moabs-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools

```bash
$ singularity exec <container> /usr/local/bin/samtools
$ podman run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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