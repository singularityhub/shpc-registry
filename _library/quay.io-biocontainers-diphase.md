---
layout: container
name:  "quay.io/biocontainers/diphase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/diphase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/diphase/container.yaml"
updated_at: "2025-11-08 03:43:04.809959"
latest: "1.0.3--h739ee2d_0"
container_url: "https://biocontainers.pro/tools/diphase"
aliases:
 - "eval.py"
 - "phasing"
 - "pipeline.py"
 - "plot.py"
 - "preprocessing.py"
 - "tools.py"
 - "util.py"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
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
 - "md5sum-lite"
 - "plot-bamstats"
 - "psl2sam.pl"
 - "sam2vcf.pl"
 - "samtools.pl"
 - "seq_cache_populate.pl"
 - "soap2sam.pl"
 - "zoom2sam.pl"
 - "novo2sam.pl"
 - "wgsim"
 - "wgsim_eval.pl"
 - "samtools"
versions:
 - "1.0.0--h739ee2d_0"
 - "1.0.2--h739ee2d_0"
 - "1.0.3--h739ee2d_0"
description: "singularity registry hpc automated addition for diphase"
config: {"url": "https://biocontainers.pro/tools/diphase", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for diphase", "latest": {"1.0.3--h739ee2d_0": "sha256:3b5647648ac2e4601974b3f1891113001a4c3ecfcf4cb78a9cf8dfbb8ea9fb8c"}, "tags": {"1.0.0--h739ee2d_0": "sha256:f3d3c3b64b74f0413d0bff9b44089b7e0a2081ff219f28f627f56cf9cde1aec1", "1.0.2--h739ee2d_0": "sha256:9dc9bf2b2e8770ce7e5c27a98cbc3f38be3934e99b105cb13976e08a39c48e4a", "1.0.3--h739ee2d_0": "sha256:3b5647648ac2e4601974b3f1891113001a4c3ecfcf4cb78a9cf8dfbb8ea9fb8c"}, "docker": "quay.io/biocontainers/diphase", "aliases": {"eval.py": "/usr/local/bin/eval.py", "phasing": "/usr/local/bin/phasing", "pipeline.py": "/usr/local/bin/pipeline.py", "plot.py": "/usr/local/bin/plot.py", "preprocessing.py": "/usr/local/bin/preprocessing.py", "tools.py": "/usr/local/bin/tools.py", "util.py": "/usr/local/bin/util.py", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite", "plot-bamstats": "/usr/local/bin/plot-bamstats", "psl2sam.pl": "/usr/local/bin/psl2sam.pl", "sam2vcf.pl": "/usr/local/bin/sam2vcf.pl", "samtools.pl": "/usr/local/bin/samtools.pl", "seq_cache_populate.pl": "/usr/local/bin/seq_cache_populate.pl", "soap2sam.pl": "/usr/local/bin/soap2sam.pl", "zoom2sam.pl": "/usr/local/bin/zoom2sam.pl", "novo2sam.pl": "/usr/local/bin/novo2sam.pl", "wgsim": "/usr/local/bin/wgsim", "wgsim_eval.pl": "/usr/local/bin/wgsim_eval.pl", "samtools": "/usr/local/bin/samtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/diphase.
singularity registry hpc automated addition for diphase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/diphase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/diphase:1.0.3--h739ee2d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/diphase/1.0.3--h739ee2d_0
$ module help quay.io/biocontainers/diphase/1.0.3--h739ee2d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### diphase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### diphase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### diphase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### diphase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### diphase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### diphase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eval.py

```bash
$ singularity exec <container> /usr/local/bin/eval.py
$ podman run --it --rm --entrypoint /usr/local/bin/eval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phasing

```bash
$ singularity exec <container> /usr/local/bin/phasing
$ podman run --it --rm --entrypoint /usr/local/bin/phasing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phasing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot.py

```bash
$ singularity exec <container> /usr/local/bin/plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocessing.py

```bash
$ singularity exec <container> /usr/local/bin/preprocessing.py
$ podman run --it --rm --entrypoint /usr/local/bin/preprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tools.py

```bash
$ singularity exec <container> /usr/local/bin/tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### util.py

```bash
$ singularity exec <container> /usr/local/bin/util.py
$ podman run --it --rm --entrypoint /usr/local/bin/util.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/util.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### zoom2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/zoom2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/novo2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim

```bash
$ singularity exec <container> /usr/local/bin/wgsim
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim_eval.pl

```bash
$ singularity exec <container> /usr/local/bin/wgsim_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools

```bash
$ singularity exec <container> /usr/local/bin/samtools
$ podman run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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