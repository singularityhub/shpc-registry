---
layout: container
name:  "quay.io/biocontainers/genotyphi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genotyphi/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/genotyphi/container.yaml"
updated_at: "2022-10-29 05:32:45.999435"
latest: "1.9.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/genotyphi"
aliases:
 - "genotyphi"
 - "genotyphi.py"
 - "parse_typhi_mykrobe.py"
 - "ace2sam"
 - "bcftools"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "color-chrs.pl"
 - "export2sam.pl"
 - "f2py2"
 - "f2py2.7"
 - "fasta-sanitize.pl"
versions:
 - "1.9.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for genotyphi"
config: {"url": "https://biocontainers.pro/tools/genotyphi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genotyphi", "latest": {"1.9.1--hdfd78af_1": "sha256:90425b7c4c6327b2394880b97f86ed7f97943df385264d87bbb90e133f5e0cde"}, "tags": {"1.9.1--hdfd78af_1": "sha256:90425b7c4c6327b2394880b97f86ed7f97943df385264d87bbb90e133f5e0cde"}, "docker": "quay.io/biocontainers/genotyphi", "aliases": {"genotyphi": "/usr/local/bin/genotyphi", "genotyphi.py": "/usr/local/bin/genotyphi.py", "parse_typhi_mykrobe.py": "/usr/local/bin/parse_typhi_mykrobe.py", "ace2sam": "/usr/local/bin/ace2sam", "bcftools": "/usr/local/bin/bcftools", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genotyphi.
shpc-registry automated BioContainers addition for genotyphi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genotyphi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genotyphi:1.9.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genotyphi/1.9.1--hdfd78af_1
$ module help quay.io/biocontainers/genotyphi/1.9.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genotyphi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genotyphi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genotyphi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genotyphi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genotyphi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genotyphi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genotyphi

```bash
$ singularity exec <container> /usr/local/bin/genotyphi
$ podman run --it --rm --entrypoint /usr/local/bin/genotyphi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotyphi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotyphi.py

```bash
$ singularity exec <container> /usr/local/bin/genotyphi.py
$ podman run --it --rm --entrypoint /usr/local/bin/genotyphi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotyphi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_typhi_mykrobe.py

```bash
$ singularity exec <container> /usr/local/bin/parse_typhi_mykrobe.py
$ podman run --it --rm --entrypoint /usr/local/bin/parse_typhi_mykrobe.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_typhi_mykrobe.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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