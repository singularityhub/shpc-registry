---
layout: container
name:  "quay.io/biocontainers/ivar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ivar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ivar/container.yaml"
updated_at: "2023-11-27 02:47:12.055332"
latest: "1.4.2--h0033a41_2"
container_url: "https://biocontainers.pro/tools/ivar"
aliases:
 - "ivar"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
versions:
 - "1.3.1--ha04fe3b_4"
 - "1.3--h089eab3_1"
 - "1.3.2--ha04fe3b_0"
 - "1.4--h6b7c446_1"
 - "1.3.2--ha04fe3b_1"
 - "1.4.2--h6b7c446_0"
 - "1.4.2--h6b7c446_1"
 - "1.4.2--h0033a41_2"
description: "shpc-registry automated BioContainers addition for ivar"
config: {"url": "https://biocontainers.pro/tools/ivar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ivar", "latest": {"1.4.2--h0033a41_2": "sha256:e062187153ffcc5f46be625deab88cf0190daceffcab596e188ae2d4dd643c63"}, "tags": {"1.3.1--ha04fe3b_4": "sha256:36131bfeb1c0699df733e121cd123a58f922769026b667e889c5c4f55fe87931", "1.3--h089eab3_1": "sha256:8826f9d967aa3f56a51662744f535483e0644165f186fc1d9399a7f037fea77f", "1.3.2--ha04fe3b_0": "sha256:8e7e8351863d16a15d364fd577b724f562c88abafe4891a66360233601594840", "1.4--h6b7c446_1": "sha256:0fa9e230e541512c13303ac7f4654c24f97a31535e727bd3b68338d67ed8fecd", "1.3.2--ha04fe3b_1": "sha256:0ecdc6956287408db59fe7f32f75a783e51c81ff08c909e8b00929b0928ea874", "1.4.2--h6b7c446_0": "sha256:f3af849617f93459497af44aa9448abc346f0aa19ff1938be61aeacf72cbc486", "1.4.2--h6b7c446_1": "sha256:0324a6d8db42aa6eed27e61fce22c8278c273198d4a8d0490216ace2eeee251e", "1.4.2--h0033a41_2": "sha256:e062187153ffcc5f46be625deab88cf0190daceffcab596e188ae2d4dd643c63"}, "docker": "quay.io/biocontainers/ivar", "aliases": {"ivar": "/usr/local/bin/ivar", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ivar.
shpc-registry automated BioContainers addition for ivar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ivar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ivar:1.4.2--h0033a41_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ivar/1.4.2--h0033a41_2
$ module help quay.io/biocontainers/ivar/1.4.2--h0033a41_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ivar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ivar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ivar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ivar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ivar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ivar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ivar

```bash
$ singularity exec <container> /usr/local/bin/ivar
$ podman run --it --rm --entrypoint /usr/local/bin/ivar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ivar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-short

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa

```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
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