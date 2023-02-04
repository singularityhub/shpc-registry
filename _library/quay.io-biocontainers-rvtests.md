---
layout: container
name:  "quay.io/biocontainers/rvtests"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rvtests/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rvtests/container.yaml"
updated_at: "2023-02-04 02:43:41.080940"
latest: "2.0.7--h3d151dd_2"
container_url: "https://biocontainers.pro/tools/rvtests"
aliases:
 - "bgen2vcf"
 - "bgenFileInfo"
 - "combineKinship"
 - "kinshipDecompose"
 - "plink2vcf"
 - "rvtest"
 - "vcf2geno"
 - "vcf2kinship"
 - "vcf2ld_gene"
 - "vcf2ld_neighbor"
 - "vcf2ld_window"
 - "vcf2plink"
 - "vcfAnnoSummaryLite"
 - "vcfConcordance"
 - "vcfExtractSite"
 - "vcfIndvSummary"
 - "vcfPair"
 - "vcfPeek"
 - "vcfSummary"
 - "vcfSummaryLite"
 - "vcfVariantSummaryLite"
versions:
 - "2.0.7--h3d151dd_2"
description: "shpc-registry automated BioContainers addition for rvtests"
config: {"url": "https://biocontainers.pro/tools/rvtests", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rvtests", "latest": {"2.0.7--h3d151dd_2": "sha256:1ec0c28520172dee852ce6c1c7c1fd18d6a09af580499af97f868f71b757e3bf"}, "tags": {"2.0.7--h3d151dd_2": "sha256:1ec0c28520172dee852ce6c1c7c1fd18d6a09af580499af97f868f71b757e3bf"}, "docker": "quay.io/biocontainers/rvtests", "aliases": {"bgen2vcf": "/usr/local/bin/bgen2vcf", "bgenFileInfo": "/usr/local/bin/bgenFileInfo", "combineKinship": "/usr/local/bin/combineKinship", "kinshipDecompose": "/usr/local/bin/kinshipDecompose", "plink2vcf": "/usr/local/bin/plink2vcf", "rvtest": "/usr/local/bin/rvtest", "vcf2geno": "/usr/local/bin/vcf2geno", "vcf2kinship": "/usr/local/bin/vcf2kinship", "vcf2ld_gene": "/usr/local/bin/vcf2ld_gene", "vcf2ld_neighbor": "/usr/local/bin/vcf2ld_neighbor", "vcf2ld_window": "/usr/local/bin/vcf2ld_window", "vcf2plink": "/usr/local/bin/vcf2plink", "vcfAnnoSummaryLite": "/usr/local/bin/vcfAnnoSummaryLite", "vcfConcordance": "/usr/local/bin/vcfConcordance", "vcfExtractSite": "/usr/local/bin/vcfExtractSite", "vcfIndvSummary": "/usr/local/bin/vcfIndvSummary", "vcfPair": "/usr/local/bin/vcfPair", "vcfPeek": "/usr/local/bin/vcfPeek", "vcfSummary": "/usr/local/bin/vcfSummary", "vcfSummaryLite": "/usr/local/bin/vcfSummaryLite", "vcfVariantSummaryLite": "/usr/local/bin/vcfVariantSummaryLite"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rvtests.
shpc-registry automated BioContainers addition for rvtests
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rvtests
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rvtests:2.0.7--h3d151dd_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rvtests/2.0.7--h3d151dd_2
$ module help quay.io/biocontainers/rvtests/2.0.7--h3d151dd_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rvtests-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rvtests-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rvtests-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rvtests-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rvtests-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rvtests-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bgen2vcf

```bash
$ singularity exec <container> /usr/local/bin/bgen2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/bgen2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgen2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgenFileInfo

```bash
$ singularity exec <container> /usr/local/bin/bgenFileInfo
$ podman run --it --rm --entrypoint /usr/local/bin/bgenFileInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgenFileInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineKinship

```bash
$ singularity exec <container> /usr/local/bin/combineKinship
$ podman run --it --rm --entrypoint /usr/local/bin/combineKinship   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineKinship   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinshipDecompose

```bash
$ singularity exec <container> /usr/local/bin/kinshipDecompose
$ podman run --it --rm --entrypoint /usr/local/bin/kinshipDecompose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinshipDecompose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plink2vcf

```bash
$ singularity exec <container> /usr/local/bin/plink2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/plink2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plink2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rvtest

```bash
$ singularity exec <container> /usr/local/bin/rvtest
$ podman run --it --rm --entrypoint /usr/local/bin/rvtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rvtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2geno

```bash
$ singularity exec <container> /usr/local/bin/vcf2geno
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2kinship

```bash
$ singularity exec <container> /usr/local/bin/vcf2kinship
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2kinship   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2kinship   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2ld_gene

```bash
$ singularity exec <container> /usr/local/bin/vcf2ld_gene
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2ld_gene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2ld_gene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2ld_neighbor

```bash
$ singularity exec <container> /usr/local/bin/vcf2ld_neighbor
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2ld_neighbor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2ld_neighbor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2ld_window

```bash
$ singularity exec <container> /usr/local/bin/vcf2ld_window
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2ld_window   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2ld_window   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2plink

```bash
$ singularity exec <container> /usr/local/bin/vcf2plink
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2plink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2plink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfAnnoSummaryLite

```bash
$ singularity exec <container> /usr/local/bin/vcfAnnoSummaryLite
$ podman run --it --rm --entrypoint /usr/local/bin/vcfAnnoSummaryLite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfAnnoSummaryLite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfConcordance

```bash
$ singularity exec <container> /usr/local/bin/vcfConcordance
$ podman run --it --rm --entrypoint /usr/local/bin/vcfConcordance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfConcordance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfExtractSite

```bash
$ singularity exec <container> /usr/local/bin/vcfExtractSite
$ podman run --it --rm --entrypoint /usr/local/bin/vcfExtractSite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfExtractSite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfIndvSummary

```bash
$ singularity exec <container> /usr/local/bin/vcfIndvSummary
$ podman run --it --rm --entrypoint /usr/local/bin/vcfIndvSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfIndvSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfPair

```bash
$ singularity exec <container> /usr/local/bin/vcfPair
$ podman run --it --rm --entrypoint /usr/local/bin/vcfPair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfPair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfPeek

```bash
$ singularity exec <container> /usr/local/bin/vcfPeek
$ podman run --it --rm --entrypoint /usr/local/bin/vcfPeek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfPeek   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfSummary

```bash
$ singularity exec <container> /usr/local/bin/vcfSummary
$ podman run --it --rm --entrypoint /usr/local/bin/vcfSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfSummaryLite

```bash
$ singularity exec <container> /usr/local/bin/vcfSummaryLite
$ podman run --it --rm --entrypoint /usr/local/bin/vcfSummaryLite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfSummaryLite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfVariantSummaryLite

```bash
$ singularity exec <container> /usr/local/bin/vcfVariantSummaryLite
$ podman run --it --rm --entrypoint /usr/local/bin/vcfVariantSummaryLite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfVariantSummaryLite   -v ${PWD} -w ${PWD} <container> -c " $@"
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