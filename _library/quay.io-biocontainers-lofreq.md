---
layout: container
name:  "quay.io/biocontainers/lofreq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lofreq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lofreq/container.yaml"
updated_at: "2024-07-23 02:43:47.703784"
latest: "2.1.5--py38h7cf9df2_11"
container_url: "https://biocontainers.pro/tools/lofreq"
aliases:
 - "lofreq"
 - "lofreq2_call_pparallel.py"
 - "lofreq2_indel_ovlp.py"
 - "lofreq2_somatic.py"
 - "lofreq2_vcfplot.py"
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
 - "2.1.5--py38ha1fcc84_8"
 - "broken---2.5.1--py38h1bd3507_2"
 - "2.1.5--py38h794fc9e_10"
 - "2.1.5--py38h7cf9df2_11"
description: "shpc-registry automated BioContainers addition for lofreq"
config: {"url": "https://biocontainers.pro/tools/lofreq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lofreq", "latest": {"2.1.5--py38h7cf9df2_11": "sha256:b24bf1b0fdb83c43b7a82577e7b4fa400a6c05e1b67bdcd04b3e1a20f6712fe3"}, "tags": {"2.1.5--py38ha1fcc84_8": "sha256:d5d773ded7be9fa618fa7475ba11b3761e46099f1f01618e39b097e2ddddb0b8", "broken---2.5.1--py38h1bd3507_2": "sha256:1b8da7808ef98f526df7781f69dd67775d88d87236e126ec0c2f310a036355ba", "2.1.5--py38h794fc9e_10": "sha256:1d586fd2dcc67327f6799c7f0fd17b98906d4282b6ea2e109f1c8286d9350361", "2.1.5--py38h7cf9df2_11": "sha256:b24bf1b0fdb83c43b7a82577e7b4fa400a6c05e1b67bdcd04b3e1a20f6712fe3"}, "docker": "quay.io/biocontainers/lofreq", "aliases": {"lofreq": "/usr/local/bin/lofreq", "lofreq2_call_pparallel.py": "/usr/local/bin/lofreq2_call_pparallel.py", "lofreq2_indel_ovlp.py": "/usr/local/bin/lofreq2_indel_ovlp.py", "lofreq2_somatic.py": "/usr/local/bin/lofreq2_somatic.py", "lofreq2_vcfplot.py": "/usr/local/bin/lofreq2_vcfplot.py", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lofreq.
shpc-registry automated BioContainers addition for lofreq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lofreq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lofreq:2.1.5--py38h7cf9df2_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lofreq/2.1.5--py38h7cf9df2_11
$ module help quay.io/biocontainers/lofreq/2.1.5--py38h7cf9df2_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lofreq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lofreq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lofreq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lofreq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lofreq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lofreq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lofreq

```bash
$ singularity exec <container> /usr/local/bin/lofreq
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_call_pparallel.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_call_pparallel.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_call_pparallel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_call_pparallel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_indel_ovlp.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_indel_ovlp.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_somatic.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_somatic.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_somatic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_somatic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_vcfplot.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_vcfplot.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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