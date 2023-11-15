---
layout: container
name:  "quay.io/biocontainers/bactopia-variants"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bactopia-variants/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bactopia-variants/container.yaml"
updated_at: "2023-11-15 03:05:05.887424"
latest: "1.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bactopia-variants"
aliases:
 - "RNAmultifold"
 - "TMalign"
 - "bactopia-variants"
 - "cleanup-coverage.py"
 - "make_pscores.pl"
 - "mask-consensus.py"
 - "poa"
 - "sam_add_rg.pl"
 - "snippy"
 - "snippy-clean_full_aln"
 - "snippy-core"
 - "snippy-multi"
 - "snippy-vcf_extract_subs"
 - "snippy-vcf_report"
 - "snippy-vcf_to_tab"
 - "split_ref_by_bai_datasize.py"
 - "update_version.sh"
 - "vcf-annotator"
 - "snp-sites"
 - "clustalo"
 - "vt"
 - "rename"
 - "tabix++"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
 - "megablast"
 - "samclip"
 - "any2fasta"
 - "snpEff"
 - "bamleftalign"
 - "bc"
 - "coverage_to_regions.py"
 - "dc"
 - "fasta_generate_regions.py"
 - "freebayes-parallel"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for bactopia-variants"
config: {"url": "https://biocontainers.pro/tools/bactopia-variants", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bactopia-variants", "latest": {"1.0.1--hdfd78af_0": "sha256:8ede899763f9285cbb84c0449ccc7407d55fcace9e8e071126e1653639ebc04b"}, "tags": {"1.0.0--hdfd78af_0": "sha256:8d3abb93dd5a3dc0e7cd0aaa3eb76a5572aa366c7f93d0ac916e5bf4e9b19fcd", "1.0.1--hdfd78af_0": "sha256:8ede899763f9285cbb84c0449ccc7407d55fcace9e8e071126e1653639ebc04b"}, "docker": "quay.io/biocontainers/bactopia-variants", "aliases": {"RNAmultifold": "/usr/local/bin/RNAmultifold", "TMalign": "/usr/local/bin/TMalign", "bactopia-variants": "/usr/local/bin/bactopia-variants", "cleanup-coverage.py": "/usr/local/bin/cleanup-coverage.py", "make_pscores.pl": "/usr/local/bin/make_pscores.pl", "mask-consensus.py": "/usr/local/bin/mask-consensus.py", "poa": "/usr/local/bin/poa", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "snippy": "/usr/local/bin/snippy", "snippy-clean_full_aln": "/usr/local/bin/snippy-clean_full_aln", "snippy-core": "/usr/local/bin/snippy-core", "snippy-multi": "/usr/local/bin/snippy-multi", "snippy-vcf_extract_subs": "/usr/local/bin/snippy-vcf_extract_subs", "snippy-vcf_report": "/usr/local/bin/snippy-vcf_report", "snippy-vcf_to_tab": "/usr/local/bin/snippy-vcf_to_tab", "split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py", "update_version.sh": "/usr/local/bin/update_version.sh", "vcf-annotator": "/usr/local/bin/vcf-annotator", "snp-sites": "/usr/local/bin/snp-sites", "clustalo": "/usr/local/bin/clustalo", "vt": "/usr/local/bin/vt", "rename": "/usr/local/bin/rename", "tabix++": "/usr/local/bin/tabix++", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat", "megablast": "/usr/local/bin/megablast", "samclip": "/usr/local/bin/samclip", "any2fasta": "/usr/local/bin/any2fasta", "snpEff": "/usr/local/bin/snpEff", "bamleftalign": "/usr/local/bin/bamleftalign", "bc": "/usr/local/bin/bc", "coverage_to_regions.py": "/usr/local/bin/coverage_to_regions.py", "dc": "/usr/local/bin/dc", "fasta_generate_regions.py": "/usr/local/bin/fasta_generate_regions.py", "freebayes-parallel": "/usr/local/bin/freebayes-parallel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bactopia-variants.
singularity registry hpc automated addition for bactopia-variants
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bactopia-variants
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bactopia-variants:1.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bactopia-variants/1.0.1--hdfd78af_0
$ module help quay.io/biocontainers/bactopia-variants/1.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bactopia-variants-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bactopia-variants-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bactopia-variants-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bactopia-variants-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bactopia-variants-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bactopia-variants-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-variants

```bash
$ singularity exec <container> /usr/local/bin/bactopia-variants
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleanup-coverage.py

```bash
$ singularity exec <container> /usr/local/bin/cleanup-coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/cleanup-coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanup-coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pscores.pl

```bash
$ singularity exec <container> /usr/local/bin/make_pscores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mask-consensus.py

```bash
$ singularity exec <container> /usr/local/bin/mask-consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/mask-consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mask-consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_add_rg.pl

```bash
$ singularity exec <container> /usr/local/bin/sam_add_rg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy

```bash
$ singularity exec <container> /usr/local/bin/snippy
$ podman run --it --rm --entrypoint /usr/local/bin/snippy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-clean_full_aln

```bash
$ singularity exec <container> /usr/local/bin/snippy-clean_full_aln
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-clean_full_aln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-clean_full_aln   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-core

```bash
$ singularity exec <container> /usr/local/bin/snippy-core
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-multi

```bash
$ singularity exec <container> /usr/local/bin/snippy-multi
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-vcf_extract_subs

```bash
$ singularity exec <container> /usr/local/bin/snippy-vcf_extract_subs
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-vcf_extract_subs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-vcf_extract_subs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-vcf_report

```bash
$ singularity exec <container> /usr/local/bin/snippy-vcf_report
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-vcf_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-vcf_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snippy-vcf_to_tab

```bash
$ singularity exec <container> /usr/local/bin/snippy-vcf_to_tab
$ podman run --it --rm --entrypoint /usr/local/bin/snippy-vcf_to_tab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snippy-vcf_to_tab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_ref_by_bai_datasize.py

```bash
$ singularity exec <container> /usr/local/bin/split_ref_by_bai_datasize.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_version.sh

```bash
$ singularity exec <container> /usr/local/bin/update_version.sh
$ podman run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-annotator

```bash
$ singularity exec <container> /usr/local/bin/vcf-annotator
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp-sites

```bash
$ singularity exec <container> /usr/local/bin/snp-sites
$ podman run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename

```bash
$ singularity exec <container> /usr/local/bin/rename
$ podman run --it --rm --entrypoint /usr/local/bin/rename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megablast

```bash
$ singularity exec <container> /usr/local/bin/megablast
$ podman run --it --rm --entrypoint /usr/local/bin/megablast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megablast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samclip

```bash
$ singularity exec <container> /usr/local/bin/samclip
$ podman run --it --rm --entrypoint /usr/local/bin/samclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpEff

```bash
$ singularity exec <container> /usr/local/bin/snpEff
$ podman run --it --rm --entrypoint /usr/local/bin/snpEff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpEff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamleftalign

```bash
$ singularity exec <container> /usr/local/bin/bamleftalign
$ podman run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamleftalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_to_regions.py

```bash
$ singularity exec <container> /usr/local/bin/coverage_to_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_generate_regions.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_generate_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_generate_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freebayes-parallel

```bash
$ singularity exec <container> /usr/local/bin/freebayes-parallel
$ podman run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freebayes-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
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