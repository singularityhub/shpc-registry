---
layout: container
name:  "quay.io/biocontainers/snippy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snippy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snippy/container.yaml"
updated_at: "2024-06-30 03:22:09.222725"
latest: "4.6.0--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/snippy"
aliases:
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
 - "snp-sites"
 - "vt"
 - "tabix++"
 - "samclip"
 - "any2fasta"
 - "bc"
 - "dc"
 - "snpEff"
 - "bamleftalign"
 - "coverage_to_regions.py"
versions:
 - "4.6.0--hdfd78af_2"
 - "4.6.0--hdfd78af_3"
 - "4.6.0--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for snippy"
config: {"url": "https://biocontainers.pro/tools/snippy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snippy", "latest": {"4.6.0--hdfd78af_4": "sha256:3324d693964f7f3985cc92ebd9d8fcded8a41f6224093481f2cb1378836cb055"}, "tags": {"4.6.0--hdfd78af_2": "sha256:8d1589ab60af6a9dac53dd069b71fdffc2d6530047e4b9742b59a89fbe2a5b70", "4.6.0--hdfd78af_3": "sha256:9495647055257f5ed6c5ad1b53faced942c788aa755c298e87bb8536d6b59cfc", "4.6.0--hdfd78af_4": "sha256:3324d693964f7f3985cc92ebd9d8fcded8a41f6224093481f2cb1378836cb055"}, "docker": "quay.io/biocontainers/snippy", "aliases": {"sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "snippy": "/usr/local/bin/snippy", "snippy-clean_full_aln": "/usr/local/bin/snippy-clean_full_aln", "snippy-core": "/usr/local/bin/snippy-core", "snippy-multi": "/usr/local/bin/snippy-multi", "snippy-vcf_extract_subs": "/usr/local/bin/snippy-vcf_extract_subs", "snippy-vcf_report": "/usr/local/bin/snippy-vcf_report", "snippy-vcf_to_tab": "/usr/local/bin/snippy-vcf_to_tab", "split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py", "update_version.sh": "/usr/local/bin/update_version.sh", "snp-sites": "/usr/local/bin/snp-sites", "vt": "/usr/local/bin/vt", "tabix++": "/usr/local/bin/tabix++", "samclip": "/usr/local/bin/samclip", "any2fasta": "/usr/local/bin/any2fasta", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "snpEff": "/usr/local/bin/snpEff", "bamleftalign": "/usr/local/bin/bamleftalign", "coverage_to_regions.py": "/usr/local/bin/coverage_to_regions.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snippy.
shpc-registry automated BioContainers addition for snippy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snippy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snippy:4.6.0--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snippy/4.6.0--hdfd78af_4
$ module help quay.io/biocontainers/snippy/4.6.0--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snippy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snippy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snippy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snippy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snippy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snippy-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### snp-sites

```bash
$ singularity exec <container> /usr/local/bin/snp-sites
$ podman run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### coverage_to_regions.py

```bash
$ singularity exec <container> /usr/local/bin/coverage_to_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_to_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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