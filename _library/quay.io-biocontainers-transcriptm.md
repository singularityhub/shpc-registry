---
layout: container
name:  "quay.io/biocontainers/transcriptm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transcriptm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transcriptm/container.yaml"
updated_at: "2026-01-03 03:29:29.599296"
latest: "0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/transcriptm"
aliases:
 - "bamFlags"
 - "bamm"
 - "bioruby"
 - "br_biofetch.rb"
 - "br_bioflat.rb"
 - "br_biogetseq.rb"
 - "br_pmfetch.rb"
 - "create-db-indices.sh"
 - "dirseq"
 - "fxtract"
 - "indexdb_rna"
 - "sortmerna"
 - "transcriptm"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
 - "fastqc"
 - "trimmomatic"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
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
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
versions:
 - "0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for transcriptm"
config: {"url": "https://biocontainers.pro/tools/transcriptm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for transcriptm", "latest": {"0.2--pyhdfd78af_0": "sha256:0c5eda84165be9ccf81bd2a8835f766ec0fc99253980a2a1b8207806e707ee0e"}, "tags": {"0.2--pyhdfd78af_0": "sha256:0c5eda84165be9ccf81bd2a8835f766ec0fc99253980a2a1b8207806e707ee0e"}, "docker": "quay.io/biocontainers/transcriptm", "aliases": {"bamFlags": "/usr/local/bin/bamFlags", "bamm": "/usr/local/bin/bamm", "bioruby": "/usr/local/bin/bioruby", "br_biofetch.rb": "/usr/local/bin/br_biofetch.rb", "br_bioflat.rb": "/usr/local/bin/br_bioflat.rb", "br_biogetseq.rb": "/usr/local/bin/br_biogetseq.rb", "br_pmfetch.rb": "/usr/local/bin/br_pmfetch.rb", "create-db-indices.sh": "/usr/local/bin/create-db-indices.sh", "dirseq": "/usr/local/bin/dirseq", "fxtract": "/usr/local/bin/fxtract", "indexdb_rna": "/usr/local/bin/indexdb_rna", "sortmerna": "/usr/local/bin/sortmerna", "transcriptm": "/usr/local/bin/transcriptm", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby", "fastqc": "/usr/local/bin/fastqc", "trimmomatic": "/usr/local/bin/trimmomatic", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "shiftBed": "/usr/local/bin/shiftBed", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transcriptm.
singularity registry hpc automated addition for transcriptm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transcriptm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transcriptm:0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transcriptm/0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/transcriptm/0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transcriptm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transcriptm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transcriptm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transcriptm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transcriptm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transcriptm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamFlags

```bash
$ singularity exec <container> /usr/local/bin/bamFlags
$ podman run --it --rm --entrypoint /usr/local/bin/bamFlags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamFlags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamm

```bash
$ singularity exec <container> /usr/local/bin/bamm
$ podman run --it --rm --entrypoint /usr/local/bin/bamm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioruby

```bash
$ singularity exec <container> /usr/local/bin/bioruby
$ podman run --it --rm --entrypoint /usr/local/bin/bioruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_biofetch.rb

```bash
$ singularity exec <container> /usr/local/bin/br_biofetch.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_biofetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_biofetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_bioflat.rb

```bash
$ singularity exec <container> /usr/local/bin/br_bioflat.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_bioflat.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_bioflat.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_biogetseq.rb

```bash
$ singularity exec <container> /usr/local/bin/br_biogetseq.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_biogetseq.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_biogetseq.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_pmfetch.rb

```bash
$ singularity exec <container> /usr/local/bin/br_pmfetch.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_pmfetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_pmfetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-db-indices.sh

```bash
$ singularity exec <container> /usr/local/bin/create-db-indices.sh
$ podman run --it --rm --entrypoint /usr/local/bin/create-db-indices.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-db-indices.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dirseq

```bash
$ singularity exec <container> /usr/local/bin/dirseq
$ podman run --it --rm --entrypoint /usr/local/bin/dirseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dirseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fxtract

```bash
$ singularity exec <container> /usr/local/bin/fxtract
$ podman run --it --rm --entrypoint /usr/local/bin/fxtract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fxtract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_rna

```bash
$ singularity exec <container> /usr/local/bin/indexdb_rna
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_rna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_rna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortmerna

```bash
$ singularity exec <container> /usr/local/bin/sortmerna
$ podman run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transcriptm

```bash
$ singularity exec <container> /usr/local/bin/transcriptm
$ podman run --it --rm --entrypoint /usr/local/bin/transcriptm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transcriptm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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