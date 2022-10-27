---
layout: container
name:  "quay.io/biocontainers/viral-ngs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/viral-ngs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/viral-ngs/container.yaml"
updated_at: "2022-10-27 00:36:47.251141"
latest: "1.13.4--py35_0"
container_url: "https://biocontainers.pro/tools/viral-ngs"
aliases:
 - ".viral-ngs-post-link.sh"
 - "Trinity-test"
 - "assembly.py"
 - "bamtools-2.4.0"
 - "bmfilter"
 - "bmtagger.sh"
 - "bmtool"
 - "broad_utils.py"
 - "coverage-3.5"
 - "coverage3"
 - "extract_fullseq"
 - "flake8"
 - "gatk-register"
 - "illumina.py"
 - "install_tools.py"
 - "interhost.py"
 - "intrahost.py"
 - "isnovoindex"
 - "kraken-build.bak"
 - "kraken-filter.bak"
 - "kraken-mpa-report.bak"
 - "kraken-report.bak"
 - "kraken-translate.bak"
 - "kraken.bak"
 - "metagenomics.py"
 - "mvicuna"
 - "ncbi.py"
 - "novo2paf"
 - "novoalign"
 - "novoalign-license-register"
 - "novoalignCS"
 - "novoalignCSMPI"
 - "novoalignMPI"
 - "novobarcode"
 - "novoindex"
 - "novomethyl"
 - "novope2bed.pl"
 - "novorun.pl"
 - "novosort"
 - "novoutil"
 - "prinseq-graphs-noPCA.pl"
 - "prinseq-graphs.pl"
 - "prinseq-lite.pl"
 - "py.test-3.5"
 - "pyflakes"
 - "read_utils.py"
 - "reports.py"
 - "srprism"
 - "taxon_filter.py"
 - "variant_caller"
 - "vphaser2"
versions:
 - "1.13.4--py35_0"
description: "shpc-registry automated BioContainers addition for viral-ngs"
config: {"url": "https://biocontainers.pro/tools/viral-ngs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for viral-ngs", "latest": {"1.13.4--py35_0": "sha256:cd9bfe241ddfdd6c7928778258fdcbd17621b1e32c944db3d0cba7072bddb5eb"}, "tags": {"1.13.4--py35_0": "sha256:cd9bfe241ddfdd6c7928778258fdcbd17621b1e32c944db3d0cba7072bddb5eb"}, "docker": "quay.io/biocontainers/viral-ngs", "aliases": {".viral-ngs-post-link.sh": "/usr/local/bin/.viral-ngs-post-link.sh", "Trinity-test": "/usr/local/bin/Trinity-test", "assembly.py": "/usr/local/bin/assembly.py", "bamtools-2.4.0": "/usr/local/bin/bamtools-2.4.0", "bmfilter": "/usr/local/bin/bmfilter", "bmtagger.sh": "/usr/local/bin/bmtagger.sh", "bmtool": "/usr/local/bin/bmtool", "broad_utils.py": "/usr/local/bin/broad_utils.py", "coverage-3.5": "/usr/local/bin/coverage-3.5", "coverage3": "/usr/local/bin/coverage3", "extract_fullseq": "/usr/local/bin/extract_fullseq", "flake8": "/usr/local/bin/flake8", "gatk-register": "/usr/local/bin/gatk-register", "illumina.py": "/usr/local/bin/illumina.py", "install_tools.py": "/usr/local/bin/install_tools.py", "interhost.py": "/usr/local/bin/interhost.py", "intrahost.py": "/usr/local/bin/intrahost.py", "isnovoindex": "/usr/local/bin/isnovoindex", "kraken-build.bak": "/usr/local/bin/kraken-build.bak", "kraken-filter.bak": "/usr/local/bin/kraken-filter.bak", "kraken-mpa-report.bak": "/usr/local/bin/kraken-mpa-report.bak", "kraken-report.bak": "/usr/local/bin/kraken-report.bak", "kraken-translate.bak": "/usr/local/bin/kraken-translate.bak", "kraken.bak": "/usr/local/bin/kraken.bak", "metagenomics.py": "/usr/local/bin/metagenomics.py", "mvicuna": "/usr/local/bin/mvicuna", "ncbi.py": "/usr/local/bin/ncbi.py", "novo2paf": "/usr/local/bin/novo2paf", "novoalign": "/usr/local/bin/novoalign", "novoalign-license-register": "/usr/local/bin/novoalign-license-register", "novoalignCS": "/usr/local/bin/novoalignCS", "novoalignCSMPI": "/usr/local/bin/novoalignCSMPI", "novoalignMPI": "/usr/local/bin/novoalignMPI", "novobarcode": "/usr/local/bin/novobarcode", "novoindex": "/usr/local/bin/novoindex", "novomethyl": "/usr/local/bin/novomethyl", "novope2bed.pl": "/usr/local/bin/novope2bed.pl", "novorun.pl": "/usr/local/bin/novorun.pl", "novosort": "/usr/local/bin/novosort", "novoutil": "/usr/local/bin/novoutil", "prinseq-graphs-noPCA.pl": "/usr/local/bin/prinseq-graphs-noPCA.pl", "prinseq-graphs.pl": "/usr/local/bin/prinseq-graphs.pl", "prinseq-lite.pl": "/usr/local/bin/prinseq-lite.pl", "py.test-3.5": "/usr/local/bin/py.test-3.5", "pyflakes": "/usr/local/bin/pyflakes", "read_utils.py": "/usr/local/bin/read_utils.py", "reports.py": "/usr/local/bin/reports.py", "srprism": "/usr/local/bin/srprism", "taxon_filter.py": "/usr/local/bin/taxon_filter.py", "variant_caller": "/usr/local/bin/variant_caller", "vphaser2": "/usr/local/bin/vphaser2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/viral-ngs.
shpc-registry automated BioContainers addition for viral-ngs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/viral-ngs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/viral-ngs:1.13.4--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/viral-ngs/1.13.4--py35_0
$ module help quay.io/biocontainers/viral-ngs/1.13.4--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### viral-ngs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### viral-ngs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### viral-ngs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### viral-ngs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### viral-ngs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### viral-ngs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .viral-ngs-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.viral-ngs-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.viral-ngs-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.viral-ngs-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Trinity-test

```bash
$ singularity exec <container> /usr/local/bin/Trinity-test
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assembly.py

```bash
$ singularity exec <container> /usr/local/bin/assembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools-2.4.0

```bash
$ singularity exec <container> /usr/local/bin/bamtools-2.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bmfilter

```bash
$ singularity exec <container> /usr/local/bin/bmfilter
$ podman run --it --rm --entrypoint /usr/local/bin/bmfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bmtagger.sh

```bash
$ singularity exec <container> /usr/local/bin/bmtagger.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bmtagger.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmtagger.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bmtool

```bash
$ singularity exec <container> /usr/local/bin/bmtool
$ podman run --it --rm --entrypoint /usr/local/bin/bmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### broad_utils.py

```bash
$ singularity exec <container> /usr/local/bin/broad_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/broad_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/broad_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage-3.5

```bash
$ singularity exec <container> /usr/local/bin/coverage-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/coverage-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage3

```bash
$ singularity exec <container> /usr/local/bin/coverage3
$ podman run --it --rm --entrypoint /usr/local/bin/coverage3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_fullseq

```bash
$ singularity exec <container> /usr/local/bin/extract_fullseq
$ podman run --it --rm --entrypoint /usr/local/bin/extract_fullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_fullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flake8

```bash
$ singularity exec <container> /usr/local/bin/flake8
$ podman run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk-register

```bash
$ singularity exec <container> /usr/local/bin/gatk-register
$ podman run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illumina.py

```bash
$ singularity exec <container> /usr/local/bin/illumina.py
$ podman run --it --rm --entrypoint /usr/local/bin/illumina.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illumina.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_tools.py

```bash
$ singularity exec <container> /usr/local/bin/install_tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/install_tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interhost.py

```bash
$ singularity exec <container> /usr/local/bin/interhost.py
$ podman run --it --rm --entrypoint /usr/local/bin/interhost.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interhost.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intrahost.py

```bash
$ singularity exec <container> /usr/local/bin/intrahost.py
$ podman run --it --rm --entrypoint /usr/local/bin/intrahost.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intrahost.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isnovoindex

```bash
$ singularity exec <container> /usr/local/bin/isnovoindex
$ podman run --it --rm --entrypoint /usr/local/bin/isnovoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isnovoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-build.bak

```bash
$ singularity exec <container> /usr/local/bin/kraken-build.bak
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-build.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-build.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-filter.bak

```bash
$ singularity exec <container> /usr/local/bin/kraken-filter.bak
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-filter.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-filter.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-mpa-report.bak

```bash
$ singularity exec <container> /usr/local/bin/kraken-mpa-report.bak
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-report.bak

```bash
$ singularity exec <container> /usr/local/bin/kraken-report.bak
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-report.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-report.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-translate.bak

```bash
$ singularity exec <container> /usr/local/bin/kraken-translate.bak
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-translate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-translate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken.bak

```bash
$ singularity exec <container> /usr/local/bin/kraken.bak
$ podman run --it --rm --entrypoint /usr/local/bin/kraken.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagenomics.py

```bash
$ singularity exec <container> /usr/local/bin/metagenomics.py
$ podman run --it --rm --entrypoint /usr/local/bin/metagenomics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagenomics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mvicuna

```bash
$ singularity exec <container> /usr/local/bin/mvicuna
$ podman run --it --rm --entrypoint /usr/local/bin/mvicuna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mvicuna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2paf

```bash
$ singularity exec <container> /usr/local/bin/novo2paf
$ podman run --it --rm --entrypoint /usr/local/bin/novo2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novo2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalign

```bash
$ singularity exec <container> /usr/local/bin/novoalign
$ podman run --it --rm --entrypoint /usr/local/bin/novoalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalign-license-register

```bash
$ singularity exec <container> /usr/local/bin/novoalign-license-register
$ podman run --it --rm --entrypoint /usr/local/bin/novoalign-license-register   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalign-license-register   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalignCS

```bash
$ singularity exec <container> /usr/local/bin/novoalignCS
$ podman run --it --rm --entrypoint /usr/local/bin/novoalignCS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalignCS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalignCSMPI

```bash
$ singularity exec <container> /usr/local/bin/novoalignCSMPI
$ podman run --it --rm --entrypoint /usr/local/bin/novoalignCSMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalignCSMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoalignMPI

```bash
$ singularity exec <container> /usr/local/bin/novoalignMPI
$ podman run --it --rm --entrypoint /usr/local/bin/novoalignMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoalignMPI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novobarcode

```bash
$ singularity exec <container> /usr/local/bin/novobarcode
$ podman run --it --rm --entrypoint /usr/local/bin/novobarcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novobarcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoindex

```bash
$ singularity exec <container> /usr/local/bin/novoindex
$ podman run --it --rm --entrypoint /usr/local/bin/novoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novomethyl

```bash
$ singularity exec <container> /usr/local/bin/novomethyl
$ podman run --it --rm --entrypoint /usr/local/bin/novomethyl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novomethyl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novope2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/novope2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novope2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novope2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novorun.pl

```bash
$ singularity exec <container> /usr/local/bin/novorun.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novorun.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novorun.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novosort

```bash
$ singularity exec <container> /usr/local/bin/novosort
$ podman run --it --rm --entrypoint /usr/local/bin/novosort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novosort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoutil

```bash
$ singularity exec <container> /usr/local/bin/novoutil
$ podman run --it --rm --entrypoint /usr/local/bin/novoutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prinseq-graphs-noPCA.pl

```bash
$ singularity exec <container> /usr/local/bin/prinseq-graphs-noPCA.pl
$ podman run --it --rm --entrypoint /usr/local/bin/prinseq-graphs-noPCA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prinseq-graphs-noPCA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prinseq-graphs.pl

```bash
$ singularity exec <container> /usr/local/bin/prinseq-graphs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/prinseq-graphs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prinseq-graphs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prinseq-lite.pl

```bash
$ singularity exec <container> /usr/local/bin/prinseq-lite.pl
$ podman run --it --rm --entrypoint /usr/local/bin/prinseq-lite.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prinseq-lite.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test-3.5

```bash
$ singularity exec <container> /usr/local/bin/py.test-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/py.test-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflakes

```bash
$ singularity exec <container> /usr/local/bin/pyflakes
$ podman run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_utils.py

```bash
$ singularity exec <container> /usr/local/bin/read_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reports.py

```bash
$ singularity exec <container> /usr/local/bin/reports.py
$ podman run --it --rm --entrypoint /usr/local/bin/reports.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reports.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srprism

```bash
$ singularity exec <container> /usr/local/bin/srprism
$ podman run --it --rm --entrypoint /usr/local/bin/srprism   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srprism   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxon_filter.py

```bash
$ singularity exec <container> /usr/local/bin/taxon_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/taxon_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxon_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variant_caller

```bash
$ singularity exec <container> /usr/local/bin/variant_caller
$ podman run --it --rm --entrypoint /usr/local/bin/variant_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variant_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vphaser2

```bash
$ singularity exec <container> /usr/local/bin/vphaser2
$ podman run --it --rm --entrypoint /usr/local/bin/vphaser2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vphaser2   -v ${PWD} -w ${PWD} <container> -c " $@"
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