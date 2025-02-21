---
layout: container
name:  "quay.io/biocontainers/localhgt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/localhgt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/localhgt/container.yaml"
updated_at: "2025-02-21 03:05:51.406946"
latest: "1.0.1--h9948957_3"
container_url: "https://biocontainers.pro/tools/localhgt"
aliases:
 - "accurate_bkp.py"
 - "evaluation.py"
 - "extractSplitReads_BwaMem.py"
 - "extract_ref"
 - "extract_transferred_seq.py"
 - "generate_run_scripts.py"
 - "get_bed_file.py"
 - "get_raw_bkp.py"
 - "infer_HGT_breakpoint.py"
 - "infer_HGT_event.py"
 - "localhgt"
 - "localhgt.py"
 - "pipeline.sh"
 - "remove_repeat.py"
 - "simulation.py"
 - "annot-tsv"
 - "h5tools_test_utils"
 - "seqkit"
 - "biom"
 - "fastp"
 - "h5fuse.sh"
 - "h5delete"
 - "igzip"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "faidx"
 - "natsort"
 - "py.test"
 - "pytest"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "normalizer"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
versions:
 - "1.0.1--h4ac6f70_0"
 - "1.0.1--h4ac6f70_2"
 - "1.0.1--h9948957_3"
description: "singularity registry hpc automated addition for localhgt"
config: {"url": "https://biocontainers.pro/tools/localhgt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for localhgt", "latest": {"1.0.1--h9948957_3": "sha256:6f6b82084838f0446e5835a5e7371ad1e9d0053c901e550479c67a47983bfeef"}, "tags": {"1.0.1--h4ac6f70_0": "sha256:b066b3045299e2a1433dded0d62906d292982a08d68181d72ebaebafb2a5740b", "1.0.1--h4ac6f70_2": "sha256:20efa1b8f0d5bd67ac947aaa868c25651e9753a9645d029fb4837964fdcd205d", "1.0.1--h9948957_3": "sha256:6f6b82084838f0446e5835a5e7371ad1e9d0053c901e550479c67a47983bfeef"}, "docker": "quay.io/biocontainers/localhgt", "aliases": {"accurate_bkp.py": "/usr/local/bin/accurate_bkp.py", "evaluation.py": "/usr/local/bin/evaluation.py", "extractSplitReads_BwaMem.py": "/usr/local/bin/extractSplitReads_BwaMem.py", "extract_ref": "/usr/local/bin/extract_ref", "extract_transferred_seq.py": "/usr/local/bin/extract_transferred_seq.py", "generate_run_scripts.py": "/usr/local/bin/generate_run_scripts.py", "get_bed_file.py": "/usr/local/bin/get_bed_file.py", "get_raw_bkp.py": "/usr/local/bin/get_raw_bkp.py", "infer_HGT_breakpoint.py": "/usr/local/bin/infer_HGT_breakpoint.py", "infer_HGT_event.py": "/usr/local/bin/infer_HGT_event.py", "localhgt": "/usr/local/bin/localhgt", "localhgt.py": "/usr/local/bin/localhgt.py", "pipeline.sh": "/usr/local/bin/pipeline.sh", "remove_repeat.py": "/usr/local/bin/remove_repeat.py", "simulation.py": "/usr/local/bin/simulation.py", "annot-tsv": "/usr/local/bin/annot-tsv", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "seqkit": "/usr/local/bin/seqkit", "biom": "/usr/local/bin/biom", "fastp": "/usr/local/bin/fastp", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "h5delete": "/usr/local/bin/h5delete", "igzip": "/usr/local/bin/igzip", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "faidx": "/usr/local/bin/faidx", "natsort": "/usr/local/bin/natsort", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "normalizer": "/usr/local/bin/normalizer", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/localhgt.
singularity registry hpc automated addition for localhgt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/localhgt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/localhgt:1.0.1--h9948957_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/localhgt/1.0.1--h9948957_3
$ module help quay.io/biocontainers/localhgt/1.0.1--h9948957_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### localhgt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### localhgt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### localhgt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### localhgt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### localhgt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### localhgt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### accurate_bkp.py

```bash
$ singularity exec <container> /usr/local/bin/accurate_bkp.py
$ podman run --it --rm --entrypoint /usr/local/bin/accurate_bkp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accurate_bkp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evaluation.py

```bash
$ singularity exec <container> /usr/local/bin/evaluation.py
$ podman run --it --rm --entrypoint /usr/local/bin/evaluation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractSplitReads_BwaMem.py

```bash
$ singularity exec <container> /usr/local/bin/extractSplitReads_BwaMem.py
$ podman run --it --rm --entrypoint /usr/local/bin/extractSplitReads_BwaMem.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractSplitReads_BwaMem.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_ref

```bash
$ singularity exec <container> /usr/local/bin/extract_ref
$ podman run --it --rm --entrypoint /usr/local/bin/extract_ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_transferred_seq.py

```bash
$ singularity exec <container> /usr/local/bin/extract_transferred_seq.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_transferred_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_transferred_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_run_scripts.py

```bash
$ singularity exec <container> /usr/local/bin/generate_run_scripts.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_run_scripts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_run_scripts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_bed_file.py

```bash
$ singularity exec <container> /usr/local/bin/get_bed_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_bed_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_bed_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_raw_bkp.py

```bash
$ singularity exec <container> /usr/local/bin/get_raw_bkp.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_raw_bkp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_raw_bkp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infer_HGT_breakpoint.py

```bash
$ singularity exec <container> /usr/local/bin/infer_HGT_breakpoint.py
$ podman run --it --rm --entrypoint /usr/local/bin/infer_HGT_breakpoint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infer_HGT_breakpoint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infer_HGT_event.py

```bash
$ singularity exec <container> /usr/local/bin/infer_HGT_event.py
$ podman run --it --rm --entrypoint /usr/local/bin/infer_HGT_event.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infer_HGT_event.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### localhgt

```bash
$ singularity exec <container> /usr/local/bin/localhgt
$ podman run --it --rm --entrypoint /usr/local/bin/localhgt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/localhgt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### localhgt.py

```bash
$ singularity exec <container> /usr/local/bin/localhgt.py
$ podman run --it --rm --entrypoint /usr/local/bin/localhgt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/localhgt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pipeline.sh

```bash
$ singularity exec <container> /usr/local/bin/pipeline.sh
$ podman run --it --rm --entrypoint /usr/local/bin/pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_repeat.py

```bash
$ singularity exec <container> /usr/local/bin/remove_repeat.py
$ podman run --it --rm --entrypoint /usr/local/bin/remove_repeat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_repeat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulation.py

```bash
$ singularity exec <container> /usr/local/bin/simulation.py
$ podman run --it --rm --entrypoint /usr/local/bin/simulation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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