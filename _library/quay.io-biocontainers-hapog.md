---
layout: container
name:  "quay.io/biocontainers/hapog"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hapog/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hapog/container.yaml"
updated_at: "2025-09-09 03:40:22.857213"
latest: "1.3.8--py312he57d009_1"
container_url: "https://biocontainers.pro/tools/hapog"
aliases:
 - "hapog"
 - "hapog_bin"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "f2py3.10"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
 - "md5sum-lite"
 - "plot-bamstats"
 - "psl2sam.pl"
 - "sam2vcf.pl"
 - "samtools.pl"
 - "seq_cache_populate.pl"
 - "soap2sam.pl"
versions:
 - "1.3.4--py310hfa7d255_1"
 - "1.3.4--py310h295bcc1_2"
 - "1.3.4--py310ha48c3da_3"
 - "1.3.6--py39hbbc4c85_0"
 - "1.3.7--py38he5da3d1_0"
 - "1.3.8--py310h83093d7_0"
 - "1.3.8--py312he57d009_1"
description: "singularity registry hpc automated addition for hapog"
config: {"url": "https://biocontainers.pro/tools/hapog", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hapog", "latest": {"1.3.8--py312he57d009_1": "sha256:707fe096543c663010eba85c25c47475fd4b9f750f3491f6657b696f30eb88c4"}, "tags": {"1.3.4--py310hfa7d255_1": "sha256:7d1ab8604eb025c5dbd3dfe56e92988a453d0e45f706cf1c48d57caabb0dd2a2", "1.3.4--py310h295bcc1_2": "sha256:ae121cbe04edbac69d2e82d5002e543468425208b9127c21cd787bbfe925dd21", "1.3.4--py310ha48c3da_3": "sha256:51291166eba17a2ee55d8eed2555260737bff65b1b858c0a4fdefc0d35b7be54", "1.3.6--py39hbbc4c85_0": "sha256:95a58b0363f016c96151e60e195e3710d7635d30fb8323474fde09bc9c2348ed", "1.3.7--py38he5da3d1_0": "sha256:54d45a5fab9c0b6945e5c7ca1d159c3134a00e212a556a37895c1e0d3a308efb", "1.3.8--py310h83093d7_0": "sha256:dc2e0db412fe94fdb85406b1c5391c2602973d156241ba8f9626f769ff1b96a9", "1.3.8--py312he57d009_1": "sha256:707fe096543c663010eba85c25c47475fd4b9f750f3491f6657b696f30eb88c4"}, "docker": "quay.io/biocontainers/hapog", "aliases": {"hapog": "/usr/local/bin/hapog", "hapog_bin": "/usr/local/bin/hapog_bin", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "f2py3.10": "/usr/local/bin/f2py3.10", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite", "plot-bamstats": "/usr/local/bin/plot-bamstats", "psl2sam.pl": "/usr/local/bin/psl2sam.pl", "sam2vcf.pl": "/usr/local/bin/sam2vcf.pl", "samtools.pl": "/usr/local/bin/samtools.pl", "seq_cache_populate.pl": "/usr/local/bin/seq_cache_populate.pl", "soap2sam.pl": "/usr/local/bin/soap2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hapog.
singularity registry hpc automated addition for hapog
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hapog
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hapog:1.3.8--py312he57d009_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hapog/1.3.8--py312he57d009_1
$ module help quay.io/biocontainers/hapog/1.3.8--py312he57d009_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hapog-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hapog-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hapog-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hapog-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hapog-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hapog-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hapog

```bash
$ singularity exec <container> /usr/local/bin/hapog
$ podman run --it --rm --entrypoint /usr/local/bin/hapog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapog_bin

```bash
$ singularity exec <container> /usr/local/bin/hapog_bin
$ podman run --it --rm --entrypoint /usr/local/bin/hapog_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapog_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### md5sum-lite

```bash
$ singularity exec <container> /usr/local/bin/md5sum-lite
$ podman run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-bamstats

```bash
$ singularity exec <container> /usr/local/bin/plot-bamstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/psl2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/sam2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools.pl

```bash
$ singularity exec <container> /usr/local/bin/samtools.pl
$ podman run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.pl

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/soap2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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