---
layout: container
name:  "quay.io/biocontainers/jbrowse2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jbrowse2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jbrowse2/container.yaml"
updated_at: "2022-10-29 05:45:23.926149"
latest: "1.7.9--h9d45583_0"
container_url: "https://biocontainers.pro/tools/jbrowse2"
aliases:
 - "check-disorder.pl"
 - "corepack"
 - "gff3sort.pl"
 - "jbrowse"
 - "ace2sam"
 - "bcftools"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "color-chrs.pl"
 - "export2sam.pl"
 - "fasta-sanitize.pl"
 - "findrule"
 - "gff2gff.py"
versions:
 - "1.7.9--h9d45583_0"
description: "shpc-registry automated BioContainers addition for jbrowse2"
config: {"url": "https://biocontainers.pro/tools/jbrowse2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jbrowse2", "latest": {"1.7.9--h9d45583_0": "sha256:d9346d8b6e01a4572dfca6ba912bb5e6d6b3c7abe64f8ae9bc26ea5b81e0f9fc"}, "tags": {"1.7.9--h9d45583_0": "sha256:d9346d8b6e01a4572dfca6ba912bb5e6d6b3c7abe64f8ae9bc26ea5b81e0f9fc"}, "docker": "quay.io/biocontainers/jbrowse2", "aliases": {"check-disorder.pl": "/usr/local/bin/check-disorder.pl", "corepack": "/usr/local/bin/corepack", "gff3sort.pl": "/usr/local/bin/gff3sort.pl", "jbrowse": "/usr/local/bin/jbrowse", "ace2sam": "/usr/local/bin/ace2sam", "bcftools": "/usr/local/bin/bcftools", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "findrule": "/usr/local/bin/findrule", "gff2gff.py": "/usr/local/bin/gff2gff.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jbrowse2.
shpc-registry automated BioContainers addition for jbrowse2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jbrowse2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jbrowse2:1.7.9--h9d45583_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jbrowse2/1.7.9--h9d45583_0
$ module help quay.io/biocontainers/jbrowse2/1.7.9--h9d45583_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jbrowse2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jbrowse2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jbrowse2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jbrowse2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jbrowse2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jbrowse2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check-disorder.pl

```bash
$ singularity exec <container> /usr/local/bin/check-disorder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/check-disorder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check-disorder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3sort.pl

```bash
$ singularity exec <container> /usr/local/bin/gff3sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jbrowse

```bash
$ singularity exec <container> /usr/local/bin/jbrowse
$ podman run --it --rm --entrypoint /usr/local/bin/jbrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jbrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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