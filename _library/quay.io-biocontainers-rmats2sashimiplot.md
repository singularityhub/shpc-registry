---
layout: container
name:  "quay.io/biocontainers/rmats2sashimiplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rmats2sashimiplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rmats2sashimiplot/container.yaml"
updated_at: "2025-01-26 03:27:55.376186"
latest: "3.0.0--py39hdff8610_2"
container_url: "https://biocontainers.pro/tools/rmats2sashimiplot"
aliases:
 - "index_gff"
 - "rmats2sashimiplot"
 - "sashimi_plot"
 - "f2py2"
 - "f2py2.7"
 - "fasta-sanitize.pl"
 - "shiftBed"
 - "plot-ampliconstats"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
versions:
 - "2.0.4--py27h21c881e_2"
 - "3.0.0--py38ha5a061d_0"
 - "3.0.0--py310h079770c_0"
 - "2.0.4--py310h079770c_2"
 - "3.0.0--py39hdff8610_2"
description: "shpc-registry automated BioContainers addition for rmats2sashimiplot"
config: {"url": "https://biocontainers.pro/tools/rmats2sashimiplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rmats2sashimiplot", "latest": {"3.0.0--py39hdff8610_2": "sha256:ccc4857e10ecf7ba8c31ed19051d0424fd8c253df23cefe7ada816c4217cf385"}, "tags": {"2.0.4--py27h21c881e_2": "sha256:f9847503f54c249ec84ff20cd23184f93da09be654c6745d951860b3485b31c5", "3.0.0--py38ha5a061d_0": "sha256:116f7f4a3b581505b634b3057c12617df506121be418f921e1623a4cc01e13d4", "3.0.0--py310h079770c_0": "sha256:7a59f1747e90d3ea4eff214443b02e7fe05b3a77ba893d8ccfa8f3251d0450cc", "2.0.4--py310h079770c_2": "sha256:554802bf1fd63d51fd3b285ca5c8ae1c7cd090f7969203bc75d4a9cd9db53af3", "3.0.0--py39hdff8610_2": "sha256:ccc4857e10ecf7ba8c31ed19051d0424fd8c253df23cefe7ada816c4217cf385"}, "docker": "quay.io/biocontainers/rmats2sashimiplot", "aliases": {"index_gff": "/usr/local/bin/index_gff", "rmats2sashimiplot": "/usr/local/bin/rmats2sashimiplot", "sashimi_plot": "/usr/local/bin/sashimi_plot", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "shiftBed": "/usr/local/bin/shiftBed", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rmats2sashimiplot.
shpc-registry automated BioContainers addition for rmats2sashimiplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rmats2sashimiplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rmats2sashimiplot:3.0.0--py39hdff8610_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rmats2sashimiplot/3.0.0--py39hdff8610_2
$ module help quay.io/biocontainers/rmats2sashimiplot/3.0.0--py39hdff8610_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rmats2sashimiplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rmats2sashimiplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rmats2sashimiplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rmats2sashimiplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rmats2sashimiplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rmats2sashimiplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### index_gff

```bash
$ singularity exec <container> /usr/local/bin/index_gff
$ podman run --it --rm --entrypoint /usr/local/bin/index_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmats2sashimiplot

```bash
$ singularity exec <container> /usr/local/bin/rmats2sashimiplot
$ podman run --it --rm --entrypoint /usr/local/bin/rmats2sashimiplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmats2sashimiplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sashimi_plot

```bash
$ singularity exec <container> /usr/local/bin/sashimi_plot
$ podman run --it --rm --entrypoint /usr/local/bin/sashimi_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sashimi_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
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