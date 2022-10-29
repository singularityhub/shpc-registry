---
layout: container
name:  "quay.io/biocontainers/phenix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phenix/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/phenix/container.yaml"
updated_at: "2022-10-29 05:31:48.218284"
latest: "1.4.1a--py27h3dcb392_1"
container_url: "https://biocontainers.pro/tools/phenix"
aliases:
 - "GenomeAnalysisTK"
 - "filter_vcf.py"
 - "gatk-register"
 - "phenix.py"
 - "prepare_reference.py"
 - "run_snp_pipeline.py"
 - "vcf2distancematrix.py"
 - "vcf2fasta.py"
 - "vcf2json.py"
 - "ace2sam"
 - "appletviewer"
 - "aserver"
 - "assistant"
 - "bcftools"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
versions:
 - "1.4.1a--py27h3dcb392_1"
description: "shpc-registry automated BioContainers addition for phenix"
config: {"url": "https://biocontainers.pro/tools/phenix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phenix", "latest": {"1.4.1a--py27h3dcb392_1": "sha256:ae932d62d620e9d607e94ccd20809f7f8215001600dc3851c47e2c4076946b3d"}, "tags": {"1.4.1a--py27h3dcb392_1": "sha256:ae932d62d620e9d607e94ccd20809f7f8215001600dc3851c47e2c4076946b3d"}, "docker": "quay.io/biocontainers/phenix", "aliases": {"GenomeAnalysisTK": "/usr/local/bin/GenomeAnalysisTK", "filter_vcf.py": "/usr/local/bin/filter_vcf.py", "gatk-register": "/usr/local/bin/gatk-register", "phenix.py": "/usr/local/bin/phenix.py", "prepare_reference.py": "/usr/local/bin/prepare_reference.py", "run_snp_pipeline.py": "/usr/local/bin/run_snp_pipeline.py", "vcf2distancematrix.py": "/usr/local/bin/vcf2distancematrix.py", "vcf2fasta.py": "/usr/local/bin/vcf2fasta.py", "vcf2json.py": "/usr/local/bin/vcf2json.py", "ace2sam": "/usr/local/bin/ace2sam", "appletviewer": "/usr/local/bin/appletviewer", "aserver": "/usr/local/bin/aserver", "assistant": "/usr/local/bin/assistant", "bcftools": "/usr/local/bin/bcftools", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phenix.
shpc-registry automated BioContainers addition for phenix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phenix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phenix:1.4.1a--py27h3dcb392_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phenix/1.4.1a--py27h3dcb392_1
$ module help quay.io/biocontainers/phenix/1.4.1a--py27h3dcb392_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phenix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phenix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phenix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phenix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phenix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phenix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GenomeAnalysisTK

```bash
$ singularity exec <container> /usr/local/bin/GenomeAnalysisTK
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_vcf.py

```bash
$ singularity exec <container> /usr/local/bin/filter_vcf.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_vcf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk-register

```bash
$ singularity exec <container> /usr/local/bin/gatk-register
$ podman run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phenix.py

```bash
$ singularity exec <container> /usr/local/bin/phenix.py
$ podman run --it --rm --entrypoint /usr/local/bin/phenix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phenix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_reference.py

```bash
$ singularity exec <container> /usr/local/bin/prepare_reference.py
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_snp_pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/run_snp_pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_snp_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_snp_pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2distancematrix.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2distancematrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2distancematrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2distancematrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2fasta.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2json.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2json.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2json.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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