---
layout: container
name:  "quay.io/biocontainers/uvp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/uvp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/uvp/container.yaml"
updated_at: "2024-05-27 03:35:36.056868"
latest: "2.7.0--py_0"
container_url: "https://biocontainers.pro/tools/uvp"
aliases:
 - "GenomeAnalysisTK"
 - "UVP"
 - "coverage_estimator.py"
 - "del_parse.py"
 - "fqtools"
 - "gatk-register"
 - "kraken"
 - "kraken-build"
 - "kraken-filter"
 - "kraken-mpa-report"
 - "kraken-report"
 - "kraken-translate"
 - "lineage_parser.py"
 - "parse_annotation.py"
 - "prinseq-graphs-noPCA.pl"
 - "prinseq-graphs.pl"
 - "prinseq-lite.pl"
 - "qualimap"
 - "raw_vcf_parse.py"
 - "resis_parser.py"
 - "tab-to-vcf"
 - "uvp"
 - "varfilter.py"
 - "vcf-haplotypes"
 - "vcftools"
 - "fill-aa"
 - "fill-an-ac"
 - "fill-fs"
 - "fill-ref-md5"
 - "vcf-annotate"
 - "vcf-compare"
 - "vcf-concat"
 - "vcf-consensus"
 - "vcf-contrast"
 - "vcf-convert"
versions:
 - "2.7.0--py_0"
description: "shpc-registry automated BioContainers addition for uvp"
config: {"url": "https://biocontainers.pro/tools/uvp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for uvp", "latest": {"2.7.0--py_0": "sha256:90c38a58b23f84fff1d5433f3de2a87a9f2246a40b3a3c5af6ee3bee0257174f"}, "tags": {"2.7.0--py_0": "sha256:90c38a58b23f84fff1d5433f3de2a87a9f2246a40b3a3c5af6ee3bee0257174f"}, "docker": "quay.io/biocontainers/uvp", "aliases": {"GenomeAnalysisTK": "/usr/local/bin/GenomeAnalysisTK", "UVP": "/usr/local/bin/UVP", "coverage_estimator.py": "/usr/local/bin/coverage_estimator.py", "del_parse.py": "/usr/local/bin/del_parse.py", "fqtools": "/usr/local/bin/fqtools", "gatk-register": "/usr/local/bin/gatk-register", "kraken": "/usr/local/bin/kraken", "kraken-build": "/usr/local/bin/kraken-build", "kraken-filter": "/usr/local/bin/kraken-filter", "kraken-mpa-report": "/usr/local/bin/kraken-mpa-report", "kraken-report": "/usr/local/bin/kraken-report", "kraken-translate": "/usr/local/bin/kraken-translate", "lineage_parser.py": "/usr/local/bin/lineage_parser.py", "parse_annotation.py": "/usr/local/bin/parse_annotation.py", "prinseq-graphs-noPCA.pl": "/usr/local/bin/prinseq-graphs-noPCA.pl", "prinseq-graphs.pl": "/usr/local/bin/prinseq-graphs.pl", "prinseq-lite.pl": "/usr/local/bin/prinseq-lite.pl", "qualimap": "/usr/local/bin/qualimap", "raw_vcf_parse.py": "/usr/local/bin/raw_vcf_parse.py", "resis_parser.py": "/usr/local/bin/resis_parser.py", "tab-to-vcf": "/usr/local/bin/tab-to-vcf", "uvp": "/usr/local/bin/uvp", "varfilter.py": "/usr/local/bin/varfilter.py", "vcf-haplotypes": "/usr/local/bin/vcf-haplotypes", "vcftools": "/usr/local/bin/vcftools", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/uvp.
shpc-registry automated BioContainers addition for uvp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/uvp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/uvp:2.7.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/uvp/2.7.0--py_0
$ module help quay.io/biocontainers/uvp/2.7.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### uvp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### uvp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### uvp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### uvp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### uvp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uvp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GenomeAnalysisTK

```bash
$ singularity exec <container> /usr/local/bin/GenomeAnalysisTK
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### UVP

```bash
$ singularity exec <container> /usr/local/bin/UVP
$ podman run --it --rm --entrypoint /usr/local/bin/UVP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/UVP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage_estimator.py

```bash
$ singularity exec <container> /usr/local/bin/coverage_estimator.py
$ podman run --it --rm --entrypoint /usr/local/bin/coverage_estimator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage_estimator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### del_parse.py

```bash
$ singularity exec <container> /usr/local/bin/del_parse.py
$ podman run --it --rm --entrypoint /usr/local/bin/del_parse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/del_parse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fqtools

```bash
$ singularity exec <container> /usr/local/bin/fqtools
$ podman run --it --rm --entrypoint /usr/local/bin/fqtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk-register

```bash
$ singularity exec <container> /usr/local/bin/gatk-register
$ podman run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk-register   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken

```bash
$ singularity exec <container> /usr/local/bin/kraken
$ podman run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-build

```bash
$ singularity exec <container> /usr/local/bin/kraken-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-filter

```bash
$ singularity exec <container> /usr/local/bin/kraken-filter
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-translate

```bash
$ singularity exec <container> /usr/local/bin/kraken-translate
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lineage_parser.py

```bash
$ singularity exec <container> /usr/local/bin/lineage_parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/lineage_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lineage_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse_annotation.py

```bash
$ singularity exec <container> /usr/local/bin/parse_annotation.py
$ podman run --it --rm --entrypoint /usr/local/bin/parse_annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### qualimap

```bash
$ singularity exec <container> /usr/local/bin/qualimap
$ podman run --it --rm --entrypoint /usr/local/bin/qualimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raw_vcf_parse.py

```bash
$ singularity exec <container> /usr/local/bin/raw_vcf_parse.py
$ podman run --it --rm --entrypoint /usr/local/bin/raw_vcf_parse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raw_vcf_parse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resis_parser.py

```bash
$ singularity exec <container> /usr/local/bin/resis_parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/resis_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/resis_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tab-to-vcf

```bash
$ singularity exec <container> /usr/local/bin/tab-to-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvp

```bash
$ singularity exec <container> /usr/local/bin/uvp
$ podman run --it --rm --entrypoint /usr/local/bin/uvp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varfilter.py

```bash
$ singularity exec <container> /usr/local/bin/varfilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-haplotypes

```bash
$ singularity exec <container> /usr/local/bin/vcf-haplotypes
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcftools

```bash
$ singularity exec <container> /usr/local/bin/vcftools
$ podman run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-aa

```bash
$ singularity exec <container> /usr/local/bin/fill-aa
$ podman run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-an-ac

```bash
$ singularity exec <container> /usr/local/bin/fill-an-ac
$ podman run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-fs

```bash
$ singularity exec <container> /usr/local/bin/fill-fs
$ podman run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-ref-md5

```bash
$ singularity exec <container> /usr/local/bin/fill-ref-md5
$ podman run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-annotate

```bash
$ singularity exec <container> /usr/local/bin/vcf-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-compare

```bash
$ singularity exec <container> /usr/local/bin/vcf-compare
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-concat

```bash
$ singularity exec <container> /usr/local/bin/vcf-concat
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-consensus

```bash
$ singularity exec <container> /usr/local/bin/vcf-consensus
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-contrast

```bash
$ singularity exec <container> /usr/local/bin/vcf-contrast
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-convert

```bash
$ singularity exec <container> /usr/local/bin/vcf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
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